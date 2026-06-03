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
    agg_dict = {}
    if 'stock' in df.columns:
        agg_dict['stock'] = 'sum'
    if 'demand' in df.columns:
        agg_dict['demand'] = 'sum'
    if 'on_order' in df.columns:
        agg_dict['on_order'] = 'sum'
    # fallback: include any numeric column not yet included
    for c in df.select_dtypes(include=['number']).columns:
        if c not in agg_dict and c not in cols:
            agg_dict[c] = 'sum'

    if not agg_dict:
        # nothing numeric to aggregate, just return unique groups
        agg = df[cols].drop_duplicates().reset_index(drop=True)
    else:
        agg = df.groupby(cols).agg(agg_dict).reset_index()
    return agg
