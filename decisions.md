# Smart Factory Command Center Architecture Decisions

## Decision Log

### 1. Architecture Pattern

* Decision: Use a modular containerized architecture with separate frontend, backend, database, and ML tracking services.
* Rationale: Provides clear service boundaries, independent development, and simpler deployment.
* Alternatives considered: monolithic full-stack app, serverless-only architecture.

### 2. Backend Framework

* Decision: FastAPI for the backend API.
* Rationale: FastAPI supports async I/O, automatic validation with Pydantic, and quick API iteration.
* Alternatives considered: Flask, Django REST Framework.

### 3. Frontend Stack

* Decision: React with Material UI.
* Rationale: React provides responsive SPA capabilities and Material UI accelerates dashboard development.
* Alternatives considered: Vue, Angular, plain HTML.

### 4. Machine Learning Frameworks

* Decision: Use Scikit-Learn, XGBoost, and TensorFlow/Keras.
* Rationale: Scikit-Learn is ideal for tabular ML pipelines; XGBoost delivers strong performance for structured data; TensorFlow/Keras supports advanced neural architectures.
* Alternatives considered: PyTorch, LightGBM.

### 5. Model Registry and MLOps

* Decision: MLflow for experiment tracking and model registry.
* Rationale: MLflow is lightweight, integrates with Python pipelines, and supports versioned model artifacts.
* Alternatives considered: Kubeflow, SageMaker, DVC alone.

### 6. Database Choice

* Decision: PostgreSQL for persistence.
* Rationale: PostgreSQL is reliable, supports relational queries, and is easy to containerize.
* Alternatives considered: MySQL, SQLite, NoSQL stores.

### 7. Configuration Strategy

* Decision: Centralize config in `configs/env/*.env` and use a root `.env.example`.
* Rationale: Keeps environment-specific values distinct from code and supports local, staging, and production environments.
* Alternatives considered: config.py-only, hardcoded settings.

### 8. Logging Strategy

* Decision: Structured logging with request correlation IDs.
* Rationale: Structured logs enhance observability, filtering, and downstream analysis.
* Alternatives considered: plain text logs without structure.

### 9. Testing Strategy

* Decision: Separate tests into unit, integration, ML, and end-to-end suites.
* Rationale: Enables precise coverage across backend logic, data pipelines, model behavior, and user workflows.
* Alternatives considered: single test suite.

### 10. Deployment Strategy

* Decision: Use Docker Compose for local development and baseline deployment.
* Rationale: Docker Compose simplifies service orchestration and aligns with infrastructure-as-code principles.
* Alternatives considered: direct VM deployment, Kubernetes from day one.

### 11. Security Approach

* Decision: Protect all service credentials through environment variables and maintain least privilege for database access.
* Rationale: Minimizes risk from leaked credentials and prevents over-permissioned services.
* Alternatives considered: embedding credentials in configs, no RBAC enforcement.

### 12. Observability Approach

* Decision: Support structured application logging, metrics, and MLflow experiment visibility.
* Rationale: Observability is essential for diagnosing production incidents and validating model quality.
* Alternatives considered: no observability tools beyond basic logs.

## Summary of Key Decisions

* Modular service boundaries reduce coupling between frontend, backend, ML, and data stores.
* Data flows should maintain separation between training pipelines and inference serving.
* MLflow is the primary source of truth for model experiments and registry state.
* Docker-based deployment provides a reproducible runtime for development and early production.
* Security is enforced through environment isolation, request validation, and network boundaries.
* Documentation and test structure support maintainability and team collaboration.
