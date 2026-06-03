from __future__ import annotations
from typing import Any

import pandas as pd

from app.data.schemas import ProfileReport


class DataProfiler:
    """Responsible for producing lightweight dataset profile summaries."""

    @staticmethod
    def profile(df: pd.DataFrame) -> ProfileReport:
        row_count = int(df.shape[0])
        column_count = int(df.shape[1])
        data_types = {col: str(dtype) for col, dtype in df.dtypes.items()}

        missing_values = df.isna().sum().to_dict()
        missing_percent = {
            col: float(count / row_count) if row_count else 0.0
            for col, count in missing_values.items()
        }

        numeric_df = df.select_dtypes(include=["number"])
        summary_statistics: dict[str, dict[str, float]] = {}
        for column in numeric_df.columns:
            series = numeric_df[column].dropna()
            if series.empty:
                summary_statistics[column] = {
                    "min": 0.0,
                    "max": 0.0,
                    "mean": 0.0,
                    "median": 0.0,
                    "std": 0.0,
                }
                continue
            summary_statistics[column] = {
                "min": float(series.min()),
                "max": float(series.max()),
                "mean": float(series.mean()),
                "median": float(series.median()),
                "std": float(series.std(ddof=0)),
            }

        top_values: dict[str, list[Any]] = {}
        for column in df.columns:
            top_values[column] = [
                value for value in df[column].dropna().value_counts().head(5).index.tolist()
            ]

        return ProfileReport(
            row_count=row_count,
            column_count=column_count,
            data_types=data_types,
            missing_values={str(k): int(v) for k, v in missing_values.items()},
            missing_percent={str(k): v for k, v in missing_percent.items()},
            summary_statistics=summary_statistics,
            top_values={str(k): v for k, v in top_values.items()},
        )
