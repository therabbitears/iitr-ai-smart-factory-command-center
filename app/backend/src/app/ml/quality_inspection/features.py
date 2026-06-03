from __future__ import annotations

import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

NUMERIC_COLUMNS = [
    "X_Minimum",
    "X_Maximum",
    "Y_Minimum",
    "Y_Maximum",
    "Pixel_area",
    "Bare_Nuclei",
]

ENGINEERED_COLUMNS = [
    "x_range",
    "y_range",
    "area_ratio",
    "nuclei_density",
    "shape_ratio",
]

ALL_FEATURE_COLUMNS = NUMERIC_COLUMNS + ENGINEERED_COLUMNS


class FeatureEngineer:
    """Transform raw surface/defect features with fit-transform pattern to prevent data leakage."""

    def __init__(self) -> None:
        self.pixel_area_mean: float = 1.0
        self.pixel_area_std: float = 1.0
        self._is_fitted = False

    def fit(self, df: pd.DataFrame) -> "FeatureEngineer":
        """Fit engineer on training data to capture statistics.
        
        Args:
            df: Training features
        
        Returns:
            Self for chaining
        """
        self.pixel_area_mean = df["Pixel_area"].mean()
        self.pixel_area_std = max(df["Pixel_area"].std(), 1.0)
        self._is_fitted = True
        logger.info("QI FeatureEngineer fitted on training data")
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform data using fitted statistics.
        
        Args:
            df: Features to transform
        
        Returns:
            DataFrame with engineered features
        """
        if not self._is_fitted:
            raise ValueError("FeatureEngineer must be fitted before transform")
        
        df = df.copy()
        df["x_range"] = df["X_Maximum"] - df["X_Minimum"]
        df["y_range"] = df["Y_Maximum"] - df["Y_Minimum"]
        df["area_ratio"] = df["Pixel_area"] / max(self.pixel_area_mean, 1.0)
        df["nuclei_density"] = df["Bare_Nuclei"] / df["Pixel_area"].replace(0, 1.0)
        df["shape_ratio"] = df["x_range"] / df["y_range"].replace(0, 1.0)
        return df

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit and transform in one step.
        
        Args:
            df: Features to fit and transform
        
        Returns:
            Transformed DataFrame
        """
        return self.fit(df).transform(df)


def get_feature_columns() -> list[str]:
    """Return all feature columns in training order.
    
    Returns:
        List of feature column names
    """
    return ALL_FEATURE_COLUMNS


def get_numeric_columns() -> list[str]:
    """Return raw numeric columns.
    
    Returns:
        List of numeric column names
    """
    return NUMERIC_COLUMNS
