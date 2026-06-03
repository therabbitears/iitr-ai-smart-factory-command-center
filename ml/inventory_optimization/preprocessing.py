"""Preprocessing utilities for Inventory Optimization."""
from typing import Tuple
import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning: drop duplicates, fill or drop NA, ensure sensible types."""
    df = df.copy()
    initial = len(df)
    df = df.drop_duplicates()
    df = df.dropna()
    # ensure date column exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    # common numeric columns
    for c in ['stock', 'demand', 'on_order', 'lead_time']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    final = len(df)
    print(f"clean_data: removed {initial-final} rows")
    return df


def aggregate_inventory(df: pd.DataFrame, group_cols=('warehouse','sku','date')) -> pd.DataFrame:
    """Aggregate to desired granularity (e.g., SKU x warehouse x day)."""
    df = df.copy()
    # ensure grouping columns exist
    cols = [c for c in group_cols if c in df.columns]
    if not cols:
        raise ValueError('No grouping columns present for aggregation')
    agg = df.groupby(cols).agg({
        'stock': 'sum' if 'stock' in df.columns else 'first',
        'demand': 'sum' if 'demand' in df.columns else 'first',
        'on_order': 'sum' if 'on_order' in df.columns else 'first'
    }).reset_index()
    return agg
