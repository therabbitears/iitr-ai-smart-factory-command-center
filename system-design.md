# Smart Factory Command Center System Design

## Purpose

This document describes system-level design decisions for the Smart Factory Command Center, including service boundaries, deployment topology, data flow, and operational architecture.

## System Overview

The command center is built as a modular platform with clear separation between frontend, backend, data, and ML responsibilities.

### Primary Services

* `frontend` — React + Material UI dashboard for operators and planners.
* `backend` — FastAPI service exposing prediction, analytics, and orchestration endpoints.
* `postgres` — Relational data store for predictions, audit logs, master data, and reference tables.
* `mlflow` — Experiment tracking and model registry.

### AI Modules

1. Predictive Maintenance
2. Quality Inspection
3. Demand Forecasting
4. Inventory Optimization

Each module has its own data ingestion, preprocessing, model pipeline, and inference interface.

## Container Architecture

### Containers

* `frontend`
  * Hosts the React dashboard
  * Calls backend prediction and reporting APIs
* `backend`
  * Handles API requests and business logic
  * Orchestrates ML module execution and persistence
* `postgres`
  * Stores application data, model metadata, and audit records
* `mlflow`
  * Stores experiment runs, metrics, and model artifacts

### Communication

* Frontend <-> Backend: HTTPS / REST
* Backend <-> PostgreSQL: SQLAlchemy / secure credentials
* Backend <-> MLflow: HTTP API
* Backend <-> External systems: optional webhook or message broker integration

## Component Responsibilities

### Backend Components

* `api/v1/endpoints` — Request routing for each module and common services.
* `core/config.py` — Central configuration management using environment variables.
* `core/logging.py` — Logging bootstrap and logger factory.
* `db/repository.py` — Data access abstraction.
* `ml/*` — Module-specific training, inference, and preprocessing logic.
* `schemas/` — Pydantic models for validation and serialization.
* `services/` — Business orchestration and module coordination.

### Frontend Components

* `src/pages` — Dashboard, module detail pages, and system overview.
* `src/api` — API clients and request helpers.
* `src/components` — Reusable UI components.
* `src/store` — Local application state and caching.
* `src/theme` — Material UI theme and design tokens.

## Data Flow

1. Source data is ingested from manufacturing equipment, quality scans, demand logs, and inventory systems.
2. Data is validated and normalized in Python ETL pipelines.
3. Feature engineering produces model-ready datasets.
4. Models are trained, validated, and logged in MLflow.
5. Selected models are deployed to the backend service.
6. The backend serves predictions via API.
7. The frontend visualizes predictions and operational KPIs.
8. User feedback and audit events feed back into future training cycles.

## Training Architecture

The training architecture is designed for repeatability and traceability.

* Offline pipelines ingest datasets from the `data/` folder.
* Preprocessing and feature engineering are implemented in dedicated module packages.
* Training jobs are tracked in MLflow with parameter, metric, and artifact logging.
* Models are registered and promoted through quality gates before production use.
* Evaluation metrics include accuracy, precision, recall, F1, RMSE, MAE, and MAPE depending on module type.

## Deployment Architecture

The deployment architecture is infrastructure-agnostic but container-centric.

* `docker-compose.yml` defines service dependencies and shared networks.
* `configs/env/development.env` and `configs/env/production.env` provide environment-specific configuration.
* `app/backend/Dockerfile` and `app/frontend/Dockerfile` package application runtime.
* `postgres` uses volumes for persistent storage.
* MLflow uses a mounted artifact volume for model persistence.

## Observability

The design includes observability at multiple layers:

* Request and inference logging in the backend.
* Metrics for request latency, model latency, and error rate.
* MLflow experiment tracking for model health and versioning.
* Structured logs for traceability and troubleshooting.
* Optional metrics stack (Prometheus + Grafana) for infrastructure monitoring.

## Security

Security design emphasizes least privilege and strong separation:

* Environment variables are used for secrets and credentials.
* The backend enforces input validation and authentication.
* Database access is limited to the backend service account.
* Services communicate over a trusted application network.
* No sensitive data is stored in plaintext in source control.

## Non-Functional Requirements

* Scalability: containerized services are horizontally scalable.
* Reliability: PostgreSQL and MLflow have persistent storage.
* Maintainability: modular codebase, clear naming, and documented architecture.
* Testability: unit, integration, ML, and end-to-end tests cover each layer.

## Operational Considerations

* CI/CD pipelines validate code, run tests, and build containers.
* ML pipelines use MLflow to capture reproducibility metadata.
* Local development uses `docker-compose up` with environment sample files.
* Production deployments may extend this design with orchestrators like Kubernetes.
