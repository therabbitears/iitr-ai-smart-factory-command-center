# Inventory Optimization - Supply Chain Analytics

Module: Inventory Optimization

- Purpose: Build models and pipeline to support SKU-level inventory optimization and demand-informed replenishment.
- Models: Linear Regression, Random Forest, XGBoost
- Components:
  - `loader.py` - CSV / DataFrame loader
  - `preprocessing.py` - cleaning and aggregation helpers
  - `features.py` - lag and rolling features for demand/stock
  - `train.py` - model builders and training helper
  - `evaluate.py` - metrics and comparison
  - `pipeline.py` - end-to-end orchestration and model persistence
  - `run.py` - CLI entrypoint

Next steps: Add MLflow logging, hyperparameter tuning, and API serving.
