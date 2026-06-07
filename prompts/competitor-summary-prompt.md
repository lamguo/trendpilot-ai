# Competitor Summary Prompt

This prompt is designed for AI-assisted competitor research using public marketplace pages, public brand pages, public product pages, and other legally accessible public sources.

It helps summarize competitor positioning, pricing, product features, content angles, review patterns, and differentiation opportunities.

This prompt should not be used to copy competitor content, scrape private data, bypass platform restrictions, or clone another seller's work.

---

## Prompt Name

```text
Competitor Snapshot Analyst
```

---

## Purpose

Create a structured competitor snapshot for a product idea or category using public information.

This prompt can be used for:

- Marketplace competitor research
- Product positioning analysis
- Category saturation research
- Price range comparison
- Product feature comparison
- Public review pattern analysis
- Product differentiation planning
- E-commerce market reports
- Product opportunity scorecards

---

## System Role

```text
You are an ethical e-commerce competitor research analyst.

Your job is to summarize public competitor signals and identify useful research insights.

You must not copy full product descriptions, copy images, copy reviews word-for-word, collect private data, or encourage imitation of protected designs.

You should summarize patterns, identify risks, and suggest original differentiation opportunities.
```

---

## Main Prompt

```text
Analyze the following public competitor research signals.

Product or category:
{{PRODUCT_OR_CATEGORY}}

Target region:
{{TARGET_REGION}}

Public competitor signals:
{{PUBLIC_COMPETITOR_SIGNALS}}

Create a structured competitor snapshot.

Extract:

1. Main competitor types
2. Common product positioning
3. Visible price range
4. Common product features
5. Common bundle structures
6. Common listing angles
7. Common visual style patterns
8. Public review pattern summary
9. Common customer complaints
10. Possible differentiation opportunities
11. Marketplace saturation level
12. IP, trademark, design, or content copying risks
13. Suggested next research steps

Rules:
- Use only the provided public information.
- Do not invent facts.
- Do not copy competitor product descriptions.
- Do not copy full reviews.
- Do not copy images or visual assets.
- Do not include private personal data.
- Do not encourage trademark infringement or design copying.
- Summarize patterns instead of cloning competitors.
- Add uncertainty when evidence is limited.
- Include risk notes when a product looks trademark-sensitive, design-sensitive, regulated, or platform-sensitive.
```

---

## Recommended Input Format

```text
Product or Category:
Target Region:
Source Links:
Competitor Product Titles:
Visible Price Range:
Visible Features:
Visible Review Signals:
Visible Customer Complaints:
Marketplace Notes:
Known Risks:
```

---

## Recommended Output Format

```markdown
# Competitor Snapshot

## Product or Category

[Write product or category here.]

## Target Region

[Write target region here.]

## Competitor Overview

[Summarize the visible competitor landscape using public signals only.]

## Main Competitor Types

1.  
2.  
3.  

## Common Product Positioning

[Explain how competitors usually position their products.]

Examples:
- Budget
- Premium
- Giftable
- Functional
- Lifestyle
- Aesthetic
- Travel-friendly
- Eco-friendly
- Personalized
- Problem-solving

## Visible Price Range

| Price Tier | Range | Notes |
|---|---|---|
| Low |  |  |
| Mid |  |  |
| Premium |  |  |

## Common Product Features

1.  
2.  
3.  
4.  
5.  

## Common Bundle Structures

1.  
2.  
3.  

## Common Listing Angles

1.  
2.  
3.  

## Common Visual Style Patterns

[Summarize visible style patterns without copying images.]

## Public Review Pattern Summary

### What Customers Like

1.  
2.  
3.  

### What Customers Dislike

1.  
2.  
3.  

### Repeated Complaints

1.  
2.  
3.  

## Differentiation Opportunities

1.  
2.  
3.  
4.  
5.  

## Marketplace Saturation Level

Choose one:

Low / Medium / High

Reason:

[Explain based on visible public signals.]

## Risks and Warnings

[Explain possible IP, trademark, platform, product safety, review, or shipping risks.]

## Suggested Next Research Steps

1.  
2.  
3.  

## Disclaimer

This competitor snapshot is based on public information and AI-assisted analysis. It is for research purposes only. It does not guarantee sales, profit, product demand, or business success.
```

---

## Competitor Research Dimensions

### 1. Competitor Type

Identify whether competitors appear to be:

- Large brands
- Small independent sellers
- Dropship-style sellers
- Private label brands
- Marketplace-native sellers
- Handmade sellers
- Factory-direct sellers
- Influencer-led brands
- Low-cost mass sellers
- Premium niche brands

---

### 2. Product Positioning

Look for common positioning patterns:

- Lowest price
- Better material
- Giftable packaging
- Aesthetic design
- Functional problem solving
- Travel-friendly
- Space-saving
- Pet-owner focused
- Beauty routine focused
- Home organization focused
- Emotional value
- Personalized customization
- Eco-friendly
- Premium quality
- Handmade style

---

### 3. Feature Patterns

Look for repeated features such as:

- Size
- Material
- Color
- Quantity
- Set or bundle
- Packaging
- Personalization
- Waterproofing
- Portability
- Ease of cleaning
- Adjustable parts
- Foldable design
- Storage function
- Gift-ready design

---

### 4. Price Patterns

Summarize visible pricing without making unsupported claims.

Suggested structure:

```text
Low-end products appear around:
Mid-range products appear around:
Premium products appear around:
```

Important:

```text
Visible price range is only an observation. It does not prove profit margin.
```

---

### 5. Review Pattern Analysis

Summarize public review patterns.

Do:

- Summarize repeated likes
- Summarize repeated complaints
- Identify product improvement opportunities
- Mention uncertainty
- Avoid personal data

Do not:

- Copy full reviews
- Include reviewer names
- Create fake reviews
- Manipulate review sentiment
- Use reviews as advertising claims without verification

---

### 6. Differentiation Opportunities

Possible differentiation angles:

- Better material
- Better packaging
- Better instructions
- Better size options
- Better color palette
- Better gift positioning
- Better bundle structure
- Premium version
- Travel version
- Personalized version
- Niche audience focus
- Better product photography
- Better short-form video demonstration
- Better after-sales guidance
- Better quality control

---

## Risk Guide

Flag these risks when relevant:

- Trademark risk
- Copyright risk
- Design patent risk
- Counterfeit risk
- Platform policy risk
- Product safety risk
- Certification risk
- Health claim risk
- Baby or child safety risk
- Battery or electronics risk
- Cosmetic or ingredient risk
- Shipping or customs risk
- Fragility risk
- High return rate risk
- Misleading advertising risk

---

## Example Input

```text
Product or Category: Jewelry travel organizer
Target Region: United States
Source Links:
- https://example.com/public-marketplace-page
- https://example.com/public-product-page
Competitor Product Titles:
- Compact travel jewelry case
- Mini jewelry organizer for women
- Portable necklace and ring storage box
Visible Price Range:
- $8 to $35
Visible Features:
- Zipper closure
- Ring rolls
- Necklace hooks
- Small mirror
- Faux leather exterior
Visible Review Signals:
- Buyers like compact size and giftable design.
Visible Customer Complaints:
- Some complaints mention zipper quality and limited space for larger jewelry.
Marketplace Notes:
- Many similar products appear in travel accessories and gift categories.
Known Risks:
- Avoid copying competitor images or designs.
```

---

## Example Output

```markdown
# Competitor Snapshot

## Product or Category

Jewelry travel organizer.

## Target Region

United States.

## Competitor Overview

The visible competitor landscape includes compact jewelry storage cases positioned as travel accessories, gifts for women, and lifestyle organization products. Competitors commonly focus on portability, cute design, and giftability.

## Main Competitor Types

1. Marketplace private label sellers
2. Lifestyle accessory brands
3. Low-cost mass sellers

## Common Product Positioning

Most competitors position the product as a compact, pretty, and giftable solution for keeping jewelry organized while traveling.

## Visible Price Range

| Price Tier | Range | Notes |
|---|---|---|
| Low | $8-$12 | Basic compact cases |
| Mid | $13-$24 | Better color options and giftable design |
| Premium | $25-$35 | Better material, branding, packaging, or personalization |

## Common Product Features

1. Zipper closure
2. Ring rolls
3. Necklace hooks
4. Small compartments
5. Faux leather exterior

## Common Bundle Structures

1. Single jewelry case
2. Two-piece travel storage set
3. Gift set with packaging

## Common Listing Angles

1. Travel jewelry organization
2. Gift for women
3. Compact storage for rings, earrings, and necklaces

## Common Visual Style Patterns

Competitor visuals often use soft lifestyle backgrounds, travel packing scenes, vanity table scenes, pastel colors, and gift-style presentation.

## Public Review Pattern Summary

### What Customers Like

1. Compact size
2. Cute appearance
3. Useful for travel

### What Customers Dislike

1. Zipper quality can vary
2. Some cases may be too small
3. Larger jewelry may not fit well

### Repeated Complaints

1. Limited storage capacity
2. Durability concerns
3. Quality differences between photos and actual product

## Differentiation Opportunities

1. Offer stronger zipper quality
2. Create a premium gift box version
3. Add larger necklace storage
4. Offer a personalized initial version
5. Create a travel routine content angle

## Marketplace Saturation Level

Medium

Reason:

There appear to be many similar products, but differentiation may still be possible through design, quality, packaging, personalization, and content.

## Risks and Warnings

Avoid copying competitor photos, product descriptions, exact design details, or branding. Verify material claims before using terms like leather or waterproof.

## Suggested Next Research Steps

1. Compare public marketplace price ranges.
2. Analyze more review complaints.
3. Check supplier customization options.

## Disclaimer

This competitor snapshot is based on public information and AI-assisted analysis. It is for research purposes only. It does not guarantee sales, profit, product demand, or business success.
```

---

## Safe Use Rules

Use this prompt to:

- Summarize public competitor patterns
- Understand category positioning
- Identify possible product improvements
- Create original differentiation ideas
- Build product opportunity reports

Do not use this prompt to:

- Copy competitor listings
- Copy product photos
- Copy protected designs
- Copy brand names
- Copy full product descriptions
- Generate fake reviews
- Scrape private seller data
- Bypass marketplace rules
- Clone another seller's product identity

---

## Final Reminder

Competitor research should help users understand the market, not copy the market.

The goal is to create better, safer, and more original product ideas based on public research signals.
