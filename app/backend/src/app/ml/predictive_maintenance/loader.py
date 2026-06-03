from pathlib import Path

import pandas as pd

from app.data.loaders import AI4IDatasetLoader


class PredictiveMaintenanceLoader:
    """Loads AI4I predictive maintenance data and returns a normalized DataFrame."""

    def __init__(self, source_path: Path | str) -> None:
        self.loader = AI4IDatasetLoader(source_path)

    def load(self) -> pd.DataFrame:
        df = self.loader.load_raw()
        return df

    def validate(self, df: pd.DataFrame) -> dict[str, object]:
        return self.loader.validate(df).dict()

    def profile(self, df: pd.DataFrame) -> dict[str, object]:
        return self.loader.profile(df).dict()

    def version(self, df: pd.DataFrame) -> dict[str, object]:
        return self.loader.version(df).dict()
