from pathlib import Path
import logging

import pandas as pd

from app.data.loaders import AI4IDatasetLoader

logger = logging.getLogger(__name__)


class PredictiveMaintenanceLoader:
    """Loads AI4I predictive maintenance data with validation and profiling."""

    def __init__(self, source_path: Path | str) -> None:
        self.source_path = Path(source_path)
        self.loader = AI4IDatasetLoader(source_path)
        logger.info(f"Initialized loader for {source_path}")

    def load(self) -> pd.DataFrame:
        """Load raw dataset.

        Returns:
            DataFrame with raw data
        """
        df = self.loader.load_raw()
        logger.info(f"Loaded {len(df)} rows from {self.source_path}")
        return df

    def validate(self, df: pd.DataFrame) -> dict[str, object]:
        """Validate dataset schema and content.

        Args:
            df: Dataset to validate

        Returns:
            Validation result dict with 'success' key
        """
        try:
            result = self.loader.validate(df)
            if not result.success:
                logger.warning(f"Validation failed with errors: {result.errors}")
            return result.dict()
        except Exception as e:
            logger.error(f"Validation exception: {str(e)}")
            raise

    def profile(self, df: pd.DataFrame) -> dict[str, object]:
        """Generate dataset profile.

        Args:
            df: Dataset to profile

        Returns:
            Profile dict with statistics
        """
        return self.loader.profile(df).dict()

    def version(self, df: pd.DataFrame) -> dict[str, object]:
        """Generate version info for the dataset.

        Args:
            df: Dataset to version

        Returns:
            Version info dict with checksums and timestamps
        """
        return self.loader.version(df).dict()
