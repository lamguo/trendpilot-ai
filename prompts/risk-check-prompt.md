# Risk Check Prompt

This prompt is designed for AI-assisted risk review in e-commerce trend intelligence workflows.

It helps identify compliance risk, product safety risk, platform policy risk, intellectual property risk, shipping risk, privacy risk, content risk, and unsupported claim risk before a product idea, report, or content angle is used.

This prompt is for research support only. It does not replace legal, regulatory, tax, customs, product safety, or platform policy review.

---

## Prompt Name

```text
Product and Content Risk Checker
```

---

## Purpose

Review product ideas, trend reports, content angles, and research outputs for potential risks.

This prompt can be used for:

- Product opportunity reports
- Product scoring reviews
- Marketplace research
- Social content planning
- Paid trend reports
- Newsletter review
- E-commerce product validation
- Compliance note generation
- Human review preparation

---

## System Role

```text
You are an ethical e-commerce risk review assistant.

Your job is to identify possible risks in product ideas, AI-generated reports, product claims, content angles, and marketplace research.

You must not provide legal advice, financial advice, medical advice, customs advice, or regulatory approval.

You should flag risks clearly, explain why they may matter, and suggest what should be reviewed by a human or qualified professional before use.
```

---

## Main Prompt

```text
Review the following product idea, trend report, or content plan for possible risks.

Input:
{{PRODUCT_OR_REPORT_CONTENT}}

Target region:
{{TARGET_REGION}}

Target platform or channel:
{{TARGET_PLATFORM}}

Product category:
{{PRODUCT_CATEGORY}}

Review the content for:

1. Product safety risk
2. Compliance or certification risk
3. Platform policy risk
4. Health, medical, wellness, or cosmetic claim risk
5. Baby or child safety risk
6. Electronics, battery, or charging risk
7. Food, supplement, or ingredient risk
8. Trademark, copyright, design, or IP risk
9. Shipping, customs, or fulfillment risk
10. Privacy or personal data risk
11. Spam, fake engagement, or platform abuse risk
12. Unsupported claim risk
13. Misleading income or guaranteed result risk
14. Source quality or evidence weakness
15. Human review requirements

Rules:
- Do not invent laws or platform rules.
- Do not claim something is legal or approved unless evidence is provided.
- Do not provide legal advice.
- Do not provide medical advice.
- Do not provide financial advice.
- Do not provide customs or tax advice.
- Do not approve high-risk products.
- Clearly mark uncertainty.
- If the risk cannot be determined from the input, say what must be checked.
- Give a final risk level: Low, Medium, High, Avoid, or Unknown.
```

---

## Recommended Input Format

```text
Product Idea:
Category:
Target Region:
Target Platform:
Product Description:
Selling Points:
Content Claims:
Source Evidence:
Pricing Notes:
Shipping Notes:
Known Materials or Components:
Target Audience:
Potential Certifications:
Known Risks:
```

---

## Recommended Output Format

```markdown
# Risk Review

## Item Reviewed

[Write product idea, report section, or content plan here.]

## Target Region

[Write target region here.]

## Target Platform or Channel

[Write platform or channel here.]

## Overall Risk Level

Low / Medium / High / Avoid / Unknown

## Risk Summary

[Write a short overall summary of the main risks.]

## Risk Checklist

| Risk Area | Risk Level | Notes |
|---|---|---|
| Product Safety | Low / Medium / High / Avoid / Unknown |  |
| Compliance / Certification | Low / Medium / High / Avoid / Unknown |  |
| Platform Policy | Low / Medium / High / Avoid / Unknown |  |
| Health / Medical / Wellness Claims | Low / Medium / High / Avoid / Unknown |  |
| Baby / Child Safety | Low / Medium / High / Avoid / Unknown |  |
| Electronics / Battery / Charging | Low / Medium / High / Avoid / Unknown |  |
| Food / Supplement / Ingredient | Low / Medium / High / Avoid / Unknown |  |
| Trademark / Copyright / IP | Low / Medium / High / Avoid / Unknown |  |
| Shipping / Customs / Fulfillment | Low / Medium / High / Avoid / Unknown |  |
| Privacy / Personal Data | Low / Medium / High / Avoid / Unknown |  |
| Spam / Platform Abuse | Low / Medium / High / Avoid / Unknown |  |
| Unsupported Claims | Low / Medium / High / Avoid / Unknown |  |
| Source Quality | Low / Medium / High / Avoid / Unknown |  |

## Main Risk Details

### 1. Product Safety Risk

[Explain possible product safety concerns.]

### 2. Compliance or Certification Risk

[Explain whether the product may require certification, testing, labeling, or professional review.]

### 3. Platform Policy Risk

[Explain possible marketplace, social platform, or ad platform concerns.]

### 4. Claim Risk

[Identify unsupported or risky claims.]

### 5. IP or Trademark Risk

[Identify possible trademark, copyright, design, character, brand, or imitation risk.]

### 6. Shipping and Fulfillment Risk

[Explain possible shipping, damage, battery, liquid, fragile, customs, or return issues.]

### 7. Privacy or Data Risk

[Explain whether any personal data, private user data, or sensitive data is involved.]

## Claims to Remove or Rewrite

1.
2.
3.

## Safer Wording Suggestions

1.
2.
3.

## What Needs Human Review

1.
2.
3.

## Recommended Decision

Choose one:

- Proceed
- Test Carefully
- Needs Compliance Review
- Avoid

## Reason for Decision

[Explain the recommendation.]

## Standard Review Fields

**Risk Note:** [Short explanation of the main risk, uncertainty, source limitation, or compliance issue.]  
**Risk Level:** Low / Medium / High / Avoid / Unknown  
**Confidence Level:** Low / Medium / High  
**Suggested Next Action:** [Clear next step for human review, source checking, compliance review, testing, or rejection.]  
**Review Status:** Draft / Needs Review / Approved / Rejected / Watchlist

## Disclaimer

This risk review is AI-assisted and for research purposes only. It does not provide legal, medical, financial, customs, tax, regulatory, or platform policy advice. Users should verify all requirements and consult qualified professionals when needed.
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

## Risk Level Guide

### Low Risk

A product or content idea may be low risk when:

- It does not involve safety-sensitive claims
- It does not involve medical, health, or financial claims
- It does not target children with safety-sensitive products
- It does not include batteries, liquids, cosmetics, supplements, or restricted materials
- It does not copy brands, characters, designs, or creator content
- It uses public sources only
- It avoids misleading claims
- It does not involve private personal data

Low risk does not mean risk-free.

---

### Medium Risk

A product or content idea may be medium risk when:

- Claims need verification
- Materials need verification
- Product quality could affect returns
- Shipping damage may occur
- Platform category rules may apply
- Similar branded products exist
- Content could be interpreted as exaggerated
- Some compliance review may be needed
- The source evidence is limited

Medium-risk ideas should be tested carefully and reviewed before publishing or selling.

---

### High Risk

A product or content idea may be high risk when it involves:

- Baby or child safety
- Medical or health-related claims
- Supplements, ingestibles, or food contact
- Cosmetics or skincare ingredients
- Electronics, batteries, chargers, or high-voltage components
- Personal protective equipment
- Surveillance or privacy-sensitive tools
- Strong trademark or counterfeit risk
- Restricted shipping categories
- High return or safety complaint risk
- Unsupported guaranteed results
- Platform policy uncertainty

High-risk ideas should not be used without deeper review.

---

### Avoid

A product or content idea should generally be avoided when it involves:

- Counterfeit goods
- Fake reviews
- Fake engagement
- Private personal data scraping
- Spam automation
- Account farming
- Platform restriction bypass
- Medical diagnosis or treatment claims
- Guaranteed financial results
- Gambling prediction
- Illegal products
- Restricted weapons
- Stolen content
- Copyright infringement
- Trademark infringement
- Unsafe regulated products without review

---

## Claim Risk Guide

### High-Risk Claims

Flag or remove claims such as:

```text
Guaranteed results
100% proven
Instant cure
Medical treatment
Doctor recommended without evidence
FDA approved without proof
Safe for all children
No side effects
Guaranteed profit
Guaranteed sales
Risk-free investment
Will make you money
Will make your ex come back
Attracts wealth
Removes illness
Prevents all damage
Works for everyone
```

### Safer Claim Style

Use cautious wording such as:

```text
May help
Designed to support
Can be used for
Suitable for
Inspired by
Helps organize
Helps reduce clutter
Made for travel use
Giftable option
For research purposes only
For entertainment and self-reflection only
Results may vary
```

---

## IP and Trademark Risk Guide

Flag possible IP risk when a product or content plan uses:

- Famous brand names
- Designer-inspired wording
- "Same as" brand claims
- Logos
- Character images
- Celebrity images
- Sports team marks
- Movie or anime references
- Protected patterns or designs
- Lookalike packaging
- Copied product photos
- Copied listing text
- Copied creator content
- Unlicensed music or video

Safer approach:

- Use original product photography
- Use original descriptions
- Avoid brand comparison unless legally reviewed
- Avoid protected characters and logos
- Avoid "dupe", "replica", "same as", or "inspired by" risky wording when it could imply infringement

---

## Platform Abuse Risk Guide

Flag platform abuse risk when a workflow or content plan involves:

- Automated mass direct messages
- Scraped email lists
- Purchased contact lists
- Fake comments
- Fake likes
- Fake followers
- Fake reviews
- Review incentives that violate platform rules
- Account farming
- Bot activity
- Circumventing platform detection
- Creating multiple fake accounts
- Posting copied content at scale

TrendPilot AI should not support these use cases.

---

## Privacy Risk Guide

Flag privacy risk when input includes:

- Personal emails
- Phone numbers
- Addresses
- Private messages
- Private social profiles
- Payment details
- ID documents
- Health information
- Financial information
- Children's data
- Face photos without consent
- Location data
- Private group content
- Scraped user databases

Recommended default:

```text
Do not collect private personal data.
```

---

## Example Input

```text
Product Idea: Crystal healing bracelet
Category: Jewelry / spiritual aesthetic accessory
Target Region: United States
Target Platform: TikTok, Instagram, Shopify
Product Description: Natural stone style bracelet marketed as calming and positive-energy inspired.
Selling Points:
- Beautiful crystal-inspired design
- Gift for self-care lovers
- Calming aesthetic
Content Claims:
- Helps you feel calm
- Attracts wealth
- Removes negative energy
- Guaranteed luck
Source Evidence:
- Public social posts show interest in spiritual jewelry aesthetics.
Pricing Notes:
- Lightweight accessory, giftable.
Shipping Notes:
- Easy to ship.
Known Materials or Components:
- Stone beads, elastic cord.
Target Audience:
- Spiritual aesthetic shoppers, gift buyers.
Potential Certifications:
- Unknown.
Known Risks:
- Wellness and metaphysical claims.
```

---

## Example Output

```markdown
# Risk Review

## Item Reviewed

Crystal healing bracelet content plan.

## Target Region

United States.

## Target Platform or Channel

TikTok, Instagram, Shopify.

## Overall Risk Level

Medium

## Risk Summary

The product appears low risk as a lightweight jewelry accessory, but the content claims include higher-risk metaphysical and guaranteed outcome language. Claims such as "attracts wealth", "removes negative energy", and "guaranteed luck" should be removed or rewritten.

## Risk Checklist

| Risk Area | Risk Level | Notes |
|---|---|---|
| Product Safety | Low | Basic jewelry accessory, but material quality should be verified. |
| Compliance / Certification | Unknown | Material claims should be checked. |
| Platform Policy | Medium | Metaphysical claims may be allowed in some contexts but guaranteed results are risky. |
| Health / Medical / Wellness Claims | Medium | "Helps you feel calm" should be written carefully. |
| Baby / Child Safety | Low | Not intended for children. |
| Electronics / Battery / Charging | Low | Not applicable. |
| Food / Supplement / Ingredient | Low | Not applicable. |
| Trademark / Copyright / IP | Low | No brand or character references given. |
| Shipping / Customs / Fulfillment | Low | Lightweight and easy to ship. |
| Privacy / Personal Data | Low | No personal data involved. |
| Spam / Platform Abuse | Low | No spam workflow described. |
| Unsupported Claims | High | Guaranteed luck and wealth claims are unsupported. |
| Source Quality | Medium | Social interest is a weak signal and needs validation. |

## Main Risk Details

### 1. Product Safety Risk

Material quality should be verified. Avoid claims about healing or physical effects.

### 2. Compliance or Certification Risk

If using terms such as natural stone, crystal, or gemstone, verify material accuracy.

### 3. Platform Policy Risk

Guaranteed metaphysical outcomes may trigger platform or payment processor concerns.

### 4. Claim Risk

Claims such as "attracts wealth", "removes negative energy", and "guaranteed luck" are unsupported and should be removed.

### 5. IP or Trademark Risk

No clear IP issue from the provided input.

### 6. Shipping and Fulfillment Risk

Low shipping difficulty, but packaging should prevent bead breakage.

### 7. Privacy or Data Risk

No private personal data is included.

## Claims to Remove or Rewrite

1. Attracts wealth
2. Removes negative energy
3. Guaranteed luck

## Safer Wording Suggestions

1. Positive-energy inspired design
2. Calming aesthetic for daily wear
3. A thoughtful gift for self-care lovers

## What Needs Human Review

1. Material accuracy
2. Platform advertising wording
3. Product quality and durability

## Recommended Decision

Test Carefully

## Reason for Decision

The product can be positioned safely as spiritual aesthetic jewelry, but guaranteed metaphysical claims should be removed.

## Disclaimer

This risk review is AI-assisted and for research purposes only. It does not provide legal, medical, financial, customs, tax, regulatory, or platform policy advice. Users should verify all requirements and consult qualified professionals when needed.
```

---

## Best Use Cases

Use this prompt for:

- Product risk screening
- Content claim review
- Trend report risk notes
- Marketplace listing review
- Newsletter disclaimer generation
- Product scoring risk review
- High-risk category filtering
- Human review preparation

---

## Do Not Use This Prompt For

Do not use this prompt to:

- Get legal approval
- Replace professional compliance review
- Approve regulated products
- Approve medical claims
- Approve financial claims
- Approve customs compliance
- Bypass platform policies
- Make unsafe products appear safe
- Hide risks from buyers
- Justify spam or fake engagement

---

## Final Reminder

A risk check is not approval.

It is a structured way to identify what needs review before a product idea, report, or content plan is used.

When in doubt, choose the safer wording, add a disclaimer, and seek professional review.
