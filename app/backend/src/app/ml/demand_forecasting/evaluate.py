from __future__ import annotations

from typing import Any
import logging

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

logger = logging.getLogger(__name__)


def compute_metrics(
    y_true: np.ndarray | pd.Series,
    y_pred: np.ndarray,
) -> dict[str, float]:
    """Compute regression metrics.
    
    Args:
        y_true: True values
        y_pred: Predicted values
    
    Returns:
        Dictionary of regression metrics
    """
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()
    
    # Ensure same length
    min_len = min(len(y_true), len(y_pred))
    y_true = y_true[:min_len]
    y_pred = y_pred[:min_len]
    
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    mae = float(mean_absolute_error(y_true, y_pred))
    mape = float(np.mean(np.abs((y_true - y_pred) / (np.abs(y_true) + 1e-6)))) * 100
    r2 = float(r2_score(y_true, y_pred))
    
    return {
        'rmse': rmse,
        'mae': mae,
        'mape': mape,
        'r2': r2,
    }


def predict_model(model: Any, X: np.ndarray | pd.DataFrame) -> np.ndarray:
    """Generate predictions from a model.
    
    Args:
        model: Trained regressor or LSTM model
        X: Feature data for prediction
    
    Returns:
        Predictions array
    """
    if hasattr(model, 'predict'):
        # sklearn model
        predictions = model.predict(X)
    else:
        # Keras LSTM model
        if len(X.shape) == 2:
            X = X.reshape((X.shape[0], X.shape[1], 1))
        predictions = model.predict(X, verbose=0)
    
    return predictions.flatten()


def compare_models(
    models: dict[str, Any],
    X_test: np.ndarray | pd.DataFrame,
    y_test: np.ndarray | pd.Series,
) -> pd.DataFrame:
    """Compare performance of multiple regressor models.
    
    Args:
        models: Dictionary of trained models
        X_test: Test features
        y_test: Test targets
    
    Returns:
        DataFrame with model names and metrics, sorted by R2
    """
    rows: list[dict[str, float | str]] = []
    
    for name, model in models.items():
        try:
            y_pred = predict_model(model, X_test)
            metrics = compute_metrics(y_test, y_pred)
            rows.append({'model': name, **metrics})
            logger.info(f"Model {name} evaluation: R2={metrics['r2']:.4f}, RMSE={metrics['rmse']:.4f}")
        except Exception as e:
            logger.error(f"Failed to evaluate model {name}: {str(e)}")
            raise
    
    return pd.DataFrame(rows).sort_values(by='r2', ascending=False).reset_index(drop=True)


def forecast_future(
    model: Any,
    X_test: np.ndarray,
    y_test: np.ndarray | None = None,
) -> dict[str, np.ndarray | float]:
    """Generate predictions and compute metrics if targets provided.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Optional test targets for metric computation
    
    Returns:
        Dictionary with predictions and optionally metrics
    """
    y_pred = predict_model(model, X_test)
    
    result = {'predictions': y_pred}
    
    if y_test is not None:
        metrics = compute_metrics(y_test, y_pred)
        result.update(metrics)
        logger.info(f"Forecast evaluation: R2={metrics['r2']:.4f}, RMSE={metrics['rmse']:.4f}")
    
    return result
