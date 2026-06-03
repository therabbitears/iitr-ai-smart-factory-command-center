"""Data loader for Inventory Optimization (Supply Chain Analytics)"""
from typing import Optional
import pandas as pd


class InventoryLoader:
    """Load inventory / supply chain datasets from CSV or DataFrame."""

    @staticmethod
    def load_csv(path: str, date_col: str = 'date', parse_dates=True) -> pd.DataFrame:
        df = pd.read_csv(path)
        if parse_dates and date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col])
        return df

    @staticmethod
    def from_df(df: pd.DataFrame, ensure_types: Optional[dict] = None) -> pd.DataFrame:
        df = df.copy()
        if ensure_types:
            for c, t in ensure_types.items():
                if c in df.columns:
                    df[c] = df[c].astype(t)
        return df
