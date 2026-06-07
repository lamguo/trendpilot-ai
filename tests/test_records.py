import csv
import tempfile
import unittest
from pathlib import Path

from trendpilot.fields import SOURCE_LOG_FIELDS
from trendpilot.records import read_source_log, validate_source_log_records


class RecordTests(unittest.TestCase):
    def test_read_and_validate_source_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source-log.csv"
            row = {field: "demo" for field in SOURCE_LOG_FIELDS}
            row.update({
                "risk_level": "Low",
                "confidence": "Medium",
                "review_status": "Needs Review",
                "opportunity_score": "7",
                "source_url": "https://example.com/source",
            })
            with path.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=SOURCE_LOG_FIELDS)
                writer.writeheader()
                writer.writerow(row)

            records = read_source_log(path)
            self.assertEqual(len(records), 1)
            self.assertEqual(validate_source_log_records(records), [])

    def test_invalid_enums_are_reported(self):
        record = {field: "demo" for field in SOURCE_LOG_FIELDS}
        record.update({"risk_level": "Maybe", "confidence": "Medium", "review_status": "Needs Review", "opportunity_score": "7"})
        errors = validate_source_log_records([record])
        self.assertTrue(any("risk_level" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
