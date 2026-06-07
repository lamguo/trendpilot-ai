# Changelog

All notable changes to this project should be documented in this file.

This project follows a simple changelog format inspired by Keep a Changelog. Version numbers are intended to match the package version in `pyproject.toml` when releases are tagged.

## [Unreleased]

### Added

- N/A

### Changed

- N/A

### Fixed

- N/A

## [0.2.1] - 2026-06-07

### Added

- GitHub Actions CI workflow for linting, unit tests, schema sample validation, and CLI smoke tests.
- Schema validation script for sample records.
- CLI tests for JSON-input scoring.
- Sample JSON records for product scores, trend signals, and report records.
- JSON-input mode for `trendpilot score`.
- Setup compatibility through `setup.py` for older pip / setuptools workflows.
- Development dependency set for linting, schema validation, and package builds.

### Changed

- Improved Python packaging metadata for beta-stage package distribution.
- Simplified Makefile scoring command by moving sample input into `examples/sample-product-score-input.json`.
- Updated product scoring and trend analysis prompts to support schema-aligned JSON output while preserving scoring guidance.
- Clarified that pseudo-workflows are planning references, not importable n8n exports.
- Removed default hardcoded n8n password from `docker-compose.yml`; users must provide credentials through `.env`.

### Fixed

- Reduced repeated standard field definitions in pseudo-workflow files by referencing schemas and shared field constants.
- Improved local validation flow for CLI, schema samples, and generated example outputs.

## [0.2.0] - 2026-06-07

### Added

- Executable Python package under `trendpilot/`.
- Local CLI for CSV validation, Markdown report generation, and product idea scoring.
- Unit tests for scoring, record validation, report generation, and CLI behavior.
- Makefile shortcuts for installation, testing, validation, report generation, scoring, CI checks, and cleanup.
- Local n8n `docker-compose.yml` starter shell.
- `.env.example` for local n8n configuration.
- Integration example scripts for Firecrawl fetching and Google Sheets append workflows.
- Runtime, integration, and development requirements files.
- Execution-layer documentation.

### Changed

- Moved the project from a documentation-first starter kit toward a lightweight executable toolkit.
- Added README instructions for installing and running the local CLI.
- Added upgrade notes for the execution-layer transition.

## [0.1.0] - 2026-06-07

### Added

- Initial TrendPilot AI starter kit structure.
- Core documentation for architecture, data sources, tool mapping, workflow design, compliance, license risk, and monetization.
- Prompt library for trend analysis, product scoring, competitor summaries, review pain points, content angles, and risk checks.
- Report and scoring templates.
- Source log template with standardized review fields.
- Pseudo n8n workflow examples.
- Integration guides for n8n, Firecrawl, Dify, Browser Use, and Google Sheets.
- JSON schemas for trend signals, product scores, and report records.
- Example reports and sample CSV records.
- Lightweight Python examples for local report generation and product idea scoring.
- Security policy.
- Funding configuration.
- Contribution guide, code of conduct, GitHub issue templates, and pull request template.

### Project Standards

- Standard risk levels: Low / Medium / High / Avoid / Unknown.
- Standard confidence levels: Low / Medium / High.
- Standard review statuses: Draft / Needs Review / Approved / Rejected / Watchlist.
- Human review required before publishing, acting on, or automating outputs.
