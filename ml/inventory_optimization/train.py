"""Training helpers for Inventory Optimization models."""
from typing import Dict, Any
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def build_linear_pipeline() -> Pipeline:
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', LinearRegression())
    ])


def build_rf_pipeline(n_estimators: int = 200, random_state: int = 42) -> Pipeline:
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(n_estimators=n_estimators, random_state=random_state, n_jobs=-1))
    ])


def build_xgb_pipeline(params: Dict[str, Any] = None) -> Pipeline:
    params = params or {'n_estimators':200, 'max_depth':6, 'learning_rate':0.1, 'objective':'reg:squarederror', 'random_state':42}
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', XGBRegressor(**params))
    ])


def train_models(X, y):
    """Train three candidate models and return dict of trained pipelines and metrics placeholder."""
    models = {}

    lr = build_linear_pipeline()
    lr.fit(X, y)
    models['Linear Regression'] = lr

    rf = build_rf_pipeline()
    rf.fit(X, y)
    models['Random Forest'] = rf

    xgb = build_xgb_pipeline()
    xgb.fit(X, y)
    models['XGBoost'] = xgb

    return models


def save_model(pipeline, path: str):
    joblib.dump(pipeline, path)
