from __future__ import annotations

from typing import Any
import logging

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

logger = logging.getLogger(__name__)


def compute_metrics(
    y_true: pd.Series | np.ndarray,
    y_pred: np.ndarray,
    y_proba: np.ndarray | None = None,
) -> dict[str, float]:
    """Compute classification metrics for multi-class evaluation.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_proba: Predicted probabilities (optional for weighted F1)
    
    Returns:
        Dictionary of metrics
    """
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision_macro": float(precision_score(y_true, y_pred, average="macro", zero_division=0)),
        "precision_weighted": float(precision_score(y_true, y_pred, average="weighted", zero_division=0)),
        "recall_macro": float(recall_score(y_true, y_pred, average="macro", zero_division=0)),
        "recall_weighted": float(recall_score(y_true, y_pred, average="weighted", zero_division=0)),
        "f1_macro": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "f1_weighted": float(f1_score(y_true, y_pred, average="weighted", zero_division=0)),
    }


def predict_model(model: Any, X: pd.DataFrame | np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Generate predictions and probabilities from a model.
    
    Args:
        model: Trained classification model
        X: Feature data for prediction
    
    Returns:
        Tuple of (predictions, probabilities)
    """
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X)
        predictions = model.predict(X)
    else:
        # ANN returns probabilities directly
        probabilities = model.predict(X, verbose=0)
        predictions = np.argmax(probabilities, axis=1)

    return predictions, probabilities


def compare_models(
    models: dict[str, Any],
    X_test: pd.DataFrame,
    y_test: pd.Series,
) -> pd.DataFrame:
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
            logger.info(f"Model {name} evaluation complete: F1={metrics['f1_weighted']:.4f}")
        except Exception as e:
            logger.error(f"Failed to evaluate model {name}: {str(e)}")
            raise

    return pd.DataFrame(rows).sort_values(by="f1_weighted", ascending=False).reset_index(drop=True)
