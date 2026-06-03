"""Simple model store utilities (local disk)."""
import os
import joblib
from typing import Any


def persist(pipeline: Any, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(pipeline, path)


def load(path: str):
    return joblib.load(path)


def path_for_registry(model_dir: str, model_name: str, version: str):
    """Return a local path where a registered model copy can be stored."""
    os.makedirs(model_dir, exist_ok=True)
    return os.path.join(model_dir, f"{model_name.replace(' ', '_')}_v{version}.pkl")
