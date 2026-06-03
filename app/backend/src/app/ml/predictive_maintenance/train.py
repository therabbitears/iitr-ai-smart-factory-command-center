from __future__ import annotations

from typing import Any

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

NUMERIC_COLUMNS = [
    "air_temperature",
    "process_temperature",
    "rotational_speed",
    "torque",
    "tool_wear",
    "temp_delta",
    "wear_rate",
    "torque_ratio",
    "temperature_ratio",
]


def build_ann_model(input_shape: int) -> Any:
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
    return model


def build_classifiers(random_state: int = 42) -> dict[str, Any]:
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
    X_train: "np.ndarray",
    y_train: "np.ndarray",
    X_val: "np.ndarray",
    y_val: "np.ndarray",
    epochs: int = 50,
    batch_size: int = 32,
) -> Any:
    model = build_ann_model(X_train.shape[1])
    callback = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
    model.fit(
        X_train,
        y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        callbacks=[callback],
        verbose=0,
    )
    return model
