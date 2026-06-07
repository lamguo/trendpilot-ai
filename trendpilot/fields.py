"""Central field definitions used by CLI, examples, and tests."""

RISK_LEVELS = ("Low", "Medium", "High", "Avoid", "Unknown")
CONFIDENCE_LEVELS = ("Low", "Medium", "High")
REVIEW_STATUSES = ("Draft", "Needs Review", "Approved", "Rejected", "Watchlist")
SCORE_INTERPRETATIONS = ("Strong Candidate", "Test Carefully", "Watchlist", "Avoid")

SOURCE_LOG_FIELDS = [
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

PRODUCT_SCORE_FIELDS = [
    "score_id",
    "product_idea",
    "category",
    "target_region",
    "target_audience",
    "evaluated_at",
    "source_urls",
    "evidence_summary",
    "scores",
    "opportunity_score",
    "score_interpretation",
    "main_strengths",
    "main_risks",
    "risk_note",
    "risk_level",
    "confidence",
    "next_action",
    "review_status",
    "reviewer_note",
]

SCORE_FIELDS = [
    "demand_signal",
    "social_visibility",
    "price_potential",
    "supplier_availability",
    "differentiation_potential",
    "competition_level",
    "shipping_difficulty",
    "compliance_risk",
]
