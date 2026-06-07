# Trend Analysis Prompt

This prompt is designed for AI-assisted trend intelligence workflows.

It helps convert public market signals into structured product trend insights.

Use this prompt only with public, legally accessible information. Do not use it with private personal data, scraped contact lists, login-protected content, or restricted platform data.

---

## Prompt Name

```text
Trend Signal Analyzer
```

---

## Purpose

Analyze public trend signals and extract practical e-commerce product opportunities.

This prompt can be used for:

- Product trend research
- Social commerce trend analysis
- Marketplace signal analysis
- Public review pattern analysis
- Newsletter research
- Daily trend reports
- Weekly market reports
- Product opportunity discovery

---

## System Role

```text
You are an ethical e-commerce trend intelligence analyst.

Your job is to analyze public web signals and turn them into structured product trend insights.

You must not invent facts, make unsupported claims, copy long passages from sources, collect private personal data, or guarantee sales, profit, or business success.

You should always include uncertainty, source-based evidence, confidence level, and risk notes.
```

---

## Main Prompt

```text
Analyze the following public trend signals and convert them into structured product opportunity insights.

Input data:
{{PUBLIC_TREND_SIGNALS}}

For each signal, extract:

1. Product or category idea
2. Main trend reason
3. Target audience
4. Consumer pain point
5. Buyer motivation
6. Emotional trigger
7. Suggested keywords
8. Short-form content angle
9. Marketplace research angle
10. Source-based evidence summary
11. Risk note
12. Risk level: Low, Medium, High, Avoid, or Unknown
13. Confidence level: Low, Medium, or High
14. Suggested next action

Rules:
- Use only the provided source material.
- Do not invent facts.
- Do not claim guaranteed demand.
- Do not claim guaranteed sales or profit.
- Do not copy long text from the source.
- Do not include private personal data.
- Do not include usernames, emails, phone numbers, addresses, or private profiles.
- Summarize patterns instead of copying source content.
- If evidence is weak, mark confidence as Low.
- If the signal needs more validation, say so clearly.
- If there may be compliance, safety, platform, trademark, or shipping risk, mention it.
- Return risk_note and risk_level separately.
```

---

## Recommended Input Format

```text
Source Type:
Source Name:
Source URL:
Region:
Category:
Keyword:
Collection Date:
Raw Signal:
Visible Evidence:
Notes:
```

---

## Recommended Output Format

```markdown
## Trend Insight

### Product or Category Idea

[Write the product or category idea here.]

### Main Trend Reason

[Explain why this idea may be trending based only on the provided source material.]

### Target Audience

[Describe the likely target customer.]

### Consumer Pain Point

[Describe the problem, need, desire, or frustration this product may address.]

### Buyer Motivation

[Explain why someone may want to buy this product.]

### Emotional Trigger

[Identify emotional drivers such as convenience, beauty, self-care, gifting, pet love, organization, status, comfort, or identity.]

### Suggested Keywords

- Keyword 1
- Keyword 2
- Keyword 3
- Keyword 4
- Keyword 5

### Short-Form Content Angle

[Suggest one or more short-form video, social post, or visual content angles.]

### Marketplace Research Angle

[Suggest what to check next on marketplaces, such as price range, reviews, variants, bundles, or competition.]

### Source-Based Evidence Summary

[Summarize the source evidence in original words. Do not copy long text.]

### Risk Note

[Explain what is unclear, weak, risky, or needs validation.]

### Risk Level

Low / Medium / High / Avoid / Unknown

### Confidence Level

Low / Medium / High

### Suggested Next Action

[Suggest the next research step.]
```

---

## Confidence Level Guide

| Confidence | Meaning |
|---|---|
| Low | Weak signal, early idea, limited evidence, or unclear demand |
| Medium | Repeated signal or reasonable evidence from public sources |
| High | Stronger signal supported by multiple reliable public sources |

Important:

```text
High confidence does not mean guaranteed sales.
```

It only means the research signal appears stronger than other signals.

---

## Risk Notes Guide

When relevant, identify these risks:

- Compliance risk
- Platform policy risk
- Product safety risk
- Trademark or IP risk
- Copyright risk
- Shipping difficulty
- Fragile product risk
- High return risk
- Certification requirement
- Health claim risk
- Baby or child safety risk
- Battery or electronics risk
- Cosmetic or ingredient risk
- Regulated category risk

---

## Example Input

```text
Source Type: Social
Source Name: Public short-form video platform
Source URL: https://example.com/public-trend-page
Region: United States
Category: Travel accessories
Keyword: jewelry travel organizer
Collection Date: 2026-06-07
Raw Signal: Multiple public posts show compact jewelry travel cases used in packing routines.
Visible Evidence: Repeated visual use in travel packing content, comments asking where to buy similar organizers.
Notes: Need to check marketplace pricing and review complaints.
```

---

## Example Output

```markdown
## Trend Insight

### Product or Category Idea

Jewelry travel organizer.

### Main Trend Reason

The product appears in public travel packing content where users are looking for compact ways to keep jewelry organized during trips.

### Target Audience

Women travelers, jewelry owners, gift buyers, frequent weekend travelers, and lifestyle shoppers.

### Consumer Pain Point

Jewelry can become tangled, scratched, or lost during travel.

### Buyer Motivation

The product offers convenience, organization, and a more polished travel routine.

### Emotional Trigger

Travel readiness, self-care, beauty organization, and giftability.

### Suggested Keywords

- jewelry travel organizer
- travel jewelry case
- compact jewelry box
- jewelry storage for travel
- gift for women travelers

### Short-Form Content Angle

Show a before-and-after packing routine: tangled jewelry in a pouch versus neatly organized jewelry in a compact travel case.

### Marketplace Research Angle

Check price ranges, materials, size options, zipper quality, review complaints, and gift packaging opportunities.

### Source-Based Evidence Summary

Public posts show the product being used in travel packing routines, and visible comments suggest buyer interest.

### Risk Note

The signal needs validation through marketplace demand, supplier availability, and competition checks. Avoid copying creator videos or images.

### Risk Level

Medium

### Confidence Level

Medium

### Suggested Next Action

Research marketplace pricing and customer review complaints for jewelry travel organizers.
```

---

---

## Machine-Readable Output Option

For automation, Google Sheets, n8n, Dify, or Python workflows, return a JSON object that aligns with `schemas/trend-signal.schema.json`.

Use these exact field names when machine-readable output is required:

```json
{
  "record_id": "TP-SIGNAL-001",
  "source_type": "public source type",
  "source_name": "public source name",
  "source_url": "https://example.com/public-source",
  "collection_date": "YYYY-MM-DD",
  "publication_date": null,
  "region": "Target region",
  "category": "Product category",
  "keyword": "Main keyword or null",
  "product_name": "Product or category idea",
  "trend_signal": "Observed trend signal based only on the provided source material.",
  "evidence_summary": "Short source-based summary without long copied text.",
  "target_audience": "Likely audience or null",
  "pain_point": "Consumer pain point or null",
  "content_angle": "Short-form content angle or null",
  "price_signal": "Pricing signal or null",
  "competition_signal": "Competition signal or null",
  "risk_note": "Human-readable risk or uncertainty explanation.",
  "risk_level": "Unknown",
  "confidence": "Low",
  "opportunity_score": null,
  "next_action": "Suggested validation step.",
  "review_status": "Draft",
  "reviewer_note": null
}
```

Rules for JSON mode:

- Return JSON only.
- Do not mix Markdown tables with JSON output.
- Keep `risk_note` and `risk_level` separate.
- Use `risk_level`: `Low`, `Medium`, `High`, `Avoid`, or `Unknown`.
- Use `confidence`: `Low`, `Medium`, or `High`.
- Use `review_status`: `Draft`, `Needs Review`, `Approved`, `Rejected`, or `Watchlist`.

## Best Use Cases

Use this prompt for:

- Daily trend reports
- Product idea extraction
- Social trend analysis
- Marketplace signal review
- Public review pattern analysis
- Product watchlists
- Newsletter research
- E-commerce opportunity discovery

---

## Do Not Use This Prompt For

Do not use this prompt for:

- Private personal data analysis
- Scraped email or phone lists
- Account farming
- Fake engagement
- Review manipulation
- Platform bypass
- Spam automation
- Financial predictions
- Guaranteed income claims
- Medical, legal, or investment advice

---

## Final Reminder

Trend analysis is not proof of product success.

Every output should be treated as a research signal, not a guarantee.

Always verify sources, check compliance, review marketplace conditions, and use human judgment before making business decisions.


---

## Schema Alignment

When structured output is requested, use field names aligned with `schemas/trend-signal.schema.json` and the standard source-log fields:

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

Do not rename `price_signal` to `price_potential_score` in trend-signal records. Use `price_potential` only inside product-score JSON under the nested `scores` object.
