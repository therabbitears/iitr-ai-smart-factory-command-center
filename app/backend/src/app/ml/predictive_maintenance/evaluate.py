from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def compute_metrics(y_true: pd.Series | np.ndarray, y_pred: np.ndarray, y_proba: np.ndarray) -> dict[str, float]:
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1_score": float(f1_score(y_true, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, y_proba)),
    }


def predict_model(model: Any, X: pd.DataFrame | np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X)[:, 1]
        predictions = (probabilities >= 0.5).astype(int)
    else:
        probabilities = model.predict(X).ravel()
        predictions = (probabilities >= 0.5).astype(int)

    return predictions, probabilities


def compare_models(models: dict[str, Any], X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    rows: list[dict[str, float | str]] = []
    for name, model in models.items():
        y_pred, y_proba = predict_model(model, X_test)
        metrics = compute_metrics(y_test, y_pred, y_proba)
        rows.append({"model": name, **metrics})

    return pd.DataFrame(rows).sort_values(by="f1_score", ascending=False).reset_index(drop=True)
