#!/usr/bin/env python3
"""Backward-compatible wrapper for local Markdown report generation."""

from __future__ import annotations

import argparse
from pathlib import Path

from trendpilot.records import read_source_log, validate_source_log_records
from trendpilot.report import build_daily_report, filter_records


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown trend report from a TrendPilot AI source log CSV.")
    parser.add_argument("--input", required=True,
                        help="Path to source-log CSV, e.g. examples/sample-source-log.csv")
    parser.add_argument("--output", required=True, help="Path to output Markdown report")
    parser.add_argument("--region", default=None, help="Optional exact region filter, for example 'United States'")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of records to include")
    parser.add_argument("--title", default="TrendPilot AI Daily Trend Report")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = read_source_log(args.input)
    errors = validate_source_log_records(records)
    if errors:
        raise SystemExit("Validation failed:\n" + "\n".join(f"- {error}" for error in errors))
    selected = filter_records(records, region=args.region, limit=args.limit)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_daily_report(selected, title=args.title, source_path=args.input), encoding="utf-8")
    print(f"Generated report: {output_path}")
    print(f"Records included: {len(selected)}")


if __name__ == "__main__":
    main()
