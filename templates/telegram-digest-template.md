# Telegram Digest Template

This template is designed for short daily or weekly trend intelligence digests delivered through Telegram, Slack, Discord, email, or internal chat channels.

It is suitable for AI-assisted e-commerce trend monitoring, product research alerts, opportunity scoring summaries, and internal team notifications.

This digest should be based on public, legally accessible sources only.

It does not guarantee product demand, sales, profit, or business success.

---

# Telegram Trend Digest

## Standard Fields

TrendPilot AI digest messages should use the same standard fields as the source log and workflows.

```text
product_name
category
region
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
source_url
```

Important:

```text
risk_note = human-readable explanation of the risk
risk_level = standardized risk category: Low / Medium / High / Avoid / Unknown
```

---

## Short Version

```text
🚀 TrendPilot AI Daily Digest

Date: {{DATE}}
Region: {{REGION}}
Category: {{CATEGORY}}

Top Opportunities Today:

1. {{PRODUCT_IDEA_1}}
Score: {{OPPORTUNITY_SCORE_1}}
Confidence: {{CONFIDENCE_1}}
Risk Level: {{RISK_LEVEL_1}}
Risk Note: {{RISK_NOTE_1}}
Why it matters: {{SHORT_REASON_1}}
Next action: {{NEXT_ACTION_1}}

2. {{PRODUCT_IDEA_2}}
Score: {{OPPORTUNITY_SCORE_2}}
Confidence: {{CONFIDENCE_2}}
Risk Level: {{RISK_LEVEL_2}}
Risk Note: {{RISK_NOTE_2}}
Why it matters: {{SHORT_REASON_2}}
Next action: {{NEXT_ACTION_2}}

3. {{PRODUCT_IDEA_3}}
Score: {{OPPORTUNITY_SCORE_3}}
Confidence: {{CONFIDENCE_3}}
Risk Level: {{RISK_LEVEL_3}}
Risk Note: {{RISK_NOTE_3}}
Why it matters: {{SHORT_REASON_3}}
Next action: {{NEXT_ACTION_3}}

Watchlist:
- {{WATCHLIST_ITEM_1}}
- {{WATCHLIST_ITEM_2}}

Important:
This digest is for research only. It does not guarantee sales, profit, or product success.
```

---

## Detailed Version

```text
🚀 TrendPilot AI Trend Intelligence Digest

Date: {{DATE}}
Region: {{REGION}}
Main Category: {{CATEGORY}}
Sources Reviewed: {{SOURCE_COUNT}}
Review Status: {{REVIEW_STATUS}}

━━━━━━━━━━━━━━━━━━━━

🔥 Top Product Opportunities

1. {{PRODUCT_IDEA_1}}

Category:
{{CATEGORY_1}}

Target Audience:
{{TARGET_AUDIENCE_1}}

Trend Signal:
{{TREND_SIGNAL_1}}

Why it may matter:
{{TREND_REASON_1}}

Opportunity Score:
{{OPPORTUNITY_SCORE_1}}

Confidence:
{{CONFIDENCE_1}}

Risk Level:
{{RISK_LEVEL_1}}

Risk Note:
{{RISK_NOTE_1}}

Suggested Next Action:
{{NEXT_ACTION_1}}

Source:
{{SOURCE_LINK_1}}

━━━━━━━━━━━━━━━━━━━━

2. {{PRODUCT_IDEA_2}}

Category:
{{CATEGORY_2}}

Target Audience:
{{TARGET_AUDIENCE_2}}

Trend Signal:
{{TREND_SIGNAL_2}}

Why it may matter:
{{TREND_REASON_2}}

Opportunity Score:
{{OPPORTUNITY_SCORE_2}}

Confidence:
{{CONFIDENCE_2}}

Risk Level:
{{RISK_LEVEL_2}}

Risk Note:
{{RISK_NOTE_2}}

Suggested Next Action:
{{NEXT_ACTION_2}}

Source:
{{SOURCE_LINK_2}}

━━━━━━━━━━━━━━━━━━━━

3. {{PRODUCT_IDEA_3}}

Category:
{{CATEGORY_3}}

Target Audience:
{{TARGET_AUDIENCE_3}}

Trend Signal:
{{TREND_SIGNAL_3}}

Why it may matter:
{{TREND_REASON_3}}

Opportunity Score:
{{OPPORTUNITY_SCORE_3}}

Confidence:
{{CONFIDENCE_3}}

Risk Level:
{{RISK_LEVEL_3}}

Risk Note:
{{RISK_NOTE_3}}

Suggested Next Action:
{{NEXT_ACTION_3}}

Source:
{{SOURCE_LINK_3}}

━━━━━━━━━━━━━━━━━━━━

👀 Watchlist

- {{WATCHLIST_ITEM_1}}
Reason: {{WATCHLIST_REASON_1}}
Confidence: {{WATCHLIST_CONFIDENCE_1}}
Risk Level: {{WATCHLIST_RISK_LEVEL_1}}

- {{WATCHLIST_ITEM_2}}
Reason: {{WATCHLIST_REASON_2}}
Confidence: {{WATCHLIST_CONFIDENCE_2}}
Risk Level: {{WATCHLIST_RISK_LEVEL_2}}

- {{WATCHLIST_ITEM_3}}
Reason: {{WATCHLIST_REASON_3}}
Confidence: {{WATCHLIST_CONFIDENCE_3}}
Risk Level: {{WATCHLIST_RISK_LEVEL_3}}

━━━━━━━━━━━━━━━━━━━━

⚠️ High-Risk Ideas

These items should not be treated as recommended opportunities without deeper review.

- {{HIGH_RISK_ITEM_1}}
Risk Level: {{HIGH_RISK_LEVEL_1}}
Risk Note: {{HIGH_RISK_REASON_1}}

- {{HIGH_RISK_ITEM_2}}
Risk Level: {{HIGH_RISK_LEVEL_2}}
Risk Note: {{HIGH_RISK_REASON_2}}

━━━━━━━━━━━━━━━━━━━━

✅ Recommended Next Steps

1. {{ACTION_1}}
2. {{ACTION_2}}
3. {{ACTION_3}}

━━━━━━━━━━━━━━━━━━━━

Disclaimer:
This digest is based on public web signals and AI-assisted analysis. It is for research and informational purposes only. It does not guarantee product demand, sales, profit, or business success.
```

---

## Alert Version

Use this format when a product idea reaches a high opportunity score.

Only use this for records that have been reviewed and do not carry High, Avoid, or Unknown risk levels.

```text
🚨 New Trend Alert

Product:
{{PRODUCT_IDEA}}

Category:
{{CATEGORY}}

Region:
{{REGION}}

Opportunity Score:
{{OPPORTUNITY_SCORE}}

Confidence:
{{CONFIDENCE_LEVEL}}

Risk Level:
{{RISK_LEVEL}}

Risk Note:
{{RISK_NOTE}}

Why it matters:
{{TREND_REASON}}

Target Audience:
{{TARGET_AUDIENCE}}

Consumer Pain Point:
{{PAIN_POINT}}

Suggested Content Angle:
{{CONTENT_ANGLE}}

Suggested Next Action:
{{NEXT_ACTION}}

Source:
{{SOURCE_LINK}}

Note:
This is a research signal, not a guarantee of demand or sales.
```

---

## Weekly Summary Version

```text
📊 TrendPilot AI Weekly Brief

Week:
{{WEEK}}

Region:
{{REGION}}

Main Categories Reviewed:
{{CATEGORIES_REVIEWED}}

Top 5 Opportunities:

1. {{PRODUCT_1}} — Score: {{SCORE_1}} — Confidence: {{CONFIDENCE_1}} — Risk Level: {{RISK_LEVEL_1}}
2. {{PRODUCT_2}} — Score: {{SCORE_2}} — Confidence: {{CONFIDENCE_2}} — Risk Level: {{RISK_LEVEL_2}}
3. {{PRODUCT_3}} — Score: {{SCORE_3}} — Confidence: {{CONFIDENCE_3}} — Risk Level: {{RISK_LEVEL_3}}
4. {{PRODUCT_4}} — Score: {{SCORE_4}} — Confidence: {{CONFIDENCE_4}} — Risk Level: {{RISK_LEVEL_4}}
5. {{PRODUCT_5}} — Score: {{SCORE_5}} — Confidence: {{CONFIDENCE_5}} — Risk Level: {{RISK_LEVEL_5}}

Strongest Category:
{{STRONGEST_CATEGORY}}

Main Consumer Theme:
{{MAIN_CONSUMER_THEME}}

Main Risk This Week:
{{MAIN_RISK}}

Recommended Next Action:
{{RECOMMENDED_ACTION}}

Disclaimer:
For research and informational purposes only. No sales or profit guaranteed.
```

---

## Field Reference

| Field | Meaning |
|---|---|
| DATE | Report date |
| REGION | Target country or market |
| CATEGORY | Product category |
| PRODUCT_IDEA | Product or category idea |
| OPPORTUNITY_SCORE | Product opportunity score |
| CONFIDENCE | Low, Medium, or High |
| RISK_LEVEL | Low, Medium, High, Avoid, or Unknown |
| RISK_NOTE | Human-readable explanation of the risk |
| TREND_SIGNAL | Public signal summary |
| TREND_REASON | Why the idea may be worth watching |
| TARGET_AUDIENCE | Likely buyer group |
| PAIN_POINT | Consumer problem |
| CONTENT_ANGLE | Suggested content idea |
| NEXT_ACTION | Suggested next research step |
| SOURCE_LINK | Public source URL |
| REVIEW_STATUS | Draft, Needs Review, Approved, Rejected, or Watchlist |

---

## Risk Level Rules

For public or paid digest delivery:

| Risk Level | Suggested Use |
|---|---|
| Low | Can be included after review |
| Medium | Can be included after review, with risk note |
| High | Do not include as a top opportunity |
| Avoid | Exclude from digest |
| Unknown | Mark as Needs Review before use |

Recommended filter for top opportunities:

```text
review_status = Approved
confidence = Medium or High
risk_level = Low or Medium
```

Avoid using these records in public or paid digest sections:

```text
review_status = Draft
review_status = Needs Review
review_status = Rejected
risk_level = High
risk_level = Avoid
risk_level = Unknown
```

---

## Writing Guidelines

A good Telegram digest should be:

- Short
- Clear
- Source-aware
- Risk-aware
- Easy to scan
- Free from hype
- Free from guaranteed income claims
- Useful for next actions

Avoid:

- Long paragraphs
- Unsupported statistics
- Private data
- Copied source text
- Clickbait
- Fake urgency
- Guaranteed sales claims
- “Auto money” language
- Hiding risk level
- Removing disclaimers

---

## Recommended Disclaimer

```text
This digest is based on public web signals and AI-assisted analysis. It is intended for research and informational purposes only. It does not guarantee product demand, sales, profit, or business success. Users should verify all sources and conduct their own due diligence before making business decisions.
```

---

## Safe Use Rules

Use this template for:

- Internal team alerts
- Opt-in Telegram channels
- Paid research communities
- Newsletter previews
- Product opportunity alerts
- Trend monitoring summaries

Do not use this template for:

- Spam messages
- Mass unsolicited DMs
- Fake urgency marketing
- Misleading income claims
- Private data distribution
- Scraped contact list outreach
- Platform abuse
- High-risk product promotion without review

---

## Human Review Checklist

Before sending a digest, confirm:

- [ ] Records are from public sources
- [ ] Source links or source references are available
- [ ] Review status is Approved
- [ ] Confidence level is included
- [ ] Risk level is included
- [ ] Risk note is included
- [ ] High / Avoid / Unknown risk records are excluded from top opportunities
- [ ] No private personal data is included
- [ ] No guaranteed sales or profit claims are included
- [ ] Disclaimer is included
