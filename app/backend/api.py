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

# Optional instrumentation: Prometheus and OpenTelemetry
try:
    # Prometheus instrumentation
    from prometheus_fastapi_instrumentator import Instrumentator
    instr = Instrumentator()
    instr.instrument(app).expose(app)
except Exception:
    pass

try:
    # OpenTelemetry tracing (OTLP -> Collector)
    from opentelemetry import trace
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    resource = Resource.create({"service.name": "smart-factory-api"})
    provider = TracerProvider(resource=resource)
    exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
except Exception:
    pass

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
