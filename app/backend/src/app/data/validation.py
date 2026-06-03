from __future__ import annotations
from typing import Any

import pandera as pa
from pandera.errors import SchemaError

from app.data.schemas import ValidationResult


class ValidationEngine:
    """Validation engine for dataset DataFrames using Pandera."""

    @staticmethod
    def validate(df: "pd.DataFrame", schema: pa.DataFrameSchema) -> ValidationResult:
        try:
            schema.validate(df, lazy=True)
            return ValidationResult(success=True, errors=[])
        except SchemaError as exc:
            errors: list[dict[str, Any]] = []
            if hasattr(exc, "failure_cases") and exc.failure_cases is not None:
                errors = exc.failure_cases.to_dict("records")
            return ValidationResult(success=False, errors=errors)
