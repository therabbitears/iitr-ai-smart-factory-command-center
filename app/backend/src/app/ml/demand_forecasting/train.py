from __future__ import annotations

from typing import Any
import logging

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow as tf

logger = logging.getLogger(__name__)


def build_linear_regression() -> Pipeline:
    """Build Linear Regression pipeline for demand forecasting.
    
    Returns:
        sklearn Pipeline
    """
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', LinearRegression())
    ])


def build_random_forest() -> Pipeline:
    """Build Random Forest Regressor pipeline.
    
    Returns:
        sklearn Pipeline
    """
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(
            n_estimators=200,
            max_depth=20,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        ))
    ])


def build_xgboost() -> Pipeline:
    """Build XGBoost Regressor pipeline.
    
    Returns:
        sklearn Pipeline
    """
    return Pipeline([
        ('scaler', StandardScaler()),
        ('model', XGBRegressor(
            n_estimators=200,
            max_depth=8,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            objective='reg:squarederror',
            random_state=42,
            n_jobs=-1,
            verbosity=0
        ))
    ])


def build_lstm_model(input_shape: int) -> Any:
    """Build LSTM model for sequence-to-sequence demand forecasting.
    
    Args:
        input_shape: Number of features (lookback window size)
    
    Returns:
        Compiled Keras Sequential model
    """
    model = Sequential([
        LSTM(128, activation='relu', return_sequences=True, input_shape=(input_shape, 1)),
        Dropout(0.2),
        LSTM(64, activation='relu', return_sequences=False),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dropout(0.1),
        Dense(1)
    ])
    
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='mse',
        metrics=['mae']
    )
    logger.info(f"Built LSTM model with input_shape={input_shape}")
    return model


def train_lstm(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    epochs: int = 100,
    batch_size: int = 32,
) -> Any:
    """Train LSTM model with early stopping.
    
    Args:
        X_train: Training sequences (samples, lookback, features)
        y_train: Training targets
        X_val: Validation sequences
        y_val: Validation targets
        epochs: Maximum training epochs
        batch_size: Batch size for training
    
    Returns:
        Trained Keras model
    """
    # Reshape for LSTM (samples, lookback, 1)
    X_train_lstm = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_val_lstm = X_val.reshape((X_val.shape[0], X_val.shape[1], 1))
    
    model = build_lstm_model(X_train.shape[1])
    
    callback = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    )
    
    history = model.fit(
        X_train_lstm,
        y_train,
        validation_data=(X_val_lstm, y_val),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=[callback],
        verbose=0
    )
    
    logger.info(f"LSTM training complete: epochs={len(history.epoch)}")
    return model


def build_regressors() -> dict[str, Any]:
    """Build dictionary of regressor models.
    
    Returns:
        Dict mapping model names to sklearn Pipeline/Keras objects
    """
    return {
        'linear_regression': build_linear_regression(),
        'random_forest': build_random_forest(),
        'xgboost': build_xgboost(),
    }
