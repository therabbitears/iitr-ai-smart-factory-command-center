import os
from pathlib import Path

import pandas as pd


def test_predictive_maintenance_pipeline(tmp_path: Path) -> None:
    os.environ["MLFLOW_TRACKING_URI"] = f"file://{tmp_path / 'mlruns'}"
    os.environ["MLFLOW_EXPERIMENT_NAME"] = "test_predictive_maintenance"
    os.environ["MLFLOW_ARTIFACT_ROOT"] = str(tmp_path / "mlruns")

    from app.ml.predictive_maintenance.pipeline import PredictiveMaintenancePipeline

    data = {
        "machine_id": ["M-1"] * 20,
        "timestamp": pd.date_range("2024-01-01", periods=20, freq="H"),
        "air_temperature": [20.0 + i * 0.5 for i in range(20)],
        "process_temperature": [45.0 + i * 0.4 for i in range(20)],
        "rotational_speed": [1500 + i * 5 for i in range(20)],
        "torque": [35.0 + i * 0.2 for i in range(20)],
        "tool_wear": [0.5 + i * 0.1 for i in range(20)],
        "machine_failure": [0 if i < 15 else 1 for i in range(20)],
        "failure_type": ["Tool wear" if i < 15 else "Power failure" for i in range(20)],
    }
    df = pd.DataFrame(data)
    csv_path = tmp_path / "ai4i.csv"
    df.to_csv(csv_path, index=False)

    pipeline = PredictiveMaintenancePipeline(csv_path)
    result = pipeline.run()

    assert result["best_model"] in ["logistic_regression", "random_forest", "xgboost", "ann"]
    assert Path(result["persisted_path"]).exists()
    assert result["metrics"]
