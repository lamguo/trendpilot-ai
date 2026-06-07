# Firecrawl Integration Guide

This guide explains how Firecrawl can be used as a public web extraction layer for TrendPilot AI.

TrendPilot AI does not include, copy, redistribute, or modify Firecrawl source code.  
Firecrawl is referenced as an external web extraction tool.

Official repository:

https://github.com/firecrawl/firecrawl

Official website:

https://www.firecrawl.dev

---

## Role in TrendPilot AI

Firecrawl can help convert public web pages into AI-readable formats such as clean text, markdown, or structured data.

In a TrendPilot AI workflow, Firecrawl may help with:

- Collecting public trend pages
- Extracting public product pages
- Extracting public marketplace category pages
- Reading public article pages
- Preparing source text for AI analysis
- Turning messy web pages into cleaner research inputs
- Supporting daily or weekly trend intelligence reports

Firecrawl should be treated as an external public web extraction tool, not as bundled TrendPilot AI code.

---

## Recommended Position in the Architecture

```text
Public Web Sources
        ↓
Firecrawl / Public Extraction Layer
        ↓
Clean Text or Structured Data
        ↓
n8n Workflow Automation
        ↓
AI Trend Analysis
        ↓
Product Opportunity Scoring
        ↓
Risk Check
        ↓
Human Review
        ↓
Report Generation
```

---

## Best Use Cases

Firecrawl may be useful for:

- Public article extraction
- Public product page extraction
- Public marketplace page research
- Public trend report extraction
- Public news and industry page extraction
- Public blog post summarization
- Public documentation extraction
- Public source preparation for AI prompts

---

## Not Recommended For

Firecrawl should not be used in TrendPilot AI for:

- Login-protected data
- Private user data
- Private social profiles
- Private groups
- Private messages
- Paywalled content without permission
- Anti-bot bypass
- CAPTCHA bypass
- Personal contact list scraping
- Scraped email or phone number databases
- Automated platform abuse
- Reposting copyrighted content

---

## Core Principle

Firecrawl should be used for:

```text
Public research source extraction
```

Not for:

```text
Private data scraping or platform restriction bypass
```

---

## Suggested MVP Use

A simple TrendPilot AI workflow can use Firecrawl like this:

```text
Load Public Source URL
        ↓
Check Source Safety
        ↓
Extract Public Page Content
        ↓
Clean Extracted Text
        ↓
Send to AI Trend Analysis Prompt
        ↓
Save Summary and Source URL
```

Related pseudo workflow:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
```

---

## Suggested Input Fields

Before sending a URL to Firecrawl, store the source information clearly.

Recommended fields:

```text
source_id
source_type
source_name
source_url
region
category
keyword
risk_level
collection_date
notes
```

Example:

```text
source_id: SRC-001
source_type: News / Report
source_name: Example Public Industry Blog
source_url: https://example.com/public-trend-report
region: United States
category: Home Organization
keyword: small space storage
risk_level: Low
collection_date: 2026-06-07
notes: Public article page, suitable for summarization.
```

---

## Source Safety Filter

Before extracting a page, ask:

```text
Is this page public?
Does it require login?
Does it contain private personal data?
Does it require bypassing restrictions?
Is it allowed to summarize this content?
Is the source relevant to trend research?
Can the source URL be saved for citation?
```

If the answer is unclear, mark the source as:

```text
Needs Review
```

and do not collect it automatically.

---

## Suggested Extracted Fields

After extracting a public page, TrendPilot AI should keep only useful research fields.

Recommended extracted fields:

```text
source_url
page_title
source_type
source_name
region
category
keyword
collection_date
raw_summary
visible_product_mentions
visible_price_signal
visible_review_signal
visible_social_signal
main_topic
source_evidence_summary
risk_note
risk_level
```

Do not store unnecessary personal data.

---

## Data Cleaning Rules

After extraction, clean the data before sending it to AI.

Recommended cleaning steps:

1. Remove navigation menus.
2. Remove cookie banners.
3. Remove unrelated footer text.
4. Remove duplicate blocks.
5. Remove irrelevant advertisements.
6. Keep source URL.
7. Keep publication date if visible.
8. Keep collection date.
9. Summarize in original words.
10. Add risk note if needed.

---

## AI Analysis Step

After extraction and cleaning, send the content to:

```text
prompts/trend-analysis-prompt.md
```

The AI should extract:

- Product or category idea
- Main trend reason
- Target audience
- Consumer pain point
- Buyer motivation
- Emotional trigger
- Suggested keywords
- Short-form content angle
- Marketplace research angle
- Source-based evidence summary
- Risk or uncertainty
- Confidence level
- Suggested next action

Important AI rules:

```text
Use only the provided source material.
Do not invent facts.
Do not claim guaranteed demand.
Do not copy long source text.
Do not include private personal data.
Add uncertainty when evidence is weak.
```

---

## Example Extraction Flow

```text
1. n8n loads a public source URL.
2. Source Safety Filter checks whether the URL is safe.
3. Firecrawl extracts readable page content.
4. The workflow removes irrelevant page sections.
5. AI summarizes the extracted public content.
6. AI identifies product or category opportunities.
7. Product scoring prompt evaluates the idea.
8. Risk check prompt reviews claim, compliance, and platform risks.
9. The structured record is saved to Google Sheets.
10. Human reviewer checks before report delivery.
```

---

## Example Public Source Categories

Firecrawl may be used with public sources such as:

```text
Official trend reports
Public industry news
Public marketplace category pages
Public product pages
Public brand blog posts
Public review pages where allowed
Public e-commerce reports
Public platform update pages
Public research summaries
```

Avoid using it with:

```text
Private groups
Private messages
Login-only pages
User account pages
Payment pages
Checkout pages
Contact databases
Scraped email lists
Restricted APIs
Paywalled pages without permission
```

---

## Recommended Output Record

A Firecrawl-based extraction should eventually become a structured TrendPilot AI record.

Example:

```text
record_id: TRD-20260607-001
source_type: News / Report
source_name: Example Public Trend Report
source_url: https://example.com/public-trend-report
collection_date: 2026-06-07
publication_date: 2026-06-01
region: United States
category: Home Organization
keyword: small space storage
product_name: Foldable storage basket
trend_signal: Public content suggests interest in flexible home organization for small apartments.
evidence_summary: The source discusses consumer interest in compact, multi-use storage products.
target_audience: Apartment renters, small home owners, home organization shoppers
pain_point: Limited space and clutter in small living areas
content_angle: Before-and-after small apartment organization routine
price_signal: Needs marketplace validation
competition_signal: Unknown
risk_note: Avoid copying article text. Verify marketplace demand and product quality.
risk_level: Medium
confidence: Medium
opportunity_score: 
next_action: Check marketplace pricing, public reviews, and supplier availability.
review_status: Draft
reviewer_note:
```

---

## Risk Notes

When using Firecrawl or any web extraction tool, watch for:

- Copyright risk
- Privacy risk
- Platform terms risk
- Source reliability risk
- Outdated source risk
- Paywall or login restriction risk
- Excessive crawling risk
- Misleading extraction results
- AI hallucination after extraction
- Republishing source content instead of summarizing it

---

## Copyright Safety

TrendPilot AI should not use Firecrawl output to copy or republish third-party content.

Safer behavior:

```text
Summarize public information in original words.
Keep source links.
Use short excerpts only when necessary.
Create original analysis.
Create original templates and reports.
```

Unsafe behavior:

```text
Copying full articles.
Copying full product descriptions.
Copying full reviews.
Copying creator captions.
Copying paid reports.
Reposting extracted content as original work.
Removing attribution.
```

---

## Privacy Safety

TrendPilot AI should not collect:

```text
Emails
Phone numbers
Addresses
Private messages
Private profiles
Payment details
ID documents
Health information
Financial information
Children's data
Face photos without consent
Private group content
Scraped user databases
```

Recommended default:

```text
Do not collect private personal data.
```

---

## Platform Safety

Do not use Firecrawl to:

```text
Bypass login restrictions
Bypass paywalls
Bypass anti-bot systems
Bypass CAPTCHA
Automate checkout
Scrape private account pages
Collect private marketplace data
Collect personal contact databases
Mass harvest social profiles
```

If a website blocks automated access, respect that restriction.

---

## Human Review Checklist

Before using extracted content in a report, confirm:

- [ ] The page is public
- [ ] The source URL is saved
- [ ] The content was summarized, not copied
- [ ] No private personal data is included
- [ ] No long copyrighted text is included
- [ ] No login or paywall was bypassed
- [ ] The source is recent enough
- [ ] The source is relevant
- [ ] The AI summary matches the source
- [ ] Confidence level is included
- [ ] Risk note is included
- [ ] Risk level is included
- [ ] Human reviewer has checked the output

---

## Suggested Error Handling

A Firecrawl-based workflow should handle:

```text
Invalid URL
Blocked source
Empty extraction
Irrelevant content
Duplicate source
Rate limit
Timeout
Page unavailable
High-risk source
Private data detected
Missing source URL
```

Suggested handling:

```text
Log error
Mark as Needs Review
Do not publish incomplete data
Do not retry aggressively
Notify operator if needed
```

---

## Secrets and API Keys

Do not commit secrets to GitHub.

Possible secret values:

```text
FIRECRAWL_API_KEY
AI_API_KEY
N8N_WEBHOOK_SECRET
GOOGLE_SHEETS_CREDENTIALS
TELEGRAM_BOT_TOKEN
NOTION_API_KEY
```

Safe practices:

- Store keys in n8n credentials.
- Use environment variables.
- Never paste real keys into public workflow files.
- Never store API keys in Google Sheets.
- Rotate leaked keys immediately.

---

## License and Attribution Notes

Firecrawl is an external project.

Before using Firecrawl in production, review:

- Official repository
- Current license file
- Official documentation
- Commercial usage terms
- Deployment terms
- API terms

TrendPilot AI should not:

- Copy Firecrawl source code
- Modify Firecrawl source code inside this repository
- Repackage Firecrawl as TrendPilot AI
- Remove Firecrawl attribution
- Claim official partnership with Firecrawl
- Teach users how to bypass website restrictions

Recommended wording:

```text
TrendPilot AI references Firecrawl as an external public web extraction tool. This repository does not include or redistribute Firecrawl source code.
```

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
workflows/n8n-google-sheets-output.pseudo.json
```

Prompts:

```text
prompts/trend-analysis-prompt.md
prompts/product-scoring-prompt.md
prompts/risk-check-prompt.md
```

Templates:

```text
templates/source-log-template.csv
templates/daily-trend-report.md
```

---

## Final Note

Firecrawl can be useful for turning public web pages into cleaner AI research inputs.

But extraction is only one part of a safe trend intelligence workflow.

A responsible TrendPilot AI flow should include:

```text
Public source check
+ Safe extraction
+ Cleaning
+ AI analysis
+ Risk review
+ Risk level classification
+ Source logging
+ Human review
+ Clear disclaimer
```

It should not become:

```text
Private data scraper
Copyright copying tool
Platform bypass system
Spam engine
Auto-money bot
```

Use Firecrawl responsibly and review all extracted content before using it in reports.
