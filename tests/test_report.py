import unittest

from trendpilot.report import build_daily_report, filter_records


class ReportTests(unittest.TestCase):
    def test_filter_records_sorts_by_score(self):
        records = [
            {"product_name": "Low", "region": "US", "opportunity_score": "2"},
            {"product_name": "High", "region": "US", "opportunity_score": "9"},
        ]
        selected = filter_records(records, region="US", limit=1)
        self.assertEqual(selected[0]["product_name"], "High")

    def test_build_report_contains_review_fields(self):
        report = build_daily_report([
            {
                "record_id": "TP-1",
                "product_name": "Desk organizer",
                "category": "Home office",
                "region": "US",
                "keyword": "desk organization",
                "trend_signal": "Rising public interest",
                "evidence_summary": "Sample evidence",
                "target_audience": "Remote workers",
                "pain_point": "Clutter",
                "content_angle": "Small desk setup",
                "price_signal": "Mid price",
                "competition_signal": "Crowded",
                "opportunity_score": "7",
                "risk_level": "Low",
                "risk_note": "Needs source review",
                "confidence": "Medium",
                "review_status": "Needs Review",
                "next_action": "Validate sources",
                "source_name": "Example",
                "source_url": "https://example.com",
            }
        ])
        self.assertIn("Risk Level", report)
        self.assertIn("Human Review Checklist", report)


if __name__ == "__main__":
    unittest.main()
