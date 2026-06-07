# TrendPilot AI

**AI-powered toolkit for global trend intelligence, product research, and e-commerce opportunity reports.**

TrendPilot AI is a license-safe starter kit for builders, marketers, researchers, and e-commerce operators who want to design AI-powered trend intelligence workflows using public data sources, prompt templates, report templates, scoring models, pseudo-workflows, and integration guides.

It does **not** copy or redistribute third-party project code.

Instead, it organizes original documentation, prompts, templates, workflows, schemas, and safe integration guidance to help users build responsible AI-powered trend research systems.

---

## What This Project Is

TrendPilot AI helps users design workflows that can:

- Monitor public trend signals
- Analyze e-commerce product opportunities
- Summarize marketplace, social, community, review, and news signals
- Score product ideas with a transparent framework
- Generate daily or weekly trend reports
- Create Telegram or email digests
- Store research records in Google Sheets
- Add human review before publishing or monetizing reports

---

## What This Project Is Not

TrendPilot AI is not:

- An auto-money system
- A guaranteed profit system
- A scraping farm
- A spam automation tool
- A fake engagement tool
- A fake review generator
- A private data scraper
- A platform bypass toolkit
- A trading bot
- A financial prediction system
- A replacement for legal, compliance, or business due diligence

This project is for research, education, workflow planning, and responsible market intelligence.

---

## Core Workflow

```text
Public Trend Sources
        ↓
Data Collection Layer
        ↓
AI Trend Analysis
        ↓
Product Opportunity Scoring
        ↓
Risk Check
        ↓
Human Review
        ↓
Source Log / Google Sheets
        ↓
Report Templates
        ↓
Telegram / Email / Notion / PDF
```

---

## Repository Structure

```text
trendpilot-ai/
├── README.md
├── LICENSE
├── ATTRIBUTION.md
├── DISCLAIMER.md
├── docs/
│   ├── architecture.md
│   ├── data-sources.md
│   ├── tool-map.md
│   ├── workflow-design.md
│   ├── compliance.md
│   ├── license-risk-matrix.md
│   └── monetization.md
├── prompts/
│   ├── trend-analysis-prompt.md
│   ├── product-scoring-prompt.md
│   ├── competitor-summary-prompt.md
│   ├── review-pain-point-prompt.md
│   ├── content-angle-prompt.md
│   └── risk-check-prompt.md
├── templates/
│   ├── daily-trend-report.md
│   ├── product-opportunity-scorecard.md
│   ├── ecommerce-market-report.md
│   ├── weekly-market-brief.md
│   ├── competitor-snapshot.md
│   ├── source-log-template.csv
│   └── telegram-digest-template.md
├── workflows/
│   ├── README.md
│   ├── n8n-daily-trend-intelligence.pseudo.json
│   ├── n8n-community-trend-monitor.pseudo.json
│   ├── n8n-google-sheets-output.pseudo.json
│   └── n8n-telegram-digest.pseudo.json
└── integrations/
    ├── n8n.md
    ├── firecrawl.md
    ├── dify.md
    ├── browser-use.md
    └── google-sheets.md
```

---

## Quick Start

### 1. Understand the system

Start here:

- [System Architecture](docs/architecture.md)
- [Workflow Design](docs/workflow-design.md)
- [Data Sources](docs/data-sources.md)

### 2. Choose a research workflow

Use one of the pseudo-workflows:

- [Daily Trend Intelligence Workflow](workflows/n8n-daily-trend-intelligence.pseudo.json)
- [Community Trend Monitor Workflow](workflows/n8n-community-trend-monitor.pseudo.json)
- [Google Sheets Output Workflow](workflows/n8n-google-sheets-output.pseudo.json)
- [Telegram Digest Workflow](workflows/n8n-telegram-digest.pseudo.json)

These files are pseudo-workflows. They are not real n8n export files and should not be imported directly into n8n.

### 3. Use the prompts

Core prompts:

- [Trend Analysis Prompt](prompts/trend-analysis-prompt.md)
- [Product Scoring Prompt](prompts/product-scoring-prompt.md)
- [Competitor Summary Prompt](prompts/competitor-summary-prompt.md)
- [Review Pain Point Prompt](prompts/review-pain-point-prompt.md)
- [Content Angle Prompt](prompts/content-angle-prompt.md)
- [Risk Check Prompt](prompts/risk-check-prompt.md)

### 4. Save structured records

Use:

- [Source Log CSV Template](templates/source-log-template.csv)
- [Google Sheets Integration Guide](integrations/google-sheets.md)

### 5. Generate reports

Use:

- [Daily Trend Report Template](templates/daily-trend-report.md)
- [Weekly Market Brief Template](templates/weekly-market-brief.md)
- [E-commerce Market Report Template](templates/ecommerce-market-report.md)
- [Product Opportunity Scorecard](templates/product-opportunity-scorecard.md)
- [Competitor Snapshot Template](templates/competitor-snapshot.md)
- [Telegram Digest Template](templates/telegram-digest-template.md)

---

## Standard Record Fields

TrendPilot AI uses one consistent record structure across templates, workflows, and integrations.

```text
record_id
source_type
source_name
source_url
collection_date
publication_date
region
category
keyword
product_name
trend_signal
evidence_summary
target_audience
pain_point
content_angle
price_signal
competition_signal
risk_note
risk_level
confidence
opportunity_score
next_action
review_status
reviewer_note
```

Important:

```text
risk_note = human-readable explanation of the risk
risk_level = standardized risk category
```

Recommended risk level values:

```text
Low
Medium
High
Avoid
Unknown
```

Recommended confidence values:

```text
Low
Medium
High
```

Recommended review status values:

```text
Draft
Needs Review
Approved
Rejected
Watchlist
```

---

## Product Opportunity Scoring Model

TrendPilot AI uses a simple 1-5 scoring model.

Positive factors:

```text
Demand Signal
Social Visibility
Price Potential
Supplier Availability
Differentiation Potential
```

Negative factors:

```text
Competition Level
Shipping Difficulty
Compliance Risk
```

Formula:

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

Score interpretation:

| Final Score | Interpretation |
|---:|---|
| 12 or higher | Strong candidate for deeper research |
| 8 to 11 | Test carefully |
| 4 to 7 | Watchlist |
| Below 4 | Avoid unless stronger evidence appears |

Important:

```text
A high score does not guarantee sales, profit, or product success.
```

---

## Documentation

Core documentation:

- [System Architecture](docs/architecture.md)
- [Data Sources](docs/data-sources.md)
- [Tool Map](docs/tool-map.md)
- [Workflow Design](docs/workflow-design.md)
- [Compliance Guide](docs/compliance.md)
- [License Risk Matrix](docs/license-risk-matrix.md)
- [Monetization Guide](docs/monetization.md)

---

## Prompts

Prompt library:

- [Trend Analysis Prompt](prompts/trend-analysis-prompt.md)
- [Product Scoring Prompt](prompts/product-scoring-prompt.md)
- [Competitor Summary Prompt](prompts/competitor-summary-prompt.md)
- [Review Pain Point Prompt](prompts/review-pain-point-prompt.md)
- [Content Angle Prompt](prompts/content-angle-prompt.md)
- [Risk Check Prompt](prompts/risk-check-prompt.md)

---

## Templates

Report and research templates:

- [Daily Trend Report Template](templates/daily-trend-report.md)
- [Weekly Market Brief Template](templates/weekly-market-brief.md)
- [E-commerce Market Report Template](templates/ecommerce-market-report.md)
- [Product Opportunity Scorecard](templates/product-opportunity-scorecard.md)
- [Competitor Snapshot Template](templates/competitor-snapshot.md)
- [Telegram Digest Template](templates/telegram-digest-template.md)
- [Source Log CSV Template](templates/source-log-template.csv)

---

## Workflows

Pseudo-workflow blueprints:

- [Workflows Overview](workflows/README.md)
- [Daily Trend Intelligence](workflows/n8n-daily-trend-intelligence.pseudo.json)
- [Community Trend Monitor](workflows/n8n-community-trend-monitor.pseudo.json)
- [Google Sheets Output](workflows/n8n-google-sheets-output.pseudo.json)
- [Telegram Digest](workflows/n8n-telegram-digest.pseudo.json)

Important:

```text
These workflow files are planning templates only.
They are not real n8n workflow exports.
They should not be imported directly into n8n.
```

---

## Integrations

External tool integration guides:

- [n8n Integration Guide](integrations/n8n.md)
- [Firecrawl Integration Guide](integrations/firecrawl.md)
- [Dify Integration Guide](integrations/dify.md)
- [Browser-use Integration Guide](integrations/browser-use.md)
- [Google Sheets Integration Guide](integrations/google-sheets.md)

TrendPilot AI does not include or redistribute third-party source code.

These tools are referenced as external tools only.

---

## Safe Use Principles

TrendPilot AI workflows should:

- Use public and legally accessible information only
- Keep source links
- Summarize instead of copying
- Add confidence levels
- Add risk notes
- Add standardized risk levels
- Use human review before publishing or monetizing reports
- Avoid guaranteed income or guaranteed sales claims
- Respect platform rules and third-party licenses

TrendPilot AI workflows should not:

- Scrape private personal data
- Build contact databases
- Send spam
- Generate fake reviews
- Generate fake engagement
- Farm accounts
- Bypass platform restrictions
- Copy competitor images or creator content
- Repackage third-party code as original work
- Claim guaranteed product demand or profit

---

## License-Safe Integration

TrendPilot AI references external tools such as n8n, Firecrawl, Dify, Browser-use, and Google Sheets.

This repository does not:

- Copy third-party source code
- Redistribute third-party workflow exports
- Remove third-party attribution
- Repackage external tools as TrendPilot AI
- Claim official partnership with referenced projects

For external project references, see:

- [Attribution](ATTRIBUTION.md)
- [License Risk Matrix](docs/license-risk-matrix.md)

---

## Human Review Checklist

Before publishing, selling, or sending any report, confirm:

- [ ] Sources are public
- [ ] Source links are included
- [ ] Claims are supported by evidence
- [ ] No private personal data is included
- [ ] No long copyrighted text is copied
- [ ] No platform restriction bypass is involved
- [ ] No fake engagement or spam is involved
- [ ] No product success is guaranteed
- [ ] Confidence levels are included
- [ ] Risk notes are included
- [ ] Risk levels are included
- [ ] Human reviewer has approved the output

---

## Monetization

TrendPilot AI may support ethical monetization models such as:

- Paid trend reports
- Paid newsletters
- Research templates
- Product opportunity scorecards
- Internal dashboards
- Consulting reports
- Educational content
- Workflow setup services

It should not be marketed as:

- Guaranteed income system
- Auto-money bot
- Passive profit machine
- Platform loophole
- Spam automation system
- Scraping farm

See:

- [Monetization Guide](docs/monetization.md)
- [Disclaimer](DISCLAIMER.md)

---

## Roadmap

Planned next additions:

```text
schemas/
├── trend-signal.schema.json
├── product-score.schema.json
└── report-record.schema.json
```

```text
examples/
├── sample-daily-report-en.md
├── sample-daily-report-cn.md
├── sample-product-score.csv
└── sample-source-log.csv
```

```text
examples/python/
├── daily_report_generator.py
└── score_product_idea.py
```

```text
.github/
├── FUNDING.yml
└── ISSUE_TEMPLATE/
```

Other planned files:

```text
SECURITY.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
```

---

## Disclaimer

TrendPilot AI is for research and educational purposes only.

It does not guarantee:

- Product demand
- Sales
- Profit
- Business success
- Viral content
- Marketplace ranking
- Advertising performance
- Subscriber growth
- Any financial outcome

Users should verify all sources, review platform rules, check compliance requirements, and conduct their own due diligence before making business decisions.

Read the full disclaimer:

- [DISCLAIMER.md](DISCLAIMER.md)

---

## License

This repository uses the MIT License for original TrendPilot AI content.

This does not change the licenses of third-party tools referenced in this repository.

Before using any external project, review that project's own license, documentation, and terms.
