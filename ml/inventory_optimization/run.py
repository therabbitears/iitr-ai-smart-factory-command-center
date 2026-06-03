"""CLI entrypoint to run Inventory Optimization pipeline."""
import argparse
import pandas as pd
from .pipeline import InventoryOptimizationPipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, help='Path to inventory CSV')
    args = parser.parse_args()

    pipeline = InventoryOptimizationPipeline()
    if args.csv:
        out = pipeline.run(csv_path=args.csv)
    else:
        print('Please provide --csv path to run the pipeline')

if __name__ == '__main__':
    main()
