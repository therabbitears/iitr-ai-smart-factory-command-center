# Smart Factory Command Center Architecture

## Overview

The Smart Factory Command Center is an integrated AI operations platform for manufacturing. It delivers four core intelligence modules:

* Predictive Maintenance
* Quality Inspection
* Demand Forecasting
* Inventory Optimization

These modules are supported by a FastAPI backend, React dashboard, PostgreSQL persistence, MLflow tracking, and Docker-based deployment.

## Context Diagram

```mermaid
flowchart TB
  Operator["Plant Operator / Manager"]
  Manufacturing["Manufacturing Systems & Sensors"]
  SmartCenter["Smart Factory Command Center"]
  External["ERP / BI / External Systems"]
  Storage["PostgreSQL / Data Lake / MLflow"]

  Operator -->|Uses dashboard, reviews alerts| SmartCenter
  Manufacturing -->|Telemetry, quality, demand, inventory data| SmartCenter
  SmartCenter -->|Insights, recommendations| Operator
  SmartCenter -->|API / events| External
  SmartCenter -->|Stores models, metrics, audit logs| Storage
```

## Container Diagram

```mermaid
flowchart TB
  subgraph App[Smart Factory Command Center]
    FE["Frontend (React + MUI)"]
    BE["Backend API (FastAPI)"]
    ML["ML Service / Model Runner"]
    DB["PostgreSQL"]
    MF["MLflow Tracking Server"]
  end

  Sensors["Factory Sensors / PLCs / ERP Data"]
  Users["Operators / Planners / Analysts"]
  Ext["External Systems / Integrations"]

  Users --> FE
  FE --> BE
  BE --> DB
  BE --> MF
  BE --> ML
  Sensors --> BE
  Ext --> BE
```

## Component Diagram

```mermaid
flowchart TB
  subgraph BE[Backend Service]
    API["API Router / v1 Endpoints"]
    Auth["Authentication / Authorization"]
    Orchestrator["AI Module Orchestrator"]
    Repo["Repository Layer"]
    Schemas["Request / Response Schemas"]
    MLModules["ML Module Implementations"]
    Config["Configuration Loader"]
    Logging["Structured Logging / Audit"]
  end

  subgraph ML[ML Modules]
    PM["Predictive Maintenance"]
    QI["Quality Inspection"]
    DF["Demand Forecasting"]
    IO["Inventory Optimization"]
  end

  API --> Auth
  API --> Orchestrator
  Orchestrator --> MLModules
  Orchestrator --> Repo
  MLModules --> MF["MLflow"]
  Repo --> DB
  API --> Logging
  Config --> API
  Config --> Orchestrator
```

## Data Flow Diagram

```mermaid
flowchart TD
  A["Raw Datasets"] --> B["Ingestion + Validation"]
  B --> C["Feature Engineering"]
  C --> D["Training / Experimentation"]
  D --> E["Model Registry (MLflow)"]
  E --> F["Model Deployment / Serving"]
  F --> G["Prediction APIs"]
  G --> H["Dashboard & Alerts"]
  H --> I["Operator Feedback / Label Capture"]
  I --> B
```

## Training Architecture

* Training pipelines are built around dataset-specific modules:
  * `ai4i-2020-predictive-maintenance`
  * `steel-plates-faults`
  * `store-item-demand-forecasting`
  * `supply-chain-analytics`
* Feature engineering, validation, and model evaluation are separated from inference.
* MLflow tracks experiments, parameters, metrics, and artifacts.
* Models are versioned and promoted through:
  * development
  * staging
  * production
* Training jobs may run locally, in CI, or in a containerized batch environment.

### Training Architecture Diagram

```mermaid
flowchart LR
  Raw["Raw Data Sources"] --> Clean["Data Cleaning & Validation"]
  Clean --> Features["Feature Engineering"]
  Features --> Train["Model Training Pipeline"]
  Train --> Validate["Validation & Test"]
  Validate --> Registry["MLflow Model Registry"]
  Registry --> Deploy["Deployment Candidate"]
```

## Deployment Architecture

* Deployment is container-first using Docker Compose.
* Core runtime containers:
  * `frontend` — React dashboard
  * `backend` — FastAPI service
  * `postgres` — PostgreSQL database
  * `mlflow` — MLflow tracking server
* Environment-specific config files are stored in `configs/env/` and injected at runtime.
* Production deployment can be extended to Kubernetes or cloud container services.

### Deployment Architecture Diagram

```mermaid
flowchart TB
  subgraph Infra
    Compose["Docker Compose"]
    Postgres["PostgreSQL"]
    MLflow["MLflow Server"]
    Backend["FastAPI Backend"]
    Frontend["React Frontend"]
  end

  Compose --> Postgres
  Compose --> MLflow
  Compose --> Backend
  Compose --> Frontend
  Backend --> Postgres
  Backend --> MLflow
  Frontend --> Backend
```

## Observability Architecture

* Logging
  * Structured logs emitted by `app/backend/src/core/logging.py`
  * Standardized log format with timestamp, level, module, correlation ID, and request metadata.
* Monitoring
  * Application metrics from API request latency, error rate, and model inference duration.
  * Optionally integrate Prometheus and Grafana for infrastructure-level metrics.
* Tracing
  * Correlation IDs flow from frontend requests through backend API calls and database operations.
* ML observability
  * MLflow records experiment metrics, model versions, and artifact lineage.

### Observability Diagram

```mermaid
flowchart TD
  Backend["FastAPI Backend"] --> Logs["Structured Logs"]
  Backend --> Metrics["Metrics / Monitoring"]
  Backend --> Traces["Distributed Tracing"]
  MLflow["MLflow"] --> Experiments["Experiment Tracking"]
  Logs --> Observability["Log Store / Dashboard"]
  Metrics --> Observability
  Traces --> Observability
```

## Security Architecture

* API access is protected using authentication tokens and role-based access control at the FastAPI layer.
* Secrets and credentials are managed via environment variables, not checked into source control.
* Network isolation ensures backend and database communication is limited to trusted service boundaries inside Docker Compose or the chosen deployment platform.
* Database access uses dedicated service accounts and least-privilege grants.
* Data privacy and governance are enforced by keeping training data and production inference data logically separated.
* Input validation and schema enforcement prevent malformed requests from reaching model and persistence layers.

### Security Architecture Diagram

```mermaid
flowchart TB
  User["Authenticated User"] -->|HTTPS| Frontend
  Frontend -->|HTTPS| Backend
  Backend -->|TLS / Private Network| Postgres
  Backend -->|Secure API| MLflow
  Env["Env Config"] --> Backend
  Secrets["Secrets Store"] --> Env
```
* MAPE

API Endpoint:

POST /api/forecast-demand

Output:

{
"next_week_forecast": 15420,
"confidence": 0.91
}

---

### Inventory Optimization Module

Dataset:
Supply Chain Analytics

Input Features:

* Inventory Levels
* Lead Times
* Demand Forecast
* Supplier Performance

Feature Engineering:

* Days of Inventory
* Consumption Rate
* Supplier Risk Score

Algorithms:

Baseline:

* Linear Regression

Intermediate:

* Random Forest

Primary Production Model:

* XGBoost

Evaluation Metrics:

* MAE
* RMSE

API Endpoint:

POST /api/inventory-risk

Output:

{
"stockout_probability": 0.74,
"recommended_reorder": 500
}

---

## Database Design

Tables:

ManufacturingAssets
MaintenancePredictions
QualityPredictions
DemandForecasts
InventoryRecommendations
ModelMetadata
PredictionAudit

---

## Deployment Architecture

Docker Containers

1. Frontend

   * React

2. Backend

   * FastAPI

3. Database

   * PostgreSQL

4. ML Services

   * Scikit-Learn Models
   * TensorFlow Models

5. MLflow Server

6. Monitoring

Optional:

* Prometheus
* Grafana

---

## CI/CD Pipeline

GitHub

↓

GitHub Actions

↓

Unit Tests

↓

Model Validation

↓

Docker Build

↓

Container Registry

↓

Deployment

---

## Future Architecture

Phase 2:

* Kafka Event Streaming
* Real-Time Predictions
* IoT Sensor Integration

Phase 3:

* CNN-Based Visual Inspection
* OpenCV Integration
* Transfer Learning

Phase 4:

* Reinforcement Learning
* Production Scheduling Optimization

Phase 5:

* Multi-Factory Command Center
* Cross-Plant Analytics
* Digital Twin Integration
