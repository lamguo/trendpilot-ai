# Google Sheets Integration Guide

This guide explains how Google Sheets can be used as a lightweight storage, review, and reporting layer for TrendPilot AI.

TrendPilot AI does not require Google Sheets, but it is a practical option for early MVP workflows because it is easy to review, edit, filter, and share.

Google Sheets should be treated as a storage and review layer, not as a private data warehouse or spam contact database.

---

## Role in TrendPilot AI

Google Sheets can be used to store structured trend intelligence records.

In a TrendPilot AI workflow, Google Sheets may help with:

- Saving public trend signals
- Tracking source URLs
- Storing product opportunity scores
- Adding risk notes
- Managing human review status
- Creating watchlists
- Reviewing AI-generated product ideas
- Preparing daily or weekly reports
- Exporting CSV files
- Supporting simple dashboards

---

## Recommended Position in the Architecture

```text
Public Data Sources
        ↓
Data Collection Layer
        ↓
AI Trend Analysis
        ↓
Product Opportunity Scoring
        ↓
Risk Check
        ↓
Google Sheets Source Log
        ↓
Human Review
        ↓
Report Generation
        ↓
Telegram / Email / Notion / PDF
```

---

## Best Use Cases

Google Sheets is useful for:

- MVP trend intelligence workflows
- Source logging
- Product opportunity tracking
- Manual review
- Simple scoring dashboards
- Watchlists
- Daily reports
- Weekly reports
- Team review
- CSV export

---

## Not Recommended For

Google Sheets should not be used for:

- Storing private personal data
- Storing scraped emails or phone numbers
- Storing private social media profiles
- Storing API keys or secrets
- Storing payment data
- Storing ID documents
- Storing confidential customer data
- Building spam outreach lists
- Publishing unreviewed AI output as final truth

---

## Core Principle

Google Sheets should be used for:

```text
Structured public research records
```

Not for:

```text
Private data storage, contact scraping, or spam workflows
```

---

## Suggested Spreadsheet Structure

A simple TrendPilot AI Google Sheets file can include these tabs:

```text
source_log
daily_summary
watchlist
rejected_records
settings
```

---

## Tab 1: source_log

Purpose:

Store structured trend signal records.

Recommended columns:

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

## Tab 2: daily_summary

Purpose:

Summarize daily trend records.

Recommended columns:

```text
summary_date
region
category
total_records
approved_records
draft_records
needs_review_records
watchlist_records
rejected_records
top_product_idea
top_opportunity_score
highest_risk_item
main_category_signal
reviewer_note
```

Example use:

```text
Every day, summarize how many records were collected, which product ideas scored highest, and which records need review.
```

---

## Tab 3: watchlist

Purpose:

Track product ideas, categories, or keywords that are interesting but not ready for action.

Recommended columns:

```text
watchlist_id
date_added
region
category
keyword
product_idea
reason_to_watch
confidence
risk_level
next_check_date
source_url
status
reviewer_note
```

Recommended status values:

```text
Watching
Needs More Evidence
Ready for Scorecard
Rejected
Archived
```

---

## Tab 4: rejected_records

Purpose:

Keep a log of rejected or unsafe records for audit and workflow improvement.

Recommended columns:

```text
rejected_id
record_id
source_url
source_type
rejection_date
rejection_reason
risk_type
reviewer_note
```

Possible rejection reasons:

```text
Private data
Login-protected source
Missing source URL
Unsupported claim
High compliance risk
Copyright risk
Platform policy risk
Duplicate record
Low relevance
Unsafe automation
```

---

## Tab 5: settings

Purpose:

Store workflow configuration values.

Recommended fields:

```text
allowed_regions
allowed_categories
allowed_source_types
blocked_source_types
minimum_confidence_for_digest
minimum_score_for_alert
review_required
default_review_status
digest_channel
report_frequency
```

Important:

```text
Do not store API keys, bot tokens, passwords, or private credentials in this tab.
```

---

## Recommended Review Status Values

Use consistent review status labels.

| Status | Meaning |
|---|---|
| Draft | AI-generated and not reviewed |
| Needs Review | Requires human inspection |
| Approved | Ready to use or publish |
| Rejected | Unsafe, unsupported, duplicate, or low quality |
| Watchlist | Interesting but not ready for action |

Recommended default:

```text
Draft
```

AI-generated records should not be automatically marked as Approved.

---

## Recommended Confidence Values

Use simple confidence labels:

```text
Low
Medium
High
```

Meaning:

| Confidence | Meaning |
|---|---|
| Low | Weak signal, limited evidence, or unclear demand |
| Medium | Reasonable signal from public sources, but still needs validation |
| High | Stronger signal from multiple reliable public sources |

Important:

```text
High confidence does not mean guaranteed sales.
```

---

## Recommended Risk Values

Use simple risk labels:

```text
Low
Medium
High
Avoid
Unknown
```

Meaning:

| Risk Level | Meaning |
|---|---|
| Low | No major obvious risk from available information |
| Medium | Needs careful review |
| High | Requires deeper compliance, safety, IP, or platform review |
| Avoid | Should not be used in current form |
| Unknown | Not enough information to judge |

---

## Suggested Source Type Values

Recommended values:

```text
Search
Marketplace
Social
Community
Review
News / Report
Manual
```

These should match:

```text
docs/data-sources.md
templates/source-log-template.csv
workflows/n8n-google-sheets-output.pseudo.json
```

---

## Suggested Data Validation

In Google Sheets, users can add dropdowns for:

```text
source_type
confidence
risk_level
review_status
region
category
```

This helps keep records consistent.

Example dropdown values:

```text
review_status:
Draft, Needs Review, Approved, Rejected, Watchlist
```

```text
confidence:
Low, Medium, High
```

```text
risk_level:
Low, Medium, High, Avoid, Unknown
```

---

## Suggested Conditional Formatting

Conditional formatting can make review easier.

Examples:

```text
Approved = green
Needs Review = yellow
Rejected = red
Watchlist = blue
Draft = gray
```

Risk level:

```text
Low = green
Medium = yellow
High = orange
Avoid = red
Unknown = gray
```

Opportunity score:

```text
12 or higher = strong candidate
8 to 11 = test carefully
4 to 7 = watchlist
below 4 = weak or avoid
```

---

## Suggested Opportunity Score Formula

TrendPilot AI uses a simple 1-5 scoring model.

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

Related prompt:

```text
prompts/product-scoring-prompt.md
```

Related template:

```text
templates/product-opportunity-scorecard.md
```

---

## Suggested Google Sheets Workflow

A basic workflow can look like this:

```text
1. Collect public trend signal.
2. Generate AI trend analysis.
3. Score product opportunity.
4. Run risk check.
5. Save record to source_log.
6. Mark review_status as Draft.
7. Human reviews the record.
8. Human updates review_status.
9. Approved records are used in reports.
10. Watchlist records are checked later.
```

---

## Related Pseudo Workflow

Google Sheets output is described in:

```text
workflows/n8n-google-sheets-output.pseudo.json
```

High-level flow:

```text
Receive Trend Record
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
        ↓
Trigger Report Generation
```

---

## Required Field Validation

Before saving a record, check that these fields exist:

```text
source_type
source_name
source_url
collection_date
region
category
trend_signal
evidence_summary
risk_note
confidence
```

If `source_url` is missing, mark the record as:

```text
Needs Review
```

If private personal data is detected, mark the record as:

```text
Rejected
```

---

## Private Data Filter

Before saving any record, check whether it includes:

```text
Email addresses
Phone numbers
Private addresses
Private messages
Payment details
ID documents
Health information
Financial information
Private social media profiles
Private group content
Scraped user databases
```

Recommended default:

```text
Do not store private personal data.
```

---

## Duplicate Check

To avoid duplicate records, compare:

```text
source_url
product_name
keyword
collection_date
```

If a record looks duplicated, mark it as:

```text
Needs Review
```

Do not automatically delete duplicates unless the user confirms.

---

## Human Review Workflow

A human reviewer should check:

```text
Source URL
Evidence summary
Trend signal
Product idea
Risk note
Confidence level
Opportunity score
Next action
Review status
```

Reviewer decisions:

```text
Approve
Reject
Move to Watchlist
Request More Research
```

Reviewer notes should be added to:

```text
reviewer_note
```

---

## Suggested Daily Summary Metrics

A daily summary can include:

```text
total_records
approved_records
draft_records
needs_review_records
watchlist_records
rejected_records
top_opportunity_score
top_product_idea
most_common_category
highest_risk_category
```

This makes it easier to generate daily reports and Telegram digests.

---

## Suggested Dashboard Ideas

A simple Google Sheets dashboard may include:

- Total records by date
- Records by category
- Records by region
- Top opportunity scores
- Watchlist count
- Needs Review count
- High-risk count
- Approved records count
- Top keywords
- Top product ideas

---

## Sharing and Permissions

Be careful with Google Sheets sharing settings.

Recommended practices:

```text
Keep the sheet private by default.
Share only with trusted users.
Use viewer access for clients when possible.
Use editor access only for team members.
Do not publish sheets containing internal notes.
Do not expose paid report records publicly.
```

Avoid:

```text
Anyone with the link can edit
Public editable research logs
Publishing private notes
Sharing sheets with secrets
Storing API keys in cells
```

---

## API Keys and Secrets

Do not store secrets in Google Sheets.

Never store:

```text
AI_API_KEY
FIRECRAWL_API_KEY
GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY
TELEGRAM_BOT_TOKEN
EMAIL_SMTP_PASSWORD
NOTION_API_KEY
N8N_WEBHOOK_SECRET
```

Safe alternatives:

```text
n8n credentials
Environment variables
Secret managers
Platform-specific credential storage
```

If a key is accidentally exposed:

```text
Revoke it immediately.
Rotate the key.
Check access logs if available.
Remove it from history if committed.
```

---

## Suggested CSV Template

TrendPilot AI already includes:

```text
templates/source-log-template.csv
```

Users can import this CSV into Google Sheets to create a starting table.

The CSV includes example records for:

```text
Jewelry travel organizer
Cable organizer bag
Pet hair remover brush
Heatless curling set
Grip socks
```

These examples are fictional research-style records and should be replaced with real public source-based records before production use.

---

## Report Generation From Google Sheets

Approved records can be used to generate:

```text
templates/daily-trend-report.md
templates/weekly-market-brief.md
templates/ecommerce-market-report.md
templates/telegram-digest-template.md
```

Suggested filter:

```text
review_status = Approved
confidence = Medium or High
risk_level is not Avoid
```

Draft and Needs Review records should be used only for internal review.

---

## Telegram Digest From Google Sheets

A Telegram digest can pull from approved records.

Related files:

```text
templates/telegram-digest-template.md
workflows/n8n-telegram-digest.pseudo.json
```

Suggested selection rules:

```text
Top 3 to 5 records by opportunity_score
Only Approved records
Exclude Avoid risk level
Include disclaimer
Include source links or source references
```

---

## Common Mistakes to Avoid

Avoid:

- Treating Google Sheets as a private data scraper database
- Storing personal contact information
- Storing API keys in cells
- Making sheets public accidentally
- Publishing AI-generated records without review
- Using records without source URLs
- Removing risk notes
- Removing disclaimers
- Overstating opportunity scores
- Using Google Sheets as a spam outreach list

---

## Related TrendPilot AI Files

Source log template:

```text
templates/source-log-template.csv
```

Google Sheets pseudo workflow:

```text
workflows/n8n-google-sheets-output.pseudo.json
```

Daily report template:

```text
templates/daily-trend-report.md
```

Telegram digest template:

```text
templates/telegram-digest-template.md
```

Product scoring prompt:

```text
prompts/product-scoring-prompt.md
```

Risk check prompt:

```text
prompts/risk-check-prompt.md
```

Compliance guide:

```text
docs/compliance.md
```

---

## Final Note

Google Sheets is a simple and practical starting point for TrendPilot AI.

A responsible Google Sheets workflow should include:

```text
Structured public records
+ Source URLs
+ Confidence levels
+ Risk notes
+ Review status
+ Human review
```

It should not become:

```text
Private data storage
Scraped contact database
Spam list
Unreviewed AI output dump
API key storage
Auto-money claim tracker
```

Use Google Sheets carefully, keep records source-aware, and review outputs before publishing or monetizing them.
