"""Evaluation helpers for Inventory Optimization."""
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def compute_metrics(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {'rmse': rmse, 'mae': mae, 'r2': r2}


def compare_models(models: dict, X_test, y_test) -> pd.DataFrame:
    records = []
    for name, model in models.items():
        y_pred = model.predict(X_test)
        m = compute_metrics(y_test, y_pred)
        records.append({'model': name, 'rmse': m['rmse'], 'mae': m['mae'], 'r2': m['r2']})
    df = pd.DataFrame(records).sort_values('r2', ascending=False).reset_index(drop=True)
    return df
