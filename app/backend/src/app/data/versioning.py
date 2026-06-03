from __future__ import annotations
from datetime import datetime
from hashlib import sha256
from pathlib import Path

import pandas as pd

from app.data.schemas import DatasetVersionInfo


class DatasetVersioning:
    """Dataset versioning service to compute stable version identifiers."""

    @staticmethod
    def hash_file(path: Path) -> str:
        digest = sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(8192), b""):
                digest.update(chunk)
        return digest.hexdigest()

    @staticmethod
    def hash_schema(df: pd.DataFrame) -> str:
        items = [f"{col}:{str(dtype)}" for col, dtype in df.dtypes.items()]
        sorted_items = sorted(items)
        digest = sha256("|".join(sorted_items).encode("utf-8"))
        return digest.hexdigest()

    @staticmethod
    def version_id(raw_checksum: str, schema_checksum: str, row_count: int, column_count: int) -> str:
        digest = sha256(
            f"{raw_checksum}:{schema_checksum}:{row_count}:{column_count}".encode("utf-8")
        )
        return digest.hexdigest()

    @classmethod
    def create_version(cls, dataset_name: str, raw_path: Path, df: pd.DataFrame) -> DatasetVersionInfo:
        raw_checksum = cls.hash_file(raw_path)
        schema_checksum = cls.hash_schema(df)

        version_info = DatasetVersionInfo(
            dataset_name=dataset_name,
            version_id=cls.version_id(raw_checksum, schema_checksum, df.shape[0], df.shape[1]),
            source_path=raw_path,
            raw_checksum=raw_checksum,
            schema_checksum=schema_checksum,
            row_count=int(df.shape[0]),
            column_count=int(df.shape[1]),
            created_at=datetime.utcnow(),
            metadata={
                "raw_uri": str(raw_path),
                "generated_at": datetime.utcnow().isoformat(),
            },
        )
        return version_info
