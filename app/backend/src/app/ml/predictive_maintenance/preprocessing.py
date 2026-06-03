from __future__ import annotations

import pandas as pd
from sklearn.model_selection import train_test_split


NUMERIC_COLUMNS = [
    "air_temperature",
    "process_temperature",
    "rotational_speed",
    "torque",
    "tool_wear",
]

TARGET_COLUMN = "machine_failure"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.rename(columns={"machine_failure": TARGET_COLUMN})
    df = df.drop_duplicates()

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

    df = df.dropna(subset=NUMERIC_COLUMNS + [TARGET_COLUMN])
    return df


def encode_labels(df: pd.DataFrame) -> pd.DataFrame:
    return df.copy()


def split_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    X = df[NUMERIC_COLUMNS]
    y = df[TARGET_COLUMN].astype(int)
    return train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
