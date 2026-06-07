# Contributing to TrendPilot AI

Thank you for considering a contribution to TrendPilot AI.

TrendPilot AI is a license-safe starter kit for AI-powered trend intelligence. It focuses on documentation, prompts, templates, pseudo workflows, schemas, examples, and lightweight local utilities.

## Project Scope

Contributions should support one or more of these goals:

- Improve trend intelligence workflows using public and legally accessible information.
- Improve prompts, templates, schemas, or examples.
- Clarify safe use, compliance boundaries, or human review steps.
- Improve lightweight local tools that do not require private data access.
- Improve documentation quality, examples, or onboarding.

## What Not to Add

Please do not add:

- Private data collection workflows.
- Spam automation or fake engagement workflows.
- Guaranteed-profit, auto-money, or investment return claims.
- Third-party source code copied without a compatible license.
- Real API keys, tokens, cookies, session data, or credentials.
- Workflows that bypass paywalls, logins, robots rules, or platform restrictions.
- Automated outreach, mass messaging, or unsolicited lead scraping.

## Standard Record Fields

When adding prompts, templates, schemas, workflows, or examples, keep these fields aligned:

```text
risk_note
risk_level
confidence
opportunity_score
review_status
```

Use these standard values:

```text
Risk Level: Low / Medium / High / Avoid / Unknown
Confidence: Low / Medium / High
Review Status: Draft / Needs Review / Approved / Rejected / Watchlist
```

`risk_note` should explain the issue in human-readable language.  
`risk_level` should only contain the standardized label.

## Documentation Style

Use clear, practical language. Avoid hype. Avoid claims that the project can automatically generate profit.

Good contributions should answer:

- What problem does this solve?
- What data does it use?
- What are the limitations?
- What should a human reviewer check?
- What risk or uncertainty remains?

## Prompt and Template Contributions

For new prompts or templates, include:

- Purpose
- Input requirements
- Output format
- Risk note
- Risk level
- Confidence level
- Suggested next action
- Human review reminder

## Workflow Contributions

Workflow files in this project are pseudo workflows unless clearly marked otherwise. When contributing workflows:

- Keep them license-safe.
- Do not include real credentials.
- Do not assume private platform access.
- Clearly separate collection, analysis, review, and output steps.
- Include source logging and human review checkpoints.

## Python Example Contributions

Python examples should remain lightweight and easy to inspect.

Preferred rules:

- Use the Python standard library when possible.
- Avoid external API calls by default.
- Avoid network scraping by default.
- Provide `--help` usage.
- Keep generated output local.
- Do not include credentials or private datasets.

Before submitting Python changes, run:

```bash
python -m py_compile examples/python/*.py
python examples/python/daily_report_generator.py --help
python examples/python/score_product_idea.py --help
```

## Pull Request Checklist

Before opening a pull request, check:

- [ ] No credentials, tokens, cookies, or private data are included.
- [ ] No copied third-party code without attribution and compatible license.
- [ ] Standard risk, confidence, and review fields are aligned.
- [ ] Markdown links are valid.
- [ ] CSV examples can be opened normally.
- [ ] JSON and schema files parse correctly.
- [ ] Python examples pass syntax checks, if changed.
- [ ] The contribution does not promise automatic profit or guaranteed results.

## Reporting Security Issues

Please do not open a public issue for security-sensitive reports. Follow the instructions in `SECURITY.md`.
