FastAPI microservice for Smart Factory Command Center

Run locally:

1. Install dependencies (example):

```bash
pip install fastapi uvicorn pydantic
```

2. Start the server:

```bash
uvicorn app.backend.api:app --reload --host 0.0.0.0 --port 8000
```

Endpoints:
- POST `/api/predict-maintenance` — Predict failure risk from sensor readings.
- POST `/api/predict-quality` — Predict batch quality pass rate.
- POST `/api/forecast-demand` — Forecast demand given history.
- POST `/api/inventory-risk` — Compute inventory risk and reorder recommendation.

OpenAPI UI: `http://localhost:8000/docs`
