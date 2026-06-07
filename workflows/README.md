# Workflows

This folder contains original pseudo-workflow designs for TrendPilot AI.

These workflows are not copied from third-party projects. They are high-level workflow blueprints that show how an AI-powered trend intelligence system can be structured using external tools such as n8n, Firecrawl, Dify, Google Sheets, Telegram, and email.

TrendPilot AI does not redistribute third-party workflow exports, source code, API keys, or platform-specific private configurations.

---

## Purpose

The workflows in this folder help users understand how to build ethical AI-powered trend intelligence pipelines.

They can be used for:

- Daily trend monitoring
- Public data collection planning
- AI-assisted product opportunity analysis
- Product scoring
- Risk level classification
- Report generation
- Telegram or email digest delivery
- Google Sheets research logging
- Human review workflows

---

## Important Notice

These files are pseudo-workflows.

They are not guaranteed to run directly inside n8n, Dify, Make, Zapier, or any other automation platform.

They are intended as:

- Architecture references
- Workflow planning documents
- Implementation blueprints
- Educational examples
- Safe automation design patterns

Before using any workflow in production, users must adapt it to their own tools, APIs, permissions, and compliance requirements.

---

## Workflow Files

Current workflow files:

```text
workflows/
├── README.md
├── n8n-daily-trend-intelligence.pseudo.json
├── n8n-community-trend-monitor.pseudo.json
├── n8n-google-sheets-output.pseudo.json
└── n8n-telegram-digest.pseudo.json
```

---

## Workflow 1: Daily Trend Intelligence

File:

```text
n8n-daily-trend-intelligence.pseudo.json
```

Purpose:

Collect public trend signals, summarize them with AI, score product opportunities, classify risk levels, and generate a daily report.

High-level flow:

```text
Schedule Trigger
    ↓
Load Public Source List
    ↓
Collect Public Trend Signals
    ↓
Clean and Normalize Data
    ↓
AI Trend Analysis
    ↓
Product Opportunity Scoring
    ↓
Risk Check
    ↓
Human Review Status
    ↓
Save to Google Sheets
    ↓
Generate Daily Digest
```

---

## Workflow 2: Public Community Trend Monitor

File:

```text
n8n-community-trend-monitor.pseudo.json
```

Purpose:

Monitor public community discussions for product problems, repeated complaints, buyer language, and product opportunity signals.

This workflow can be used for public sources such as:

- Public Reddit discussions
- Public Quora questions
- Public forums
- Public hobby communities
- Public product discussion pages
- Public community threads

High-level flow:

```text
Schedule Trigger
    ↓
Load Public Community Topics
    ↓
Source Safety Filter
    ↓
Collect Public Discussion Signals
    ↓
Extract Pain Points
    ↓
Analyze Repeated Questions
    ↓
Generate Product Opportunity Notes
    ↓
Risk Check
    ↓
Save to Source Log
```

Important:

This workflow should only use public community pages and should not collect private user data.

It should not be used for spam, automated comments, private message scraping, or personal contact collection.

---

## Workflow 3: Google Sheets Output

File:

```text
n8n-google-sheets-output.pseudo.json
```

Purpose:

Save collected trend signals, product scores, risk notes, risk levels, confidence levels, and review status into a structured Google Sheets table.

High-level flow:

```text
Receive Trend Signal
    ↓
Validate Required Fields
    ↓
Private Data Filter
    ↓
Normalize Record Fields
    ↓
Generate Record ID
    ↓
Map to Source Log Columns
    ↓
Duplicate Check
    ↓
Append Row to Google Sheets
    ↓
Add Review Status Logic
```

Related template:

```text
templates/source-log-template.csv
```

---

## Workflow 4: Telegram Digest

File:

```text
n8n-telegram-digest.pseudo.json
```

Purpose:

Generate short daily or weekly trend intelligence summaries and send them to an opt-in Telegram channel or internal team.

High-level flow:

```text
Load Approved Trend Records
    ↓
Filter by Review Status, Confidence, and Risk Level
    ↓
Select Top Opportunities
    ↓
Format Telegram Digest
    ↓
Add Risk Notes and Disclaimer
    ↓
Human Approval
    ↓
Send to Telegram
```

Important:

This workflow should not be used for spam, mass unsolicited messaging, or misleading income claims.

---

## Standard TrendPilot AI Record Fields

TrendPilot AI workflows should use one consistent record structure.

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

## Safe Workflow Design Rules

All TrendPilot AI workflows should follow these rules:

1. Use public and legally accessible sources only.
2. Do not collect private personal data.
3. Do not bypass login walls, paywalls, anti-bot systems, or platform restrictions.
4. Do not automate spam, fake engagement, fake reviews, or account farming.
5. Do not copy third-party content into reports.
6. Do not copy competitor images, creator videos, or protected designs.
7. Do not generate guaranteed income or guaranteed sales claims.
8. Add source links wherever possible.
9. Add confidence levels, risk notes, and risk levels.
10. Use human review before publishing or monetizing reports.

---

## Recommended Workflow Status Labels

Use these labels to control workflow output quality:

| Status | Meaning |
|---|---|
| Draft | AI-generated and not reviewed |
| Needs Review | Requires human review |
| Approved | Ready to use or publish |
| Rejected | Unsafe, low-quality, unsupported, or irrelevant |
| Watchlist | Interesting but not ready for action |

---

## Recommended Data Flow

A clean TrendPilot AI workflow should follow this structure:

```text
Source
    ↓
Collection
    ↓
Cleaning
    ↓
AI Analysis
    ↓
Scoring
    ↓
Risk Check
    ↓
Human Review
    ↓
Storage
    ↓
Report Delivery
```

---

## Recommended Output Fields

Each workflow should try to produce structured records with these fields:

| Field | Description |
|---|---|
| record_id | Unique record ID |
| source_type | Search, marketplace, social, community, review, report, or news |
| source_name | Platform, publisher, or website |
| source_url | Public source URL |
| collection_date | Date collected |
| publication_date | Date published, if available |
| region | Target market |
| category | Product category |
| keyword | Main keyword |
| product_name | Product or category idea |
| trend_signal | Short trend signal |
| evidence_summary | Source-based evidence summary |
| target_audience | Likely buyer group |
| pain_point | Consumer problem |
| content_angle | Suggested content angle |
| price_signal | Visible public price signal |
| competition_signal | Low, medium, or high |
| risk_note | Human-readable risk explanation |
| risk_level | Low, Medium, High, Avoid, or Unknown |
| confidence | Low, Medium, or High |
| opportunity_score | Internal score |
| next_action | Suggested next step |
| review_status | Draft, Needs Review, Approved, Rejected, or Watchlist |
| reviewer_note | Human reviewer note |

---

## Risk Level Rules

Suggested rules:

| Risk Level | Suggested Handling |
|---|---|
| Low | Can move forward after review |
| Medium | Needs careful review before use |
| High | Do not use as a top opportunity without deeper review |
| Avoid | Exclude or reject |
| Unknown | Mark as Needs Review |

For public or paid reports, recommended filter:

```text
review_status = Approved
confidence = Medium or High
risk_level = Low or Medium
```

Avoid using these in public or paid reports:

```text
review_status = Draft
review_status = Needs Review
review_status = Rejected
risk_level = High
risk_level = Avoid
risk_level = Unknown
```

---

## Human Review Checklist

Before any workflow output is published, sold, or sent to subscribers, confirm:

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

## What These Workflows Should Not Become

These workflows should not become:

- Private data scrapers
- Contact database builders
- Spam automation systems
- Fake review generators
- Fake engagement bots
- Account farming tools
- Platform bypass tools
- Copyright copying systems
- Auto-money bots
- Guaranteed income systems

---

## Final Note

The value of TrendPilot AI workflows is not in automation alone.

The value is in:

- Clean public data
- Ethical collection
- Clear structure
- Useful analysis
- Transparent scoring
- Risk awareness
- Human review
- Practical reports

TrendPilot AI should remain a safe, useful, and license-aware workflow starter kit.

---

## Important: Pseudo-workflow Scope

Files ending in `.pseudo.json` are planning references only.

They are not import-ready n8n exports and should not be presented as working automation files. For runnable local examples, use:

- `python -m trendpilot validate`
- `python -m trendpilot report`
- `python -m trendpilot score`
- `docker-compose.yml` for a local n8n runtime shell

The pseudo-workflows remain in the repository to explain workflow logic without copying third-party workflow exports or implying platform-ready automation.


## Source of Truth for Fields

The `.pseudo.json` files intentionally avoid repeating the full standard field list in every workflow.

Use these files as the canonical references instead:

- `trendpilot/fields.py` for Python constants
- `schemas/trend-signal.schema.json` for trend signal JSON records
- `schemas/product-score.schema.json` for product score JSON records
- `templates/source-log-template.csv` for CSV source log columns

This reduces maintenance risk when field names or allowed enum values change.
