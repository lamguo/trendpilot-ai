"""Command line interface for TrendPilot AI."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from . import __version__
from .fields import CONFIDENCE_LEVELS, REVIEW_STATUSES, RISK_LEVELS, SCORE_FIELDS
from .records import read_source_log, validate_source_log_records
from .report import build_daily_report, filter_records
from .scoring import build_product_score_record


def _score_arg(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("score must be an integer from 1 to 5") from exc
    if number < 1 or number > 5:
        raise argparse.ArgumentTypeError("score must be between 1 and 5")
    return number


def _add_score_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--demand-signal", "--demand", type=_score_arg)
    parser.add_argument("--social-visibility", "--social", type=_score_arg)
    parser.add_argument("--price-potential", "--price", type=_score_arg)
    parser.add_argument("--supplier-availability", "--supplier", type=_score_arg)
    parser.add_argument("--differentiation-potential", "--differentiation", type=_score_arg)
    parser.add_argument("--competition-level", "--competition", type=_score_arg)
    parser.add_argument("--shipping-difficulty", "--shipping", type=_score_arg)
    parser.add_argument("--compliance-risk", "--compliance", type=_score_arg)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="trendpilot", description="TrendPilot AI local execution toolkit")
    parser.add_argument("--version", action="version", version=f"TrendPilot AI {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate a source log CSV")
    validate.add_argument("--input", required=True, help="Path to source log CSV")

    report = subparsers.add_parser("report", help="Generate a Markdown daily report from source log CSV")
    report.add_argument("--input", required=True, help="Path to source log CSV")
    report.add_argument("--output", required=True, help="Path to output Markdown report")
    report.add_argument("--region", default=None, help="Optional exact region filter")
    report.add_argument("--limit", type=int, default=10, help="Maximum number of records to include")
    report.add_argument("--title", default="TrendPilot AI Daily Trend Report")

    score = subparsers.add_parser("score", help="Score a product idea and output schema-aligned JSON")
    score.add_argument("--input", default=None, help="Optional product score input JSON file")
    score.add_argument("--score-id", default=None)
    score.add_argument("--product-idea", default=None)
    score.add_argument("--category", default=None)
    score.add_argument("--target-region", default=None)
    score.add_argument("--target-audience", default=None)
    score.add_argument("--source-url", action="append", default=[], help="Source URL. Can be used multiple times.")
    score.add_argument("--evidence-summary", default=None)
    score.add_argument("--main-strength", action="append", default=[])
    score.add_argument("--main-risk", action="append", default=[])
    score.add_argument("--risk-note", default=None)
    score.add_argument("--risk-level", default=None, choices=RISK_LEVELS)
    score.add_argument("--confidence", default=None, choices=CONFIDENCE_LEVELS)
    score.add_argument("--next-action", default=None)
    score.add_argument("--review-status", default=None, choices=REVIEW_STATUSES)
    score.add_argument("--reviewer-note", default=None)
    score.add_argument("--output", default=None, help="Optional JSON output file. If omitted, prints to stdout.")
    _add_score_args(score)

    return parser


def _load_json(path: str | Path) -> dict[str, Any]:
    input_path = Path(path)
    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Input JSON file not found: {input_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Input JSON is invalid: {input_path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object.")
    return data


def _choose(cli_value: Any, payload: dict[str, Any], key: str, default: Any = None) -> Any:
    return cli_value if cli_value not in (None, [], "") else payload.get(key, default)


def _required(value: Any, field_name: str) -> Any:
    if value in (None, ""):
        raise ValueError(f"Missing required field: {field_name}")
    return value


def _scores_from_args(args: argparse.Namespace, payload: dict[str, Any]) -> dict[str, Any]:
    payload_scores = payload.get("scores", {})
    if payload_scores is None:
        payload_scores = {}
    if not isinstance(payload_scores, dict):
        raise ValueError("Input JSON field 'scores' must be an object.")

    scores: dict[str, Any] = {}
    for field in SCORE_FIELDS:
        arg_name = field
        cli_value = getattr(args, arg_name)
        scores[field] = _choose(cli_value, payload_scores, field)
    missing = [field for field, value in scores.items() if value in (None, "")]
    if missing:
        raise ValueError("Missing score fields: " + ", ".join(missing))
    return scores


def run_validate(args: argparse.Namespace) -> int:
    records = read_source_log(args.input)
    errors = validate_source_log_records(records)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validation passed: {len(records)} record(s) checked.")
    return 0


def run_report(args: argparse.Namespace) -> int:
    records = read_source_log(args.input)
    errors = validate_source_log_records(records)
    if errors:
        print("Validation failed. Fix the source log before generating a report:")
        for error in errors:
            print(f"- {error}")
        return 1
    selected = filter_records(records, region=args.region, limit=args.limit)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_daily_report(selected, title=args.title, source_path=args.input), encoding="utf-8")
    print(f"Generated report: {output_path}")
    print(f"Records included: {len(selected)}")
    return 0


def run_score(args: argparse.Namespace) -> int:
    try:
        payload = _load_json(args.input) if args.input else {}
        scores = _scores_from_args(args, payload)
        record = build_product_score_record(
            score_id=_required(_choose(args.score_id, payload, "score_id", "TP-MANUAL-001"), "score_id"),
            product_idea=_required(_choose(args.product_idea, payload, "product_idea"), "product_idea"),
            category=_choose(args.category, payload, "category"),
            target_region=_required(_choose(args.target_region, payload, "target_region"), "target_region"),
            target_audience=_required(_choose(args.target_audience, payload, "target_audience"), "target_audience"),
            source_urls=_choose(args.source_url, payload, "source_urls", []),
            evidence_summary=_choose(
                args.evidence_summary, payload, "evidence_summary",
                "Needs source review before use."),
            main_strengths=_choose(args.main_strength, payload, "main_strengths", []),
            main_risks=_choose(args.main_risk, payload, "main_risks", []),
            scores=scores,
            risk_note=_choose(args.risk_note, payload, "risk_note", "Needs human review before business use."),
            risk_level=_choose(args.risk_level, payload, "risk_level", "Unknown"),
            confidence=_choose(args.confidence, payload, "confidence", "Low"),
            next_action=_choose(
                args.next_action,
                payload,
                "next_action",
                "Validate sources, competitors, pricing, and compliance requirements.",
            ),
            review_status=_choose(args.review_status, payload, "review_status", "Needs Review"),
            reviewer_note=_choose(args.reviewer_note, payload, "reviewer_note"),
            evaluated_at=_choose(None, payload, "evaluated_at"),
        )
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1

    output_payload = json.dumps(record, indent=2, ensure_ascii=False)
    if args.output:
        path = Path(args.output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output_payload + "\n", encoding="utf-8")
        print(f"Saved product score JSON: {path}")
    else:
        print(output_payload)
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "validate":
        return run_validate(args)
    if args.command == "report":
        return run_report(args)
    if args.command == "score":
        return run_score(args)
    parser.error("Unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
