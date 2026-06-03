"""End-to-end pipeline for Inventory Optimization training and evaluation."""
from typing import Optional
import os
import joblib
from .loader import InventoryLoader
from .preprocessing import clean_data, aggregate_inventory
from .features import InventoryFeatureEngineer
from .train import train_models, save_model
from .evaluate import compare_models


class InventoryOptimizationPipeline:
    def __init__(self, model_dir: str = 'models/inventory_optimization'):
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)

    def run(self, df=None, csv_path: Optional[str] = None):
        if df is None and csv_path is None:
            raise ValueError('Provide df or csv_path')

        if df is None:
            df = InventoryLoader.load_csv(csv_path)

        df = clean_data(df)
        df = aggregate_inventory(df, group_cols=('warehouse','sku','date'))

        fe = InventoryFeatureEngineer()
        df_feat = fe.fit_transform(df)

        # simple temporal split
        n = len(df_feat)
        train_end = int(n * 0.7)
        val_end = train_end + int(n * 0.15)

        df_train = df_feat.iloc[:train_end].reset_index(drop=True)
        df_val = df_feat.iloc[train_end:val_end].reset_index(drop=True)
        df_test = df_feat.iloc[val_end:].reset_index(drop=True)

        feature_cols = [c for c in df_feat.columns if c not in ['date','warehouse','sku','demand']]

        X_train = df_train[feature_cols].values
        y_train = df_train['demand'].values
        X_test = df_test[feature_cols].values
        y_test = df_test['demand'].values

        models = train_models(X_train, y_train)
        results = compare_models(models, X_test, y_test)

        # save best model
        best_name = results.iloc[0]['model']
        best_model = models[best_name]
        save_model(best_model, os.path.join(self.model_dir, f'best_{best_name.replace(" ","_")}.pkl'))

        return {'models': models, 'results': results, 'feature_columns': feature_cols}
