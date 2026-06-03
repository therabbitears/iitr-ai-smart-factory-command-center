"""MLflow integration utilities for Inventory Optimization.

Provides experiment tracking, model registration, versioning, artifact handling, and promotion helpers.
"""
from typing import Dict, Any
import os
from sklearn.base import BaseEstimator
import numpy as np
from .evaluate import compute_metrics

# Try optional MLflow imports; provide graceful fallback when MLflow isn't installed.
try:
    import mlflow
    import mlflow.sklearn
    from mlflow.tracking import MlflowClient
    _MLFLOW_AVAILABLE = True
except Exception:
    _MLFLOW_AVAILABLE = False


def init_mlflow(tracking_uri: str = None, experiment_name: str = 'Inventory-Optimization'):
    if not _MLFLOW_AVAILABLE:
        # fallback: ensure local artifact folder exists
        os.makedirs('mlruns_local', exist_ok=True)
        return None
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)
    return MlflowClient()


def log_and_register_models(models: Dict[str, BaseEstimator], X_test, y_test, feature_columns, model_dir: str,
                            registry_prefix: str = 'InventoryOptimization') -> Dict[str, Dict[str, Any]]:
    """Log each model to MLflow, register it, and return registration metadata.

    - models: dict name->trained estimator (could be sklearn Pipeline)
    - X_test/y_test: arrays for evaluation and sample predictions
    - feature_columns: list of feature names
    - model_dir: local directory to also persist copies
    - registry_prefix: prefix for registry model names
    """
    client = MlflowClient() if _MLFLOW_AVAILABLE else None
    results = {}

    for name, model in models.items():
        # compute metrics
        y_pred = model.predict(X_test)
        metrics = compute_metrics(y_test, y_pred)

        if _MLFLOW_AVAILABLE:
            with mlflow.start_run(run_name=name) as run:
                run_id = run.info.run_id
                # log metrics and params
                for k, v in metrics.items():
                    mlflow.log_metric(k, float(v))
                mlflow.log_param('model_name', name)
                mlflow.log_param('n_test_samples', int(len(y_test)))
                mlflow.log_param('n_features', int(len(feature_columns)))

                artifact_path = 'model'
                try:
                    mlflow.sklearn.log_model(model, artifact_path)
                except Exception:
                    import joblib
                    local_path = os.path.join(model_dir, f'{name.replace(" ", "_")}.pkl')
                    os.makedirs(os.path.dirname(local_path), exist_ok=True)
                    joblib.dump(model, local_path)
                    mlflow.log_artifact(local_path, artifact_path)

                # register model
                model_name = f"{registry_prefix}-{name.replace(' ', '_')}"
                try:
                    client.create_registered_model(model_name)
                except Exception:
                    pass

                model_uri = f"runs:/{run_id}/{artifact_path}"
                mv = client.create_model_version(name=model_name, source=model_uri, run_id=run_id)
                client.transition_model_version_stage(name=model_name, version=mv.version, stage='Staging', archive_existing_versions=False)

                results[name] = {
                    'run_id': run_id,
                    'metrics': metrics,
                    'model_name': model_name,
                    'version': mv.version,
                    'stage': 'Staging'
                }
        else:
            # MLflow not available: persist locally and write summary
            import joblib, json
            local_path = os.path.join(model_dir, f'{name.replace(" ", "_")}.pkl')
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            joblib.dump(model, local_path)
            # fake registry info
            info = {
                'run_id': None,
                'metrics': metrics,
                'model_name': f'local-{registry_prefix}-{name.replace(" ", "_")}',
                'version': 'local',
                'stage': 'None',
                'local_path': local_path
            }
            # write a small JSON summary next to model
            with open(local_path + '.meta.json', 'w') as f:
                json.dump(info, f, indent=2)
            results[name] = info

    return results


def promote_model(model_name: str, version: str, target_stage: str = 'Production'):
    if not _MLFLOW_AVAILABLE:
        raise RuntimeError('MLflow not available in this environment')
    client = MlflowClient()
    client.transition_model_version_stage(name=model_name, version=version, stage=target_stage, archive_existing_versions=True)
    return True
