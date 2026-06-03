"""Feature engineering for Inventory Optimization."""
from typing import List
import pandas as pd
import numpy as np


class InventoryFeatureEngineer:
    """Create lag and rolling features for inventory/demand forecasting and optimization.

    Usage:
        fe = InventoryFeatureEngineer(lags=[1,7,14], rolls=[7,30])
        df_feat = fe.fit_transform(df)
    """

    def __init__(self, lags: List[int] = (1,7,14), rolls: List[int] = (7,30)):
        self.lags = list(lags)
        self.rolls = list(rolls)
        self._is_fitted = False

    def fit(self, df: pd.DataFrame):
        # Nothing heavy to fit, placeholder to keep API consistent
        self._is_fitted = True
        return self

    def _make_lags(self, series: pd.Series) -> pd.DataFrame:
        out = pd.DataFrame()
        for lag in self.lags:
            out[f'demand_lag_{lag}'] = series.shift(lag)
        return out

    def _make_rolls(self, series: pd.Series) -> pd.DataFrame:
        out = pd.DataFrame()
        for w in self.rolls:
            out[f'demand_roll_mean_{w}'] = series.rolling(window=w, min_periods=1).mean()
            out[f'demand_roll_std_{w}'] = series.rolling(window=w, min_periods=1).std().fillna(0)
        return out

    def _temporal(self, dates: pd.Series) -> pd.DataFrame:
        out = pd.DataFrame()
        out['dow'] = dates.dt.dayofweek
        out['month'] = dates.dt.month
        out['is_weekend'] = (out['dow'] >= 5).astype(int)
        return out

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if not self._is_fitted:
            raise ValueError('FeatureEngineer must be fitted first')
        df = df.copy()
        if 'date' in df.columns:
            dates = pd.to_datetime(df['date'])
        else:
            dates = pd.Series(pd.date_range('2000-01-01', periods=len(df)))

        lag_df = self._make_lags(df['demand']) if 'demand' in df.columns else pd.DataFrame()
        roll_df = self._make_rolls(df['demand']) if 'demand' in df.columns else pd.DataFrame()
        temp_df = self._temporal(dates)

        df_feat = pd.concat([df.reset_index(drop=True), lag_df.reset_index(drop=True), roll_df.reset_index(drop=True), temp_df.reset_index(drop=True)], axis=1)
        df_feat = df_feat.dropna().reset_index(drop=True)
        return df_feat

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.fit(df).transform(df)
