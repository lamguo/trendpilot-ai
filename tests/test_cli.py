import json
import tempfile
import unittest
from pathlib import Path

from trendpilot.cli import main


class CliTests(unittest.TestCase):
    def test_score_from_json_input(self):
        payload = {
            "score_id": "TP-TEST-001",
            "product_idea": "Portable desk organizer",
            "target_region": "United States",
            "target_audience": "Remote workers",
            "scores": {
                "demand_signal": 4,
                "social_visibility": 3,
                "price_potential": 3,
                "supplier_availability": 4,
                "differentiation_potential": 3,
                "competition_level": 4,
                "shipping_difficulty": 2,
                "compliance_risk": 1,
            },
            "risk_note": "Example-only test record; verify real sources before use.",
            "risk_level": "Medium",
            "confidence": "Medium",
            "review_status": "Draft",
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            input_file = tmp_path / "score-input.json"
            output_file = tmp_path / "score-output.json"
            input_file.write_text(json.dumps(payload), encoding="utf-8")

            exit_code = main([
                "score",
                "--input",
                str(input_file),
                "--output",
                str(output_file),
            ])

            self.assertEqual(exit_code, 0)
            data = json.loads(output_file.read_text(encoding="utf-8"))
            self.assertEqual(data["product_idea"], "Portable desk organizer")
            self.assertEqual(data["opportunity_score"], 10)
            self.assertEqual(data["score_interpretation"], "Test Carefully")


if __name__ == "__main__":
    unittest.main()
