# Tool Map

This document maps the external tools and GitHub projects referenced by TrendPilot AI.

TrendPilot AI does not copy or redistribute third-party source code.  
It provides original documentation, workflow ideas, prompt templates, report templates, scoring models, and safe integration guidance.

---

## Tool Map Overview

| Tool / Project | Main Role | Best Used For | Risk Level |
|---|---|---|---|
| n8n | Workflow automation | Scheduling, connecting services, report delivery | Medium |
| Firecrawl | Web data extraction | Public web scraping, search, page-to-markdown extraction | Medium |
| Dify | AI workflow orchestration | LLM workflows, prompt chains, report generation | Medium |
| Browser-use | Browser automation | AI-controlled browser tasks on public web pages | Medium to High |
| eCommerce-Skills | E-commerce research framework | Product research, competitor analysis, keyword analysis | Medium |
| Product Research Agent | Product research reference | Product comparison and AI-assisted research workflows | Medium |
| Awesome n8n Templates | Workflow reference library | Learning workflow structures and automation patterns | Low to Medium |
| Google Sheets | Data storage | Lightweight structured records and scoring tables | Low |
| Notion | Knowledge base | Research notes, dashboards, report archives | Low |
| Telegram / Email | Delivery channels | Daily alerts and report delivery | Low |

---

## 1. n8n

Repository:

https://github.com/n8n-io/n8n

### Role in TrendPilot AI

n8n can be used as the workflow automation layer.

It can connect different tools together and run scheduled workflows.

Example tasks:

- Run a daily trend collection workflow
- Trigger public data collection
- Send collected data to an AI analysis workflow
- Save results to Google Sheets or Notion
- Send reports to Telegram, email, or Slack
- Create recurring weekly report tasks

### Strengths

- Visual workflow builder
- Large integration ecosystem
- Supports scheduled automation
- Can connect APIs, webhooks, databases, and AI tools
- Good for non-developers and builders who want low-code automation

### Possible Limitations

- Some advanced workflows still require technical setup
- Self-hosting requires server management
- Public workflows from other users may have unclear licensing
- Complex workflows can become hard to maintain
- API rate limits and platform rules still need to be respected

### License and Safety Notes

TrendPilot AI should not copy or redistribute n8n source code.

It may provide:

- Original workflow diagrams
- Original workflow descriptions
- Original field mappings
- Original node planning documents
- Links to n8n documentation
- Example workflow concepts

It should avoid:

- Copying third-party workflow exports without permission
- Presenting n8n as part of TrendPilot AI
- Removing attribution from external workflow templates
- Implying official partnership with n8n

### What TrendPilot AI Adds

TrendPilot AI can provide:

- Trend intelligence workflow design
- Daily report workflow structure
- Safe data collection checklist
- Product opportunity scoring framework
- Report delivery logic
- Non-technical implementation notes

---

## 2. Firecrawl

Repository:

https://github.com/firecrawl/firecrawl

### Role in TrendPilot AI

Firecrawl can be used as a public web data extraction layer.

It can help convert web pages into structured text or markdown that AI systems can analyze.

Example tasks:

- Collect public product pages
- Extract article content
- Convert marketplace category pages into readable text
- Collect public trend report pages
- Search and scrape public web sources
- Prepare clean text for AI analysis

### Strengths

- Designed for AI-readable web extraction
- Can convert web pages into structured formats
- Useful for building research agents
- Helpful for public trend and product research workflows

### Possible Limitations

- Web scraping rules vary by website
- Some websites may block automated access
- Some sources may require login and should be avoided
- Scraped content should not be republished directly
- Overuse can create compliance or rate-limit issues

### License and Safety Notes

TrendPilot AI should not copy or redistribute Firecrawl source code.

It may provide:

- Integration notes
- Public data collection patterns
- Example extraction fields
- Prompt templates for analyzing extracted pages
- Safe usage checklists

It should avoid:

- Copying Firecrawl source code
- Repackaging Firecrawl as a TrendPilot AI component
- Encouraging scraping of private or restricted data
- Encouraging bypassing anti-bot systems

### What TrendPilot AI Adds

TrendPilot AI can define:

- Which public sources are appropriate
- What fields to extract
- How to summarize source content
- How to score trend signals
- How to cite or record sources
- How to avoid unsafe scraping behavior

---

## 3. Dify

Repository:

https://github.com/langgenius/dify

### Role in TrendPilot AI

Dify can be used as an AI workflow and LLM orchestration layer.

It can help build structured AI workflows for trend analysis, product scoring, and report generation.

Example tasks:

- Turn raw trend data into summaries
- Extract product ideas from source text
- Generate opportunity scorecards
- Produce daily or weekly reports
- Create reusable prompt chains
- Build RAG-style knowledge workflows

### Strengths

- Visual AI workflow builder
- Supports prompt management
- Can connect knowledge bases
- Useful for non-developers building AI apps
- Good for repeatable report generation workflows

### Possible Limitations

- Requires proper prompt design
- AI outputs may hallucinate if sources are weak
- Users still need to verify data
- Deployment and model costs need to be managed
- Licensing and usage terms should be reviewed before commercial use

### License and Safety Notes

TrendPilot AI should not copy or redistribute Dify source code.

It may provide:

- Original prompt templates
- AI workflow concepts
- Report structures
- Data schema examples
- Source verification checklists
- Hallucination-reduction guidelines

It should avoid:

- Copying Dify code
- Rebranding Dify as TrendPilot AI
- Claiming unsupported data accuracy
- Generating reports without source references

### What TrendPilot AI Adds

TrendPilot AI can provide:

- E-commerce trend prompt chains
- Product opportunity scoring prompts
- Risk analysis prompts
- Report templates
- Structured output formats
- Human review guidelines

---

## 4. Browser-use

Repository:

https://github.com/browser-use/browser-use

### Role in TrendPilot AI

Browser-use can be used as a browser automation layer for AI agents.

It is useful when a workflow needs to interact with public web pages through a browser interface.

Example tasks:

- Navigate public pages
- Click through public category pages
- Collect visible public information
- Assist with repetitive research browsing
- Extract information from pages that are difficult to access through static scraping

### Strengths

- Allows AI agents to use a browser
- Useful for complex public web workflows
- Can handle page interaction better than simple scraping
- Helpful for research tasks that require navigation

### Possible Limitations

- Higher platform policy risk than simple public-page reading
- May trigger anti-bot systems
- Browser automation can be fragile
- It should not be used to bypass login, paywalls, or access controls
- Requires careful guardrails to avoid unsafe automation

### License and Safety Notes

TrendPilot AI should not copy or redistribute Browser-use source code.

It may provide:

- Safe browser automation scenarios
- Guardrail checklists
- Public data usage guidelines
- Research workflow examples
- Risk warnings

It should avoid:

- Teaching bypass techniques
- Automating spam behavior
- Logging into accounts to collect restricted data
- Collecting private user information
- Creating account farming workflows

### What TrendPilot AI Adds

TrendPilot AI can provide:

- Ethical browser automation boundaries
- Use-case selection rules
- Public-page-only workflow examples
- Human-in-the-loop review steps
- Safe research patterns

---

## 5. eCommerce-Skills

Repository:

https://github.com/nexscope-ai/eCommerce-Skills

### Role in TrendPilot AI

eCommerce-Skills can be referenced as an e-commerce research framework.

It is useful for thinking about product research, competitor tracking, keyword research, business analytics, and marketplace analysis.

### Strengths

- Focused on e-commerce tasks
- Relevant to product research
- Can inspire structured research workflows
- Useful as a reference for AI agent capabilities in commerce

### Possible Limitations

- It may not provide real-time data by itself
- It may require external data sources or APIs
- Some marketplace data may be restricted
- Users must check the license and usage terms before reuse

### License and Safety Notes

TrendPilot AI should not copy or redistribute eCommerce-Skills source code.

It may provide:

- Original e-commerce research templates
- Original opportunity scoring models
- Original report structures
- Links to the project as an external reference

It should avoid:

- Copying its skills directly without license review
- Repackaging its skill files as TrendPilot AI content
- Claiming compatibility without testing

### What TrendPilot AI Adds

TrendPilot AI can provide:

- A more complete trend intelligence framework
- Compliance-first data source guidance
- Cross-platform research structure
- Report and newsletter templates
- Monetization-friendly report formats

---

## 6. Product Research Agent

Repository:

https://github.com/scarnyc/product-research-agent

### Role in TrendPilot AI

Product Research Agent can be referenced as an example of AI-assisted product research.

It is useful for understanding how AI can help compare products, summarize product information, and support shopping or product research decisions.

### Strengths

- Product research focused
- Useful for understanding agent-style research
- Can inspire product comparison workflows
- Helpful reference for product intelligence logic

### Possible Limitations

- May depend on specific APIs
- May focus more on shopping comparison than trend intelligence
- May not include compliance or source-risk logic
- May not be designed for recurring trend reports

### License and Safety Notes

TrendPilot AI should not copy or redistribute Product Research Agent source code.

It may provide:

- Conceptual references
- Original comparison templates
- Original product scoring frameworks
- Links to the project as an external tool

It should avoid:

- Copying implementation files
- Using its code without license review
- Rebranding its workflow as TrendPilot AI

### What TrendPilot AI Adds

TrendPilot AI can add:

- Trend monitoring layer
- Source risk classification
- Report generation templates
- Product opportunity scoring
- Cross-border e-commerce use cases
- Human review process

---

## 7. Awesome n8n Templates

Repository:

https://github.com/enescingoz/awesome-n8n-templates

### Role in TrendPilot AI

Awesome n8n Templates can be used as a reference library for workflow structure and automation ideas.

It can help users understand what kinds of workflows are possible with n8n.

### Strengths

- Useful for learning automation patterns
- Good source of workflow inspiration
- Helps users understand common n8n use cases
- Can reduce learning time

### Possible Limitations

- Individual workflow templates may have different authors
- License status may vary by template
- Some templates may become outdated
- Some workflows may rely on paid APIs or unavailable services

### License and Safety Notes

TrendPilot AI should not copy workflow exports unless their license clearly allows reuse and attribution is provided.

It may provide:

- Links to external template collections
- Original workflow concepts
- Original n8n node planning documents
- Educational notes

It should avoid:

- Copying workflow JSON from other authors without permission
- Removing attribution
- Uploading third-party workflow exports as TrendPilot AI templates

### What TrendPilot AI Adds

TrendPilot AI can provide:

- Original trend-specific workflow blueprints
- Report automation structures
- Safe public data collection logic
- E-commerce research workflow planning

---

## 8. Google Sheets

### Role in TrendPilot AI

Google Sheets can be used as a lightweight database for early versions of a trend intelligence system.

Example use cases:

- Store collected trend signals
- Track product opportunity scores
- Build simple dashboards
- Share research with a small team
- Export CSV reports

### Strengths

- Easy to use
- Familiar to most users
- Works well with automation tools
- Good for MVP workflows
- Easy to review manually

### Possible Limitations

- Not ideal for very large datasets
- Requires careful access control
- API quotas may apply
- Sensitive data should not be stored casually

### What TrendPilot AI Adds

TrendPilot AI can provide:

- Suggested column structures
- Opportunity scoring fields
- Report-ready table formats
- Manual review workflows

---

## 9. Notion

### Role in TrendPilot AI

Notion can be used as a research knowledge base and report archive.

Example use cases:

- Store weekly trend reports
- Organize product ideas
- Maintain source notes
- Build a simple trend dashboard
- Share research pages with clients or team members

### Strengths

- Easy to organize
- Good for written reports
- Friendly interface
- Works well with AI-generated summaries
- Useful for paid report archives

### Possible Limitations

- API setup may require technical steps
- Not ideal for heavy automation at scale
- Access permissions should be managed carefully

### What TrendPilot AI Adds

TrendPilot AI can provide:

- Report page templates
- Category structures
- Product research database fields
- Weekly report formats

---

## 10. Telegram and Email

### Role in TrendPilot AI

Telegram and email can be used as delivery channels for daily or weekly trend intelligence reports.

Example use cases:

- Send daily product trend alerts
- Deliver weekly market summaries
- Notify users when a high-score opportunity appears
- Send internal team digests

### Strengths

- Easy to receive
- Good for alerts
- Good for simple paid communities
- Works well with n8n and other automation tools

### Possible Limitations

- Should not be used for spam
- Email deliverability may require setup
- Telegram groups need moderation
- Paid report access control needs planning

### What TrendPilot AI Adds

TrendPilot AI can provide:

- Daily digest templates
- Weekly report formats
- Alert message structures
- Subscriber-safe delivery guidelines

---

## Integration Strategy

TrendPilot AI should integrate external tools by reference, not by copying.

Safe integration methods:

- Link to external projects
- Explain what each tool is useful for
- Provide original workflow diagrams
- Provide original prompts
- Provide original report templates
- Provide original data schemas
- Provide safe usage checklists

Unsafe integration methods:

- Copying third-party source code
- Copying third-party workflow exports without permission
- Removing original licenses
- Repackaging external tools as original code
- Claiming official partnership
- Encouraging platform restriction bypass
- Building spam or fake engagement automation

---

## Recommended MVP Stack

A simple MVP version of TrendPilot AI can be built with:

| Layer | Tool |
|---|---|
| Scheduler | n8n |
| Public data extraction | Firecrawl or RSS |
| AI analysis | Dify or OpenAI-compatible API |
| Data storage | Google Sheets |
| Report format | Markdown |
| Delivery | Telegram or Email |

Example MVP flow:

1. n8n runs every morning.
2. Public trend pages are collected.
3. AI summarizes signals.
4. Product ideas are scored.
5. Results are saved to Google Sheets.
6. A short report is sent to Telegram or email.

---

## Recommended Advanced Stack

An advanced version can include:

| Layer | Tool |
|---|---|
| Scheduler | n8n |
| Public data extraction | Firecrawl |
| Browser interaction | Browser-use |
| AI workflow | Dify |
| Data storage | Google Sheets, Notion, or database |
| Report generation | Markdown, PDF, or webpage |
| Delivery | Telegram, email, Notion, newsletter |
| Human review | Manual approval step |
| Monetization | Paid newsletter, paid reports, consulting, templates |

---

## Final Note

The value of TrendPilot AI is not in copying existing tools.

The value is in connecting ideas safely:

- What to collect
- Why to collect it
- How to classify risk
- How to analyze signals
- How to score opportunities
- How to generate reports
- How to avoid unsafe or unethical automation

TrendPilot AI should remain a clean, useful, license-safe research toolkit.
