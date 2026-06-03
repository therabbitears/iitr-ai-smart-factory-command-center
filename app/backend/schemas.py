from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, conlist, conint


class MaintenanceSensor(BaseModel):
    sensor_id: str = Field(..., example='temp_sensor_1')
    timestamp: datetime = Field(...)
    readings: Dict[str, float] = Field(..., example={'vibration': 0.12, 'temp': 75.3})


class MaintenanceRequest(BaseModel):
    device_id: str = Field(..., example='machine_01')
    sensors: List[MaintenanceSensor]


class MaintenanceResponse(BaseModel):
    device_id: str
    failure_risk: float = Field(..., ge=0.0, le=1.0)
    eta_hours: Optional[float]
    explanation: Optional[str]


class QualityRequest(BaseModel):
    batch_id: str
    metrics: Dict[str, float] = Field(..., example={'width': 10.2, 'height': 5.1})


class QualityResponse(BaseModel):
    batch_id: str
    pass_rate: float = Field(..., ge=0.0, le=1.0)
    defects_expected: int
    details: Optional[Dict[str, float]]


class DemandHistoryPoint(BaseModel):
    date: datetime
    demand: float


class DemandForecastRequest(BaseModel):
    store_id: str
    item_id: str
    history: conlist(DemandHistoryPoint, min_items=7)  # require >=7 days
    horizon: conint(gt=0, le=90) = 14


class DemandForecastResponse(BaseModel):
    store_id: str
    item_id: str
    horizon: int
    forecast: List[float]
    method: str


class InventoryRiskRequest(BaseModel):
    sku: str
    warehouse: str
    current_stock: float
    forecast_next_horizon: List[float]
    reorder_point: Optional[float]


class InventoryRiskResponse(BaseModel):
    sku: str
    warehouse: str
    risk_score: float = Field(..., ge=0.0, le=1.0)
    recommended_order: float
    note: Optional[str]
