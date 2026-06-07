#!/usr/bin/env python3
"""
Generate a simple Markdown daily trend report from a TrendPilot AI source log CSV.

This script is intentionally dependency-free and uses only Python's standard library.
It does not scrape websites, call external APIs, or send messages.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path
from typing import Any

REQUIRED_COLUMNS = [
    "record_id",
    "source_type",
    "source_name",
    "source_url",
    "collection_date",
    "publication_date",
    "region",
    "category",
    "keyword",
    "product_name",
    "trend_signal",
    "evidence_summary",
    "target_audience",
    "pain_point",
    "content_angle",
    "price_signal",
    "competition_signal",
    "risk_note",
    "risk_level",
    "confidence",
    "opportunity_score",
    "next_action",
    "review_status",
    "reviewer_note",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown trend report from a TrendPilot AI source log CSV."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to source-log CSV, for example examples/sample-source-log.csv",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to output Markdown report, for example examples/generated-daily-report.md",
    )
    parser.add_argument(
        "--region",
        default=None,
        help="Optional region filter, for example 'United States'",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of records to include. Default: 10",
    )
    parser.add_argument(
        "--title",
        default="TrendPilot AI Daily Trend Report",
        help="Report title. Default: TrendPilot AI Daily Trend Report",
    )
    return parser.parse_args()


def read_records(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames is None:
            raise ValueError("CSV file does not contain a header row.")

        missing = [column for column in REQUIRED_COLUMNS if column not in reader.fieldnames]
        if missing:
            raise ValueError(f"CSV is missing required columns: {', '.join(missing)}")

        return [dict(row) for row in reader]


def score_value(record: dict[str, str]) -> int:
    try:
        return int(str(record.get("opportunity_score", "0")).strip() or "0")
    except ValueError:
        return 0


def filter_records(
    records: list[dict[str, str]], region: str | None, limit: int
) -> list[dict[str, str]]:
    filtered = records
    if region:
        filtered = [
            record
            for record in filtered
            if record.get("region", "").strip().lower() == region.strip().lower()
        ]

    filtered = sorted(filtered, key=score_value, reverse=True)
    return filtered[: max(limit, 0)]


def safe_text(value: Any, fallback: str = "Not provided") -> str:
    text = str(value or "").strip()
    return text if text else fallback


def build_report(records: list[dict[str, str]], title: str, source_path: Path) -> str:
    today = date.today().isoformat()
    lines: list[str] = [
        f"# {title}",
        "",
        f"Generated: {today}",
        f"Source file: `{source_path}`",
        "",
        "> This report is generated from local CSV records. It is for research and workflow demonstration only. It does not guarantee demand, sales, profit, or product success.",
        "",
        "## Summary",
        "",
        f"Records included: {len(records)}",
        "",
    ]

    if not records:
        lines.extend(
            [
                "No matching records found.",
                "",
                "## Human Review Reminder",
                "",
                "- Check source freshness and source URLs.",
                "- Confirm risk notes and risk levels.",
                "- Do not publish or monetize without human review.",
                "",
            ]
        )
        return "\n".join(lines)

    lines.extend(["## Top Trend Signals", ""])

    for index, record in enumerate(records, start=1):
        product_name = safe_text(record.get("product_name"), "Unnamed product idea")
        lines.extend(
            [
                f"### {index}. {product_name}",
                "",
                f"- **Record ID:** {safe_text(record.get('record_id'))}",
                f"- **Category:** {safe_text(record.get('category'))}",
                f"- **Region:** {safe_text(record.get('region'))}",
                f"- **Keyword:** {safe_text(record.get('keyword'))}",
                f"- **Trend Signal:** {safe_text(record.get('trend_signal'))}",
                f"- **Evidence Summary:** {safe_text(record.get('evidence_summary'))}",
                f"- **Target Audience:** {safe_text(record.get('target_audience'))}",
                f"- **Pain Point:** {safe_text(record.get('pain_point'))}",
                f"- **Content Angle:** {safe_text(record.get('content_angle'))}",
                f"- **Price Signal:** {safe_text(record.get('price_signal'))}",
                f"- **Competition Signal:** {safe_text(record.get('competition_signal'))}",
                f"- **Opportunity Score:** {safe_text(record.get('opportunity_score'))}",
                f"- **Risk Level:** {safe_text(record.get('risk_level'))}",
                f"- **Risk Note:** {safe_text(record.get('risk_note'))}",
                f"- **Confidence:** {safe_text(record.get('confidence'))}",
                f"- **Review Status:** {safe_text(record.get('review_status'))}",
                f"- **Suggested Next Action:** {safe_text(record.get('next_action'))}",
                f"- **Source:** {safe_text(record.get('source_name'))} — {safe_text(record.get('source_url'))}",
                "",
            ]
        )

    lines.extend(
        [
            "## Human Review Checklist",
            "",
            "- [ ] Sources are public and legally accessible.",
            "- [ ] Source URLs are checked and still available.",
            "- [ ] No private personal data is included.",
            "- [ ] Risk note and risk level are reviewed.",
            "- [ ] No sales, profit, or demand guarantee is made.",
            "- [ ] Final report is approved by a human reviewer before use.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    records = read_records(input_path)
    selected_records = filter_records(records, args.region, args.limit)
    report = build_report(selected_records, args.title, input_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    print(f"Generated report: {output_path}")
    print(f"Records included: {len(selected_records)}")


if __name__ == "__main__":
    main()
