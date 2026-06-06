# Data Sources

TrendPilot AI is designed to work with public, legally accessible trend signals.

This document explains what types of data sources can be used, what each source is useful for, what risks may exist, and what information should be avoided.

The goal is to help users build ethical AI-powered trend intelligence workflows without scraping private data, bypassing platform restrictions, or collecting sensitive personal information.

---

## Core Principle

TrendPilot AI should only use:

- Public web pages
- Public trend pages
- Public marketplace pages
- Public product pages
- Public search results
- Public community discussions
- Public news and industry pages
- Public product reviews where allowed
- Official platform trend reports
- Public RSS feeds
- Public APIs where available

TrendPilot AI should not use:

- Private user data
- Login-protected information
- Paid databases copied without permission
- Personal phone numbers
- Private emails collected without consent
- Private social media profiles
- Scraped account lists
- Bypassed platform data
- Data collected by breaking website terms
- Data obtained through hacking, credential sharing, or account farming

---

## Recommended Data Source Categories

### 1. Search Trend Sources

Search trend sources can help identify rising interest in a product, category, keyword, lifestyle, or consumer problem.

Possible sources:

- Google Trends
- Search engine autocomplete
- Search result pages
- Public keyword tools
- Public SEO trend pages
- Marketplace search suggestions

Useful signals:

- Rising keywords
- Seasonal patterns
- Regional interest
- Related queries
- New search phrases
- Long-tail product demand
- Consumer problem keywords

Example use cases:

- Finding rising product categories
- Detecting seasonal demand
- Comparing regions
- Discovering long-tail keywords
- Creating SEO content ideas
- Validating product demand before sourcing

Suggested fields to collect:

| Field | Description |
|---|---|
| Keyword | Main keyword or query |
| Related Query | Related search phrase |
| Region | Country or market |
| Trend Direction | Rising, stable, declining, seasonal |
| Time Window | Daily, weekly, monthly, yearly |
| Source URL | Where the signal was found |
| Collection Date | Date of collection |
| Notes | Human or AI summary |

Risk level: Low to Medium

Important notes:

- Prefer official trend pages or legitimate APIs.
- Avoid excessive automated querying.
- Avoid using unofficial tools as the only data source.
- Some unofficial search trend libraries may break when platforms change their endpoints.

---

### 2. Marketplace Trend Sources

Marketplace sources are useful for understanding what people are buying, reviewing, searching for, and comparing.

Possible sources:

- Amazon public bestseller pages
- Amazon public product pages
- Etsy public trend pages where accessible
- eBay public search result pages
- Walmart public category pages
- AliExpress public category pages
- Temu public category pages
- TikTok Shop public product pages where accessible
- SHEIN public category pages
- Shopify brand stores
- Niche marketplace public pages

Useful signals:

- Bestseller ranking
- Product titles
- Price ranges
- Review counts
- Rating patterns
- Product image style
- Bundle structure
- Common product variants
- Frequently mentioned features
- High-volume category keywords

Example use cases:

- Finding product ideas
- Comparing price ranges
- Discovering bundle opportunities
- Identifying common product complaints
- Mapping competitors
- Studying title and image patterns
- Understanding category saturation

Suggested fields to collect:

| Field | Description |
|---|---|
| Platform | Marketplace name |
| Product Name | Product title |
| Category | Marketplace category |
| Price | Listed price or range |
| Rating | Public rating if available |
| Review Count | Public review count if available |
| Rank Signal | Bestseller or category rank if visible |
| Main Keywords | Extracted product keywords |
| Product URL | Public product page |
| Image Style Notes | Visual pattern notes |
| Collection Date | Date of collection |

Risk level: Medium

Important notes:

- Use public pages only.
- Do not scrape behind login walls.
- Do not attempt to bypass anti-bot systems.
- Do not collect private buyer data.
- Do not copy product images for commercial reuse.
- Do not use marketplace content in a way that violates terms.
- Use marketplace pages as research signals, not as data to republish directly.

---

### 3. Social Media Trend Sources

Social media sources can reveal what people are talking about, sharing, commenting on, and emotionally reacting to.

Possible sources:

- TikTok public videos and public hashtag pages
- Instagram public posts and Reels
- YouTube Shorts and public video pages
- Pinterest public trend pages
- Reddit public communities
- X public posts
- Facebook public pages and groups where permitted
- Lemon8 public content where accessible

Useful signals:

- Viral hooks
- Comment questions
- Product demonstration formats
- User pain points
- Visual trends
- Aesthetic styles
- Hashtag growth
- Cultural trends
- Consumer language
- Content angles

Example use cases:

- Finding video content ideas
- Discovering emotional selling points
- Identifying product pain points
- Understanding consumer language
- Studying hooks and short-form video structures
- Detecting visual aesthetics
- Monitoring niche community discussions

Suggested fields to collect:

| Field | Description |
|---|---|
| Platform | Social platform |
| Topic | Trend topic |
| Hashtag | Public hashtag |
| Content Format | Video, image, text, thread |
| Engagement Signal | Likes, comments, shares, views if public |
| Common Questions | Repeated user questions |
| Pain Points | Problems users mention |
| Content Hook | Opening hook or angle |
| Source URL | Public link |
| Collection Date | Date of collection |

Risk level: Medium to High

Important notes:

- Do not collect private messages.
- Do not collect personal profile databases.
- Do not scrape private groups.
- Do not automate spam comments or direct messages.
- Do not impersonate users.
- Do not repost creator content without permission.
- Use public social content as trend inspiration, not as content to steal.

---

### 4. Community Discussion Sources

Community discussions can reveal real user problems, frustrations, product gaps, and niche language.

Possible sources:

- Reddit public subreddits
- Quora public questions
- Public forums
- Product-specific communities
- Hobby communities
- Parenting forums
- Pet owner forums
- Fitness communities
- Home organization communities
- Beauty and skincare communities
- Travel communities

Useful signals:

- Repeated complaints
- Product requests
- Buying hesitation
- Confusing product features
- Real-life use cases
- Comparison questions
- Niche slang
- Emotional triggers
- Unsolved problems

Example use cases:

- Finding product improvement ideas
- Identifying customer pain points
- Creating FAQ sections
- Writing product page copy
- Discovering content topics
- Building buyer personas
- Comparing user needs across markets

Suggested fields to collect:

| Field | Description |
|---|---|
| Community | Forum or community name |
| Topic | Discussion topic |
| User Problem | Main pain point |
| Product Mentioned | Product or category |
| Sentiment | Positive, negative, mixed |
| Repeated Questions | Common questions |
| Opportunity Note | Possible product or content opportunity |
| Source URL | Public discussion link |
| Collection Date | Date of collection |

Risk level: Medium

Important notes:

- Avoid collecting usernames unless necessary for citation.
- Do not collect private personal details.
- Do not quote large blocks of user content without permission.
- Summarize patterns instead of copying personal stories.
- Respect community rules.
- Do not use communities for spam promotion.

---

### 5. Review and Feedback Sources

Product reviews are useful for understanding what customers like, dislike, and wish existed.

Possible sources:

- Public marketplace reviews
- Public brand review pages
- Public app reviews
- Trustpilot public reviews
- Product review websites
- Public YouTube review comments
- Public Reddit product discussions

Useful signals:

- Common complaints
- Desired features
- Quality issues
- Packaging issues
- Sizing issues
- Usage scenarios
- Reasons for returns
- Positive selling points
- Upgrade opportunities

Example use cases:

- Improving product design
- Finding bundle ideas
- Writing better product descriptions
- Creating comparison content
- Identifying premium feature opportunities
- Building product opportunity scorecards

Suggested fields to collect:

| Field | Description |
|---|---|
| Product | Product or category |
| Review Source | Platform or website |
| Positive Signals | What users like |
| Negative Signals | What users dislike |
| Feature Requests | What users want improved |
| Quality Issues | Repeated product problems |
| Packaging Issues | Delivery or packaging complaints |
| Opportunity Note | Product improvement idea |
| Source URL | Public review page |
| Collection Date | Date of collection |

Risk level: Medium

Important notes:

- Do not copy full reviews into reports.
- Use summaries and aggregated insights.
- Do not collect reviewer personal data.
- Do not manipulate reviews.
- Do not generate fake reviews.
- Do not use review content in misleading advertising.

---

### 6. Official Trend Reports

Official reports can provide higher-quality background signals and more credible market context.

Possible sources:

- Pinterest Predicts
- TikTok trend reports
- Google consumer insights
- Meta trend reports
- YouTube culture reports
- McKinsey consumer reports
- Nielsen reports
- Statista public summaries
- Government trade data
- Industry association reports
- Platform seller reports
- Public e-commerce reports

Useful signals:

- Macro trends
- Consumer behavior shifts
- Regional demand changes
- Category-level growth
- Platform-level changes
- Demographic insights
- Long-term themes
- Policy or logistics changes

Example use cases:

- Validating short-term trend signals
- Writing weekly reports
- Building market overview sections
- Supporting opportunity scoring
- Comparing countries or regions
- Identifying macro consumer themes

Suggested fields to collect:

| Field | Description |
|---|---|
| Report Name | Title of report |
| Publisher | Organization |
| Region | Market covered |
| Category | Product or industry category |
| Key Insight | Main insight |
| Data Year | Year covered |
| Source URL | Report link |
| Collection Date | Date of collection |
| Reliability Note | Authority and limitation |

Risk level: Low

Important notes:

- Cite sources clearly.
- Do not copy long sections from copyrighted reports.
- Use short summaries and original analysis.
- Prefer official and reputable sources.
- Check publication date before using.
- Avoid outdated data unless clearly labeled.

---

### 7. Public News and Industry Sources

News sources can help detect emerging categories, policy changes, logistics changes, and market shifts.

Possible sources:

- Business news
- Retail news
- E-commerce news
- Consumer trend news
- Logistics news
- Trade policy news
- Technology news
- Industry blogs
- Public press releases
- Brand announcements

Useful signals:

- New regulations
- Platform policy changes
- Shipping cost changes
- New product launches
- Category expansion
- Consumer behavior changes
- Funding and startup activity
- Retailer strategy shifts

Example use cases:

- Monitoring market environment
- Detecting policy risks
- Finding emerging brands
- Creating weekly intelligence briefs
- Understanding platform changes
- Finding early category signals

Suggested fields to collect:

| Field | Description |
|---|---|
| Source | Publisher |
| Article Title | News title |
| Topic | Main topic |
| Category | Industry category |
| Market | Region or country |
| Key Signal | Main trend or risk |
| Source URL | Article link |
| Publication Date | Date published |
| Collection Date | Date collected |

Risk level: Low to Medium

Important notes:

- Cite sources.
- Avoid copying full articles.
- Summarize in original language.
- Check multiple sources for important claims.
- Label uncertain signals clearly.

---

## Data Source Risk Levels

### Low-Risk Sources

Low-risk sources are usually official, public, and intended for public reading.

Examples:

- Official trend reports
- Government trade data
- Public industry reports
- Public news pages
- Official platform blog posts
- Public RSS feeds
- Public documentation pages

Allowed use:

- Summarize
- Cite
- Analyze
- Extract high-level insights
- Use in reports with attribution

---

### Medium-Risk Sources

Medium-risk sources are public but may have platform-specific terms, rate limits, or anti-scraping rules.

Examples:

- Marketplace product pages
- Public search result pages
- Public product reviews
- Public social media posts
- Public forum discussions
- Public community pages

Allowed use with caution:

- Summarize public signals
- Extract limited structured fields
- Avoid personal data
- Avoid excessive crawling
- Avoid bypassing restrictions
- Respect robots.txt and terms where applicable

---

### High-Risk Sources

High-risk sources should generally be avoided.

Examples:

- Login-protected pages
- Private groups
- Private messages
- Personal contact databases
- Paid databases without permission
- Scraped email lists
- Scraped phone number lists
- User account data
- Bypassed platform data
- Data accessed through fake accounts
- Data collected using credential sharing

Do not use:

- Private personal data
- Non-consensual contact data
- Hacked or leaked databases
- Automated account farming
- Any data collection that violates law or platform terms

---

## Suggested Data Model

TrendPilot AI can use a simple data model for collected trend signals.

Suggested fields:

| Field | Description |
|---|---|
| id | Unique record ID |
| source_type | Search, marketplace, social, community, review, report, news |
| source_name | Platform or publisher name |
| source_url | Public URL |
| collection_date | Date collected |
| region | Country or market |
| category | Product category |
| keyword | Main keyword |
| product_name | Product name if available |
| trend_signal | Short summary of the signal |
| evidence | Source-based evidence summary |
| audience | Target audience |
| pain_point | Consumer problem |
| content_angle | Suggested content angle |
| price_signal | Price range if public |
| competition_signal | Low, medium, high |
| risk_note | Compliance or platform risk |
| confidence | Low, medium, high |
| opportunity_score | Internal score |
| next_action | Suggested follow-up step |

---

## Example Trend Signal Record

| Field | Example |
|---|---|
| source_type | Social |
| source_name | Pinterest |
| region | United States |
| category | Home organization |
| keyword | jewelry travel organizer |
| trend_signal | Visual content around travel jewelry storage appears repeatedly in lifestyle boards |
| audience | Women travelers, gift buyers, jewelry owners |
| pain_point | Jewelry gets tangled during travel |
| content_angle | Before and after packing routine |
| competition_signal | Medium |
| risk_note | Avoid copying creator images |
| confidence | Medium |
| next_action | Check marketplace pricing and review complaints |

---

## Data Collection Rules

Before collecting any source, ask:

1. Is the page public?
2. Is the information meant to be publicly viewed?
3. Does the source allow automated access or provide an API?
4. Are there rate limits?
5. Does this include private personal data?
6. Does this require login?
7. Does this require bypassing restrictions?
8. Can the information be summarized instead of copied?
9. Can the source be cited?
10. Would this use case look ethical if publicly disclosed?

If the answer creates doubt, do not collect the data automatically.

---

## What TrendPilot AI Should Not Become

TrendPilot AI should not become:

- A spam automation system
- A private data scraper
- A seller contact database
- A fake review generator
- A social media scraping farm
- An account farming toolkit
- A platform restriction bypass tool
- A copyright content copying tool
- A misleading income automation project

---

## Safe Use Cases

Recommended safe use cases:

- Public trend monitoring
- Product research
- Content inspiration
- Market signal summaries
- Public review analysis
- Industry report summaries
- Search keyword research
- Social content angle research
- Newsletter creation
- Internal e-commerce research
- Product opportunity scoring
- Report generation

---

## Final Note

Data quality matters more than data volume.

A small number of clean, public, well-cited sources is better than a large amount of risky, noisy, or unauthorized data.

TrendPilot AI should help users build responsible trend intelligence workflows, not unsafe scraping systems.
