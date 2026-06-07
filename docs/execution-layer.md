# Execution Layer

TrendPilot AI is no longer only a documentation starter kit. It includes a small local execution layer that can:

- validate a source-log CSV
- calculate product opportunity scores
- generate a Markdown daily trend report
- run unit tests against scoring and report logic
- provide optional integration examples for Firecrawl and Google Sheets

The execution layer is intentionally lightweight. It does not scrape private data, send messages, auto-publish reports, or promise sales or profit.

---

## Install

```bash
python -m pip install -e .
```

## Validate CSV records

```bash
python -m trendpilot validate --input examples/sample-source-log.csv
```

## Generate a Markdown report

```bash
python -m trendpilot report \
  --input examples/sample-source-log.csv \
  --output examples/generated-daily-report.md \
  --limit 5
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

## Run tests

```bash
python -m unittest discover -s tests
```

or:

```bash
make test
```

## Optional n8n local runtime

A basic `docker-compose.yml` is included for users who want to experiment with n8n locally.

```bash
cp .env.example .env
# edit .env first
mkdir -p data outputs
docker compose up -d
```

The included `.pseudo.json` workflow files are planning references, not import-ready n8n exports.

## Optional integration examples

See:

- [Firecrawl fetch example](../integrations/examples/firecrawl_fetch.py)
- [Google Sheets append example](../integrations/examples/google_sheets_append.py)
- [Integration code examples README](../integrations/examples/README.md)

These examples require your own credentials. Never commit real API keys or service account files.

---

## Developer Workflow

Install the package locally:

```bash
make install
```

Install development tools for linting and schema validation:

```bash
make dev
```

Run the full local check:

```bash
make ci
```

The `score` shortcut now reads from a JSON input file instead of using a very long command:

```bash
make score
```

Input file:

```text
examples/sample-product-score-input.json
```

Output file:

```text
examples/generated-product-score.json
```

---

## CI Coverage

The GitHub Actions workflow in `.github/workflows/ci.yml` runs:

- editable package install
- Ruff lint check
- Python unit tests
- JSON Schema sample validation
- CLI smoke tests for `validate`, `report`, and `score`

---

## Legacy Install Compatibility

The project uses `pyproject.toml` as the primary package configuration and includes a minimal `setup.py` only to keep older setuptools/pip workflows from failing.
