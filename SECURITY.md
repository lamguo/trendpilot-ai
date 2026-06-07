# Security Policy

TrendPilot AI is a documentation, prompt, template, and workflow starter kit for building AI-assisted trend intelligence systems.

This project is **not** a hosted SaaS product, does not include production scraping infrastructure, and should not be used to collect private, restricted, or unauthorized data.

---

## Supported Scope

Security review applies to the current public repository contents, including:

- Documentation
- Prompt templates
- Report templates
- Source log templates
- Pseudo workflow examples
- Integration guides
- Future example scripts or schemas added to this repository

Only the latest version on the default branch is actively maintained.

---

## Reporting a Security Issue

If you find a security issue, please report it responsibly.

Examples of issues worth reporting:

- Exposed API keys, tokens, credentials, or private data
- Unsafe instructions that encourage unauthorized scraping or spam
- Workflow examples that could lead to credential leakage
- Example code that stores secrets insecurely
- License, attribution, or third-party source reuse concerns
- Prompts or templates that may encourage illegal, deceptive, or abusive automation

Please avoid posting exploitable security details in a public issue.

Preferred reporting options:

1. Use GitHub's private vulnerability reporting feature if it is enabled for this repository.
2. If private reporting is not available, open a minimal public issue that says a security concern exists, without including sensitive details.

---

## Data Safety Principles

TrendPilot AI should only be used with public, legally accessible, and policy-compliant data sources.

Do not use this project to:

- Collect private user data
- Bypass paywalls, login walls, robots.txt restrictions, or platform access controls
- Scrape personal data from private communities
- Generate spam, fake engagement, fake reviews, or deceptive outreach
- Make automated financial, medical, legal, or high-risk decisions without human review
- Promise guaranteed profit or automatic income

---

## Secrets and Credentials

Do not commit:

- API keys
- Access tokens
- Private keys
- Session cookies
- Service account files
- `.env` files
- Personal data exports

Use environment variables or a secret manager when adapting this project into a real system.

Recommended local-only files:

```text
.env
.env.local
.env.*.local
secrets.json
service-account.json
credentials.json
```

---

## Human Review Requirement

AI-generated trend intelligence must be reviewed by a human before use.

Every important record should preserve:

```text
source_url
evidence_summary
risk_note
risk_level
confidence
opportunity_score
review_status
```

Standard review fields:

```text
risk_level: Low / Medium / High / Avoid / Unknown
confidence: Low / Medium / High
review_status: Draft / Needs Review / Approved / Rejected / Watchlist
```

---

## Integration Safety

External tools such as n8n, Firecrawl, Dify, Browser Use, Google Sheets, Telegram, Notion, or email services should be treated as optional integrations.

Before using any third-party tool:

- Review its terms of service
- Confirm data access permissions
- Avoid sending private or sensitive data to AI tools without consent
- Store credentials securely
- Keep logs for human review
- Add rate limits and abuse-prevention controls

---

## No Warranty

This repository is provided as a starter kit and educational reference.

Users are responsible for reviewing, adapting, and validating all workflows, prompts, templates, and integrations before real-world use.
