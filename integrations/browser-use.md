# Browser-use Integration Guide

This guide explains how Browser-use can be referenced as an optional browser automation layer for TrendPilot AI.

TrendPilot AI does not include, copy, redistribute, or modify Browser-use source code.  
Browser-use is referenced as an external browser automation tool.

Official repository:

https://github.com/browser-use/browser-use

Official website:

https://browser-use.com

---

## Role in TrendPilot AI

Browser-use can help AI agents interact with public web pages through a browser-like interface.

In a TrendPilot AI workflow, Browser-use may help with:

- Navigating public web pages
- Reading public product category pages
- Opening public search result pages
- Moving through public marketplace pages
- Collecting visible public information
- Supporting research tasks that require page interaction
- Assisting with repetitive browsing workflows

Browser-use should be treated as an optional advanced module, not as a required core dependency.

---

## Recommended Position in the Architecture

```text
Public Web Pages
        ↓
Browser-use / Browser Interaction Layer
        ↓
Visible Public Page Information
        ↓
n8n / Automation Layer
        ↓
AI Analysis Layer
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

## When Browser-use May Be Useful

Browser-use may be useful when:

- A public page requires navigation
- A public page needs buttons or tabs opened
- A public category page has multiple visible sections
- A research task needs repeated browsing steps
- A static scraper does not capture enough visible context
- A user wants an AI assistant to explore public pages interactively

Example safe use cases:

```text
Open a public marketplace category page.
Read visible product titles and price ranges.
Summarize visible category patterns.
Save source URLs and notes.
Send summaries to AI trend analysis.
```

---

## When Browser-use Should Not Be Used

Browser-use should not be used for:

- Login-based scraping
- Private account pages
- Private messages
- Private groups
- Private profiles
- Paywall bypass
- CAPTCHA bypass
- Anti-bot bypass
- Automated account creation
- Account farming
- Fake engagement
- Fake comments
- Fake reviews
- Mass direct messages
- Automated following or unfollowing
- Checkout automation
- Payment automation
- Scraping personal emails or phone numbers
- Building private contact databases

---

## Core Principle

Browser-use should be used for:

```text
Public-page research assistance
```

Not for:

```text
Platform bypass, spam, fake engagement, or private data scraping
```

---

## Suggested MVP Use

A simple TrendPilot AI workflow may use Browser-use like this:

```text
Load Public Research URL
        ↓
Check Source Safety
        ↓
Open Public Page
        ↓
Read Visible Page Information
        ↓
Extract Research Notes
        ↓
Send Notes to AI Trend Analysis
        ↓
Save Structured Record
        ↓
Human Review
```

Related pseudo workflow:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
```

---

## Source Safety Filter

Before allowing any browser automation, ask:

```text
Is this page public?
Does this page require login?
Does this page contain private personal data?
Does the task require bypassing a restriction?
Does the task involve messaging users?
Does the task involve creating accounts?
Does the task involve fake engagement?
Does the task involve checkout, payment, or order placement?
Can the information be summarized instead of copied?
Is the use case ethical if publicly disclosed?
```

If the answer is unclear, mark the source as:

```text
Needs Review
```

and do not automate the task.

---

## Safe Browser Automation Examples

### Example 1: Public Product Category Review

```text
Goal:
Review a public product category page.

Allowed:
- Open public category page
- Read visible product titles
- Note visible price ranges
- Summarize category patterns
- Save source URL
- Add human review status

Not allowed:
- Copy full product descriptions
- Copy product images
- Scrape private seller data
- Bypass restrictions
```

---

### Example 2: Public Trend Page Review

```text
Goal:
Review a public trend report or public content page.

Allowed:
- Open public page
- Read visible public content
- Summarize trend themes
- Extract product or category mentions
- Keep source URL

Not allowed:
- Copy full article text
- Repost extracted content
- Remove attribution
- Access paywalled content without permission
```

---

### Example 3: Public Marketplace Comparison

```text
Goal:
Compare visible public product patterns.

Allowed:
- Observe public product titles
- Observe visible price ranges
- Summarize common features
- Summarize repeated positioning
- Identify differentiation opportunities

Not allowed:
- Copy competitor images
- Copy competitor listing text
- Clone protected designs
- Collect buyer or seller private data
```

---

## Unsafe Browser Automation Examples

Avoid workflows like:

```text
Create multiple accounts automatically.
Log in and scrape private user data.
Send mass direct messages.
Post automated comments.
Like, follow, or share content automatically.
Bypass CAPTCHA.
Bypass paywalls.
Harvest emails or phone numbers.
Automate checkout behavior.
Generate fake reviews.
```

These use cases do not belong in TrendPilot AI.

---

## Suggested Input Fields

Before using Browser-use in a TrendPilot AI workflow, define the task clearly.

Recommended input fields:

```text
task_id
source_type
source_name
source_url
region
category
keyword
task_goal
allowed_actions
blocked_actions
risk_level
review_required
notes
```

Example:

```text
task_id: BROWSE-001
source_type: Marketplace
source_name: Example Public Marketplace
source_url: https://example.com/public-category-page
region: United States
category: Travel Accessories
keyword: jewelry travel organizer
task_goal: Summarize visible public category patterns.
allowed_actions: Open page, read visible product titles, note price ranges, summarize patterns.
blocked_actions: Login, copy images, copy full descriptions, message users, bypass restrictions.
risk_level: Medium
review_required: true
notes: Public page only.
```

---

## Suggested Output Fields

Browser-use research output should be structured before being sent to AI analysis.

Recommended output fields:

```text
task_id
source_type
source_name
source_url
collection_date
region
category
keyword
visible_product_mentions
visible_price_range
visible_feature_patterns
visible_content_patterns
visible_customer_language
research_summary
risk_note
confidence
next_action
review_status
```

Default review status:

```text
Draft
```

---

## Data Cleaning Rules

After browser-based research, clean the output.

Recommended rules:

1. Keep source URL.
2. Keep collection date.
3. Remove irrelevant navigation text.
4. Remove cookie banner text.
5. Remove duplicate blocks.
6. Summarize in original words.
7. Avoid copying long text.
8. Avoid personal identifiers.
9. Add risk note.
10. Add confidence level.
11. Mark as Draft or Needs Review.

---

## AI Analysis Step

After Browser-use collects public research notes, send the cleaned notes to:

```text
prompts/trend-analysis-prompt.md
```

The AI should extract:

```text
Product or category idea
Trend reason
Target audience
Consumer pain point
Buyer motivation
Emotional trigger
Suggested keywords
Content angle
Marketplace research angle
Source-based evidence summary
Risk or uncertainty
Confidence level
Suggested next action
```

Important AI rules:

```text
Use only provided source material.
Do not invent facts.
Do not claim guaranteed demand.
Do not copy long source text.
Do not include private personal data.
Add uncertainty when evidence is weak.
```

---

## Risk Check Step

Browser-based workflows should include a risk review.

Related prompt:

```text
prompts/risk-check-prompt.md
```

Check for:

```text
Privacy risk
Platform policy risk
Copyright risk
IP or trademark risk
Unsupported claim risk
Product safety risk
Compliance risk
Shipping risk
Source quality risk
Spam or platform abuse risk
```

High-risk output should be marked:

```text
Needs Review
```

or:

```text
Rejected
```

---

## Suggested Workflow Pattern

```text
1. User defines a public research task.
2. Workflow checks whether the source and task are safe.
3. Browser-use opens the public page.
4. Browser-use reads visible public information.
5. Workflow extracts concise research notes.
6. AI summarizes trend signals.
7. AI scores product opportunity.
8. AI checks risk.
9. Record is saved to Google Sheets.
10. Human reviewer approves or rejects the output.
```

---

## Human Review Checklist

Before using browser-collected output in a report, confirm:

- [ ] The source page is public
- [ ] No login was required
- [ ] No restriction was bypassed
- [ ] No private personal data was collected
- [ ] No long copyrighted text was copied
- [ ] No product images were reused
- [ ] No user messages were sent
- [ ] No fake engagement occurred
- [ ] Source URL is saved
- [ ] Risk note is included
- [ ] Confidence level is included
- [ ] Human reviewer checked the output

---

## Recommended Guardrails

A TrendPilot AI browser automation task should include guardrails.

Recommended allowed actions:

```text
Open public URL
Read visible page text
Summarize visible information
Click public navigation elements
Collect source URL
Record visible price range
Record visible category patterns
```

Recommended blocked actions:

```text
Login
Create account
Send message
Post comment
Like content
Follow account
Buy product
Add to cart
Submit form
Bypass CAPTCHA
Bypass paywall
Download private files
Collect personal contact data
```

---

## Example Research Task

```text
Task:
Review public product category page for travel jewelry organizers.

Allowed:
- Open public category page
- Read visible titles
- Observe visible price ranges
- Summarize common features
- Save source URL

Blocked:
- Login
- Add products to cart
- Copy images
- Copy descriptions
- Message sellers
- Collect seller private data

Output:
- Category summary
- Visible price range
- Common features
- Possible differentiation angles
- Risk note
- Next research step
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

Prompts:

```text
prompts/trend-analysis-prompt.md
prompts/product-scoring-prompt.md
prompts/competitor-summary-prompt.md
prompts/content-angle-prompt.md
prompts/risk-check-prompt.md
```

Templates:

```text
templates/source-log-template.csv
templates/daily-trend-report.md
templates/competitor-snapshot.md
```

Pseudo workflows:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
workflows/n8n-google-sheets-output.pseudo.json
```

---

## Secrets and Credentials

Do not commit secrets to GitHub.

Possible secret values:

```text
AI_API_KEY
N8N_WEBHOOK_SECRET
BROWSER_AUTOMATION_SESSION_SECRET
GOOGLE_SHEETS_CREDENTIALS
TELEGRAM_BOT_TOKEN
NOTION_API_KEY
```

Safe practices:

- Store secrets in secure credential managers.
- Never paste real keys into public workflow files.
- Never store session cookies in public files.
- Never commit browser profiles containing login sessions.
- Rotate leaked keys immediately.

---

## License and Attribution Notes

Browser-use is an external project.

Before using Browser-use in production, review:

- Official repository
- Current license file
- Official documentation
- Commercial usage terms
- Deployment terms
- Security guidance

TrendPilot AI should not:

- Copy Browser-use source code
- Modify Browser-use source code inside this repository
- Repackage Browser-use as TrendPilot AI
- Remove Browser-use attribution
- Claim official partnership with Browser-use
- Teach users how to bypass platform restrictions

Recommended wording:

```text
TrendPilot AI references Browser-use as an external browser automation tool. This repository does not include or redistribute Browser-use source code.
```

---

## Final Note

Browser automation can be powerful, but it carries more risk than simple public source reading.

A responsible TrendPilot AI browser workflow should include:

```text
Public page only
+ Clear allowed actions
+ Clear blocked actions
+ Safe extraction
+ AI analysis
+ Risk check
+ Human review
```

It should not become:

```text
Account farming
Spam automation
Fake engagement
Private data scraping
Platform bypass
Auto-money system
```

Use Browser-use responsibly and review all browser-based output before using it in reports.
