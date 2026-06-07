import unittest

from trendpilot.scoring import calculate_opportunity_score, interpret_score, build_product_score_record


class ScoringTests(unittest.TestCase):
    def test_calculate_opportunity_score(self):
        scores = {
            "demand_signal": 5,
            "social_visibility": 4,
            "price_potential": 3,
            "supplier_availability": 4,
            "differentiation_potential": 3,
            "competition_level": 4,
            "shipping_difficulty": 2,
            "compliance_risk": 1,
        }
        self.assertEqual(calculate_opportunity_score(scores), 12)

    def test_interpret_score(self):
        self.assertEqual(interpret_score(12), "Strong Candidate")
        self.assertEqual(interpret_score(8), "Test Carefully")
        self.assertEqual(interpret_score(4), "Watchlist")
        self.assertEqual(interpret_score(3), "Avoid")

    def test_invalid_score_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_opportunity_score({
                "demand_signal": 6,
                "social_visibility": 4,
                "price_potential": 3,
                "supplier_availability": 4,
                "differentiation_potential": 3,
                "competition_level": 4,
                "shipping_difficulty": 2,
                "compliance_risk": 1,
            })

    def test_build_record_matches_schema_names(self):
        record = build_product_score_record(
            score_id="TP-TEST-001",
            product_idea="Desk organizer",
            category="Home office",
            target_region="United States",
            target_audience="Remote workers",
            scores={
                "demand_signal": 4,
                "social_visibility": 3,
                "price_potential": 3,
                "supplier_availability": 4,
                "differentiation_potential": 3,
                "competition_level": 4,
                "shipping_difficulty": 2,
                "compliance_risk": 1,
            },
            risk_level="Low",
            confidence="Medium",
        )
        self.assertIn("scores", record)
        self.assertIn("price_potential", record["scores"])
        self.assertEqual(record["review_status"], "Needs Review")


if __name__ == "__main__":
    unittest.main()
