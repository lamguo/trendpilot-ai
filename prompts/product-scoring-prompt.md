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

1. Demand Signal
2. Social Visibility
3. Price Potential
4. Supplier Availability
5. Differentiation Potential
6. Competition Level
7. Shipping Difficulty
8. Compliance Risk

Use this formula:

Opportunity Score =
Demand Signal
+ Social Visibility
+ Price Potential
+ Supplier Availability
+ Differentiation Potential
- Competition Level
- Shipping Difficulty
- Compliance Risk

Rules:
- Use only the provided public research signals.
- Do not invent facts.
- Do not claim guaranteed sales or profit.
- Do not treat weak signals as proven demand.
- If evidence is weak, lower the confidence level.
- If compliance or safety risk exists, clearly explain it.
- If the product may involve trademark, platform, health, baby, electronics, battery, cosmetic, medical, or shipping risk, mention it.
- Include a final recommendation: Strong Candidate, Test Carefully, Watchlist, or Avoid.
Also include:
- risk_note: short explanation of the main risk
- risk_level: Low, Medium, High, Avoid, or Unknown
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

## Recommended Output Format

```markdown
# Product Opportunity Score

## Product Summary

**Product Idea:**  
**Category:**  
**Target Region:**  
**Target Audience:**  

## Evidence Summary

Summarize the provided public evidence in original words.

## Scoring Table

| Dimension | Score | Reason |
|---|---:|---|
| Demand Signal |  |  |
| Social Visibility |  |  |
| Price Potential |  |  |
| Supplier Availability |  |  |
| Differentiation Potential |  |  |
| Competition Level |  |  |
| Shipping Difficulty |  |  |
| Compliance Risk |  |  |

## Opportunity Score

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

**Final Score:**  

## Score Interpretation

Choose one:

- Strong Candidate
- Test Carefully
- Watchlist
- Avoid

## Confidence Level

Choose one:

- Low
- Medium
- High

## Risk Level

Choose one:

- Low
- Medium
- High
- Avoid
- Unknown

## Risk Note

Write a short explanation of the main risk.

## Main Strengths

1.  
2.  
3.  

## Main Risks

1.  
2.  
3.  

## Suggested Validation Steps

1.  
2.  
3.  

## Final Recommendation

Write a short recommendation based on the score, evidence, confidence level, and risk profile.

## Disclaimer

This score is based on public signals and AI-assisted analysis. It does not guarantee sales, profit, product demand, or business success.
```

---

## Scoring Guide

### 1. Demand Signal

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

### 2. Social Visibility

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

### 3. Price Potential

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

### 4. Supplier Availability

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

### 5. Differentiation Potential

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

### 6. Competition Level

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

### 7. Shipping Difficulty

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

### 8. Compliance Risk

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

## Example Output

```markdown
# Product Opportunity Score

## Product Summary

**Product Idea:** Jewelry travel organizer  
**Category:** Travel accessories  
**Target Region:** United States  
**Target Audience:** Women travelers, jewelry owners, gift buyers  

## Evidence Summary

The provided public signals suggest that jewelry organization during travel is a visible consumer problem. The product has content potential because it can be shown in packing routines and before-and-after organization scenes.

## Scoring Table

| Dimension | Score | Reason |
|---|---:|---|
| Demand Signal | 3 | There are visible public signals, but more marketplace validation is needed. |
| Social Visibility | 5 | The product is easy to demonstrate visually in packing and travel content. |
| Price Potential | 4 | It can be sold as a giftable or premium small accessory. |
| Supplier Availability | 4 | Similar products are likely available in multiple materials and sizes. |
| Differentiation Potential | 4 | Packaging, material, color, size, and gift positioning can create differentiation. |
| Competition Level | 3 | The category may have moderate marketplace competition. |
| Shipping Difficulty | 1 | The product is small, lightweight, and easy to ship. |
| Compliance Risk | 1 | Low risk if no false material claims are made. |

## Opportunity Score

```text
3 + 5 + 4 + 4 + 4 - 3 - 1 - 1 = 15
```

**Final Score:** 15

## Score Interpretation

Strong Candidate

## Confidence Level

Medium

## Risk Level

Low

## Risk Note

Low shipping and compliance risk, but quality and competition should still be reviewed.

## Main Strengths

1. Strong short-form content potential.
2. Easy to ship and package.
3. Can be positioned as a giftable lifestyle accessory.

## Main Risks

1. Competition may be moderate.
2. Quality issues such as zipper durability should be checked.
3. More marketplace pricing validation is needed.

## Suggested Validation Steps

1. Compare marketplace price ranges.
2. Analyze public review complaints.
3. Check supplier customization options.

## Final Recommendation

This product appears to be a strong candidate for deeper research because it has visible consumer pain points, good content potential, and low shipping difficulty. It should still be validated through competitor pricing, review analysis, and supplier quality checks.

## Disclaimer

This score is based on public signals and AI-assisted analysis. It does not guarantee sales, profit, product demand, or business success.
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
The output should keep risk_note and risk_level as separate fields.
