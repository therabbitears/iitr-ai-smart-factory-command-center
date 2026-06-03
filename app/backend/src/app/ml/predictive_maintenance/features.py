from __future__ import annotations

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

NUMERIC_COLUMNS = [
    "air_temperature",
    "process_temperature",
    "rotational_speed",
    "torque",
    "tool_wear",
]

ENGINEERED_COLUMNS = [
    "temp_delta",
    "wear_rate",
    "torque_ratio",
    "temperature_ratio",
]

ALL_FEATURE_COLUMNS = NUMERIC_COLUMNS + ENGINEERED_COLUMNS


class FeatureEngineer:
    """Transform raw features to engineered features with fit-transform pattern to prevent data leakage."""

    def __init__(self) -> None:
        self.rotational_speed_min: float = 1.0
        self.air_temp_min: float = 1.0
        self._is_fitted = False

    def fit(self, df: pd.DataFrame) -> "FeatureEngineer":
        """Fit engineer on training data to capture statistics."""
        self.rotational_speed_min = max(df["rotational_speed"].min(), 1.0)
        self.air_temp_min = max(df["air_temperature"].min(), 1.0)
        self._is_fitted = True
        logger.info("FeatureEngineer fitted on training data")
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform data using fitted statistics."""
        if not self._is_fitted:
            raise ValueError("FeatureEngineer must be fitted before transform")
        
        df = df.copy()
        df["temp_delta"] = df["process_temperature"] - df["air_temperature"]
        df["wear_rate"] = df["tool_wear"] / self.rotational_speed_min
        df["torque_ratio"] = df["torque"] / self.rotational_speed_min
        df["temperature_ratio"] = df["process_temperature"] / self.air_temp_min
        return df

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit and transform in one step."""
        return self.fit(df).transform(df)


def get_feature_columns() -> list[str]:
    """Return all feature columns in training order."""
    return ALL_FEATURE_COLUMNS


def get_numeric_columns() -> list[str]:
    """Return raw numeric columns."""
    return NUMERIC_COLUMNS
