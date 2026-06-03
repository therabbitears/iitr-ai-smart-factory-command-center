import argparse
import logging
from app.core.logging import get_logger
from app.ml.demand_forecasting.pipeline import DemandForecastingPipeline

logger = get_logger(__name__)


def main():
    """CLI entry point for Demand Forecasting training pipeline."""
    parser = argparse.ArgumentParser(
        description="Train Demand Forecasting models on Store Item Demand dataset"
    )
    parser.add_argument(
        "source_path",
        type=str,
        help="Path to raw Store Item Demand CSV file",
    )
    parser.add_argument(
        "--store-id",
        type=int,
        default=None,
        help="Optional store ID to forecast (default: all stores)",
    )
    parser.add_argument(
        "--item-id",
        type=int,
        default=None,
        help="Optional item ID to forecast (default: all items)",
    )

    args = parser.parse_args()
    logger.info(f"Starting demand forecasting pipeline with source: {args.source_path}")

    pipeline = DemandForecastingPipeline()
    result = pipeline.run(args.source_path, store_id=args.store_id, item_id=args.item_id)

    logger.info(f"Pipeline result: {result}")


if __name__ == "__main__":
    main()
