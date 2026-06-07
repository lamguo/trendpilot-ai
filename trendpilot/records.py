"""CSV reading and lightweight validation helpers."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from .fields import CONFIDENCE_LEVELS, REVIEW_STATUSES, RISK_LEVELS, SOURCE_LOG_FIELDS


def read_source_log(path: str | Path) -> list[dict[str, str]]:
    """Read a TrendPilot AI source log CSV."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Source log not found: {csv_path}")

    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None:
            raise ValueError("CSV file does not contain a header row.")
        missing = [field for field in SOURCE_LOG_FIELDS if field not in reader.fieldnames]
        if missing:
            raise ValueError(f"CSV is missing required columns: {', '.join(missing)}")
        return [dict(row) for row in reader]


def _is_blank(value: Any) -> bool:
    return str(value or "").strip() == ""


def validate_source_log_records(records: list[dict[str, str]]) -> list[str]:
    """Return validation errors for source log records.

    The validator intentionally performs lightweight checks only. JSON Schema can
    be used separately by advanced users, but this keeps the core package
    dependency-free.
    """
    errors: list[str] = []
    required_non_empty = ["record_id", "source_url", "evidence_summary", "risk_note", "risk_level", "confidence", "review_status"]

    for index, record in enumerate(records, start=2):
        for field in required_non_empty:
            if _is_blank(record.get(field)):
                errors.append(f"Row {index}: {field} is required.")

        risk_level = str(record.get("risk_level", "")).strip()
        if risk_level and risk_level not in RISK_LEVELS:
            errors.append(f"Row {index}: risk_level must be one of {', '.join(RISK_LEVELS)}.")

        confidence = str(record.get("confidence", "")).strip()
        if confidence and confidence not in CONFIDENCE_LEVELS:
            errors.append(f"Row {index}: confidence must be one of {', '.join(CONFIDENCE_LEVELS)}.")

        review_status = str(record.get("review_status", "")).strip()
        if review_status and review_status not in REVIEW_STATUSES:
            errors.append(f"Row {index}: review_status must be one of {', '.join(REVIEW_STATUSES)}.")

        score = str(record.get("opportunity_score", "")).strip()
        if score:
            try:
                int(score)
            except ValueError:
                errors.append(f"Row {index}: opportunity_score must be an integer.")

    return errors


def validate_source_log_file(path: str | Path) -> list[str]:
    """Read and validate a source log CSV file."""
    return validate_source_log_records(read_source_log(path))
