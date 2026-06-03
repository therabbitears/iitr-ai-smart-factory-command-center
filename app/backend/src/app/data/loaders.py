from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import pandas as pd
import pandera as pa
from pandera import Column, Check

from app.data.profiling import DataProfiler
from app.data.schemas import DatasetIngestionResult, ProfileReport, ValidationResult
from app.data.validation import ValidationEngine
from app.data.versioning import DatasetVersioning


class BaseDatasetLoader(ABC):
    dataset_name: str
    date_columns: list[str] = []

    def __init__(self, source_path: Path | str) -> None:
        self.source_path = Path(source_path)

    @property
    @abstractmethod
    def schema(self) -> pa.DataFrameSchema:
        raise NotImplementedError

    @property
    @abstractmethod
    def required_columns(self) -> list[str]:
        raise NotImplementedError

    def load_raw(self) -> pd.DataFrame:
        if not self.source_path.exists():
            raise FileNotFoundError(f"Source dataset not found: {self.source_path}")

        if self.source_path.suffix.lower() == ".csv":
            df = pd.read_csv(self.source_path, parse_dates=self.date_columns)
        elif self.source_path.suffix.lower() in {".parquet", ".pq"}:
            df = pd.read_parquet(self.source_path)
        else:
            raise ValueError(
                f"Unsupported file format: {self.source_path.suffix}. Use CSV or Parquet."
            )

        return self._normalize_columns(df)

    def _normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df.columns = [col.strip() for col in df.columns]
        return df

    def validate(self, df: pd.DataFrame) -> ValidationResult:
        return ValidationEngine.validate(df, self.schema)

    def profile(self, df: pd.DataFrame) -> "ProfileReport":
        return DataProfiler.profile(df)

    def analyze_missing(self, df: pd.DataFrame) -> dict[str, Any]:
        missing = df.isna().sum()
        total_rows = len(df)
        return {
            "missing_counts": missing.to_dict(),
            "missing_percent": {
                str(column): float(count / total_rows) if total_rows else 0.0
                for column, count in missing.items()
            },
            "columns_with_missing": [str(column) for column, count in missing.items() if count > 0],
        }

    def statistics(self, df: pd.DataFrame) -> dict[str, Any]:
        duplicates = int(df.duplicated().sum())
        memory_usage_mb = float(df.memory_usage(deep=True).sum() / 1024**2)
        return {
            "row_count": int(df.shape[0]),
            "column_count": int(df.shape[1]),
            "duplicate_rows": duplicates,
            "memory_usage_mb": memory_usage_mb,
            "columns": list(df.columns),
        }

    def version(self, df: pd.DataFrame) -> "DatasetVersionInfo":
        return DatasetVersioning.create_version(self.dataset_name, self.source_path, df)

    def ingest(self) -> DatasetIngestionResult:
        df = self.load_raw()
        validation = self.validate(df)
        profile = self.profile(df)
        statistics = self.statistics(df)
        version_info = self.version(df)

        if not validation.success:
            raise ValueError(
                f"Dataset validation failed for {self.dataset_name}: {validation.errors}"
            )

        return DatasetIngestionResult(
            dataset_name=self.dataset_name,
            version_info=version_info,
            validation=validation,
            profile=profile,
            statistics=statistics,
        )


class AI4IDatasetLoader(BaseDatasetLoader):
    dataset_name = "ai4i"
    date_columns = ["timestamp"]

    @property
    def required_columns(self) -> list[str]:
        return [
            "machine_id",
            "timestamp",
            "air_temperature",
            "process_temperature",
            "rotational_speed",
            "torque",
            "tool_wear",
            "machine_failure",
            "failure_type",
        ]

    @property
    def schema(self) -> pa.DataFrameSchema:
        return pa.DataFrameSchema(
            {
                "machine_id": Column(str, nullable=False),
                "timestamp": Column(pa.DateTime, nullable=False),
                "air_temperature": Column(float, nullable=False, checks=Check.in_range(0, 100)),
                "process_temperature": Column(float, nullable=False, checks=Check.in_range(0, 200)),
                "rotational_speed": Column(float, nullable=False, checks=Check.ge(0)),
                "torque": Column(float, nullable=False, checks=Check.ge(0)),
                "tool_wear": Column(float, nullable=False, checks=Check.in_range(0, 100)),
                "machine_failure": Column(int, nullable=False, checks=Check.isin([0, 1])),
                "failure_type": Column(str, nullable=False),
            },
            strict=True,
        )


class SteelPlatesDatasetLoader(BaseDatasetLoader):
    dataset_name = "steel_plates"
    date_columns: list[str] = []

    @property
    def required_columns(self) -> list[str]:
        return [
            "X_Minimum",
            "X_Maximum",
            "Y_Minimum",
            "Y_Maximum",
            "Pixel_area",
            "Bare_Nuclei",
            "class",
        ]

    @property
    def schema(self) -> pa.DataFrameSchema:
        return pa.DataFrameSchema(
            {
                "X_Minimum": Column(float, nullable=False),
                "X_Maximum": Column(float, nullable=False),
                "Y_Minimum": Column(float, nullable=False),
                "Y_Maximum": Column(float, nullable=False),
                "Pixel_area": Column(float, nullable=False, checks=Check.ge(0)),
                "Bare_Nuclei": Column(float, nullable=False, checks=Check.ge(0)),
                "class": Column(int, nullable=False),
            },
            strict=True,
        )


class DemandForecastingDatasetLoader(BaseDatasetLoader):
    dataset_name = "demand_forecasting"
    date_columns = ["date"]

    @property
    def required_columns(self) -> list[str]:
        return [
            "date",
            "store",
            "item",
            "sales",
            "onpromotion",
            "dayofweek",
            "month",
            "year",
        ]

    @property
    def schema(self) -> pa.DataFrameSchema:
        return pa.DataFrameSchema(
            {
                "date": Column(pa.DateTime, nullable=False),
                "store": Column(int, nullable=False, checks=Check.ge(0)),
                "item": Column(int, nullable=False, checks=Check.ge(0)),
                "sales": Column(float, nullable=False, checks=Check.ge(0)),
                "onpromotion": Column(bool, nullable=False),
                "dayofweek": Column(int, nullable=False, checks=Check.in_range(1, 7)),
                "month": Column(int, nullable=False, checks=Check.in_range(1, 12)),
                "year": Column(int, nullable=False, checks=Check.ge(2000)),
            },
            strict=True,
        )


class SupplyChainDatasetLoader(BaseDatasetLoader):
    dataset_name = "supply_chain"
    date_columns = ["date"]

    @property
    def required_columns(self) -> list[str]:
        return [
            "date",
            "product_id",
            "warehouse_id",
            "on_hand",
            "reorder_point",
            "lead_time_days",
            "demand_forecast",
            "supplier_score",
            "stockouts",
            "reorder_quantity",
        ]

    @property
    def schema(self) -> pa.DataFrameSchema:
        return pa.DataFrameSchema(
            {
                "date": Column(pa.DateTime, nullable=False),
                "product_id": Column(str, nullable=False),
                "warehouse_id": Column(str, nullable=False),
                "on_hand": Column(float, nullable=False, checks=Check.ge(0)),
                "reorder_point": Column(float, nullable=False, checks=Check.ge(0)),
                "lead_time_days": Column(float, nullable=False, checks=Check.ge(0)),
                "demand_forecast": Column(float, nullable=False, checks=Check.ge(0)),
                "supplier_score": Column(float, nullable=False, checks=Check.in_range(0, 1)),
                "stockouts": Column(int, nullable=False, checks=Check.ge(0)),
                "reorder_quantity": Column(float, nullable=False, checks=Check.ge(0)),
            },
            strict=True,
        )
