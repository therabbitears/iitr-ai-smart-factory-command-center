from __future__ import annotations

import logging
from pathlib import Path

import mlflow
import mlflow.sklearn
import mlflow.keras
import joblib

logger = logging.getLogger(__name__)


class ModelStore:
    """Manage model persistence and MLflow tracking for demand forecasting."""

    def __init__(self, mlflow_uri: str = "./mlruns") -> None:
        self.mlflow_uri = mlflow_uri
        mlflow.set_tracking_uri(self.mlflow_uri)
        logger.info(f"ModelStore initialized with MLflow URI: {self.mlflow_uri}")

    def log_run(
        self,
        model_name: str,
        model_version: str,
        dataset: str,
        best_model_name: str,
        metrics: dict,
        all_model_metrics: list[dict] | None = None,
    ) -> None:
        """Log experiment run to MLflow.
        
        Args:
            model_name: Pipeline name
            model_version: Model version string
            dataset: Dataset name
            best_model_name: Name of best model
            metrics: Best model metrics dictionary
            all_model_metrics: Metrics for all models (optional)
        """
        with mlflow.start_run(run_name=model_name):
            mlflow.log_param("model_version", model_version)
            mlflow.log_param("dataset", dataset)
            mlflow.log_param("best_model", best_model_name)

            for metric_name, metric_value in metrics.items():
                if isinstance(metric_value, (int, float)):
                    mlflow.log_metric(metric_name, metric_value)

            if all_model_metrics:
                mlflow.log_dict({"model_comparison": all_model_metrics}, "model_comparison.json")

            logger.info(f"Logged run to MLflow: {model_name}")

    def persist_best_model(
        self,
        model,
        model_name: str,
        pipeline_name: str,
    ) -> dict[str, str]:
        """Persist best model to disk and MLflow.
        
        Args:
            model: Trained model (sklearn or Keras)
            model_name: Name of the model
            pipeline_name: Name of the pipeline
        
        Returns:
            Dictionary with artifact paths
        """
        model_dir = Path(__file__).parent.parent.parent.parent.parent / "models" / pipeline_name
        model_dir.mkdir(parents=True, exist_ok=True)

        artifacts = {}

        try:
            if hasattr(model, "predict") and not hasattr(model, "fit"):
                # Keras model
                model_path = model_dir / f"{model_name}_model.h5"
                model.save(str(model_path))
                logger.info(f"Persisted Keras model: {model_path}")
                artifacts["model_path"] = str(model_path)
            else:
                # sklearn or sklearn Pipeline
                model_path = model_dir / f"{model_name}_model.pkl"
                joblib.dump(model, str(model_path))
                logger.info(f"Persisted sklearn model: {model_path}")
                artifacts["model_path"] = str(model_path)

        except Exception as e:
            logger.error(f"Failed to persist model: {str(e)}")
            raise

        return artifacts
