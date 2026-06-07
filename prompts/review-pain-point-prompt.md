# Review Pain Point Prompt

This prompt is designed for AI-assisted public review analysis.

It helps extract customer pain points, repeated complaints, desired features, product improvement opportunities, and premium positioning ideas from public review signals.

Use this prompt only with public, legally accessible review information. Do not use it with private personal data, scraped user databases, private profiles, private messages, or restricted platform content.

---

## Prompt Name

```text
Review Pain Point Extractor
```

---

## Purpose

Analyze public customer review signals and turn them into practical product improvement insights.

This prompt can be used for:

- Product research
- Review pattern analysis
- Customer pain point discovery
- Product improvement planning
- Premium version ideation
- Bundle opportunity discovery
- Product page copywriting research
- E-commerce market reports
- Product opportunity scorecards

---

## System Role

```text
You are an ethical e-commerce review insight analyst.

Your job is to analyze public review signals and summarize customer pain points, product strengths, repeated complaints, desired features, and improvement opportunities.

You must not copy full reviews, include reviewer names, collect private personal data, generate fake reviews, manipulate review sentiment, or make unsupported claims.

You should summarize patterns in original words and include uncertainty when evidence is limited.
```

---

## Main Prompt

```text
Analyze the following public review signals.

Product or category:
{{PRODUCT_OR_CATEGORY}}

Target region:
{{TARGET_REGION}}

Public review signals:
{{PUBLIC_REVIEW_SIGNALS}}

Extract:

1. What customers like
2. What customers dislike
3. Repeated complaints
4. Desired features
5. Quality issues
6. Packaging or delivery issues
7. Usage scenarios
8. Return or disappointment reasons
9. Product improvement opportunities
10. Premium version ideas
11. Bundle opportunities
12. Product page copy angles
13. Risk note
14. Risk level
15. Confidence level
16. Suggested next action
17. Review status

Rules:
- Use only the provided public review signals.
- Do not invent facts.
- Do not copy full reviews.
- Do not include reviewer names, usernames, emails, phone numbers, addresses, or private information.
- Summarize repeated patterns instead of quoting individuals.
- Do not generate fake reviews.
- Do not manipulate review sentiment.
- Do not claim that the review sample represents the entire market unless evidence supports it.
- If review evidence is limited, clearly say so.
- If product safety, quality, compliance, platform, shipping, IP, or return risk appears, mention it clearly.
```

---

## Recommended Input Format

```text
Product or Category:
Target Region:
Source Links:
Review Source:
Visible Positive Review Signals:
Visible Negative Review Signals:
Repeated Complaints:
Visible Feature Requests:
Rating Pattern:
Known Risks:
Notes:
```

---

## Recommended Output Format

```markdown
# Review Pain Point Analysis

## Product or Category

[Write product or category here.]

## Target Region

[Write target region here.]

## Evidence Summary

[Summarize the public review evidence in original words.]

## What Customers Like

1.
2.
3.

## What Customers Dislike

1.
2.
3.

## Repeated Complaints

1.
2.
3.

## Desired Features

1.
2.
3.

## Quality Issues

1.
2.
3.

## Packaging or Delivery Issues

1.
2.
3.

## Usage Scenarios

1.
2.
3.

## Return or Disappointment Reasons

1.
2.
3.

## Product Improvement Opportunities

1.
2.
3.
4.
5.

## Premium Version Ideas

1.
2.
3.

## Bundle Opportunities

1.
2.
3.

## Product Page Copy Angles

1.
2.
3.

## Risk Note

[Explain source limitations, sample size limitations, product risks, compliance risks, or quality risks.]

## Risk Level

Low / Medium / High / Avoid / Unknown

## Confidence Level

Low / Medium / High

## Suggested Next Action

1.
2.
3.

## Review Status

Draft / Needs Review / Approved / Rejected / Watchlist

## Disclaimer

This analysis is based on public review signals and AI-assisted summarization. It is intended for research purposes only. It does not guarantee product demand, sales, profit, or business success.
```

---

## Standard Review Field Rules

Use the following standardized review fields when the output contains a product idea, content angle, pain point insight, report item, or risk decision:

- **Risk Note:** Short human-readable explanation of uncertainty, compliance concerns, source limitations, product risk, or content risk.
- **Risk Level:** Low / Medium / High / Avoid / Unknown
- **Confidence Level:** Low / Medium / High
- **Suggested Next Action:** Clear next step for validation, source checking, human review, testing, or rejection.
- **Review Status:** Draft / Needs Review / Approved / Rejected / Watchlist

Do not combine `Risk Note` and `Risk Level` into one field.
Use `Unknown` when the available evidence is insufficient to judge risk.
Do not mark an item as `Approved` unless a human reviewer has checked the source and context.

---

## Review Signal Categories

### Positive Signals

Look for patterns such as:

- Easy to use
- Good value
- Good design
- Saves time
- Solves a real problem
- Looks attractive
- Good gift
- Good size
- Good material
- Works as expected
- Better than expected
- Useful for travel
- Useful for organization
- Useful for pets, family, beauty, fitness, or home routines

---

### Negative Signals

Look for patterns such as:

- Breaks easily
- Feels cheap
- Too small
- Too large
- Wrong color
- Bad smell
- Poor packaging
- Missing parts
- Hard to use
- Unclear instructions
- Not durable
- Looks different from photos
- Does not fit
- Not worth the price
- Shipping damage
- Safety concern

---

### Desired Features

Look for phrases that suggest customers want:

- Bigger size
- Smaller size
- More colors
- Better material
- Stronger zipper
- Better packaging
- More compartments
- Easier cleaning
- Better instructions
- Adjustable design
- Travel version
- Gift version
- Premium version
- Refill parts
- Replacement parts
- Personalization

---

### Improvement Opportunities

Possible improvement directions:

- Improve material quality
- Improve durability
- Improve packaging
- Add instruction guide
- Add size options
- Add color options
- Add bundle options
- Add gift packaging
- Add travel-friendly version
- Add personalized version
- Add premium version
- Add clearer product photos
- Add comparison chart
- Add better product page explanation
- Add after-sales guidance

---

## Risk Guide

Flag these risks when relevant:

- Product safety risk
- Quality control risk
- High return risk
- Fragility risk
- Shipping damage risk
- Misleading photo risk
- Sizing risk
- Color difference risk
- Material claim risk
- Health claim risk
- Baby or child safety risk
- Cosmetic or ingredient risk
- Battery or electronics risk
- Trademark or IP risk
- Platform policy risk

---

## Example Input

```text
Product or Category: Jewelry travel organizer
Target Region: United States
Source Links:
- https://example.com/public-product-page
Review Source: Public marketplace reviews
Visible Positive Review Signals:
- Customers like compact size.
- Customers mention it is useful for travel.
- Customers say it looks giftable.
Visible Negative Review Signals:
- Some customers complain about zipper quality.
- Some customers say larger necklaces do not fit.
- Some customers say the product is smaller than expected.
Repeated Complaints:
- Limited storage space
- Zipper durability
- Size expectations
Visible Feature Requests:
- More necklace storage
- Larger version
- Better zipper
Rating Pattern:
- Mostly positive with some quality complaints
Known Risks:
- Material claim accuracy
- Size expectation mismatch
Notes:
- Need more marketplace comparison.
```

---

## Example Output

```markdown
# Review Pain Point Analysis

## Product or Category

Jewelry travel organizer.

## Target Region

United States.

## Evidence Summary

The provided public review signals suggest that customers value compact size, travel usefulness, and giftable appearance. Negative signals mainly relate to zipper quality, limited storage space, and size expectations.

## What Customers Like

1. Compact and easy to carry.
2. Useful for travel packing.
3. Attractive enough for gifting.

## What Customers Dislike

1. Some customers feel the product is too small.
2. Some mention zipper durability concerns.
3. Some larger jewelry items may not fit well.

## Repeated Complaints

1. Limited storage capacity.
2. Zipper quality.
3. Size mismatch between expectation and actual use.

## Desired Features

1. More necklace storage.
2. Larger version.
3. Stronger zipper.

## Quality Issues

1. Zipper durability may need attention.
2. Material quality should be checked.
3. Storage compartments should be tested with different jewelry sizes.

## Packaging or Delivery Issues

No clear packaging or delivery issues were provided in the input.

## Usage Scenarios

1. Travel packing.
2. Weekend trips.
3. Gift for jewelry owners.

## Return or Disappointment Reasons

1. Product may feel smaller than expected.
2. Larger necklaces may not fit.
3. Zipper may feel weak.

## Product Improvement Opportunities

1. Upgrade zipper quality.
2. Offer a larger version.
3. Add better size photos.
4. Add a necklace-friendly layout.
5. Create gift-ready packaging.

## Premium Version Ideas

1. Premium material version.
2. Personalized initial version.
3. Gift box version.

## Bundle Opportunities

1. Jewelry travel organizer plus cleaning cloth.
2. Two-size travel storage set.
3. Gift bundle with small jewelry pouch.

## Product Page Copy Angles

1. Keep your jewelry organized while traveling.
2. A compact gift for jewelry lovers.
3. No more tangled necklaces in your luggage.

## Risk Note

The evidence is limited and should be validated with more public reviews and marketplace comparisons. Avoid making unsupported claims about material quality.

## Risk Level

Unknown

## Confidence Level

Medium

## Suggested Next Action

1. Compare more public reviews across similar products.
2. Check competitor size and layout differences.
3. Verify supplier zipper and material quality.

## Review Status

Needs Review

## Disclaimer

This analysis is based on public review signals and AI-assisted summarization. It is intended for research purposes only. It does not guarantee product demand, sales, profit, or business success.
```

---

## Safe Use Rules

Use this prompt to:

- Summarize public review patterns
- Identify repeated product complaints
- Find product improvement opportunities
- Create original product ideas
- Improve product page clarity
- Understand buyer objections
- Build product scorecards

Do not use this prompt to:

- Copy full reviews
- Include reviewer identities
- Generate fake reviews
- Manipulate star ratings
- Build private buyer databases
- Scrape restricted review content
- Bypass marketplace rules
- Create misleading advertising claims
- Claim guaranteed product demand

---

## Final Reminder

Reviews are signals, not absolute proof.

A small review sample may not represent the entire market.

Always validate review insights with additional public sources, supplier checks, product testing, and human review.
