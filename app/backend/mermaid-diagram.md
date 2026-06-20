flowchart LR

%% =====================================================
%% SMART FACTORY COMMAND CENTER
%% Enterprise Architecture
%% =====================================================

%% -------------------------------
%% LAYER 1 - DATA SOURCES
%% -------------------------------

subgraph DS["Layer 1 - Data Sources (Kaggle Datasets)"]
    PM["AI4I 2020 Predictive Maintenance
    CSV Telemetry Data"]

    QI["Steel Plates Faults
    Defect Classification Data"]

    DF["Store Item Demand Forecasting
    Sales Time Series"]

    IO["Supply Chain Analytics
    Inventory & Warehouse Data"]
end

%% -------------------------------
%% LAYER 2 - DATA PROCESSING
%% -------------------------------

subgraph DP["Layer 2 - Data Processing & ML Platform"]

    ING["Data Ingestion
    Pandera Validation
    Data Profiling
    Quality Rules"]

    RAW["Raw Data Layer
    data/raw/..."]

    PRE["Preprocessing
    Cleaning
    Aggregation
    Normalization"]

    FE["Feature Engineering
    Lag Features
    Rolling Windows
    Cyclical Encoding
    Domain Features"]

    FS["Feature Store"]

    SPLIT["Train / Validation / Test Split"]

    %% Predictive Maintenance
    subgraph PMM["Predictive Maintenance"]
        PM_LR["Linear Regression"]
        PM_RF["Random Forest"]
        PM_XGB["XGBoost"]
        PM_LSTM["ANN / LSTM"]
    end

    %% Quality
    subgraph QMM["Quality Inspection"]
        Q_LR["Logistic Regression"]
        Q_RF["Random Forest"]
        Q_XGB["XGBoost"]
        Q_CNN["CNN ResNet50"]
        Q_ANN["ANN"]
    end

    %% Demand Forecasting
    subgraph DMM["Demand Forecasting"]
        D_LR["Linear Regression"]
        D_RF["Random Forest"]
        D_XGB["XGBoost"]
        D_LSTM["LSTM"]
        D_NV["Naive Baseline"]
    end

    %% Inventory Optimization
    subgraph IMM["Inventory Optimization"]
        I_LR["Linear Regression"]
        I_RF["Random Forest"]
        I_XGB["XGBoost"]
        I_H["Heuristic Risk Engine"]
    end

    EVAL["Model Evaluation
    Metrics Comparison
    Champion Selection"]

    MLFLOW["MLflow Registry
    Experiment Tracking
    Model Versioning
    Staging -> Production"]

    ART["Model Artifacts
    Pickle
    JSON Metadata
    S3 / Azure Blob"]

end

%% -------------------------------
%% API LAYER
%% -------------------------------

subgraph API["Layer 3 - FastAPI Service Layer"]
    
    FASTAPI["FastAPI 0.110
    Uvicorn
    Port 8000"]

    VALID["Pydantic v2
    DTO Validation
    Dependency Injection"]

    EP1["POST /api/predict-maintenance"]
    EP2["POST /api/predict-quality"]
    EP3["POST /api/forecast-demand"]
    EP4["POST /api/inventory-risk"]

    HEALTH["GET /healthz"]
    METRICS["GET /metrics"]

end

%% -------------------------------
%% FRONTEND
%% -------------------------------

subgraph UI["Layer 4 - React Frontend"]
    
    REACT["React 18 + Vite 5
    Port 5173
    Axios + Router"]

    EXEC["Executive Dashboard"]
    MAINT["Maintenance Dashboard"]
    QUAL["Quality Dashboard"]
    FORE["Forecast Dashboard"]
    INV["Inventory Dashboard"]

    MUI["Material UI"]
    CHARTS["Recharts"]
end

%% -------------------------------
%% OBSERVABILITY
%% -------------------------------

subgraph OBS["Layer 5 - Observability Platform"]

    OTEL["OpenTelemetry Collector
    OTLP gRPC :4317
    Metrics :8888"]

    PROM["Prometheus
    :9090"]

    GRAF["Grafana
    :3000"]

    JAEGER["Jaeger
    :16686"]

    LOGSTASH["Logstash
    TCP :5000"]

    ELASTIC["Elasticsearch
    :9200"]

    KIBANA["Kibana
    :5601"]

end

%% -------------------------------
%% DEPLOYMENT
%% -------------------------------

subgraph DEP["Deployment & Runtime"]

    DOCKER["Docker
    Python 3.12 Slim"]

    K8S["Kubernetes
    Deployments
    Services
    HPA"]

    HELM["Helm Charts"]

    IAC["Terraform /
    CloudFormation"]

    CICD["GitHub Actions
    GitLab CI"]

end

%% -------------------------------
%% FLOWS
%% -------------------------------

PM --> ING
QI --> ING
DF --> ING
IO --> ING

ING --> RAW
RAW --> PRE
PRE --> FE
FE --> FS
FS --> SPLIT

SPLIT --> PMM
SPLIT --> QMM
SPLIT --> DMM
SPLIT --> IMM

PMM --> EVAL
QMM --> EVAL
DMM --> EVAL
IMM --> EVAL

EVAL --> MLFLOW
MLFLOW --> ART

ART --> FASTAPI

VALID --> FASTAPI

FASTAPI --> EP1
FASTAPI --> EP2
FASTAPI --> EP3
FASTAPI --> EP4
FASTAPI --> HEALTH
FASTAPI --> METRICS

REACT --> FASTAPI

REACT --> EXEC
REACT --> MAINT
REACT --> QUAL
REACT --> FORE
REACT --> INV

REACT --> MUI
REACT --> CHARTS

%% Observability

FASTAPI --> OTEL
OTEL --> PROM
PROM --> GRAF

FASTAPI --> LOGSTASH
LOGSTASH --> ELASTIC
ELASTIC --> KIBANA

FASTAPI --> JAEGER
OTEL --> JAEGER

PROM -.scrapes.-> METRICS

%% Deployment

DOCKER --> FASTAPI
DOCKER --> REACT

K8S --> FASTAPI
K8S --> REACT

HELM --> K8S
IAC --> K8S
CICD --> K8S

%% Styling

classDef data fill:#d9ecff,stroke:#1f77b4,color:#000;
classDef backend fill:#d5f5d5,stroke:#2e8b57,color:#000;
classDef frontend fill:#ffe6cc,stroke:#ff8c00,color:#000;
classDef obs fill:#eadcff,stroke:#8a2be2,color:#000;

class PM,QI,DF,IO,ING,RAW,PRE,FE,FS,SPLIT,PMM,QMM,DMM,IMM,EVAL,MLFLOW,ART data;
class FASTAPI,VALID,EP1,EP2,EP3,EP4,HEALTH,METRICS backend;
class REACT,EXEC,MAINT,QUAL,FORE,INV,MUI,CHARTS frontend;
class OTEL,PROM,GRAF,JAEGER,LOGSTASH,ELASTIC,KIBANA obs;