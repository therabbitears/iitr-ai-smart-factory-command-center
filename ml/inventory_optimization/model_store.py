"""Simple model store utilities (local disk)."""
import os
import joblib


def persist(pipeline, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(pipeline, path)


def load(path: str):
    return joblib.load(path)
