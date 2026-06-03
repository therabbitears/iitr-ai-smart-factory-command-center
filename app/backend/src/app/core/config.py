from pathlib import Path

from pydantic import AnyUrl, BaseSettings, Field


class Settings(BaseSettings):
    fastapi_env: str = Field("development", env="FASTAPI_ENV")
    fastapi_host: str = Field("0.0.0.0", env="FASTAPI_HOST")
    fastapi_port: int = Field(8000, env="FASTAPI_PORT")
    log_level: str = Field("INFO", env="LOG_LEVEL")
    database_url: AnyUrl = Field(..., env="DATABASE_URL")
    mlflow_tracking_uri: AnyUrl = Field("file:///tmp/mlruns", env="MLFLOW_TRACKING_URI")
    mlflow_experiment_name: str = Field("predictive_maintenance", env="MLFLOW_EXPERIMENT_NAME")
    model_registry_path: str = Field("mlruns", env="MLFLOW_ARTIFACT_ROOT")

    class Config:
        env_file = str(Path(__file__).resolve().parents[3] / ".env.example")
        env_file_encoding = "utf-8"


settings = Settings()
