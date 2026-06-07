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

Planned workflow files:

```text
workflows/
├── README.md
├── n8n-daily-trend-intelligence.pseudo.json
├── n8n-reddit-trend-monitor.pseudo.json
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

Collect public trend signals, summarize them with AI, score product opportunities, and generate a daily report.

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
Human Review Status
    ↓
Save to Google Sheets
    ↓
Generate Daily Digest
```

---

## Workflow 2: Reddit / Community Trend Monitor

File:

```text
n8n-reddit-trend-monitor.pseudo.json
```

Purpose:

Monitor public community discussions for product problems, repeated complaints, buyer language, and product opportunity signals.

High-level flow:

```text
Schedule Trigger
    ↓
Load Public Community Topics
    ↓
Collect Public Discussion Signals
    ↓
Extract Pain Points
    ↓
Analyze Repeated Questions
    ↓
Generate Product Opportunity Notes
    ↓
Save to Source Log
```

Important:

This workflow should only use public community pages and should not collect private user data.

---

## Workflow 3: Google Sheets Output

File:

```text
n8n-google-sheets-output.pseudo.json
```

Purpose:

Save collected trend signals, product scores, risk notes, and review status into a structured Google Sheets table.

High-level flow:

```text
Receive Trend Signal
    ↓
Format Record
    ↓
Validate Required Fields
    ↓
Add Risk Note
    ↓
Add Review Status
    ↓
Append Row to Google Sheets
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
Select Top Opportunities
    ↓
Format Telegram Digest
    ↓
Add Disclaimer
    ↓
Send to Telegram
```

Important:

This workflow should not be used for spam, mass unsolicited messaging, or misleading income claims.

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
9. Add confidence levels and risk notes.
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
| region | Target market |
| category | Product category |
| keyword | Main keyword |
| product_name | Product or category idea |
| trend_signal | Short trend signal |
| evidence_summary | Source-based evidence summary |
| target_audience | Likely buyer group |
| pain_point | Consumer problem |
| content_angle | Suggested content angle |
| competition_signal | Low, medium, or high |
| risk_note | Main risk |
| confidence | Low, medium, or high |
| opportunity_score | Internal score |
| next_action | Suggested next step |
| review_status | Draft, Needs Review, Approved, Rejected, or Watchlist |

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
