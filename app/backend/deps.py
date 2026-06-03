from .services import get_service, PredictionService
from typing import Callable


def get_prediction_service() -> PredictionService:
    """Dependency provider for the PredictionService."""
    return get_service()
