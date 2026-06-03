from __future__ import annotations

from __future__ import annotations

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw demand data: remove duplicates, handle missing values.
    
    Args:
        df: Raw demand data
    
    Returns:
        Cleaned DataFrame
    """
    df = df.copy()
    initial_len = len(df)
    
    # Remove duplicates by (date, store, item)
    df = df.drop_duplicates(subset=["date", "store", "item"], keep="first")
    logger.info(f"Removed {initial_len - len(df)} duplicate rows")
    
    # Drop rows with missing demand
    df = df.dropna(subset=["demand"])
    logger.info(f"Dropped {initial_len - len(df)} rows with missing demand")
    
    return df


def validate_demand_column(df: pd.DataFrame) -> bool:
    """Validate that demand column is numeric and non-negative.
    
    Args:
        df: Demand data
    
    Returns:
        True if valid
    
    Raises:
        ValueError: If validation fails
    """
    if "demand" not in df.columns:
        raise ValueError("'demand' column not found")
    
    if not pd.api.types.is_numeric_dtype(df["demand"]):
        raise ValueError("'demand' column must be numeric")
    
    if (df["demand"] < 0).any():
        logger.warning(f"Found {(df['demand'] < 0).sum()} negative demand values")
    
    logger.info(f"Demand column validated: min={df['demand'].min():.0f}, max={df['demand'].max():.0f}, mean={df['demand'].mean():.2f}")
    return True


def split_time_series(
    df: pd.DataFrame,
    train_size: float = 0.7,
    val_size: float = 0.15,
    test_size: float = 0.15,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split time-series data into train/val/test preserving temporal order.
    
    Args:
        df: Time-series data sorted by date
        train_size: Fraction of data for training (0-1)
        val_size: Fraction of data for validation (0-1)
        test_size: Fraction of data for testing (0-1)
    
    Returns:
        Tuple of (df_train, df_val, df_test)
    
    Raises:
        ValueError: If sizes don't sum to 1.0
    """
    if not np.isclose(train_size + val_size + test_size, 1.0):
        raise ValueError(f"Sizes must sum to 1.0, got {train_size + val_size + test_size}")
    
    n = len(df)
    train_end = int(n * train_size)
    val_end = train_end + int(n * val_size)
    
    df_train = df.iloc[:train_end].reset_index(drop=True)
    df_val = df.iloc[train_end:val_end].reset_index(drop=True)
    df_test = df.iloc[val_end:].reset_index(drop=True)
    
    logger.info(f"Train: {len(df_train)}, Val: {len(df_val)}, Test: {len(df_test)}")
    
    return df_train, df_val, df_test


def aggregate_by_store_item(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate demand by date, store, and item.
    
    Args:
        df: Raw demand data
    
    Returns:
        Aggregated DataFrame
    """
    df_agg = df.groupby(["date", "store", "item"]).agg({
        "demand": "sum"
    }).reset_index()
    
    logger.info(f"Aggregated to {len(df_agg)} records")
    return df_agg
