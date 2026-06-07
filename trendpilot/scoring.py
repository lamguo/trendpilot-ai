"""Product opportunity scoring utilities.

This module is deterministic and dependency-free. It does not claim or predict
real sales, profit, or demand. It only calculates a transparent research score
from user-provided evidence scores.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from .fields import (
    CONFIDENCE_LEVELS,
    REVIEW_STATUSES,
    RISK_LEVELS,
    SCORE_FIELDS,
    SCORE_INTERPRETATIONS,
)


def bounded_score(value: int | str, field_name: str) -> int:
    """Return an integer score in the inclusive 1..5 range."""
    try:
        score = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be an integer from 1 to 5.") from exc

    if score < 1 or score > 5:
        raise ValueError(f"{field_name} must be between 1 and 5.")
    return score


def normalize_scores(scores: dict[str, int | str]) -> dict[str, int]:
    """Validate and normalize all required score dimensions."""
    missing = [field for field in SCORE_FIELDS if field not in scores]
    if missing:
        raise ValueError(f"Missing score fields: {', '.join(missing)}")
    return {field: bounded_score(scores[field], field) for field in SCORE_FIELDS}


def calculate_opportunity_score(scores: dict[str, int | str]) -> int:
    """Calculate the TrendPilot AI opportunity score.

    Formula:
    demand + social visibility + price potential + supplier availability
    + differentiation potential - competition level - shipping difficulty
    - compliance risk
    """
    normalized = normalize_scores(scores)
    positive = (
        normalized["demand_signal"]
        + normalized["social_visibility"]
        + normalized["price_potential"]
        + normalized["supplier_availability"]
        + normalized["differentiation_potential"]
    )
    negative = (
        normalized["competition_level"]
        + normalized["shipping_difficulty"]
        + normalized["compliance_risk"]
    )
    return positive - negative


def interpret_score(score: int) -> str:
    """Map a numeric score to a standard recommendation label."""
    if score >= 12:
        return "Strong Candidate"
    if score >= 8:
        return "Test Carefully"
    if score >= 4:
        return "Watchlist"
    return "Avoid"


def _validate_choice(value: str, choices: tuple[str, ...], field_name: str) -> str:
    if value not in choices:
        raise ValueError(f"{field_name} must be one of: {', '.join(choices)}")
    return value


def build_product_score_record(
    *,
    score_id: str,
    product_idea: str,
    target_region: str,
    target_audience: str,
    scores: dict[str, int | str],
    category: str | None = None,
    source_urls: list[str] | None = None,
    evidence_summary: str = "Needs source review before use.",
    main_strengths: list[str] | None = None,
    main_risks: list[str] | None = None,
    risk_note: str = "Needs human review before business use.",
    risk_level: str = "Unknown",
    confidence: str = "Low",
    next_action: str = "Validate sources, competitors, pricing, and compliance requirements.",
    review_status: str = "Needs Review",
    reviewer_note: str | None = None,
    evaluated_at: str | None = None,
) -> dict[str, Any]:
    """Build a product score record aligned with schemas/product-score.schema.json."""
    normalized_scores = normalize_scores(scores)
    opportunity_score = calculate_opportunity_score(normalized_scores)
    risk_level = _validate_choice(risk_level, RISK_LEVELS, "risk_level")
    confidence = _validate_choice(confidence, CONFIDENCE_LEVELS, "confidence")
    review_status = _validate_choice(review_status, REVIEW_STATUSES, "review_status")
    interpretation = _validate_choice(interpret_score(opportunity_score), SCORE_INTERPRETATIONS, "score_interpretation")

    return {
        "score_id": score_id,
        "product_idea": product_idea,
        "category": category,
        "target_region": target_region,
        "target_audience": target_audience,
        "evaluated_at": evaluated_at or datetime.now(timezone.utc).isoformat(),
        "source_urls": source_urls or [],
        "evidence_summary": evidence_summary,
        "scores": normalized_scores,
        "opportunity_score": opportunity_score,
        "score_interpretation": interpretation,
        "main_strengths": main_strengths or [],
        "main_risks": main_risks or [],
        "risk_note": risk_note,
        "risk_level": risk_level,
        "confidence": confidence,
        "next_action": next_action,
        "review_status": review_status,
        "reviewer_note": reviewer_note,
    }
