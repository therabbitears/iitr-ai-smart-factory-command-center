"""Prometheus metrics helpers with graceful fallback when prometheus_client is unavailable."""
import time
from typing import Optional

try:
    from prometheus_client import Counter, Histogram
    _PROM_AVAILABLE = True
except Exception:
    _PROM_AVAILABLE = False


if _PROM_AVAILABLE:
    REQUEST_COUNT = Counter('api_request_count', 'API Request Count', ['endpoint', 'method', 'http_status'])
    MODEL_LATENCY = Histogram('model_latency_seconds', 'Model inference latency seconds', ['model'])
    PREDICTION_VOLUME = Counter('prediction_volume_total', 'Total predictions made', ['model'])
    ERROR_COUNT = Counter('api_error_count', 'API error count', ['endpoint', 'exception'])
else:
    REQUEST_COUNT = MODEL_LATENCY = PREDICTION_VOLUME = ERROR_COUNT = None


def observe_model_latency(model_name: str, seconds: float):
    if _PROM_AVAILABLE and MODEL_LATENCY:
        MODEL_LATENCY.labels(model=model_name).observe(seconds)


def inc_prediction_volume(model_name: str, n: int = 1):
    if _PROM_AVAILABLE and PREDICTION_VOLUME:
        PREDICTION_VOLUME.labels(model=model_name).inc(n)


def inc_error(endpoint: str, exc_name: str):
    if _PROM_AVAILABLE and ERROR_COUNT:
        ERROR_COUNT.labels(endpoint=endpoint, exception=exc_name).inc()


def timed_model(model_name: str):
    class Timer:
        def __enter__(self_inner):
            self_inner.t0 = time.time()
            return self_inner

        def __exit__(self_inner, exc_type, exc, tb):
            elapsed = time.time() - self_inner.t0
            observe_model_latency(model_name, elapsed)

    return Timer()
