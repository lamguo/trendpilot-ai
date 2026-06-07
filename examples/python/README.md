# Python Examples

These examples demonstrate the lightweight local execution layer included in TrendPilot AI.

The core package is dependency-free and can be run directly with Python 3.9+.

## Install locally

From the repository root:

```bash
python -m pip install -e .
```

## Validate the sample source log

```bash
python -m trendpilot validate --input examples/sample-source-log.csv
```

or, after editable install:

```bash
trendpilot validate --input examples/sample-source-log.csv
```

## Generate a Markdown report

```bash
python -m trendpilot report \
  --input examples/sample-source-log.csv \
  --output examples/generated-daily-report.md \
  --limit 5
```

Backward-compatible wrapper:

```bash
python examples/python/daily_report_generator.py \
  --input examples/sample-source-log.csv \
  --output examples/generated-daily-report.md
```

## Score a product idea

```bash
python -m trendpilot score \
  --score-id TP-DEMO-001 \
  --product-idea "Portable desk organizer" \
  --category "Home office" \
  --target-region "United States" \
  --target-audience "Remote workers and students" \
  --demand 4 \
  --social 3 \
  --price 3 \
  --supplier 4 \
  --differentiation 3 \
  --competition 4 \
  --shipping 2 \
  --compliance 1 \
  --risk-level Low \
  --confidence Medium
```

Backward-compatible wrapper:

```bash
python examples/python/score_product_idea.py \
  --product-name "Portable desk organizer" \
  --category "Home office" \
  --region "United States" \
  --demand 4 \
  --social 3 \
  --price 3 \
  --supplier 4 \
  --differentiation 3 \
  --competition 4 \
  --shipping 2 \
  --compliance 1
```

## Run tests

```bash
python -m unittest discover -s tests
```

## Safety note

These examples do not scrape websites, call external APIs, or send messages. They only process local inputs. Scores are research signals only and do not guarantee demand, sales, profit, or product success.
