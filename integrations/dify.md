# Dify Integration Guide

This guide explains how Dify can be used as the AI workflow and LLM orchestration layer for TrendPilot AI.

TrendPilot AI does not include, copy, redistribute, or modify Dify source code.  
Dify is referenced as an external AI workflow platform.

Official repository:

https://github.com/langgenius/dify

Official website:

https://dify.ai

---

## Role in TrendPilot AI

Dify can help build structured AI workflows for trend analysis, product opportunity scoring, risk checking, and report generation.

In a TrendPilot AI system, Dify may help with:

- Running reusable AI prompt workflows
- Summarizing public trend signals
- Extracting product ideas
- Scoring product opportunities
- Reviewing product and content risks
- Generating daily or weekly reports
- Managing prompt chains
- Structuring AI output
- Building internal AI research assistants

Dify should be treated as an external AI workflow platform, not as bundled TrendPilot AI code.

---

## Recommended Position in the Architecture

```text
Public Trend Sources
        ↓
Data Collection Layer
        ↓
n8n / Automation Layer
        ↓
Dify / AI Workflow Layer
        ↓
Trend Analysis Prompt
        ↓
Product Scoring Prompt
        ↓
Risk Check Prompt
        ↓
Structured Output
        ↓
Google Sheets / Notion / Report Templates
        ↓
Human Review
```

---

## Best Use Cases

Dify may be useful for:

- AI trend analysis workflows
- Product opportunity scoring
- Public review insight extraction
- Competitor summary generation
- Content angle generation
- Risk review workflows
- Weekly report drafting
- AI-powered research assistants
- Prompt chain management
- Reusable report generation logic

---

## Not Recommended For

Dify should not be used in TrendPilot AI for:

- Generating unsupported market claims
- Producing reports without source links
- Creating fake reviews
- Creating fake testimonials
- Generating spam content
- Processing private personal data without permission
- Making legal, financial, medical, or regulatory decisions
- Approving high-risk products automatically
- Claiming guaranteed demand, sales, profit, or business success

---

## Core Principle

Dify should be used for:

```text
Structured AI analysis and report generation
```

Not for:

```text
Unverified claims, fake content, or automatic business decisions
```

---

## Suggested MVP Use

A simple TrendPilot AI workflow can use Dify like this:

```text
Clean Public Trend Signals
        ↓
Trend Analysis Prompt
        ↓
Product Scoring Prompt
        ↓
Risk Check Prompt
        ↓
Structured JSON or Markdown Output
        ↓
Save to Google Sheets
        ↓
Generate Report Draft
        ↓
Human Review
```

Related pseudo workflow:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
```

---

## Suggested Dify Workflow Structure

A Dify workflow can be designed with multiple AI steps.

Example structure:

```text
Input Node
    ↓
Source Summary Node
    ↓
Trend Analysis Node
    ↓
Product Scoring Node
    ↓
Risk Check Node
    ↓
Report Draft Node
    ↓
Structured Output Node
```

---

## Suggested Input Fields

A Dify workflow should receive structured public research data.

Recommended input fields:

```text
source_type
source_name
source_url
collection_date
publication_date
region
category
keyword
product_name
raw_signal
evidence_summary
visible_price_signal
visible_review_signal
visible_social_signal
risk_note
notes
```

Example input:

```text
source_type: Social
source_name: Example Public Platform
source_url: https://example.com/public-trend-page
collection_date: 2026-06-07
region: United States
category: Travel Accessories
keyword: jewelry travel organizer
raw_signal: Public travel packing content shows repeated interest in compact jewelry storage.
evidence_summary: Visible public content suggests users want a cleaner way to store rings, earrings, and necklaces during travel.
risk_note: Avoid copying creator content or competitor images.
```

---

## Suggested Output Fields

A Dify workflow should return structured, reviewable output.

Recommended output fields:

```text
product_idea
category
target_region
target_audience
trend_reason
consumer_pain_point
buyer_motivation
emotional_trigger
suggested_keywords
content_angle
marketplace_research_angle
source_evidence_summary
confidence
risk_note
risk_level
opportunity_score
score_interpretation
suggested_next_action
review_status
```

Default review status:

```text
Draft
```

---

## Prompt Files Used by Dify

TrendPilot AI already includes prompt templates that can be adapted into Dify workflow nodes.

Core prompt files:

```text
prompts/trend-analysis-prompt.md
prompts/product-scoring-prompt.md
prompts/competitor-summary-prompt.md
prompts/review-pain-point-prompt.md
prompts/content-angle-prompt.md
prompts/risk-check-prompt.md
```

Recommended prompt order:

```text
1. trend-analysis-prompt.md
2. product-scoring-prompt.md
3. risk-check-prompt.md
4. content-angle-prompt.md
5. competitor-summary-prompt.md
6. review-pain-point-prompt.md
```

Not every workflow needs every prompt.  
For an MVP, use only:

```text
trend-analysis-prompt.md
product-scoring-prompt.md
risk-check-prompt.md
```

---

## Workflow Step 1: Trend Analysis

Related file:

```text
prompts/trend-analysis-prompt.md
```

Purpose:

Turn public trend signals into structured product opportunity insights.

Input:

```text
Public source summaries
Trend signals
Visible product mentions
Audience clues
Pain point notes
Source links
```

Output:

```text
Product idea
Trend reason
Target audience
Consumer pain point
Buyer motivation
Emotional trigger
Keywords
Content angle
Marketplace research angle
Evidence summary
Confidence
Next action
```

Important rules:

```text
Do not invent facts.
Use only provided source material.
Do not claim guaranteed demand.
Do not copy long source text.
Include uncertainty and risk notes.
```

---

## Workflow Step 2: Product Scoring

Related file:

```text
prompts/product-scoring-prompt.md
```

Purpose:

Score product opportunities using the TrendPilot AI 1-5 scoring model.

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

It only means the product idea appears stronger under this research framework.

---

## Workflow Step 3: Risk Check

Related file:

```text
prompts/risk-check-prompt.md
```

Purpose:

Identify product, content, claim, platform, IP, privacy, shipping, and compliance risks.

Risk areas:

```text
Product safety
Compliance or certification
Platform policy
Health or wellness claims
Baby or child safety
Electronics or batteries
Food, supplements, or ingredients
Trademark, copyright, design, or IP
Shipping and fulfillment
Privacy or personal data
Spam or platform abuse
Unsupported claims
Misleading income claims
Source quality
```

Recommended decision labels:

```text
Proceed
Test Carefully
Needs Compliance Review
Avoid
```

---

## Workflow Step 4: Content Angle Generation

Related file:

```text
prompts/content-angle-prompt.md
```

Purpose:

Generate ethical and original content angles from product research.

Possible outputs:

```text
TikTok hooks
Instagram Reels ideas
Pinterest ideas
YouTube Shorts ideas
SEO article topics
Product page angle
Newsletter angle
Ad concept ideas
Visual scene suggestions
Content ideas to avoid
```

Important rules:

```text
Do not copy creators.
Do not copy competitor captions.
Do not reuse competitor images.
Do not generate fake testimonials.
Do not create misleading advertising claims.
```

---

## Workflow Step 5: Report Draft Generation

Related templates:

```text
templates/daily-trend-report.md
templates/weekly-market-brief.md
templates/ecommerce-market-report.md
templates/product-opportunity-scorecard.md
```

Purpose:

Turn structured AI output into a human-reviewable report draft.

Reports should include:

```text
Source links
Evidence summary
Confidence level
Risk notes
Opportunity score
Suggested next actions
Disclaimer
```

Reports should not include:

```text
Guaranteed income claims
Unsupported statistics
Private personal data
Copied full source text
Fake reviews
Fake testimonials
```

---

## Suggested Dify Output Format

For automation workflows, JSON-style structured output is often easier to process.

Example output structure:

```json
{
  "product_idea": "Jewelry Travel Organizer",
  "category": "Travel Accessories",
  "target_region": "United States",
  "target_audience": "Women travelers, jewelry owners, gift buyers",
  "trend_reason": "Public travel packing content shows interest in compact jewelry storage.",
  "consumer_pain_point": "Jewelry can get tangled, scratched, or lost during travel.",
  "content_angle": "Before-and-after packing routine showing messy jewelry versus organized travel case.",
  "confidence": "Medium",
"risk_note": "Avoid copying creator content or competitor images. Verify material claims and zipper quality.",
"risk_level": "Low",
"opportunity_score": 15,
  "review_status": "Draft",
  "next_action": "Check marketplace pricing, public reviews, and supplier options."
}
```

---

## Suggested Human Review Status

Dify output should not be treated as final.

Recommended statuses:

| Status | Meaning |
|---|---|
| Draft | AI-generated and not reviewed |
| Needs Review | Requires human inspection |
| Approved | Ready to use or publish |
| Rejected | Unsafe, unsupported, or low quality |
| Watchlist | Interesting but not ready for action |

Recommended default:

```text
Draft
```

---

## Hallucination Reduction Rules

AI workflows should reduce hallucination risk.

Use these rules:

```text
Use only the provided source material.
Keep source URLs attached.
Ask for evidence summaries.
Require confidence levels.
Require uncertainty notes.
Require risk notes.
Avoid unsupported statistics.
Avoid making up market size numbers.
Avoid claiming current popularity without evidence.
Do not fill missing data with guesses.
```

If evidence is missing, the AI should write:

```text
Not enough evidence from the provided sources.
```

---

## Source Quality Rules

Dify workflows should classify source quality.

Suggested labels:

```text
Low
Medium
High
Unknown
```

High-quality sources may include:

```text
Official trend reports
Government data
Reputable industry reports
Official platform reports
Public marketplace pages with visible signals
Multiple independent public sources
```

Lower-quality sources may include:

```text
Single social post
Unverified blog
Unclear source
Old source
Copied content
Very limited evidence
```

---

## Risk Handling Rules

Suggested routing logic:

```text
Low risk + Medium/High confidence = Draft or Approved after review
Medium risk = Needs Review
High risk = Needs Compliance Review
Avoid decision = Rejected
Missing source = Needs Review
Private data detected = Rejected
Unsupported claim detected = Needs Review
```

Important:

```text
Do not auto-approve high-risk records.
```

---

## Suggested Integration With n8n

Dify can be called from n8n through an API or workflow endpoint.

High-level flow:

```text
n8n Schedule Trigger
    ↓
Collect Public Source Data
    ↓
Clean Data
    ↓
Send to Dify Workflow
    ↓
Receive Structured AI Output
    ↓
Save to Google Sheets
    ↓
Generate Report Draft
    ↓
Human Review
    ↓
Send Telegram Digest
```

Related guide:

```text
integrations/n8n.md
```

Related pseudo workflow:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
```

---

## Suggested Integration With Google Sheets

Dify output can be saved into Google Sheets.

Related guide:

```text
integrations/google-sheets.md
```

Related template:

```text
templates/source-log-template.csv
```

Recommended fields:

```text
record_id
source_type
source_name
source_url
collection_date
region
category
keyword
product_name
trend_signal
evidence_summary
target_audience
pain_point
content_angle
risk_note
risk_level
confidence
opportunity_score
next_action
review_status
reviewer_note
```

---

## Secrets and API Keys

Do not commit secrets to GitHub.

Possible secret values:

```text
DIFY_API_KEY
AI_API_KEY
N8N_WEBHOOK_SECRET
GOOGLE_SHEETS_CREDENTIALS
TELEGRAM_BOT_TOKEN
NOTION_API_KEY
```

Safe practices:

- Store keys in n8n credentials or environment variables.
- Never paste real keys into public workflow files.
- Never store keys in Markdown files.
- Never store API keys in Google Sheets.
- Rotate leaked keys immediately.

---

## Common Mistakes to Avoid

Avoid:

- Treating Dify output as final truth
- Removing human review
- Generating reports without source links
- Making up statistics
- Overstating weak trends
- Publishing unsupported product claims
- Ignoring compliance risk
- Using private data as input
- Storing secrets in public files
- Claiming guaranteed income or sales

---

## Human Review Checklist

Before publishing or using Dify-generated output, confirm:

- [ ] Sources are public
- [ ] Source links are included
- [ ] Claims are supported by evidence
- [ ] No private personal data is included
- [ ] No long copyrighted text is copied
- [ ] No unsupported statistics are included
- [ ] Confidence level is included
- [ ] Risk note is included
- [ ] Risk level is included
- [ ] Product success is not guaranteed
- [ ] Disclaimer is included
- [ ] Human reviewer has approved the output

---

## License and Attribution Notes

Dify is an external project.

Before using Dify in production, review:

- Official repository
- Current license file
- Official documentation
- Commercial usage terms
- Deployment terms
- API terms

TrendPilot AI should not:

- Copy Dify source code
- Modify Dify source code inside this repository
- Repackage Dify as TrendPilot AI
- Remove Dify attribution
- Claim official partnership with Dify
- Teach users how to bypass Dify license conditions

Recommended wording:

```text
TrendPilot AI references Dify as an external AI workflow platform. This repository does not include or redistribute Dify source code.
```

---

## Related TrendPilot AI Files

Architecture:

```text
docs/architecture.md
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
prompts/review-pain-point-prompt.md
prompts/content-angle-prompt.md
prompts/risk-check-prompt.md
```

Templates:

```text
templates/daily-trend-report.md
templates/product-opportunity-scorecard.md
templates/weekly-market-brief.md
templates/ecommerce-market-report.md
```

Pseudo workflows:

```text
workflows/n8n-daily-trend-intelligence.pseudo.json
workflows/n8n-google-sheets-output.pseudo.json
workflows/n8n-telegram-digest.pseudo.json
```

---

## Final Note

Dify can be a useful AI workflow layer for TrendPilot AI.

But the value is not in AI output alone.

A responsible TrendPilot AI system should combine:

```text
Public sources
+ Structured prompts
+ Source links
+ Confidence levels
+ Risk checks
+ Human review
+ Clear disclaimers
```

It should not become:

```text
Unverified claim generator
Fake review generator
Spam content engine
Private data processor
Auto-money system
```

Use Dify responsibly and review all AI-generated output before publishing or monetizing it.
