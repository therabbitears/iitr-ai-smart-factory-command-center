from __future__ import annotations

import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

logger = logging.getLogger(__name__)

# Feature windows for autoregression
LAG_WINDOWS = [7, 14, 30]  # 1-week, 2-week, 1-month lags
ROLLING_WINDOWS = [7, 14, 30]  # Rolling mean/std windows


class TimeSeriesFeatureEngineer:
    """Engineer time-series features with fit-transform pattern to prevent data leakage."""

    def __init__(self, lag_windows: list[int] | None = None, rolling_windows: list[int] | None = None) -> None:
        self.lag_windows = lag_windows or LAG_WINDOWS
        self.rolling_windows = rolling_windows or ROLLING_WINDOWS
        self.demand_mean: float = 1.0
        self.demand_std: float = 1.0
        self._is_fitted = False
        logger.info(f"TimeSeriesFeatureEngineer initialized: lags={self.lag_windows}, rolling={self.rolling_windows}")

    def fit(self, df: pd.DataFrame) -> "TimeSeriesFeatureEngineer":
        """Fit engineer on training data to capture statistics.
        
        Args:
            df: Training time-series data
        
        Returns:
            Self for chaining
        """
        self.demand_mean = df["demand"].mean()
        self.demand_std = max(df["demand"].std(), 1.0)
        self._is_fitted = True
        logger.info(f"TimeSeriesFeatureEngineer fitted: mean={self.demand_mean:.2f}, std={self.demand_std:.2f}")
        return self

    def create_lag_features(self, series: pd.Series) -> pd.DataFrame:
        """Create lagged demand features for autoregression.
        
        Args:
            series: Demand time-series
        
        Returns:
            DataFrame with lag features
        """
        df = pd.DataFrame({"demand": series})
        for lag in self.lag_windows:
            df[f"demand_lag_{lag}"] = series.shift(lag)
        return df

    def create_rolling_features(self, series: pd.Series) -> pd.DataFrame:
        """Create rolling statistics features.
        
        Args:
            series: Demand time-series
        
        Returns:
            DataFrame with rolling features
        """
        df = pd.DataFrame()
        for window in self.rolling_windows:
            df[f"demand_rolling_mean_{window}"] = series.rolling(window=window, min_periods=1).mean()
            df[f"demand_rolling_std_{window}"] = series.rolling(window=window, min_periods=1).std().fillna(0)
        return df

    def create_temporal_features(self, dates: pd.Series) -> pd.DataFrame:
        """Create temporal features from date column.
        
        Args:
            dates: Date column
        
        Returns:
            DataFrame with temporal features
        """
        df = pd.DataFrame()
        df["day_of_week"] = dates.dt.dayofweek
        df["month"] = dates.dt.month
        df["quarter"] = dates.dt.quarter
        df["day_of_year"] = dates.dt.dayofyear
        df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)
        return df

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform data using fitted statistics.
        
        Args:
            df: Time-series data with date and demand columns
        
        Returns:
            DataFrame with engineered features
        """
        if not self._is_fitted:
            raise ValueError("TimeSeriesFeatureEngineer must be fitted before transform")
        
        df = df.copy()
        
        # Create lag features
        lag_df = self.create_lag_features(df["demand"])
        
        # Create rolling features
        rolling_df = self.create_rolling_features(df["demand"])
        
        # Create temporal features
        temporal_df = self.create_temporal_features(df["date"])
        
        # Combine all features
        df_engineered = pd.concat([df, lag_df, rolling_df, temporal_df], axis=1)
        
        # Drop rows with NaN (from lags)
        df_engineered = df_engineered.dropna()
        logger.info(f"Created {df_engineered.shape[1]} engineered features from {df.shape[1]} base features")
        
        return df_engineered

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fit and transform in one step.
        
        Args:
            df: Time-series data
        
        Returns:
            Transformed DataFrame
        """
        return self.fit(df).transform(df)


class SlidingWindowGenerator:
    """Generate sliding window sequences for LSTM training."""

    def __init__(self, lookback: int = 30, lookahead: int = 1) -> None:
        self.lookback = lookback
        self.lookahead = lookahead
        logger.info(f"SlidingWindowGenerator initialized: lookback={lookback}, lookahead={lookahead}")

    def create_sequences(
        self,
        data: np.ndarray,
        targets: np.ndarray | None = None,
    ) -> tuple[np.ndarray, np.ndarray]:
        """Create sliding window sequences from time-series data.
        
        Args:
            data: Feature matrix (time_steps, features)
            targets: Optional target variable
        
        Returns:
            Tuple of (X_sequences, y_sequences)
        """
        X_sequences = []
        y_sequences = []

        for i in range(len(data) - self.lookback - self.lookahead + 1):
            X_sequences.append(data[i : i + self.lookback])
            if targets is not None:
                y_sequences.append(targets[i + self.lookback + self.lookahead - 1])

        X_sequences = np.array(X_sequences)
        y_sequences = np.array(y_sequences) if targets is not None else None

        logger.info(f"Created {len(X_sequences)} sequences (lookback={self.lookback}, lookahead={self.lookahead})")
        return X_sequences, y_sequences


def get_feature_columns() -> list[str]:
    """Return all engineered feature column names.
    
    Returns:
        List of feature column names
    """
    columns = ["demand", "store", "item"]
    columns += [f"demand_lag_{lag}" for lag in LAG_WINDOWS]
    columns += [f"demand_rolling_mean_{w}" for w in ROLLING_WINDOWS]
    columns += [f"demand_rolling_std_{w}" for w in ROLLING_WINDOWS]
    columns += ["day_of_week", "month", "quarter", "day_of_year", "is_weekend"]
    return columns
