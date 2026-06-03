from __future__ import annotations

import pandas as pd


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["temp_delta"] = df["process_temperature"] - df["air_temperature"]
    df["wear_rate"] = df["tool_wear"] / df["rotational_speed"].replace(0, 1)
    df["torque_ratio"] = df["torque"] / df["rotational_speed"].replace(0, 1)
    df["temperature_ratio"] = df["process_temperature"] / df["air_temperature"].replace(0, 1)
    return df


def get_feature_columns() -> list[str]:
    return [
        "air_temperature",
        "process_temperature",
        "rotational_speed",
        "torque",
        "tool_wear",
        "temp_delta",
        "wear_rate",
        "torque_ratio",
        "temperature_ratio",
    ]
