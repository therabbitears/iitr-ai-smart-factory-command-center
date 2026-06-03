from __future__ import annotations
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from app.core.config import settings
from app.ml.predictive_maintenance.evaluate import compare_models
from app.ml.predictive_maintenance.features import add_engineered_features, get_feature_columns
from app.ml.predictive_maintenance.loader import PredictiveMaintenanceLoader
from app.ml.predictive_maintenance.model_store import ModelStore
from app.ml.predictive_maintenance.preprocessing import clean_data, split_data
from app.ml.predictive_maintenance.train import build_classifiers, train_ann


class PredictiveMaintenancePipeline:
    """End-to-end predictive maintenance training and evaluation pipeline."""

    def __init__(self, source_path: Path | str) -> None:
        self.loader = PredictiveMaintenanceLoader(source_path)
        self.model_store = ModelStore()

    def run(self) -> dict[str, Any]:
        df = self.loader.load()
        validation = self.loader.validate(df)
        if not validation.get("success", False):
            raise ValueError("Validation failed for AI4I dataset")

        df = clean_data(df)
        df = add_engineered_features(df)

        X_train, X_test, y_train, y_test = split_data(df)

        models = self._train_models(X_train, y_train, X_test, y_test)
        metrics_df = compare_models(models, X_test, y_test)

        best_row = metrics_df.iloc[0]
        best_name = best_row["model"]
        best_model = models[best_name]

        run_metadata = {
            "dataset_version": self.loader.version(df),
            "validation": validation,
        }

        artifact_uri = self.model_store.log_run(
            model_name=best_name,
            model=best_model,
            params={"feature_columns": get_feature_columns()},
            metrics=best_row.drop(labels="model").to_dict(),
            artifact_path=f"{best_name}_artifact",
        )

        persistence_path = self.model_store.persist_best_model(best_model, best_name)

        return {
            "best_model": best_name,
            "metrics": metrics_df.to_dict(orient="records"),
            "artifact_uri": artifact_uri,
            "persisted_path": str(persistence_path),
            **run_metadata,
        }

    def _train_models(self, X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series) -> dict[str, Any]:
        estimators = build_classifiers()
        trained: dict[str, Any] = {}
        for name, estimator in estimators.items():
            estimator.fit(X_train, y_train)
            trained[name] = estimator

        X_ann_train, X_ann_val, y_ann_train, y_ann_val = split_data(
            pd.concat([X_train, y_train], axis=1), test_size=0.2, random_state=42
        )

        X_ann_train_arr = X_ann_train.to_numpy()
        X_ann_val_arr = X_ann_val.to_numpy()
        y_ann_train_arr = y_ann_train.to_numpy()
        y_ann_val_arr = y_ann_val.to_numpy()
        ann_model = train_ann(X_ann_train_arr, y_ann_train_arr, X_ann_val_arr, y_ann_val_arr)
        trained["ann"] = ann_model

        return trained
