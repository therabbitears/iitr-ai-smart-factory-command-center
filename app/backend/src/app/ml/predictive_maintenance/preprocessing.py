from __future__ import annotations

import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)

NUMERIC_COLUMNS = [
    "air_temperature",
    "process_temperature",
    "rotational_speed",
    "torque",
    "tool_wear",
]

TARGET_COLUMN = "machine_failure"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw data: rename columns, drop duplicates, handle timestamps."""
    df = df.copy()
    df = df.rename(columns={"machine_failure": TARGET_COLUMN})
    df = df.drop_duplicates()

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

    df = df.dropna(subset=NUMERIC_COLUMNS + [TARGET_COLUMN])
    logger.info(f"Cleaned data shape: {df.shape}")
    return df


def validate_numeric_columns(df: pd.DataFrame) -> bool:
    """Validate that all numeric columns are present and numeric."""
    missing = [col for col in NUMERIC_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    non_numeric = [
        col for col in NUMERIC_COLUMNS
        if not pd.api.types.is_numeric_dtype(df[col])
    ]
    if non_numeric:
        raise ValueError(f"Non-numeric columns: {non_numeric}")
    return True


def analyze_class_balance(y: pd.Series) -> dict[str, float]:
    """Analyze class distribution in target variable."""
    counts = y.value_counts()
    proportions = y.value_counts(normalize=True)
    balance = {
        "class_0_count": int(counts.get(0, 0)),
        "class_1_count": int(counts.get(1, 0)),
        "class_0_percent": float(proportions.get(0, 0)),
        "class_1_percent": float(proportions.get(1, 0)),
        "imbalance_ratio": float(counts.get(1, 0) / max(counts.get(0, 1), 1)),
    }
    logger.info(f"Class balance: {balance}")
    return balance


def split_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train and test sets with stratification."""
    validate_numeric_columns(df)
    X = df[NUMERIC_COLUMNS].copy()
    y = df[TARGET_COLUMN].astype(int).copy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    logger.info(f"Train set: {X_train.shape}, Test set: {X_test.shape}")
    return X_train, X_test, y_train, y_test
