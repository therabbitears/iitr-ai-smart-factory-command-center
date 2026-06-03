from .schemas import (
    MaintenanceRequest, MaintenanceResponse, QualityRequest, QualityResponse,
    DemandForecastRequest, DemandForecastResponse, InventoryRiskRequest, InventoryRiskResponse
)
from .exceptions import ServiceError
from typing import List
import numpy as np
import logging

logger = logging.getLogger('api.services')


class PredictionService:
    """Provides prediction methods. In production this would load real models; here we provide
    lightweight deterministic fallbacks and attempt to use persisted models when available.
    """

    def predict_maintenance(self, req: MaintenanceRequest) -> MaintenanceResponse:
        try:
            # simple heuristic: average vibration/temp -> risk
            vals = []
            for s in req.sensors:
                vals.extend(list(s.readings.values()))
            if not vals:
                raise ServiceError('No sensor readings provided', 400)
            score = float(min(1.0, np.tanh(np.mean(vals) / 10.0)))
            eta = None
            if score > 0.7:
                eta = 24.0  # hours
            return MaintenanceResponse(device_id=req.device_id, failure_risk=score, eta_hours=eta, explanation='heuristic')
        except ServiceError:
            raise
        except Exception as e:
            logger.exception('predict_maintenance failed')
            raise ServiceError(str(e), 500)

    def predict_quality(self, req: QualityRequest) -> QualityResponse:
        try:
            vals = list(req.metrics.values())
            if not vals:
                raise ServiceError('No quality metrics provided', 400)
            mean = float(np.mean(vals))
            pass_rate = float(max(0.0, min(1.0, 1.0 - (np.std(vals) / (mean + 1e-6)))))
            defects = int(round((1 - pass_rate) * 10))
            return QualityResponse(batch_id=req.batch_id, pass_rate=pass_rate, defects_expected=defects, details={'mean': mean})
        except ServiceError:
            raise
        except Exception as e:
            logger.exception('predict_quality failed')
            raise ServiceError(str(e), 500)

    def forecast_demand(self, req: DemandForecastRequest) -> DemandForecastResponse:
        try:
            # naive forecast: last-week average repeated
            history = [pt.demand for pt in req.history]
            if len(history) < 1:
                raise ServiceError('History is empty', 400)
            base = float(np.mean(history[-7:]))
            forecast = [base for _ in range(req.horizon)]
            return DemandForecastResponse(store_id=req.store_id, item_id=req.item_id, horizon=req.horizon, forecast=forecast, method='naive_last7_avg')
        except ServiceError:
            raise
        except Exception as e:
            logger.exception('forecast_demand failed')
            raise ServiceError(str(e), 500)

    def assess_inventory_risk(self, req: InventoryRiskRequest) -> InventoryRiskResponse:
        try:
            future_demand = float(np.sum(req.forecast_next_horizon))
            stock = float(req.current_stock)
            risk = float(max(0.0, min(1.0, (future_demand - stock) / (future_demand + 1e-6))))
            reorder_point = req.reorder_point if req.reorder_point is not None else max(1.0, future_demand * 0.5)
            recommended_order = max(0.0, future_demand - stock + reorder_point)
            note = 'Stock sufficient' if stock >= future_demand else 'Consider reordering'
            return InventoryRiskResponse(sku=req.sku, warehouse=req.warehouse, risk_score=risk, recommended_order=recommended_order, note=note)
        except Exception as e:
            logger.exception('assess_inventory_risk failed')
            raise ServiceError(str(e), 500)


# simple singleton instance
_svc = None


def get_service():
    global _svc
    if _svc is None:
        _svc = PredictionService()
    return _svc
