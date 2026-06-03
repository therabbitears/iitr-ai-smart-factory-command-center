from __future__ import annotations

import logging
import pandas as pd

logger = logging.getLogger(__name__)


class DemandForecastingLoader:
    """Load and validate Store Item Demand Forecasting dataset."""

    def __init__(self) -> None:
        self.df: pd.DataFrame | None = None
        logger.info("DemandForecastingLoader initialized")

    def load(self, source_path: str) -> pd.DataFrame:
        """Load Store Item Demand dataset from CSV.
        
        Args:
            source_path: Path to Store Item Demand CSV file
        
        Returns:
            Loaded DataFrame
        
        Raises:
            FileNotFoundError: If source file not found
            ValueError: If required columns missing
        """
        try:
            self.df = pd.read_csv(source_path)
            logger.info(f"Loaded demand data: {self.df.shape}")
        except FileNotFoundError as e:
            logger.error(f"Demand data file not found: {source_path}")
            raise
        except Exception as e:
            logger.error(f"Failed to load demand data: {str(e)}")
            raise

        # Validate required columns
        required_cols = {"date", "store", "item", "demand"}
        missing_cols = required_cols - set(self.df.columns)
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            raise ValueError(f"Missing columns: {missing_cols}")

        # Convert date to datetime
        try:
            self.df["date"] = pd.to_datetime(self.df["date"])
            self.df = self.df.sort_values("date").reset_index(drop=True)
            logger.info(f"Date range: {self.df['date'].min()} to {self.df['date'].max()}")
        except Exception as e:
            logger.error(f"Failed to parse dates: {str(e)}")
            raise

        return self.df
