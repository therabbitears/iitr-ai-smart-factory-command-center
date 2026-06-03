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

MLflow Integration:
- Experiment tracking via `mlflow` (optional fallback to local `mlruns_local`).
- Model registry and versioning using MLflow Model Registry (each model registered under `InventoryOptimization-<model>`).
- Artifacts are logged to MLflow artifact store when available; otherwise models are saved locally with `.meta.json` summaries.

Next steps: Add hyperparameter tuning (GridSearch/Optuna) and API serving.
