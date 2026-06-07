# TrendPilot AI Execution Layer Upgrade Notes

This upgrade improves the executable layer and addresses issues found after the first execution-layer pass.

## What changed

- Added `.github/workflows/ci.yml` for automated CI.
- Added `requirements-dev.txt` and `make dev` for development tooling.
- Added `setup.py` as a small legacy compatibility entry point.
- Updated `pyproject.toml` with Beta classifier, package URLs, dev extras, and build metadata.
- Updated `Makefile` with `dev`, `lint`, `schema-check`, `ci`, and `build` targets.
- Replaced the long Makefile score command with JSON input:
  - `examples/sample-product-score-input.json`
- Added schema sample JSON files:
  - `examples/sample-trend-signal.json`
  - `examples/sample-product-score.json`
  - `examples/sample-report-record.json`
- Added `scripts/validate_schema_samples.py` for JSON Schema validation.
- Added tests for CLI JSON input and schema sample validation.
- Removed the default n8n password fallback from `docker-compose.yml`.
- Kept pseudo workflows as planning files, but replaced repeated top-level field arrays with schema references.
- Restored the detailed product scoring guide while keeping JSON-only output.
- Added a machine-readable output option to the trend analysis prompt.

## Local check

```bash
make dev
make ci
```

## Security note

Do not commit `.env`, API keys, service account JSON files, tokens, cookies, or real credentials.
