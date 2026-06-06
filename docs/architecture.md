# System Architecture

TrendPilot AI is designed as a license-safe starter kit for building AI-powered trend intelligence workflows.

It does not redistribute third-party source code. Instead, it provides architecture references, workflow ideas, prompts, report templates, and integration guidance.

---

## Core Workflow

```text
Public Trend Sources
        ↓
Web Scraping / Search Layer
        ↓
Workflow Automation Layer
        ↓
AI Analysis Layer
        ↓
Product Opportunity Scoring
        ↓
Report Generation
        ↓
Delivery Channels
```

---

## Recommended Modules

### 1. Public Trend Sources

Potential sources include:

- Search trends
- Public social media signals
- E-commerce bestseller pages
- Community discussions
- Product review pages
- Industry news
- Marketplace category pages
- Public brand pages
- Public product review pages

Only public and legally accessible information should be used.

This project should avoid collecting private personal data, restricted platform data, login-protected information, or content that violates platform terms.

---

### 2. Web Scraping / Search Layer

This layer collects public web data and converts it into clean text or structured data.

Possible tools:

- Firecrawl
- Browser-use
- Playwright
- Search APIs
- RSS feeds
- Public marketplace pages
- Public social trend pages

This project does not include third-party source code from these tools. It only provides integration notes, workflow ideas, and original templates.

Recommended outputs from this layer:

- Source URL
- Page title
- Product name
- Category
- Keywords
- Mentioned price range
- Review signals
- Social engagement signal
- Raw summary
- Collection date

---

### 3. Workflow Automation Layer

This layer schedules tasks and connects tools together.

Possible tools:

- n8n
- Make
- Zapier
- GitHub Actions
- Cron jobs
- Custom Python scripts

The automation layer can be used to:

- Run daily trend collection
- Trigger product research workflows
- Send data to AI analysis
- Save results to Google Sheets or Notion
- Generate daily or weekly reports
- Send alerts to Telegram, email, or Slack

TrendPilot AI should provide workflow structures and templates, not copied workflow exports from unrelated authors unless clearly licensed and attributed.

---

### 4. AI Analysis Layer

This layer summarizes trend signals, compares product opportunities, and generates reports.

Possible tools:

- Dify
- LangChain
- OpenAI-compatible APIs
- Local LLMs
- Custom prompt workflows
- RAG pipelines

Typical AI tasks:

- Summarize public trend signals
- Extract product ideas
- Identify target audiences
- Detect content angles
- Estimate competition level
- Score product opportunities
- Generate report drafts
- Translate insights into different languages

The AI layer should avoid making unsupported claims. Every trend insight should include a source, confidence level, and risk note.

---

### 5. Product Opportunity Scoring

Each product idea can be scored by multiple dimensions.

Suggested scoring fields:

| Field | Score Range | Meaning |
|---|---:|---|
| Demand Signal | 1-5 | How strong the market interest appears |
| Social Visibility | 1-5 | How easy it is to create social content around it |
| Competition Level | 1-5 | How crowded the market appears |
| Price Potential | 1-5 | Whether the product can support healthy margins |
| Shipping Difficulty | 1-5 | Size, weight, fragility, and fulfillment complexity |
| Compliance Risk | 1-5 | Legal, platform, or category risk |
| Supplier Availability | 1-5 | How easy it may be to source |
| Differentiation Potential | 1-5 | Whether it can be improved or branded |

Example final formula:

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

This is not financial advice. It is only a research framework.

---

### 6. Report Generation

Reports can be exported as:

- Markdown
- Google Sheets
- Notion pages
- PDF files
- Telegram messages
- Email newsletters
- CSV files

A standard daily report may include:

- Product idea
- Source links
- Trend signal summary
- Target audience
- Main selling angle
- Suggested keywords
- Example content ideas
- Supplier notes
- Risk warnings
- Opportunity score

A weekly report may include:

- Top 10 trend opportunities
- Category comparison
- Region-specific demand notes
- Content strategy suggestions
- Risk and compliance notes
- Recommended next actions

---

## Example System Flow

```text
1. n8n starts a scheduled workflow every morning.
2. Firecrawl or another public-data tool collects trend pages.
3. The collected data is cleaned and saved.
4. An AI workflow summarizes trend signals.
5. Product ideas are scored with a structured prompt.
6. Results are saved to Google Sheets or Notion.
7. A daily summary is sent to Telegram or email.
8. A longer weekly report is generated in Markdown or PDF.
```

---

## License-Safe Principle

TrendPilot AI should not copy third-party project code.

Instead, this project may include:

- Tool links
- Integration notes
- Original prompts
- Original templates
- Original workflow diagrams
- Example data structures
- Educational documentation
- License comparison notes
- Safe implementation checklists

Always check each third-party project's license before using it in production.

Important license reminders:

- Do not remove original author attribution.
- Do not copy source code from projects with incompatible licenses.
- Do not repackage third-party tools as your own product.
- Do not imply official partnership with any referenced project.
- Clearly separate original TrendPilot AI content from external tool references.
- Use links and explanations instead of copying code whenever possible.

---

## Compliance Principles

TrendPilot AI is intended for ethical market research.

It should not be used for:

- Scraping private personal data
- Buying or selling personal contact databases
- Bypassing platform access restrictions
- Automated spam
- Fake engagement
- Review manipulation
- Account farming
- Fraudulent marketplace activity
- Misleading income claims

Recommended safe use cases:

- Public trend monitoring
- Product research
- Content inspiration
- Competitive research using public pages
- Internal research workflows
- Newsletter or report creation
- E-commerce opportunity analysis

---

## Project Goal

The goal of TrendPilot AI is to help users build their own AI-powered trend intelligence systems faster and more safely.

This repository focuses on:

- Clear architecture
- Curated tools
- Original prompts
- Report templates
- Workflow design
- Compliance awareness
- License-safe integration guidance

It is not an auto-money system, trading bot, scraping farm, or spam automation toolkit.
