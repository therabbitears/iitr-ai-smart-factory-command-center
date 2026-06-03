from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from app.ml.demand_forecasting.loader import DemandForecastingLoader
from app.ml.demand_forecasting.preprocessing import (
    clean_data,
    validate_demand_column,
    split_time_series,
    aggregate_by_store_item,
)
from app.ml.demand_forecasting.features import (
    TimeSeriesFeatureEngineer,
    SlidingWindowGenerator,
    get_feature_columns,
)
from app.ml.demand_forecasting.train import (
    build_regressors,
    train_lstm,
)
from app.ml.demand_forecasting.evaluate import compare_models, forecast_future
from app.ml.demand_forecasting.model_store import ModelStore

logger = logging.getLogger(__name__)


class DemandForecastingPipeline:
    """End-to-end time-series forecasting pipeline for Store Item Demand."""

    def __init__(self) -> None:
        self.loader = DemandForecastingLoader()
        self.feature_engineer = TimeSeriesFeatureEngineer()
        self.window_generator = SlidingWindowGenerator(lookback=30, lookahead=1)
        self.sklearn_models = {}
        self.lstm_model = None
        self.scaler = StandardScaler()
        self.best_model_name = None
        self.model_store = ModelStore()

    def run(
        self,
        source_path: str,
        store_id: int | None = None,
        item_id: int | None = None,
    ) -> dict:
        """Execute complete demand forecasting pipeline.
        
        Args:
            source_path: Path to raw demand data CSV
            store_id: Optional specific store to forecast (if None, forecasts all)
            item_id: Optional specific item to forecast (if None, forecasts all)
        
        Returns:
            Dictionary with pipeline results
        """
        try:
            logger.info(f"Starting Demand Forecasting pipeline (store={store_id}, item={item_id})")

            # 1. Load and validate data
            logger.info("Step 1: Loading and validating data")
            raw_df = self.loader.load(source_path)

            # 2. Clean data
            logger.info("Step 2: Cleaning data")
            clean_df = clean_data(raw_df)

            # 3. Validate demand column
            logger.info("Step 3: Validating demand column")
            validate_demand_column(clean_df)

            # 4. Aggregate demand by date, store, item
            logger.info("Step 4: Aggregating demand")
            agg_df = aggregate_by_store_item(clean_df)

            # 5. Filter by store and item if specified
            if store_id is not None:
                agg_df = agg_df[agg_df["store"] == store_id]
                logger.info(f"Filtered to store {store_id}: {len(agg_df)} records")

            if item_id is not None:
                agg_df = agg_df[agg_df["item"] == item_id]
                logger.info(f"Filtered to item {item_id}: {len(agg_df)} records")

            # 6. Train-test split (time-series preserves order)
            logger.info("Step 6: Splitting time-series data")
            df_train, df_val, df_test = split_time_series(agg_df, train_size=0.7, val_size=0.15, test_size=0.15)

            # 7. Fit feature engineer on training set
            logger.info("Step 7: Fitting feature engineer")
            self.feature_engineer.fit(df_train)
            
            df_train_eng = self.feature_engineer.transform(df_train)
            df_val_eng = self.feature_engineer.transform(df_val)
            df_test_eng = self.feature_engineer.transform(df_test)

            # 8. Prepare features and targets
            logger.info("Step 8: Preparing features and targets")
            feature_cols = [c for c in df_train_eng.columns if c not in ["date", "store", "item", "demand"]]
            
            X_train = df_train_eng[feature_cols].values
            y_train = df_train_eng["demand"].values
            
            X_val = df_val_eng[feature_cols].values
            y_val = df_val_eng["demand"].values
            
            X_test = df_test_eng[feature_cols].values
            y_test = df_test_eng["demand"].values

            # Scale features
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_val_scaled = self.scaler.transform(X_val)
            X_test_scaled = self.scaler.transform(X_test)

            # 9. Train sklearn regressors
            logger.info("Step 9: Training sklearn regressors")
            self.sklearn_models = build_regressors()
            for name, model in self.sklearn_models.items():
                model.fit(X_train, y_train)
                logger.info(f"Trained {name}")

            # 10. Train LSTM model
            logger.info("Step 10: Training LSTM model")
            X_train_lstm, y_train_lstm = self.window_generator.create_sequences(X_train_scaled, y_train)
            X_val_lstm, y_val_lstm = self.window_generator.create_sequences(X_val_scaled, y_val)
            
            self.lstm_model = train_lstm(
                X_train_lstm,
                y_train_lstm,
                X_val_lstm,
                y_val_lstm,
            )

            # 11. Prepare test sequences for LSTM
            X_test_lstm, y_test_lstm = self.window_generator.create_sequences(X_test_scaled, y_test)

            # 12. Compare all models
            logger.info("Step 12: Comparing models on test set")
            all_models = {**self.sklearn_models, "lstm": self.lstm_model}
            
            # Use appropriate test data for each model
            test_data_sklearn = X_test_scaled
            test_data_lstm = X_test_lstm
            
            comparison_rows = []
            for name, model in all_models.items():
                test_data = test_data_lstm if name == "lstm" else test_data_sklearn
                test_targets = y_test_lstm if name == "lstm" else y_test
                
                result = forecast_future(model, test_data, test_targets)
                row = {"model": name}
                row.update({k: v for k, v in result.items() if k != "predictions"})
                comparison_rows.append(row)
            
            comparison_df = pd.DataFrame(comparison_rows).sort_values(by="r2", ascending=False).reset_index(drop=True)
            logger.info(f"\nModel comparison:\n{comparison_df}")

            # 13. Select best model
            self.best_model_name = comparison_df.iloc[0]["model"]
            best_model = all_models[self.best_model_name]
            logger.info(f"Best model: {self.best_model_name}")

            # 14. Log to MLflow
            logger.info("Step 14: Logging to MLflow")
            best_metrics = comparison_df.iloc[0].to_dict()
            self.model_store.log_run(
                model_name="demand_forecasting",
                model_version="1.0",
                dataset="store_item_demand",
                best_model_name=self.best_model_name,
                metrics=best_metrics,
                all_model_metrics=comparison_df.to_dict("records"),
            )

            # 15. Persist best model
            logger.info("Step 15: Persisting best model")
            artifacts = self.model_store.persist_best_model(
                model=best_model,
                model_name=self.best_model_name,
                pipeline_name="demand_forecasting",
            )

            logger.info("Demand Forecasting pipeline completed successfully")
            return {
                "status": "success",
                "best_model": self.best_model_name,
                "metrics": best_metrics,
                "comparison": comparison_df.to_dict("records"),
                "artifacts": artifacts,
            }

        except Exception as e:
            logger.error(f"Demand Forecasting pipeline failed: {str(e)}", exc_info=True)
            raise
