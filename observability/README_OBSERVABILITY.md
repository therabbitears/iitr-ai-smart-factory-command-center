# Observability Stack

This folder contains configuration to run a local observability stack for the Smart Factory Command Center.

Components:
- Prometheus: metrics scraping and storage (port 9090)
- Grafana: dashboards (port 3000)
- Jaeger: tracing UI (port 16686)
- OpenTelemetry Collector: OTLP receiver and exporters
- ELK: Elasticsearch (9200), Kibana (5601), Logstash (5000)

Quick start (requires Docker):

```bash
cd observability
docker-compose up -d
```

Notes:
- Prometheus scrapes the FastAPI `/metrics` endpoint. When running locally in Docker, `host.docker.internal:8000` is the default target (adjust if your API runs elsewhere).
- OTEL Collector listens on gRPC OTLP (4317) and forwards traces to Jaeger and metrics to Prometheus.
- Logstash listens on TCP 5000 for JSON logs and forwards to Elasticsearch. Configure your app to emit JSON logs to `host.docker.internal:5000`.
