from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import (
    MaintenanceRequest, MaintenanceResponse,
    QualityRequest, QualityResponse,
    DemandForecastRequest, DemandForecastResponse,
    InventoryRiskRequest, InventoryRiskResponse
)
from .deps import get_prediction_service
from .exceptions import ServiceError, register_exception_handlers
from .logging_config import setup_logging

app = FastAPI(title="Smart Factory Command Center API", version="0.1.0", openapi_url="/openapi.json")

setup_logging()
register_exception_handlers(app)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.post("/api/predict-maintenance", response_model=MaintenanceResponse)
def predict_maintenance(req: MaintenanceRequest, svc=Depends(get_prediction_service)):
    try:
        return svc.predict_maintenance(req)
    except ServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@app.post("/api/predict-quality", response_model=QualityResponse)
def predict_quality(req: QualityRequest, svc=Depends(get_prediction_service)):
    try:
        return svc.predict_quality(req)
    except ServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@app.post("/api/forecast-demand", response_model=DemandForecastResponse)
def forecast_demand(req: DemandForecastRequest, svc=Depends(get_prediction_service)):
    try:
        return svc.forecast_demand(req)
    except ServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@app.post("/api/inventory-risk", response_model=InventoryRiskResponse)
def inventory_risk(req: InventoryRiskRequest, svc=Depends(get_prediction_service)):
    try:
        return svc.assess_inventory_risk(req)
    except ServiceError as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
