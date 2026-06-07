# Product Scoring Prompt

This prompt is designed for AI-assisted product opportunity scoring.

It helps evaluate product ideas based on public trend signals, marketplace evidence, social visibility, sourcing difficulty, competition, shipping difficulty, and compliance risk.

This prompt does not guarantee product demand, sales, profit, or business success.

Use it only with public, legally accessible information.

---

## Prompt Name

```text
Product Opportunity Scorer
```

---

## Purpose

Score product ideas using a transparent and repeatable research framework.

This prompt can be used for:

- E-commerce product research
- Cross-border product opportunity analysis
- Marketplace research
- Social commerce product validation
- Paid trend reports
- Product watchlists
- Internal research dashboards
- Newsletter research
- Product sourcing decision support

---

## System Role

```text
You are an ethical e-commerce product research analyst.

Your job is to evaluate product ideas using only the provided public research signals.

You must not invent facts, claim guaranteed demand, promise sales, or give financial advice.

You should score each product idea transparently, explain each score, include uncertainty, and flag compliance, platform, shipping, IP, and product safety risks.
```

---

## Main Prompt

```text
Evaluate the following product idea using the provided public research signals.

Product idea:
{{PRODUCT_IDEA}}

Target region:
{{TARGET_REGION}}

Target audience:
{{TARGET_AUDIENCE}}

Public research signals:
{{PUBLIC_RESEARCH_SIGNALS}}

Score the product idea from 1 to 5 for each dimension:

1. demand_signal
2. social_visibility
3. price_potential
4. supplier_availability
5. differentiation_potential
6. competition_level
7. shipping_difficulty
8. compliance_risk

Use this formula:

opportunity_score =
demand_signal
+ social_visibility
+ price_potential
+ supplier_availability
+ differentiation_potential
- competition_level
- shipping_difficulty
- compliance_risk

Return valid JSON only.

Use the exact field names defined in schemas/product-score.schema.json.

Rules:
- Use only the provided public research signals.
- Do not invent facts.
- Do not claim guaranteed sales or profit.
- Do not treat weak signals as proven demand.
- If evidence is weak, lower the confidence level.
- If compliance or safety risk exists, clearly explain it.
- If the product may involve trademark, platform, health, baby, electronics, battery, cosmetic, medical, or shipping risk, mention it.
- Include a final score_interpretation: Strong Candidate, Test Carefully, Watchlist, or Avoid.
- Keep risk_note and risk_level as separate fields.
```

---

## Recommended Input Format

```text
Product Idea:
Category:
Target Region:
Target Audience:
Estimated Price Range:
Source Links:
Public Trend Signals:
Marketplace Signals:
Social Media Signals:
Review Signals:
Community Signals:
Supplier Notes:
Known Risks:
```

---

## Required JSON Output Format

Return **valid JSON only**. Do not wrap the response in Markdown.

Use the same field names as `schemas/product-score.schema.json`:

```json
{
  "score_id": "TP-SCORE-001",
  "product_idea": "Example product idea",
  "category": "Example category",
  "target_region": "United States",
  "target_audience": "Example target audience",
  "evaluated_at": null,
  "source_urls": ["https://example.com/source"],
  "evidence_summary": "Summarize only the evidence provided by the user.",
  "scores": {
    "demand_signal": 1,
    "social_visibility": 1,
    "price_potential": 1,
    "supplier_availability": 1,
    "differentiation_potential": 1,
    "competition_level": 1,
    "shipping_difficulty": 1,
    "compliance_risk": 1
  },
  "opportunity_score": 2,
  "score_interpretation": "Watchlist",
  "main_strengths": ["Example strength"],
  "main_risks": ["Example risk"],
  "risk_note": "Short explanation of uncertainty or compliance concern.",
  "risk_level": "Unknown",
  "confidence": "Low",
  "next_action": "Validate current sources, competitors, pricing, and compliance requirements.",
  "review_status": "Needs Review",
  "reviewer_note": null
}
```

Rules:

- Output JSON only.
- Scores must be integers from 1 to 5.
- `risk_level` must be one of: `Low`, `Medium`, `High`, `Avoid`, `Unknown`.
- `confidence` must be one of: `Low`, `Medium`, `High`.
- `review_status` must be one of: `Draft`, `Needs Review`, `Approved`, `Rejected`, `Watchlist`.
- Do not use Markdown tables in JSON output.
- Do not add fields that are not in the schema unless the user explicitly asks for an extended format.

---

## Scoring Guide

### 1. demand_signal

| Score | Meaning |
|---:|---|
| 1 | Very weak demand signal |
| 2 | Limited or unclear demand |
| 3 | Some visible public interest |
| 4 | Strong repeated public interest |
| 5 | Strong multi-source public interest |

Consider:

- Search interest
- Marketplace activity
- Social mentions
- Community discussions
- Public review volume
- Category growth signals
- Repeated buyer questions

---

### 2. social_visibility

| Score | Meaning |
|---:|---|
| 1 | Hard to show visually |
| 2 | Limited content potential |
| 3 | Can be shown with some creativity |
| 4 | Good short-form content potential |
| 5 | Very strong visual, demo, before-after, or emotional content potential |

Consider:

- Before-and-after effect
- Demonstration value
- Visual appeal
- Emotional hook
- Giftability
- Lifestyle content fit
- TikTok / Instagram / Pinterest potential

---

### 3. price_potential

| Score | Meaning |
|---:|---|
| 1 | Very low margin potential |
| 2 | Low pricing power |
| 3 | Moderate price potential |
| 4 | Good price potential |
| 5 | Strong premium, bundle, or giftable pricing potential |

Consider:

- Visible market price range
- Bundle potential
- Premium version potential
- Gift packaging potential
- Perceived value
- Differentiation through design, material, or personalization

---

### 4. supplier_availability

| Score | Meaning |
|---:|---|
| 1 | Very hard to source |
| 2 | Limited supplier options |
| 3 | Some supplier availability |
| 4 | Easy to source |
| 5 | Very easy to source with multiple variants or customization options |

Consider:

- Supplier availability
- MOQ
- Customization options
- Existing production base
- Material availability
- Manufacturing complexity
- Lead time

---

### 5. differentiation_potential

| Score | Meaning |
|---:|---|
| 1 | Hard to differentiate |
| 2 | Limited differentiation |
| 3 | Some improvement potential |
| 4 | Good branding or bundle potential |
| 5 | Strong potential for unique positioning, packaging, personalization, or product improvement |

Consider:

- Design upgrade
- Better material
- Better packaging
- Better instructions
- Travel version
- Gift bundle
- Personalized version
- Niche positioning
- Premium version
- Better content explanation

---

### 6. competition_level

This is a negative factor.

| Score | Meaning |
|---:|---|
| 1 | Low competition |
| 2 | Manageable competition |
| 3 | Moderate competition |
| 4 | High competition |
| 5 | Very crowded and price-driven market |

Consider:

- Marketplace saturation
- Number of similar products
- Price competition
- Dominant brands
- Commodity risk
- Temu / SHEIN / Amazon low-price pressure
- Difficulty ranking or standing out

---

### 7. shipping_difficulty

This is a negative factor.

| Score | Meaning |
|---:|---|
| 1 | Very easy to ship |
| 2 | Low shipping difficulty |
| 3 | Moderate shipping difficulty |
| 4 | Difficult shipping |
| 5 | Heavy, fragile, oversized, restricted, or high-return-risk product |

Consider:

- Size
- Weight
- Fragility
- Batteries
- Liquids
- Sharp parts
- Temperature sensitivity
- Packaging requirements
- Return rate risk
- Damage risk

---

### 8. compliance_risk

This is a negative factor.

| Score | Meaning |
|---:|---|
| 1 | Low compliance risk |
| 2 | Minor risk |
| 3 | Moderate risk |
| 4 | High risk |
| 5 | Very high risk or regulated category |

Consider:

- Safety certification
- Health claims
- Medical claims
- Baby or child safety
- Cosmetics or ingredients
- Food contact
- Electronics
- Batteries
- Trademark or IP
- Platform policy
- Import restrictions
- Advertising claim restrictions

---

## Score Interpretation Guide

| Final Score | Interpretation |
|---:|---|
| 12 or higher | Strong Candidate |
| 8 to 11 | Test Carefully |
| 4 to 7 | Watchlist |
| Below 4 | Avoid unless stronger evidence appears |

Important:

```text
A high score does not guarantee product success.
```

It only means the product idea appears stronger under this research framework.

---

## Example Input

```text
Product Idea: Jewelry travel organizer
Category: Travel accessories
Target Region: United States
Target Audience: Women travelers, jewelry owners, gift buyers
Estimated Price Range: $10-$35
Source Links:
- https://example.com/public-trend-page
Public Trend Signals:
- Public travel packing content shows compact jewelry organizers.
Marketplace Signals:
- Similar products appear in travel accessory categories.
Social Media Signals:
- Visual before-and-after packing content appears suitable.
Review Signals:
- Public review patterns mention tangled jewelry and zipper quality.
Community Signals:
- Travel users discuss jewelry storage problems.
Supplier Notes:
- Likely easy to source in multiple materials and sizes.
Known Risks:
- Avoid copying creator images. Check zipper quality and material claims.
```

---

## Example JSON Output

```json
{
  "score_id": "TP-SCORE-001",
  "product_idea": "Jewelry travel organizer",
  "category": "Travel accessories",
  "target_region": "United States",
  "target_audience": "Women travelers, jewelry owners, gift buyers",
  "evaluated_at": null,
  "source_urls": ["https://example.com/public-trend-page"],
  "evidence_summary": "The provided public signals suggest that jewelry organization during travel is a visible consumer problem. The product has content potential because it can be shown in packing routines and before-and-after organization scenes.",
  "scores": {
    "demand_signal": 3,
    "social_visibility": 5,
    "price_potential": 4,
    "supplier_availability": 4,
    "differentiation_potential": 4,
    "competition_level": 3,
    "shipping_difficulty": 1,
    "compliance_risk": 1
  },
  "opportunity_score": 15,
  "score_interpretation": "Strong Candidate",
  "main_strengths": [
    "Strong short-form content potential.",
    "Easy to ship and package.",
    "Can be positioned as a giftable lifestyle accessory."
  ],
  "main_risks": [
    "Competition may be moderate.",
    "Quality issues such as zipper durability should be checked.",
    "More marketplace pricing validation is needed."
  ],
  "risk_note": "Low shipping and compliance risk, but quality and competition should still be reviewed.",
  "risk_level": "Low",
  "confidence": "Medium",
  "next_action": "Compare marketplace price ranges, analyze public review complaints, and check supplier customization options.",
  "review_status": "Needs Review",
  "reviewer_note": null
}
```

---

## Best Use Cases

Use this prompt for:

- Product opportunity scoring
- Marketplace research
- Trend report generation
- Weekly product watchlists
- Paid research reports
- Product sourcing validation
- Content-driven product selection
- Cross-border e-commerce planning

---

## Do Not Use This Prompt For

Do not use this prompt for:

- Guaranteed sales predictions
- Financial advice
- Investment decisions
- Medical product validation
- Legal compliance decisions
- Private data analysis
- Scraped personal contact lists
- Fake review generation
- Platform bypass
- Spam automation

---

## Final Reminder

Product scoring is a research framework, not a guarantee.

Every score should be reviewed by a human before making sourcing, advertising, or business decisions.
The output should keep `risk_note` and `risk_level` as separate fields.
