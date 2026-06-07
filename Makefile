.PHONY: install dev test lint schema-check validate report score ci build clean

install:
	python -m pip install -e .

dev:
	python -m pip install -e ".[dev]"

lint:
	python -m ruff check .

test:
	python -m unittest discover -s tests

schema-check:
	python scripts/validate_schema_samples.py

validate:
	python -m trendpilot validate --input examples/sample-source-log.csv

report:
	python -m trendpilot report --input examples/sample-source-log.csv --output examples/generated-daily-report.md --limit 5

score:
	python -m trendpilot score --input examples/sample-product-score-input.json --output examples/generated-product-score.json

ci: lint test schema-check validate report score

build:
	python -m build

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info
	rm -f examples/generated-*.md examples/generated-*.json
