from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel


class ValidationResult(BaseModel):
    success: bool
    errors: list[dict[str, Any]] = []


class ProfileReport(BaseModel):
    row_count: int
    column_count: int
    data_types: dict[str, str]
    missing_values: dict[str, int]
    missing_percent: dict[str, float]
    summary_statistics: dict[str, dict[str, float]]
    top_values: dict[str, list[Any]]


class DatasetVersionInfo(BaseModel):
    dataset_name: str
    version_id: str
    source_path: Path
    raw_checksum: str
    schema_checksum: str
    row_count: int
    column_count: int
    created_at: datetime
    metadata: dict[str, Any] = {}


class DatasetIngestionResult(BaseModel):
    dataset_name: str
    version_info: DatasetVersionInfo
    validation: ValidationResult
    profile: ProfileReport
    statistics: dict[str, Any]
