from __future__ import annotations
from pathlib import Path
from typing import Any

import mlflow
import mlflow.keras
import mlflow.sklearn
import tensorflow as tf

from app.core.config import settings


class ModelStore:
    """Provides MLflow integration and model persistence."""

    def __init__(self) -> None:
        mlflow.set_tracking_uri(str(settings.mlflow_tracking_uri))
        mlflow.set_experiment(settings.mlflow_experiment_name)
        self.artifact_root = Path(settings.model_registry_path)
        self.artifact_root.mkdir(parents=True, exist_ok=True)

    def log_run(
        self,
        model_name: str,
        model: Any,
        params: dict[str, Any],
        metrics: dict[str, float],
        artifact_path: str = "model",
    ) -> str:
        with mlflow.start_run(run_name=model_name):
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)
            if isinstance(model, tf.keras.Model):
                mlflow.keras.log_model(model, artifact_path)
            else:
                mlflow.sklearn.log_model(model, artifact_path)
            artifact_uri = mlflow.get_artifact_uri(artifact_path)
        return artifact_uri

    def persist_best_model(self, best_model: Any, model_name: str) -> Path:
        target_path = self.artifact_root / "predictive_maintenance" / model_name
        target_path.mkdir(parents=True, exist_ok=True)
        if isinstance(best_model, tf.keras.Model):
            mlflow.keras.save_model(best_model, str(target_path / "model"))
        else:
            mlflow.sklearn.save_model(best_model, str(target_path / "model"))
        return target_path
