import importlib.util
import unittest


@unittest.skipIf(importlib.util.find_spec("jsonschema") is None, "jsonschema is not installed")
class SchemaSampleTests(unittest.TestCase):
    def test_schema_samples_validate(self):
        from scripts.validate_schema_samples import main

        self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()
