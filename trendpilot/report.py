"""Markdown report generation helpers."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any


def safe_text(value: Any, fallback: str = "Not provided") -> str:
    text = str(value or "").strip()
    return text if text else fallback


def score_value(record: dict[str, str]) -> int:
    try:
        return int(str(record.get("opportunity_score", "0")).strip() or "0")
    except ValueError:
        return 0


def filter_records(records: list[dict[str, str]], region: str | None = None, limit: int = 10) -> list[dict[str, str]]:
    filtered = records
    if region:
        filtered = [
            record
            for record in filtered
            if safe_text(record.get("region"), "").lower() == region.strip().lower()
        ]
    return sorted(filtered, key=score_value, reverse=True)[: max(limit, 0)]


def build_daily_report(
    records: list[dict[str, str]],
    *,
    title: str = "TrendPilot AI Daily Trend Report",
    source_path: str | Path | None = None,
) -> str:
    """Build a Markdown daily trend report from source log records."""
    today = date.today().isoformat()
    lines: list[str] = [
        f"# {title}",
        "",
        f"Generated: {today}",
    ]
    if source_path:
        lines.append(f"Source file: `{source_path}`")
    lines.extend(
        [
            "",
            "> Generated from local records for research workflow demonstration only.",
            "> This does not guarantee demand, sales, profit, or product success.",
            "",
            "## Summary",
            "",
            f"Records included: {len(records)}",
            "",
        ]
    )

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
        lines.extend(
            [
                f"### {index}. {safe_text(record.get('product_name'), 'Unnamed product idea')}",
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
