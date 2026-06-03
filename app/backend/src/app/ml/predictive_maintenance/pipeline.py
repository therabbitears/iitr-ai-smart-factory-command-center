from __future__ import annotations
from pathlib import Path
from typing import Any
import logging

import numpy as np
import pandas as pd

from app.core.config import settings
from app.ml.predictive_maintenance.evaluate import compare_models
from app.ml.predictive_maintenance.features import FeatureEngineer, get_feature_columns
from app.ml.predictive_maintenance.loader import PredictiveMaintenanceLoader
from app.ml.predictive_maintenance.model_store import ModelStore
from app.ml.predictive_maintenance.preprocessing import (
    clean_data,
    split_data,
    analyze_class_balance,
)
from app.ml.predictive_maintenance.train import build_classifiers, train_ann

logger = logging.getLogger(__name__)


class PredictiveMaintenancePipeline:
    """End-to-end predictive maintenance training and evaluation pipeline with proper train/val/test split."""

    def __init__(self, source_path: Path | str) -> None:
        self.loader = PredictiveMaintenanceLoader(source_path)
        self.model_store = ModelStore()
        self.feature_engineer: FeatureEngineer | None = None

    def run(self) -> dict[str, Any]:
        """Execute full training pipeline."""
        try:
            logger.info("Starting Predictive Maintenance pipeline")
            
            # Data loading and validation
            df = self.loader.load()
            validation = self.loader.validate(df)
            if not validation.get("success", False):
                raise ValueError(f"Validation failed: {validation}")
            logger.info("Data validation passed")

            # Data cleaning
            df = clean_data(df)
            profile = self.loader.profile(df)
            logger.info(f"Data profile: {profile.row_count} rows, {profile.column_count} columns")

            # Class balance analysis
            class_balance = analyze_class_balance(df["machine_failure"])
            if class_balance["imbalance_ratio"] > 10:
                logger.warning(f"Highly imbalanced dataset: {class_balance}")

            # Train-test split BEFORE feature engineering to avoid data leakage
            X_train, X_test, y_train, y_test = split_data(df)
            logger.info("Train-test split completed")

            # Fit feature engineer on training data only
            self.feature_engineer = FeatureEngineer().fit(X_train)
            X_train_engineered = self.feature_engineer.transform(X_train)
            X_test_engineered = self.feature_engineer.transform(X_test)
            logger.info("Feature engineering completed (fitted on training data only)")

            # Model training with proper validation set for ANN
            models = self._train_models_with_validation(
                X_train_engineered, y_train, X_test_engineered, y_test
            )
            logger.info(f"Trained {len(models)} models")

            # Model evaluation and comparison
            metrics_df = compare_models(models, X_test_engineered, y_test)
            logger.info(f"Model comparison complete. Top model: {metrics_df.iloc[0]['model']}")

            # Select best model
            best_row = metrics_df.iloc[0]
            best_name = best_row["model"]
            best_model = models[best_name]
            logger.info(f"Best model selected: {best_name} with F1: {best_row['f1_score']:.4f}")

            # Persistence and logging
            run_metadata = {
                "dataset_version": self.loader.version(df),
                "validation": validation,
                "class_balance": class_balance,
                "feature_engineer_params": {
                    "rotational_speed_min": float(self.feature_engineer.rotational_speed_min),
                    "air_temp_min": float(self.feature_engineer.air_temp_min),
                },
            }

            artifact_uri = self.model_store.log_run(
                model_name=best_name,
                model=best_model,
                params={
                    "feature_columns": get_feature_columns(),
                    "class_balance": class_balance,
                },
                metrics=best_row.drop(labels="model").to_dict(),
                artifact_path=f"{best_name}_artifact",
            )

            persistence_path = self.model_store.persist_best_model(best_model, best_name)
            logger.info(f"Model persisted to: {persistence_path}")

            return {
                "best_model": best_name,
                "metrics": metrics_df.to_dict(orient="records"),
                "artifact_uri": artifact_uri,
                "persisted_path": str(persistence_path),
                **run_metadata,
            }
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}", exc_info=True)
            raise

    def _train_models_with_validation(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
        X_test: pd.DataFrame,
        y_test: pd.Series,
    ) -> dict[str, Any]:
        """Train all model types with proper validation split."""
        estimators = build_classifiers()
        trained: dict[str, Any] = {}

        # Train sklearn models
        for name, estimator in estimators.items():
            if name != "ann":
                estimator.fit(X_train, y_train)
                trained[name] = estimator
                logger.info(f"Trained {name}")

        # Train ANN with validation set from training data
        X_train_np = X_train.to_numpy()
        y_train_np = y_train.to_numpy()
        ann_train, ann_val, y_ann_train, y_ann_val = self._create_validation_split(
            X_train_np, y_train_np
        )
        ann_model = train_ann(ann_train, y_ann_train, ann_val, y_ann_val)
        trained["ann"] = ann_model
        logger.info("Trained ANN")

        return trained

    @staticmethod
    def _create_validation_split(
        X: np.ndarray,
        y: np.ndarray,
        val_size: float = 0.2,
        random_state: int = 42,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Create validation split from training data."""
        from sklearn.model_selection import train_test_split
        return train_test_split(
            X, y, test_size=val_size, random_state=random_state, stratify=y
        )
