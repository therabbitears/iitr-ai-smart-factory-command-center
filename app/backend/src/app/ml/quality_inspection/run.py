import argparse
import logging
from app.core.logging import get_logger
from app.ml.quality_inspection.pipeline import QualityInspectionPipeline

logger = get_logger(__name__)


def main():
    """CLI entry point for Quality Inspection training pipeline."""
    parser = argparse.ArgumentParser(
        description="Train Quality Inspection models on Steel Plates dataset"
    )
    parser.add_argument(
        "source_path",
        type=str,
        help="Path to raw Steel Plates CSV file",
    )

    args = parser.parse_args()
    logger.info(f"Starting QI pipeline with source: {args.source_path}")

    pipeline = QualityInspectionPipeline()
    result = pipeline.run(args.source_path)

    logger.info(f"Pipeline result: {result}")


if __name__ == "__main__":
    main()
