from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd
import numpy as np

from app.ml.quality_inspection.loader import QualityInspectionLoader
from app.ml.quality_inspection.preprocessing import (
    clean_data,
    validate_numeric_columns,
    analyze_class_balance,
    split_data,
    NUMERIC_COLUMNS,
    TARGET_COLUMN,
)
from app.ml.quality_inspection.features import FeatureEngineer, get_feature_columns
from app.ml.quality_inspection.train import build_classifiers, train_ann
from app.ml.quality_inspection.evaluate import compare_models
from app.ml.quality_inspection.model_store import ModelStore

logger = logging.getLogger(__name__)


class QualityInspectionPipeline:
    """End-to-end training pipeline for Steel Plates Quality Inspection."""

    def __init__(self) -> None:
        self.loader = QualityInspectionLoader()
        self.feature_engineer = FeatureEngineer()
        self.sklearn_models = {}
        self.ann_model = None
        self.best_model_name = None
        self.model_store = ModelStore()

    def run(self, source_path: str) -> dict:
        """Execute complete QI training pipeline.
        
        Args:
            source_path: Path to raw Steel Plates CSV file
        
        Returns:
            Dictionary with pipeline results
        """
        try:
            logger.info("Starting Quality Inspection pipeline")

            # 1. Load and validate data
            logger.info("Step 1: Loading and validating data")
            raw_df = self.loader.load(source_path)

            # 2. Data cleaning
            logger.info("Step 2: Cleaning data")
            clean_df = clean_data(raw_df)

            # 3. Column validation
            logger.info("Step 3: Validating numeric columns")
            validate_numeric_columns(clean_df)

            # 4. Class balance analysis
            logger.info("Step 4: Analyzing class balance")
            balance_report = analyze_class_balance(clean_df[TARGET_COLUMN])
            logger.info(f"Class balance: {balance_report}")

            # 5. Train-test split (BEFORE feature engineering to prevent data leakage)
            logger.info("Step 5: Splitting data into train/test")
            X_train, X_test, y_train, y_test = split_data(clean_df)
            logger.info(f"Train size: {len(X_train)}, Test size: {len(X_test)}")

            # 6. Fit feature engineer on training set
            logger.info("Step 6: Fitting feature engineer on training data")
            self.feature_engineer.fit(X_train[NUMERIC_COLUMNS])
            X_train_eng = self.feature_engineer.transform(X_train[NUMERIC_COLUMNS])
            X_test_eng = self.feature_engineer.transform(X_test[NUMERIC_COLUMNS])

            # 7. Create validation subset from training data for ANN
            n_train = len(X_train_eng)
            val_split = int(0.2 * n_train)
            X_train_split = X_train_eng[:-val_split]
            X_val_split = X_train_eng[-val_split:]
            y_train_split = y_train.iloc[:-val_split].values
            y_val_split = y_train.iloc[-val_split:].values

            # 8. Train sklearn classifiers
            logger.info("Step 8: Training sklearn classifiers")
            self.sklearn_models = build_classifiers()
            for name, model in self.sklearn_models.items():
                model.fit(X_train_eng, y_train.values)
                logger.info(f"Trained {name}")

            # 9. Train ANN
            logger.info("Step 9: Training ANN")
            self.ann_model = train_ann(
                X_train_split.values,
                y_train_split,
                X_val_split.values,
                y_val_split,
            )

            # 10. Compare all models
            logger.info("Step 10: Comparing models on test set")
            all_models = {**self.sklearn_models, "ann": self.ann_model}
            comparison_df = compare_models(all_models, X_test_eng, y_test)
            logger.info(f"\nModel comparison:\n{comparison_df}")

            # 11. Select best model
            self.best_model_name = comparison_df.iloc[0]["model"]
            best_model = all_models[self.best_model_name]
            logger.info(f"Best model: {self.best_model_name}")

            # 12. Log to MLflow
            logger.info("Step 12: Logging to MLflow")
            best_metrics = comparison_df.iloc[0].to_dict()
            self.model_store.log_run(
                model_name="quality_inspection",
                model_version="1.0",
                dataset="steel_plates",
                best_model_name=self.best_model_name,
                metrics=best_metrics,
                all_model_metrics=comparison_df.to_dict("records"),
            )

            # 13. Persist best model
            logger.info("Step 13: Persisting best model")
            artifacts = self.model_store.persist_best_model(
                model=best_model,
                model_name=self.best_model_name,
                pipeline_name="quality_inspection",
            )

            logger.info("Quality Inspection pipeline completed successfully")
            return {
                "status": "success",
                "best_model": self.best_model_name,
                "metrics": best_metrics,
                "comparison": comparison_df.to_dict("records"),
                "artifacts": artifacts,
            }

        except Exception as e:
            logger.error(f"QI pipeline failed: {str(e)}", exc_info=True)
            raise
