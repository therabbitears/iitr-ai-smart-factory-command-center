# ChatGPT Architectural Diagram Prompt

## Prompt for ChatGPT / Claude / Gemini

Please generate a detailed **enterprise-grade architectural diagram image** for the Smart Factory Command Center platform using Mermaid, draw.io, or PlantUML syntax. Include all components, data flows, and technology stack as described below.

---

## Platform Overview

**Smart Factory Command Center** is an AI-powered IoT and manufacturing intelligence platform that integrates predictive maintenance, quality inspection, demand forecasting, and inventory optimization into a unified command-and-control system.

---

## Core Architecture Components

### 1. Data Layer

#### Datasets & Sources

1. **Predictive Maintenance Module**
   - Dataset: AI4I 2020 Predictive Maintenance (Kaggle)
   - Source path: `data/raw/ai4i_predictive_maintenance/ai4i.csv`
   - Schema: machine_id, timestamp, air_temperature, process_temperature, rotational_speed, torque, tool_wear, machine_failure, failure_type
   - Primary use: Time-series equipment telemetry + failure labels

2. **Quality Inspection Module**
   - Dataset: Steel Plates Faults (Kaggle)
   - Source path: `data/raw/steel_plates_faults/steel_plates.csv`
   - Schema: X_Minimum, X_Maximum, Y_Minimum, Y_Maximum, Pixel_area, Bare_Nuclei, class (7 defect types)
   - Primary use: Defect classification (tabular + image-ready features)

3. **Demand Forecasting Module**
   - Dataset: Store Item Demand Forecasting Challenge (Kaggle)
   - Source path: `data/raw/store_demand_forecasting/train.csv`
   - Schema: date, store, item, sales, onpromotion, dayofweek, month, year
   - Primary use: Multi-store, multi-SKU daily demand time-series

4. **Inventory Optimization Module**
   - Dataset: Supply Chain Analytics (Kaggle)
   - Source path: `data/raw/supply_chain_analytics/supply_chain.csv`
   - Schema: date, product_id, warehouse_id, on_hand, reorder_point, lead_time_days, demand_forecast, supplier_score, stockouts, reorder_quantity
   - Primary use: Stock-out risk modeling and reorder optimization

#### Data Validation & Quality
- Pandera-based schema validation at ingestion
- Data profiling (row count, missing data, duplicates)
- Quality rules per dataset documented in `data_quality_rules.md`

---

### 2. ML Training Pipeline (Backend)

#### Module 1: Predictive Maintenance
- **Algorithms:**
  - Linear Regression (baseline)
  - Random Forest (ensemble)
  - XGBoost (boosted trees)
  - ANN (Multi-layer Perceptron with LSTM variants for sequential data)
- **Feature Engineering:**
  - Lag features (1, 7, 30-day rolling windows)
  - Rolling mean/std for sensor streams
  - Cyclical encoding (time-of-day, day-of-week)
  - Domain-driven features (vibration thresholds, temp deviation from baseline)
- **Hyperparameters:**
  - RF: max_depth=10, n_estimators=100, min_samples_split=5
  - XGBoost: learning_rate=0.1, max_depth=6, n_estimators=200
  - ANN: 2 hidden layers (64→32 neurons), ReLU activation, Dropout(0.3), Adam optimizer, epochs=50
- **Output:** Failure risk score (0-1), ETA to failure (hours), failure classification

#### Module 2: Quality Inspection
- **Algorithms:**
  - Logistic Regression (baseline)
  - Random Forest (multi-class classifier)
  - XGBoost (multi-class classifier)
  - CNN (ResNet50-based transfer learning for image defect detection)
  - ANN (Dense network for tabular metrics)
- **Feature Engineering:**
  - Normalization (StandardScaler on training data only)
  - Interaction terms (width × height, area ratios)
  - Statistical features (min/max/median pixel values)
- **Output:** Pass/fail prediction, defect class (7 types), confidence score

#### Module 3: Demand Forecasting
- **Algorithms:**
  - Linear Regression (seasonal baseline)
  - Random Forest Regressor (hierarchical by store/item)
  - XGBoost Regressor (non-linear interactions)
  - LSTM (sequence-to-one forecasting, 14-day input window → 14-day forecast horizon)
  - Naive baseline (last-7-day average)
- **Feature Engineering:**
  - Lag features (7, 14, 30, 365 days)
  - Rolling statistics (mean, std, min, max over windows)
  - Cyclical features (day-of-week, month, quarter via sine/cosine encoding)
  - External regressors (on-promotion flag, holidays)
- **Output:** Demand forecast (units), confidence intervals, method attribution

#### Module 4: Inventory Optimization
- **Algorithms:**
  - Linear Regression (simple reorder point calculation)
  - Random Forest Regressor (risk scoring)
  - XGBoost Regressor (recommended order quantity)
  - Heuristic risk function (demand vs. stock gap + lead time)
- **Feature Engineering:**
  - Aggregation by warehouse-SKU-date
  - Demand forecast (from Module 3)
  - Safety stock calculation (service level × demand std)
  - Reorder point = demand during lead time + safety stock
- **Output:** Risk score (0-1), recommended order quantity, stock-out probability

#### Model Store & Registry
- **MLflow Integration:**
  - Experiment tracking (parameters, metrics, artifacts)
  - Model versioning and stage transitions (Staging → Production)
  - Model Registry for governance and promotion
  - Automatic logging of dataset versions, feature sets, hyperparameters
- **Local Fallback:** Pickle + JSON metadata for models when MLflow unavailable
- **Artifact Storage:** Local `models/` directory or S3/Azure Blob Storage

---

### 3. Backend API Layer (FastAPI)

#### Service Architecture
- **Framework:** FastAPI 0.110.0 + Uvicorn ASGI server
- **Host:** 0.0.0.0:8000

#### Endpoints & DTOs

1. **POST `/api/predict-maintenance`**
   - Input: MaintenanceRequest (device_id, sensors with readings)
   - Output: MaintenanceResponse (failure_risk, eta_hours, explanation)
   - Service: `predict_maintenance()` from PredictionService

2. **POST `/api/predict-quality`**
   - Input: QualityRequest (batch_id, metrics dict)
   - Output: QualityResponse (pass_rate, defects_expected, details)
   - Service: `predict_quality()` from PredictionService

3. **POST `/api/forecast-demand`**
   - Input: DemandForecastRequest (store_id, item_id, history, horizon)
   - Output: DemandForecastResponse (forecast list, method)
   - Service: `forecast_demand()` from PredictionService

4. **POST `/api/inventory-risk`**
   - Input: InventoryRiskRequest (sku, warehouse, current_stock, forecast, reorder_point)
   - Output: InventoryRiskResponse (risk_score, recommended_order, note)
   - Service: `assess_inventory_risk()` from PredictionService

5. **GET `/healthz`** → Health check endpoint

6. **GET `/metrics`** → Prometheus metrics endpoint (prometheus_fastapi_instrumentator)

#### Patterns
- Pydantic v2 validation (conlist, conint, Field constraints)
- Dependency injection (FastAPI Depends)
- Centralized exception handling (ServiceError custom exception)
- Optional instrumentation (Prometheus, OTEL tracing)

---

### 4. Frontend Layer (React + Vite)

#### Framework & UI
- **Build tool:** Vite 5.0.0
- **Runtime:** React 18.0.0
- **UI Library:** Material UI v5 (MUI)
- **Charts:** Recharts v2.0.0 (LineChart, BarChart, PieChart, etc.)
- **Routing:** React Router DOM v6
- **HTTP Client:** Axios v1.0.0
- **Dev server port:** 5173 (configurable)

#### Pages & Components
1. **Executive Dashboard**
   - KPI tiles (OEE %, Prediction Volume, API Latency, Error Rate)
   - Trend charts (OEE + Output over 14 days)
   - Fleet health pie chart (Healthy / Warning / Critical mix)
   - Module risk snapshot bar chart

2. **Maintenance Dashboard**
   - Live prediction form (device ID + sensor inputs)
   - Failure risk output with progress bar
   - Recent risk trend line chart
   - API integration: `/api/predict-maintenance`

3. **Quality Dashboard**
   - Live batch quality form (batch metrics)
   - Pass/fail pie chart distribution
   - Defect count chips
   - API integration: `/api/predict-quality`

4. **Forecast Dashboard**
   - Forecast input form (store, item, horizon, base demand)
   - Historical + forecast dual-line chart
   - Method attribution chip
   - API integration: `/api/forecast-demand`

5. **Inventory Dashboard**
   - Risk input form (SKU, warehouse, stock, forecast list)
   - Risk score + recommended order chips
   - Bar chart (Risk vs. Recommended Order)
   - API integration: `/api/inventory-risk`

#### Layout Components
- **Header:** AppBar with title
- **Sidebar:** Persistent drawer with navigation (responsive)
- **Theme:** Material UI default theme + custom overrides

---

### 5. Observability & Monitoring Stack

#### Metrics & Monitoring (Prometheus)

**Prometheus Scrape Targets:**
- API metrics endpoint: `:8000/metrics`
- OTEL Collector: `:8888`
- Prometheus self: `:9090`

**Key Metrics Collected:**

1. **API Metrics (prometheus_fastapi_instrumentator):**
   - `http_request_duration_seconds` (histogram, per endpoint)
   - `http_requests_total` (counter, per method/endpoint/status)
   - `http_request_size_bytes` (histogram)
   - `http_response_size_bytes` (histogram)

2. **Custom Model Metrics (app/backend/metrics.py):**
   - `model_latency_seconds` (histogram, per model: maintenance_heuristic, quality_heuristic, demand_forecast_naive, inventory_risk)
   - `prediction_volume_total` (counter, per model)
   - `api_error_count` (counter, per endpoint + exception type)
   - `api_request_count` (counter, per endpoint/method/status)

3. **OTEL Collector Metrics (metrics to Prometheus):**
   - All traces converted to metrics via OTLP receiver
   - Span counts, duration distributions

#### Tracing (OpenTelemetry + Jaeger)

**OTEL Configuration:**
- **Exporter:** OTLPSpanExporter (gRPC to localhost:4317)
- **Resource:** service.name = "smart-factory-api"
- **Processor:** BatchSpanProcessor (batch size 100, timeout 5s)

**Trace Spans (auto-instrumented via FastAPI middleware when available):**
- HTTP request spans (path, method, status)
- Model inference spans (operation name per model)
- Database query spans (if DB instrumentation added)

**Jaeger UI:**
- Trace visualization: localhost:16686
- Service: smart-factory-api
- Operations: /api/predict-maintenance, /api/predict-quality, etc.

#### Logging (ELK Stack)

**Log Ingestion:**
- **Logstash:** TCP input on port 5000, JSON codec
- **Elasticsearch:** Port 9200, index template `smart-factory-logs-%{+YYYY.MM.dd}`
- **Kibana:** Port 5601

**Log Format (JSON):**
```json
{
  "timestamp": "2026-06-20T10:30:45.123Z",
  "level": "INFO",
  "logger": "api.services",
  "message": "predict_maintenance completed",
  "device_id": "machine-01",
  "failure_risk": 0.34,
  "latency_ms": 145,
  "trace_id": "abc123def456"
}
```

**Structured Logging in Python:**
- Logger: `logging.getLogger('api')` or `logging.getLogger('api.services')`
- Fields: timestamp, level, logger name, message, custom context (device_id, model_name, latency)

#### Dashboards (Grafana)

**Grafana Port:** 3000 (admin/admin)

**Sample Dashboards:**
1. **Service Health:**
   - API Latency (p50, p95, p99)
   - Request rate (req/sec)
   - Error rate (%)
   - Active requests

2. **ML Model Performance:**
   - Model latency per endpoint (histogram)
   - Prediction volume (counter)
   - Model drift detection (statistical tests on input distributions)
   - Error counts per model

3. **Infrastructure:**
   - CPU, memory, disk usage (if node exporter added)
   - OTEL Collector health
   - Elasticsearch cluster status

---

### 6. Deployment & Infrastructure

#### Containerization
- **Docker:** Dockerfile for FastAPI backend (Python 3.12-slim)
- **Container Registry:** Docker Hub or private registry

#### Orchestration & Runtime
- **Option A (Local Dev):** Docker Compose (app/backend/docker-compose.yml + observability/docker-compose.yml)
- **Option B (Production):** Kubernetes manifests (to be generated)
  - Deployments for API, ML services
  - Services, Ingress, HPA (Horizontal Pod Autoscaler)
  - ConfigMaps for feature stores, model paths
  - Secrets for API keys, database credentials

#### Infrastructure as Code
- **Terraform** or **CloudFormation** for cloud setup (AWS/Azure/GCP)
- **Helm charts** for Kubernetes package management

---

## Data Flow Diagram

```
Raw Datasets (Kaggle/CSV)
    ↓
Data Ingestion Layer (Pandera validation)
    ↓
Raw Layer (data/raw/...)
    ↓
Data Preprocessing (clean, normalize, aggregate)
    ↓
Feature Engineering (lag, rolling, cyclical, domain)
    ↓
Feature Store Layer
    ↓
Train/Val/Test Split (temporal or random)
    ↓
ML Training Pipeline (sklearn, XGBoost, TensorFlow)
    ↓
Model Evaluation & Comparison
    ↓
MLflow Model Registry (versioning, stage transitions)
    ↓
Model Artifacts (local pickle or object storage)
    ↓
FastAPI Service (model loading at startup)
    ↓
Inference Endpoints (/api/predict-*)
    ↓
Frontend React App (Axios HTTP calls)
    ↓
User Dashboard & Decisions
    ↓
Observability Stack
    ├─ Prometheus (metrics scrape)
    ├─ Grafana (visualization)
    ├─ Jaeger (trace visualization)
    ├─ ELK (logs)
    └─ OTEL Collector (trace/metric export)
```

---

## Technology Stack Summary

### Backend & ML
- Python 3.10
- FastAPI 0.110.0
- Uvicorn 0.23.2
- Scikit-Learn 1.3.2
- XGBoost 1.7.6
- TensorFlow 2.14.0 / Keras
- Pandas 2.2.3
- NumPy 1.26.4
- Pydantic 2.8.0
- Pandera 0.21.0
- SQLAlchemy 2.0.25
- MLflow 2.6.0

### Frontend
- React 18.0.0
- Vite 5.0.0
- Material UI 5.0.0
- Recharts 2.0.0
- Axios 1.0.0
- React Router DOM 6.0.0

### Observability
- Prometheus (metrics storage + scraping)
- Grafana (dashboards)
- Jaeger (distributed tracing)
- OpenTelemetry SDK (instrumentation)
- Elasticsearch 8.9.0 (log storage)
- Kibana 8.9.0 (log visualization)
- Logstash 8.9.0 (log ingestion)

### DevOps & Deployment
- Docker (containerization)
- Docker Compose (local orchestration)
- Git (version control)
- GitHub Actions / GitLab CI (CI/CD pipeline, to be added)

---

## Diagram Request Details

Please create a **multi-layer architectural diagram** showing:

### Layer 1: Data Sources
- Show 4 Kaggle datasets as external sources
- Arrows flowing into Data Ingestion Layer

### Layer 2: Data Processing (Backend)
- Data Ingestion (Pandera validation)
- Preprocessing (cleaning, aggregation)
- Feature Engineering (lag, rolling, cyclical)
- Train/Val/Test Split
- Model Training boxes for each algorithm (LR, RF, XGBoost, LSTM/ANN)
- Model Evaluation & Registry (MLflow)

### Layer 3: API Service Layer
- FastAPI service box
- 4 inference endpoints as sub-boxes
- Dependency injection and schema validation noted

### Layer 4: Frontend UI
- React + Vite dev server
- 5 dashboard pages (Executive, Maintenance, Quality, Forecast, Inventory)
- Material UI + Recharts noted

### Layer 5: Observability (Right-side cluster)
- Prometheus scraping API `/metrics`
- Grafana dashboards
- Jaeger UI (traces)
- ELK stack (Elasticsearch ← Logstash ← API logs)
- OTEL Collector (bidirectional with API)

### Annotations
- Label each component with key technologies (FastAPI, React, XGBoost, etc.)
- Show data flow arrows (CSV → Ingestion → Features → Training → Model Store → API → Frontend)
- Highlight the 4 ML modules distinctly
- Show bidirectional observability connections (tracing, metrics, logs)
- Include port numbers (8000, 5173, 9090, 16686, 5601, 4317, 5000)

### Color Coding (Optional)
- **Blue:** Data & ML (datasets, training, models)
- **Green:** API & Backend Services
- **Orange:** Frontend & UI
- **Purple:** Observability & Monitoring

---

## Example Diagram Format

You can use any of these formats:
- **Mermaid** (best for quick GitHub integration)
- **draw.io / diagrams.net** (visual editing)
- **PlantUML** (professional UML-style)
- **ArchiMate** (enterprise architecture standard)

---

## Additional Notes

- **Model Training Cadence:** Scheduled nightly or on-demand via CI/CD pipeline
- **Model Promotion:** Manual approval gate from Staging to Production via MLflow UI or API
- **Fallback Strategy:** If API unavailable, frontend displays cached predictions or local heuristics
- **Security:** (To be added) OAuth2/OpenID Connect, RBAC, secrets management (Vault/KeyVault)
- **Scalability:** (To be added) Load balancing, caching layer (Redis), message queue (Kafka/RabbitMQ)

---

End of Prompt
