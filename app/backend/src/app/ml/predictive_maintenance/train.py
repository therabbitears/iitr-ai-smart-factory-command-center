from __future__ import annotations

from typing import Any
import logging

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

logger = logging.getLogger(__name__)


def build_ann_model(input_shape: int) -> Any:
    """Build a neural network model for binary classification.
    
    Args:
        input_shape: Number of input features
    
    Returns:
        Compiled Keras sequential model
    """
    model = Sequential(
        [
            Dense(64, activation="relu", input_shape=(input_shape,)),
            Dropout(0.2),
            Dense(32, activation="relu"),
            Dropout(0.1),
            Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    logger.info(f"Built ANN model with input_shape={input_shape}")
    return model


def build_classifiers(random_state: int = 42) -> dict[str, Any]:
    """Build a dictionary of candidate classifier models.
    
    Args:
        random_state: Random seed for reproducibility
    
    Returns:
        Dict mapping model names to sklearn Pipeline objects
    """
    return {
        "logistic_regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "classifier",
                    LogisticRegression(
                        solver="liblinear",
                        penalty="l2",
                        random_state=random_state,
                        max_iter=1000,
                    ),
                ),
            ]
        ),
        "random_forest": Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "classifier",
                    RandomForestClassifier(
                        n_estimators=200,
                        max_depth=12,
                        random_state=random_state,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "xgboost": Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "classifier",
                    XGBClassifier(
                        n_estimators=200,
                        max_depth=6,
                        learning_rate=0.1,
                        use_label_encoder=False,
                        eval_metric="logloss",
                        random_state=random_state,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
    }


def train_ann(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    epochs: int = 50,
    batch_size: int = 32,
) -> Any:
    """Train a neural network with early stopping.
    
    Args:
        X_train: Training features
        y_train: Training labels
        X_val: Validation features
        y_val: Validation labels
        epochs: Maximum number of training epochs
        batch_size: Batch size for training
    
    Returns:
        Trained Keras model
    """
    model = build_ann_model(X_train.shape[1])
    callback = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
    history = model.fit(
        X_train,
        y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=[callback],
        verbose=0,
    )
    logger.info(f"ANN training complete: epochs trained={len(history.epoch)}")
    return model
