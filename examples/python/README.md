# Python Examples

This folder contains small, dependency-free Python examples for TrendPilot AI.

These scripts are intentionally lightweight.
They are designed for local testing, CSV formatting, report generation, and scoring model demonstration.

They do **not**:

- Scrape websites
- Call external APIs
- Send Telegram messages or emails
- Collect private data
- Automate outreach
- Guarantee product demand, sales, or profit

---

## Requirements

Python 3.10 or newer is recommended.

No third-party packages are required.

---

## 1. Generate a daily Markdown report

From the repository root, run:

```bash
python examples/python/daily_report_generator.py \
  --input examples/sample-source-log.csv \
  --output examples/generated-daily-report.md
```

Optional filters:

```bash
python examples/python/daily_report_generator.py \
  --input examples/sample-source-log.csv \
  --output examples/generated-daily-report.md \
  --region "United States" \
  --limit 5
```

The script reads a source log CSV and creates a simple Markdown report grouped by opportunity score.

---

## 2. Score a product idea

Example:

```bash
python examples/python/score_product_idea.py \
  --product-name "Modular Desk Cable Organizer" \
  --category "Home Office Accessories" \
  --region "United States" \
  --demand 4 \
  --social 3 \
  --price 3 \
  --supplier 4 \
  --differentiation 3 \
  --competition 3 \
  --shipping 1 \
  --compliance 1 \
  --risk-level Low \
  --confidence Medium \
  --review-status "Needs Review"
```

Optional CSV output:

```bash
python examples/python/score_product_idea.py \
  --product-name "Modular Desk Cable Organizer" \
  --category "Home Office Accessories" \
  --region "United States" \
  --demand 4 \
  --social 3 \
  --price 3 \
  --supplier 4 \
  --differentiation 3 \
  --competition 3 \
  --shipping 1 \
  --compliance 1 \
  --risk-level Low \
  --confidence Medium \
  --review-status "Needs Review" \
  --csv-output examples/generated-product-score.csv
```

---

## Scoring formula

```text
Opportunity Score =
Demand Signal
+ Social Visibility
+ Price Potential
+ Supplier Availability
+ Differentiation Potential
- Competition Level
- Shipping Difficulty
- Compliance Risk
```

A high score is only a research signal.
It does not guarantee sales, profit, or product success.
