# n8n Integration Guide

This guide explains how n8n can be used as the workflow automation layer for TrendPilot AI.

TrendPilot AI does not include, copy, redistribute, or modify n8n source code.  
n8n is referenced as an external workflow automation tool.

Official repository:

https://github.com/n8n-io/n8n

Official website:

https://n8n.io

---

## Role in TrendPilot AI

n8n can be used to connect different parts of an AI-powered trend intelligence system.

In a TrendPilot AI workflow, n8n may help with:

- Running scheduled research tasks
- Loading public source lists
- Calling public APIs
- Connecting web extraction tools
- Sending collected data to AI analysis
- Saving structured records to Google Sheets or Notion
- Generating daily or weekly reports
- Sending Telegram or email digests
- Adding human review steps
- Archiving reports

n8n should be treated as an external automation layer, not as bundled TrendPilot AI code.

---

## Recommended Position in the Architecture

```text
Public Trend Sources
        ↓
Data Collection Layer
        ↓
n8n Workflow Automation
        ↓
AI Analysis Layer
        ↓
Product Opportunity Scoring
        ↓
Risk Check
        ↓
Human Review
        ↓
Google Sheets / Notion / Database
        ↓
Telegram / Email / Report Delivery
```

---

## Best Use Cases

n8n is useful for:

- Daily trend monitoring
- Weekly market report automation
- Public data collection scheduling
- Google Sheets source log updates
- Telegram digest delivery
- Email report delivery
- Multi-step AI workflows
- Human approval workflows
- Source validation pipelines
- Report archive automation

---

## Not Recommended For

n8n should not be used in TrendPilot AI for:

- Scraping private personal data
- Sending spam messages
- Creating fake engagement
- Generating fake reviews
- Account farming
- Bypassing platform restrictions
- Automating unsolicited direct messages
- Collecting private emails or phone numbers
- Circumventing paywalls or login restrictions
- Running unsafe marketplace automation

---

## Suggested MVP Workflow With n8n

A simple MVP workflow can look like this:

```text
Schedule Trigger
    ↓
Load Public Source List
    ↓
Collect Public Trend Signals
    ↓
Clean and Normalize Records
    ↓
AI Trend Analysis
    ↓
Product Opportunity Scoring
    ↓
Risk Check
    ↓
Save to Google Sheets
    ↓
Generate Daily Digest
    ↓
Human Review
    ↓
Send Telegram / Email
```

Related pseudo workflow:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
```

---

## Suggested n8n Node Types

Depending on the final implementation, users may use node types such as:

| Purpose | Possible Node Type |
|---|---|
| Schedule workflow | Schedule Trigger |
| Receive data | Webhook |
| Fetch public data | HTTP Request |
| Transform data | Code / Function |
| Validate fields | IF / Switch |
| AI analysis | HTTP Request to AI API |
| Save records | Google Sheets |
| Store reports | Notion / Google Drive |
| Send digest | Telegram / Email |
| Manual approval | Wait / Manual workflow pattern |
| Error handling | Error Trigger |

Actual node names and availability may vary depending on the n8n version and installed integrations.

---

## Suggested Workflow Inputs

A TrendPilot AI n8n workflow may start with a public source list.

Example source list fields:

```text
source_id
source_type
source_name
source_url
region
category
keyword
risk_level
collection_frequency
notes
```

Example source types:

```text
Search
Marketplace
Social
Community
Review
News / Report
Manual
```

---

## Suggested Workflow Outputs

A TrendPilot AI n8n workflow should produce structured records.

Recommended output fields:

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

Related template:

```text
templates/source-log-template.csv
```

---

## Review Status Logic

TrendPilot AI should not automatically treat AI output as final.

Recommended review statuses:

| Status | Meaning |
|---|---|
| Draft | AI-generated and not reviewed |
| Needs Review | Requires human inspection |
| Approved | Ready to use or publish |
| Rejected | Unsafe, unsupported, or low quality |
| Watchlist | Interesting but not ready for action |

Suggested default:

```text
AI-generated records should start as Draft or Needs Review.
```

---

## Suggested n8n Workflow Stages

### 1. Schedule Trigger

Purpose:

Start the workflow on a fixed schedule.

Suggested schedule:

```text
Daily or weekly
```

Important notes:

- Avoid running too frequently.
- Respect source rate limits.
- Do not overload websites.
- Do not use automation to bypass platform restrictions.

---

### 2. Load Source List

Purpose:

Load a curated list of public trend sources.

Possible storage:

- Google Sheets
- Notion
- Airtable
- Static JSON file
- Manual source list

Important rules:

- Use public sources only.
- Do not include private groups.
- Do not include login-protected content.
- Do not include contact databases.
- Do not include scraped personal information.

---

### 3. Source Safety Filter

Purpose:

Check whether each source is safe to collect.

Suggested checks:

```text
Is the source public?
Does it require login?
Does it contain private personal data?
Does it require bypassing restrictions?
Can the information be summarized instead of copied?
Is the source relevant to product research?
```

If uncertain:

```text
Mark as Needs Review.
```

---

### 4. Public Data Collection

Purpose:

Collect visible public signals.

Possible methods:

- Public APIs
- RSS feeds
- Public pages
- Manual source extraction
- Web extraction tools
- Search APIs

Important rules:

- Do not collect private user data.
- Do not copy full copyrighted pages.
- Do not bypass anti-bot systems.
- Do not use login-based scraping.
- Keep source URLs for traceability.

---

### 5. Clean and Normalize Data

Purpose:

Convert raw collected notes into a consistent structure.

Recommended steps:

- Remove irrelevant navigation text
- Remove duplicate records
- Normalize category names
- Normalize region names
- Summarize evidence in original words
- Keep source URL
- Add collection date
- Add risk note
- Add confidence level

---

### 6. AI Trend Analysis

Purpose:

Use AI to extract product trend insights.

Related prompt:

```text
prompts/trend-analysis-prompt.md
```

AI should extract:

- Product or category idea
- Trend reason
- Target audience
- Consumer pain point
- Buyer motivation
- Emotional trigger
- Suggested keywords
- Content angle
- Marketplace research angle
- Evidence summary
- Risk or uncertainty
- Confidence level
- Next action

Important rules:

- Do not invent facts.
- Use only provided source material.
- Do not claim guaranteed demand.
- Do not include private personal data.
- Do not copy long source text.

---

### 7. Product Opportunity Scoring

Purpose:

Score product ideas using the TrendPilot AI 1-5 scoring model.

Related prompt:

```text
prompts/product-scoring-prompt.md
```

Scoring dimensions:

```text
Demand Signal
Social Visibility
Price Potential
Supplier Availability
Differentiation Potential
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

Important:

```text
A high score does not guarantee sales.
```

---

### 8. Risk Check

Purpose:

Review product and content risk before saving or sending reports.

Related prompt:

```text
prompts/risk-check-prompt.md
```

Risk areas:

- Product safety
- Compliance
- Platform policy
- Health or wellness claims
- Baby or child safety
- Electronics or batteries
- Food, supplements, or ingredients
- Trademark, copyright, or design risk
- Shipping and fulfillment
- Privacy or personal data
- Spam or platform abuse
- Unsupported claims
- Misleading income claims

High-risk records should be marked:

```text
Needs Review
```

or:

```text
Rejected
```

---

### 9. Save to Google Sheets

Purpose:

Save structured trend records for review.

Related pseudo workflow:

```text
workflows/n8n-google-sheets-output.pseudo.json
```

Related template:

```text
templates/source-log-template.csv
```

Important rules:

- Do not store private data.
- Do not store API keys.
- Do not make private sheets public accidentally.
- Use review status fields.
- Keep source URLs.

---

### 10. Generate Report Draft

Purpose:

Create a daily or weekly report draft.

Related templates:

```text
templates/daily-trend-report.md
templates/weekly-market-brief.md
templates/ecommerce-market-report.md
```

Reports should include:

- Source links
- Evidence summary
- Confidence level
- Risk notes
- Suggested next actions
- Disclaimer

Reports should not include:

- Guaranteed income claims
- Unsupported statistics
- Private personal data
- Copied full source text
- Fake reviews
- Fake testimonials

---

### 11. Human Review

Purpose:

Require human approval before publishing or monetizing outputs.

Human reviewer should check:

- Source quality
- Source recency
- Evidence strength
- Copyright risk
- Privacy risk
- Compliance risk
- Product safety risk
- Overstated claims
- Missing uncertainty notes
- Missing disclaimers

---

### 12. Send Telegram or Email Digest

Purpose:

Send approved summaries to opt-in users or internal teams.

Related pseudo workflow:

```text
workflows/n8n-telegram-digest.pseudo.json
```

Related template:

```text
templates/telegram-digest-template.md
```

Important rules:

- Send only to opt-in users.
- Do not send spam.
- Do not use scraped contact lists.
- Include disclaimer.
- Do not claim guaranteed sales or profit.

---

## Environment Variables and Secrets

Do not commit secrets to GitHub.

Possible secret values:

```text
AI_API_KEY
FIRECRAWL_API_KEY
GOOGLE_SHEETS_CREDENTIALS
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
EMAIL_SMTP_PASSWORD
NOTION_API_KEY
```

Safe practice:

- Store secrets in n8n credentials.
- Use environment variables.
- Do not paste keys into public workflow files.
- Do not store keys in Google Sheets.
- Rotate keys if leaked.

---

## Error Handling Suggestions

A production workflow should handle errors such as:

- Source unavailable
- API rate limit
- Empty response
- Invalid source URL
- AI timeout
- Missing required fields
- Duplicate records
- High-risk data detected
- Google Sheets write failure
- Telegram delivery failure

Suggested error handling:

```text
Log the error
Mark record as Needs Review
Do not publish incomplete data
Notify operator
Retry only when safe
```

---

## Human Review Checklist

Before sending any report or digest, confirm:

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
- [ ] Disclaimer is included
- [ ] Human reviewer has approved the output

---

## Common Mistakes to Avoid

Avoid:

- Treating AI output as final truth
- Collecting too many low-quality sources
- Scraping private or restricted pages
- Sending unreviewed reports to paid subscribers
- Forgetting source links
- Removing disclaimers
- Overstating demand
- Hiding risk notes
- Storing API keys in public files
- Using automation for spam

---

## Related TrendPilot AI Files

Architecture:

```text
docs/architecture.md
```

Data sources:

```text
docs/data-sources.md
```

Workflow design:

```text
docs/workflow-design.md
```

Compliance:

```text
docs/compliance.md
```

License risk:

```text
docs/license-risk-matrix.md
```

Pseudo workflows:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
workflows/n8n-community-trend-monitor.pseudo.json
workflows/n8n-google-sheets-output.pseudo.json
workflows/n8n-telegram-digest.pseudo.json
```

Templates:

```text
templates/daily-trend-report.md
templates/source-log-template.csv
templates/telegram-digest-template.md
```

Prompts:

```text
prompts/trend-analysis-prompt.md
prompts/product-scoring-prompt.md
prompts/risk-check-prompt.md
```

---

## Final Note

n8n can be a powerful automation layer for TrendPilot AI, but automation should not replace judgment.

A safe TrendPilot AI workflow should combine:

```text
Public sources
+ Ethical collection
+ AI analysis
+ Risk checking
+ Human review
+ Clear reporting
```

It should not become:

```text
Spam automation
Private data scraping
Fake engagement
Platform bypass
Auto-money claims
```

Use n8n responsibly and review all outputs before publishing or monetizing them.
