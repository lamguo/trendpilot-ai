"""TrendPilot AI lightweight execution layer.

The package intentionally stays dependency-free for the core workflow.
It provides local scoring, CSV validation, and Markdown report generation.
"""

from .scoring import calculate_opportunity_score, interpret_score, build_product_score_record
from .records import read_source_log, validate_source_log_records
from .report import build_daily_report

__all__ = [
    "calculate_opportunity_score",
    "interpret_score",
    "build_product_score_record",
    "read_source_log",
    "validate_source_log_records",
    "build_daily_report",
]

__version__ = "0.2.1"
