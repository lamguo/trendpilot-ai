# Workflow Design

This document defines the workflow structure for TrendPilot AI.

TrendPilot AI is not a single auto-money script. It is a license-safe starter kit for building AI-powered trend intelligence workflows using public data sources, automation tools, AI analysis, scoring templates, and report delivery formats.

The goal is to help users design practical systems that can collect public trend signals, analyze them with AI, score product opportunities, and generate daily or weekly reports.

---

## Workflow Design Principles

TrendPilot AI workflows should follow these principles:

1. Use public and legally accessible information only.
2. Avoid private personal data.
3. Avoid login-protected or restricted data.
4. Avoid platform restriction bypass.
5. Avoid automated spam, fake engagement, or account farming.
6. Keep source links for every important signal.
7. Add confidence levels and risk notes.
8. Use human review before publishing or monetizing reports.
9. Do not claim guaranteed income or guaranteed trend accuracy.
10. Keep third-party tools external and properly attributed.

---

## Recommended MVP Workflow

The first version should stay simple.

```text
Public Sources
    ↓
Data Collection
    ↓
AI Summarization
    ↓
Product Opportunity Scoring
    ↓
Daily Report Template
    ↓
Google Sheets / Telegram / Email
```

MVP goal:

- Collect a small number of public trend signals
- Summarize them into product ideas
- Score each idea with a transparent framework
- Generate a short daily report
- Save all records for review

The MVP should not attempt to scrape everything on the internet.

A small number of clean sources is better than a large number of risky or noisy sources.

---

## Workflow 1: Daily Trend Signal Collector

### Purpose

Collect public trend signals from selected sources every day.

### Input

Possible input sources:

- Official trend reports
- Public marketplace bestseller pages
- Public social trend pages
- Public community discussions
- Public review pages
- Public news and industry pages
- RSS feeds
- Search trend pages where allowed

### Process

```text
1. Start scheduled workflow.
2. Load source list.
3. Visit each public source.
4. Extract title, URL, topic, product mentions, and visible signals.
5. Save raw notes.
6. Add collection date.
7. Send cleaned text to AI analysis step.
```

### Recommended Output Fields

| Field | Description |
|---|---|
| source_type | Search, marketplace, social, community, review, report, news |
| source_name | Platform or publisher |
| source_url | Public source link |
| collection_date | Date collected |
| region | Country or market |
| category | Product or category |
| keyword | Main keyword |
| raw_signal | Short source-based signal |
| evidence_note | What was observed |
| risk_note | Source or compliance risk |

### Human Review

Before using collected signals in a paid report, check:

- Is the source public?
- Is the source recent?
- Is the source relevant?
- Is the content summarized rather than copied?
- Is the risk note clear?
- Is the source link saved?

---

## Workflow 2: AI Trend Summarizer

### Purpose

Turn raw public signals into clear trend summaries.

### Input

Raw collected notes from public sources.

### AI Task

The AI should identify:

- What product or category is being discussed
- Why it may be trending
- Which audience may care
- What consumer problem it solves
- What content angle may work
- What evidence supports the signal
- What uncertainty remains

### Suggested Prompt Structure

```text
You are an e-commerce trend research assistant.

Analyze the following public trend signals.

For each signal, extract:
1. Product or category idea
2. Main trend reason
3. Target audience
4. Consumer pain point
5. Possible content angle
6. Evidence from the source
7. Risk or uncertainty
8. Confidence level: Low, Medium, or High

Rules:
- Do not invent facts.
- Use only the provided source material.
- Do not claim guaranteed demand.
- Do not copy long text from the source.
- Keep the summary practical and concise.
```

### Output Fields

| Field | Description |
|---|---|
| product_idea | Product or category idea |
| trend_reason | Why it may be trending |
| audience | Target users |
| pain_point | Consumer problem |
| content_angle | Suggested short-form content angle |
| source_evidence | Source-based evidence summary |
| uncertainty | What is unclear |
| confidence | Low, Medium, or High |

---

## Workflow 3: Product Opportunity Scoring

### Purpose

Score each product idea using a consistent framework.

### Scoring Dimensions

| Dimension | Score Range | Meaning |
|---|---:|---|
| Demand Signal | 1-5 | Strength of visible market interest |
| Social Visibility | 1-5 | How easy it is to create engaging content |
| Price Potential | 1-5 | Whether margins may be possible |
| Supplier Availability | 1-5 | How easy it may be to source |
| Differentiation Potential | 1-5 | Whether it can be improved, bundled, or branded |
| Competition Level | 1-5 | How crowded the market appears |
| Shipping Difficulty | 1-5 | Size, weight, fragility, and fulfillment difficulty |
| Compliance Risk | 1-5 | Legal, platform, or category risk |

### Suggested Formula

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

### Score Interpretation

| Score | Meaning |
|---:|---|
| 12 or higher | Strong candidate for deeper research |
| 8 to 11 | Worth monitoring |
| 4 to 7 | Weak or uncertain opportunity |
| Below 4 | Not recommended without more evidence |

### Important Note

This scoring model is a research framework only.

It is not financial advice, business advice, or a guarantee of sales.

---

## Workflow 4: Competitor Snapshot

### Purpose

Create a lightweight competitor overview for a product idea.

### Input

A product idea or keyword.

### Process

```text
1. Search public marketplace pages.
2. Collect visible product titles, price ranges, review counts, and positioning notes.
3. Summarize common product features.
4. Identify repeated customer complaints.
5. Identify possible differentiation angles.
6. Add risk notes.
```

### Output Fields

| Field | Description |
|---|---|
| keyword | Product keyword |
| platform | Marketplace or source |
| price_range | Visible price range |
| common_features | Repeated features |
| review_signal | Review count or rating signal if public |
| complaint_summary | Common negative feedback |
| differentiation_angle | Possible improvement |
| risk_note | Legal, platform, or sourcing risk |

### Safe Use Rules

Do not:

- Copy product images
- Copy full product descriptions
- Copy reviews word-for-word
- Collect buyer personal data
- Bypass login or anti-bot systems
- Republish marketplace data as if it is your own dataset

---

## Workflow 5: Review Insight Extractor

### Purpose

Analyze public reviews to find product improvement opportunities.

### Input

Public review summaries or publicly visible product feedback.

### AI Task

Extract:

- What users like
- What users dislike
- What users wish existed
- What causes returns or complaints
- What can be improved
- What premium version could offer

### Suggested Prompt Structure

```text
You are an e-commerce product research assistant.

Analyze the following public review signals.

Extract:
1. Positive signals
2. Negative signals
3. Repeated complaints
4. Desired features
5. Packaging or delivery issues
6. Product improvement ideas
7. Possible premium version ideas
8. Risk notes

Rules:
- Summarize patterns instead of copying full reviews.
- Do not include reviewer names or personal details.
- Do not generate fake reviews.
- Do not exaggerate demand.
```

### Output Fields

| Field | Description |
|---|---|
| positive_signals | What customers like |
| negative_signals | What customers dislike |
| repeated_complaints | Common issues |
| desired_features | Requested improvements |
| improvement_ideas | Product improvement opportunities |
| premium_angle | Higher-value positioning |
| risk_note | Product or compliance risk |

---

## Workflow 6: Daily Report Generator

### Purpose

Generate a daily trend intelligence report from scored product ideas.

### Recommended Report Structure

```text
# Daily Trend Intelligence Report

Date:
Region:
Sources Reviewed:

## Top Product Opportunities

### 1. Product Idea
- Category:
- Trend Signal:
- Target Audience:
- Consumer Pain Point:
- Content Angle:
- Opportunity Score:
- Confidence:
- Risk Note:
- Source Links:
- Suggested Next Action:

### 2. Product Idea
...

## Watchlist

Products or categories worth monitoring.

## High-Risk Ideas

Ideas that appear interesting but have major compliance, shipping, IP, or platform risks.

## Notes

Research limitations and next steps.
```

### Delivery Options

The report can be delivered to:

- Google Sheets
- Notion
- Telegram
- Email
- Markdown file
- PDF file
- Newsletter platform

### Human Review

Before publishing:

- Verify source links
- Remove unsupported claims
- Add uncertainty notes
- Check for copyright issues
- Check for personal data
- Check for platform policy risks

---

## Workflow 7: Weekly Deep Report Generator

### Purpose

Create a more detailed weekly market report.

### Recommended Structure

```text
# Weekly Trend Intelligence Report

Week:
Region:
Main Categories Reviewed:

## Executive Summary

Short overview of the strongest signals.

## Top 10 Product Opportunities

Each opportunity includes:
- Product idea
- Category
- Trend reason
- Audience
- Pain point
- Price potential
- Content angle
- Competition note
- Risk note
- Opportunity score
- Source links

## Category Comparison

Compare categories by:
- Demand signal
- Competition
- Shipping difficulty
- Content potential
- Compliance risk

## Consumer Language

Useful phrases, questions, and problems found in public sources.

## Content Ideas

Short video hooks, SEO topics, and ad angles.

## Risk and Compliance Notes

Platform, legal, logistics, and sourcing risks.

## Recommended Next Actions

What to validate next.
```

### Monetization Use Case

A weekly report may be used for:

- Internal research
- Paid newsletter
- Private community
- Consulting deliverable
- E-commerce team report
- Factory product development insight

Do not market it as a guaranteed profit system.

---

## Workflow 8: Alert System

### Purpose

Notify users when a product idea receives a high opportunity score.

### Trigger Examples

Send an alert when:

- Opportunity Score is above 12
- Demand Signal is 5
- Social Visibility is 5
- Compliance Risk is below 2
- A keyword appears repeatedly across multiple sources
- A product appears in both social and marketplace signals

### Example Alert Format

```text
New Trend Alert

Product:
Category:
Region:
Why it matters:
Opportunity Score:
Confidence:
Risk Note:
Source Links:
Suggested Next Action:
```

### Delivery Channels

- Telegram
- Email
- Slack
- Discord
- Notion notification
- Google Sheets status column

---

## Workflow 9: Human-in-the-Loop Review

### Purpose

Prevent unsafe or low-quality automated reports.

### Review Checklist

Before sending a report:

- Are all sources public?
- Are source links included?
- Are claims supported?
- Are there any copied long passages?
- Are there private personal details?
- Are there legal or platform risks?
- Are high-risk categories clearly labeled?
- Are confidence levels included?
- Are next actions practical?
- Is the report free from guaranteed income claims?

### Recommended Status Labels

| Status | Meaning |
|---|---|
| Draft | AI-generated, not reviewed |
| Needs Review | Human review required |
| Approved | Ready to publish |
| Rejected | Unsafe or low-quality |
| Watchlist | Monitor later |

---

## Workflow 10: Report Archive

### Purpose

Store historical reports and trend records.

### Suggested Storage Options

- Google Sheets
- Notion database
- Markdown files in a private repository
- Airtable
- Local database
- Cloud storage

### Suggested Archive Fields

| Field | Description |
|---|---|
| report_date | Date of report |
| region | Target market |
| category | Main category |
| product_idea | Product idea |
| opportunity_score | Score |
| confidence | Low, Medium, High |
| status | Draft, approved, rejected, watchlist |
| report_url | Link to report |
| source_count | Number of sources |
| reviewer_note | Human review comment |

---

## MVP Implementation Plan

A simple first version can use:

| Layer | Tool |
|---|---|
| Scheduler | n8n |
| Public data collection | RSS, Firecrawl, or public pages |
| AI analysis | Dify or OpenAI-compatible API |
| Storage | Google Sheets |
| Report format | Markdown |
| Delivery | Telegram or email |

### MVP Steps

```text
1. Define 5 public sources.
2. Collect 10 to 20 public signals per day.
3. Summarize signals with AI.
4. Extract product ideas.
5. Score each idea.
6. Save results to Google Sheets.
7. Generate a daily Markdown report.
8. Send the report to Telegram or email.
9. Review manually.
10. Improve prompts and scoring rules.
```

---

## Advanced Implementation Plan

A more advanced version can include:

- Multiple region monitoring
- Multi-source signal matching
- Review insight extraction
- Competitor snapshot generation
- Product scoring dashboard
- Weekly PDF generation
- Paid newsletter export
- Human approval workflow
- Risk classification
- Source reliability scoring

### Advanced Flow

```text
1. Collect signals from multiple source categories.
2. Normalize data into a shared schema.
3. Cluster similar product ideas.
4. Compare across sources.
5. Score opportunities.
6. Generate daily alerts.
7. Generate weekly reports.
8. Archive historical data.
9. Track score changes over time.
10. Improve scoring with human feedback.
```

---

## What This Project Should Avoid

TrendPilot AI workflows should not be used for:

- Scraping private personal data
- Buying or selling contact databases
- Automated spam messaging
- Fake reviews
- Fake engagement
- Account farming
- Platform restriction bypass
- Copyright content copying
- Misleading income claims
- Unverified financial claims
- High-risk regulated product promotion

---

## Final Note

Trend intelligence is not about collecting the most data.

It is about collecting the right public signals, analyzing them responsibly, and turning them into useful research outputs.

TrendPilot AI should help users build better research systems, not unsafe automation systems.
