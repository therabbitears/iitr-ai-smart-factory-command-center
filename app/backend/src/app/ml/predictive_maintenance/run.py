from __future__ import annotations
from argparse import ArgumentParser
from pathlib import Path

from app.ml.predictive_maintenance.pipeline import PredictiveMaintenancePipeline


def main() -> None:
    parser = ArgumentParser(description="Run the predictive maintenance training pipeline.")
    parser.add_argument(
        "source_path",
        type=Path,
        help="Path to the AI4I predictive maintenance dataset file (CSV or Parquet).",
    )
    args = parser.parse_args()

    pipeline = PredictiveMaintenancePipeline(args.source_path)
    result = pipeline.run()

    print("=== Predictive Maintenance Pipeline Result ===")
    print(f"Best model: {result['best_model']}")
    print(f"Persisted path: {result['persisted_path']}")
    print(f"MLflow artifact uri: {result['artifact_uri']}")
    print("Metrics:")
    for record in result["metrics"]:
        print(record)


if __name__ == "__main__":
    main()
