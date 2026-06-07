"""Validate sample JSON files against the project JSON schemas.

This script is intended for CI and local development. Install dev tools first:

    python -m pip install -e ".[dev]"
"""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_MAP = {
    "schemas/trend-signal.schema.json": "examples/sample-trend-signal.json",
    "schemas/product-score.schema.json": "examples/sample-product-score.json",
    "schemas/report-record.schema.json": "examples/sample-report-record.json",
}


def load_json(relative_path: str) -> object:
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []
    for schema_path, sample_path in SAMPLE_MAP.items():
        schema = load_json(schema_path)
        sample = load_json(sample_path)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(sample), key=lambda error: list(error.path))
        if errors:
            failures.append(f"{sample_path} failed {schema_path}:")
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                failures.append(f"  - {location}: {error.message}")
        else:
            print(f"OK: {sample_path} matches {schema_path}")

    if failures:
        print("Schema validation failed:")
        for failure in failures:
            print(failure)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
