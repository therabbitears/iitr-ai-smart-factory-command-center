from __future__ import annotations

from typing import Any
import logging

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score

logger = logging.getLogger(__name__)


def compute_metrics(y_true: pd.Series | np.ndarray, y_pred: np.ndarray, y_proba: np.ndarray) -> dict[str, float]:
    """Compute classification metrics for model evaluation.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels (binary)
        y_proba: Predicted probabilities
    
    Returns:
        Dictionary of metrics suitable for imbalanced classification
    """
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1_score": float(f1_score(y_true, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, y_proba)),
    }


def predict_model(model: Any, X: pd.DataFrame | np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Generate predictions and probabilities from a model.
    
    Args:
        model: Trained classification model
        X: Feature data for prediction
    
    Returns:
        Tuple of (binary predictions, predicted probabilities)
    """
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X)[:, 1]
        predictions = (probabilities >= 0.5).astype(int)
    else:
        probabilities = model.predict(X).ravel()
        predictions = (probabilities >= 0.5).astype(int)

    return predictions, probabilities


def compare_models(models: dict[str, Any], X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    """Compare performance of multiple models on test set.
    
    Args:
        models: Dictionary of trained models
        X_test: Test features
        y_test: Test labels
    
    Returns:
        DataFrame with model names and their metrics, sorted by F1 score
    """
    rows: list[dict[str, float | str]] = []
    for name, model in models.items():
        try:
            y_pred, y_proba = predict_model(model, X_test)
            metrics = compute_metrics(y_test, y_pred, y_proba)
            rows.append({"model": name, **metrics})
            logger.info(f"Model {name} evaluation complete: F1={metrics['f1_score']:.4f}")
        except Exception as e:
            logger.error(f"Failed to evaluate model {name}: {str(e)}")
            raise

    return pd.DataFrame(rows).sort_values(by="f1_score", ascending=False).reset_index(drop=True)
