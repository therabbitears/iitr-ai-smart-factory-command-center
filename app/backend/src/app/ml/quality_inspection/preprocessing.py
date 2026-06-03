from __future__ import annotations

import logging
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)

NUMERIC_COLUMNS = [
    "X_Minimum",
    "X_Maximum",
    "Y_Minimum",
    "Y_Maximum",
    "Pixel_area",
    "Bare_Nuclei",
]

TARGET_COLUMN = "class"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw data: rename columns, drop duplicates, handle missing values.
    
    Args:
        df: Raw dataset
    
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna(subset=NUMERIC_COLUMNS + [TARGET_COLUMN])
    logger.info(f"Cleaned data shape: {df.shape}")
    return df


def validate_numeric_columns(df: pd.DataFrame) -> bool:
    """Validate that all numeric columns are present and numeric.
    
    Args:
        df: Dataset to validate
    
    Returns:
        True if valid
    
    Raises:
        ValueError: If columns missing or non-numeric
    """
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
    """Analyze class distribution in target variable.
    
    Args:
        y: Target labels
    
    Returns:
        Dictionary with class statistics
    """
    counts = y.value_counts()
    proportions = y.value_counts(normalize=True)
    balance = {
        "num_classes": int(len(counts)),
        "class_counts": counts.to_dict(),
        "class_proportions": proportions.to_dict(),
        "min_class_percent": float(proportions.min()),
        "max_class_percent": float(proportions.max()),
    }
    logger.info(f"Class balance: {balance}")
    return balance


def split_data(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train and test sets with stratification.
    
    Args:
        df: Dataset with features and target
        test_size: Proportion of data for test set
        random_state: Random seed
    
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    """
    validate_numeric_columns(df)
    X = df[NUMERIC_COLUMNS].copy()
    y = df[TARGET_COLUMN].astype(int).copy()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    logger.info(f"Train set: {X_train.shape}, Test set: {X_test.shape}")
    return X_train, X_test, y_train, y_test
