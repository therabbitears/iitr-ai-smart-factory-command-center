from pathlib import Path

import pandas as pd

from app.data.loaders import AI4IDatasetLoader
from app.data.profiling import DataProfiler
from app.data.validation import ValidationEngine
from app.data.schemas import DatasetIngestionResult


def test_data_profiler_summary() -> None:
    df = pd.DataFrame(
        {
            "machine_id": ["M-1", "M-2"],
            "timestamp": ["2024-01-01T00:00:00Z", "2024-01-01T01:00:00Z"],
            "air_temperature": [20.5, 22.0],
            "process_temperature": [45.3, 47.6],
            "rotational_speed": [1500, 1520],
            "torque": [35.0, 36.1],
            "tool_wear": [0.5, 0.7],
            "machine_failure": [0, 1],
            "failure_type": ["Tool wear", "Power failure"],
        }
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    report = DataProfiler.profile(df)

    assert report.row_count == 2
    assert report.column_count == 9
    assert report.data_types["air_temperature"] == "float64"
    assert report.missing_values["machine_id"] == 0


def test_ai4i_validation_success(tmp_path: Path) -> None:
    df = pd.DataFrame(
        {
            "machine_id": ["M-1"],
            "timestamp": [pd.to_datetime("2024-01-01T00:00:00Z")],
            "air_temperature": [20.5],
            "process_temperature": [45.3],
            "rotational_speed": [1500.0],
            "torque": [35.0],
            "tool_wear": [0.5],
            "machine_failure": [0],
            "failure_type": ["Tool wear"],
        }
    )

    loader = AI4IDatasetLoader(tmp_path / "ai4i.csv")
    result = ValidationEngine.validate(df, loader.schema)

    assert result.success
    assert result.errors == []
