# License Risk Matrix

This document explains the license and attribution risks of external tools referenced by TrendPilot AI.

TrendPilot AI is designed as a license-safe starter kit. It should not copy, redistribute, repackage, or modify third-party source code unless the license clearly allows it and proper attribution is provided.

This document is not legal advice. Always review the original repository, license file, official documentation, and terms before using any external project in production.

---

## Core Rule

TrendPilot AI should integrate external projects by reference, not by copying.

Safe approach:

```text
Link to external tools
+ Write original explanations
+ Write original prompts
+ Write original templates
+ Write original workflow designs
+ Write original scoring models
+ Add attribution
```

Unsafe approach:

```text
Copy third-party source code
+ Remove license files
+ Rename it as TrendPilot AI
+ Repackage tools as our own product
+ Copy workflow exports without permission
+ Copy README sections without attribution
```

---

## Risk Level Meaning

| Risk Level | Meaning |
|---|---|
| Low | Generally safe to reference with attribution, but still verify license |
| Medium | Can be referenced, but copying files or templates may require caution |
| High | Do not copy code or redistribute files without careful license review |
| Very High | Avoid copying entirely; use only as inspiration or external reference |

---

## License Risk Overview

| Project / Tool | Known License / Status | Risk Level | Recommended Use |
|---|---|---:|---|
| n8n | Sustainable Use License / fair-code style licensing | High | External workflow automation tool only |
| Firecrawl | Mainly AGPL-3.0 for core project | High | External scraping / extraction tool only |
| Dify | Modified Apache 2.0 with additional conditions | Medium to High | External AI workflow platform only |
| Browser-use | MIT License | Medium | External browser automation tool, safe-use notes required |
| eCommerce-Skills | MIT License | Medium | Reference only; do not copy skill files directly |
| Product Research Agent | License may be unclear or project-specific | Very High | Inspiration only unless license is verified |
| Awesome n8n Templates | CC-BY 4.0 | Medium | Reference with attribution; avoid copying templates directly |
| Google Sheets | Proprietary service | Low | Data storage integration |
| Notion | Proprietary service | Low | Knowledge base / report archive integration |
| Telegram | Proprietary service / Bot API terms | Low to Medium | Delivery channel; avoid spam |
| Email providers | Provider-specific terms | Medium | Delivery channel; avoid unsolicited spam |

---

## 1. n8n

Repository:

https://github.com/n8n-io/n8n

### Role in TrendPilot AI

n8n is referenced as an external workflow automation tool.

It may be used to:

- Schedule daily trend collection
- Connect public data sources
- Send data to AI analysis tools
- Write results to Google Sheets or Notion
- Send reports to Telegram, Slack, or email

### Risk Level

High

### Why It Requires Caution

n8n is not a simple MIT-style project.

Its license and business model include usage limitations and commercial conditions. Users should review n8n's current license and official terms before building commercial products around it.

### Safe Use in TrendPilot AI

Allowed:

- Link to n8n
- Explain what n8n can do
- Create original workflow diagrams
- Create original workflow planning documents
- Create pseudo workflow structures
- Explain how n8n fits into a trend intelligence architecture

Avoid:

- Copying n8n source code
- Repackaging n8n as part of TrendPilot AI
- Removing n8n branding or license notices
- Selling a modified n8n product without license review
- Claiming official partnership with n8n

### Repository Rule

TrendPilot AI should treat n8n as:

```text
External dependency / optional workflow automation tool
```

Not as:

```text
Bundled TrendPilot AI source code
```

---

## 2. Firecrawl

Repository:

https://github.com/firecrawl/firecrawl

### Role in TrendPilot AI

Firecrawl is referenced as an external public web extraction tool.

It may be used to:

- Extract public web pages into readable formats
- Convert public pages into markdown or structured data
- Collect public trend pages
- Prepare source text for AI analysis

### Risk Level

High

### Why It Requires Caution

Firecrawl's core project is mainly associated with AGPL-3.0 licensing.

AGPL-3.0 has stronger obligations than permissive licenses, especially when modified software is used over a network.

Users should review the official license before modifying, hosting, or redistributing Firecrawl.

### Safe Use in TrendPilot AI

Allowed:

- Link to Firecrawl
- Explain where Firecrawl fits in the architecture
- Create original extraction schemas
- Create original prompts for analyzing scraped text
- Create compliance checklists for public data collection

Avoid:

- Copying Firecrawl source code
- Modifying Firecrawl source code inside this repository
- Repackaging Firecrawl as TrendPilot AI
- Publishing instructions for bypassing website restrictions
- Encouraging scraping of private, restricted, or login-protected data

### Repository Rule

TrendPilot AI should treat Firecrawl as:

```text
External public web extraction tool
```

Not as:

```text
Included crawler engine
```

---

## 3. Dify

Repository:

https://github.com/langgenius/dify

### Role in TrendPilot AI

Dify is referenced as an external AI workflow and LLM application platform.

It may be used to:

- Build AI workflow chains
- Manage prompts
- Generate trend summaries
- Score product opportunities
- Generate report drafts
- Connect knowledge bases or RAG workflows

### Risk Level

Medium to High

### Why It Requires Caution

Dify uses an open-source license with additional conditions. Users should review the current license before commercial deployment, SaaS usage, logo changes, or multi-tenant service usage.

### Safe Use in TrendPilot AI

Allowed:

- Link to Dify
- Explain Dify as an optional AI workflow layer
- Create original prompt templates
- Create original workflow concepts
- Create original input/output schemas
- Create original report templates

Avoid:

- Copying Dify source code
- Removing Dify branding or copyright notices
- Repackaging Dify as TrendPilot AI
- Teaching users how to bypass Dify license conditions
- Claiming official partnership with Dify

### Repository Rule

TrendPilot AI should treat Dify as:

```text
Optional external AI workflow engine
```

Not as:

```text
Bundled report generation backend
```

---

## 4. Browser-use

Repository:

https://github.com/browser-use/browser-use

### Role in TrendPilot AI

Browser-use is referenced as an external browser automation tool for AI agents.

It may be useful when research workflows require public web page interaction.

### Risk Level

Medium

### Why It Requires Caution

Browser automation tools can be useful, but they can also be misused for unsafe activities such as account farming, spam, scraping restricted data, or bypassing platform controls.

Even when the license is permissive, the use case can still be risky.

### Safe Use in TrendPilot AI

Allowed:

- Link to Browser-use
- Explain safe public-page-only use cases
- Create original browser automation guardrails
- Create ethical automation checklists
- Use it as an optional advanced module

Avoid:

- Automated account registration
- Login-based scraping
- CAPTCHA bypass
- Automated spam comments
- Automated direct messages
- Fake engagement
- Mass following or unfollowing
- Bypassing platform restrictions

### Repository Rule

TrendPilot AI should treat Browser-use as:

```text
Optional browser automation reference
```

Not as:

```text
Growth hacking or platform bypass tool
```

---

## 5. eCommerce-Skills

Repository:

https://github.com/nexscope-ai/eCommerce-Skills

### Role in TrendPilot AI

eCommerce-Skills is referenced as an external e-commerce AI skills framework.

It may help inspire product research, keyword analysis, competitor research, review analysis, and marketplace intelligence workflows.

### Risk Level

Medium

### Why It Requires Caution

Even when a project uses a permissive license, copying skill files directly can still create attribution, quality, compatibility, and maintenance issues.

TrendPilot AI should create its own original scoring models, prompts, and report formats.

### Safe Use in TrendPilot AI

Allowed:

- Link to the repository
- Mention it as an external reference
- Learn from its category structure
- Create original e-commerce research prompts
- Create original product opportunity scorecards
- Create original workflow documents

Avoid:

- Copying skill files directly
- Copying README tables directly
- Repackaging its skills as TrendPilot AI content
- Claiming compatibility without testing
- Using it as the only source of analysis logic

### Repository Rule

TrendPilot AI should treat eCommerce-Skills as:

```text
External e-commerce research reference
```

Not as:

```text
Copied skill library
```

---

## 6. Product Research Agent

Repository:

https://github.com/scarnyc/product-research-agent

### Role in TrendPilot AI

Product Research Agent is referenced as an external inspiration for AI-assisted product research.

It may help users understand how product comparison, shopping research, and review summarization can be structured.

### Risk Level

Very High unless license is verified

### Why It Requires Caution

If a repository does not clearly include a license, the default assumption should be:

```text
Do not copy, modify, or redistribute the code.
```

Public GitHub visibility does not automatically grant permission to reuse the code.

### Safe Use in TrendPilot AI

Allowed:

- Link to the project as inspiration
- Mention it as a reference
- Create original product research workflows
- Create original prompt templates
- Create original product comparison templates

Avoid:

- Copying source code
- Copying notebook files
- Copying requirements or implementation details
- Reusing code without verified license permission
- Claiming it as a dependency

### Repository Rule

TrendPilot AI should treat Product Research Agent as:

```text
Inspiration only unless license is verified
```

Not as:

```text
Reusable code source
```

---

## 7. Awesome n8n Templates

Repository:

https://github.com/enescingoz/awesome-n8n-templates

### Role in TrendPilot AI

Awesome n8n Templates is referenced as an external workflow template collection.

It may help users discover automation patterns and understand how n8n workflows are commonly structured.

### Risk Level

Medium

### Why It Requires Caution

Template collections may include work from many contributors. Even when reuse is allowed, attribution may be required.

The project is associated with CC-BY 4.0, which generally requires attribution when sharing or adapting content.

### Safe Use in TrendPilot AI

Allowed:

- Link to the repository
- Mention it as an external resource
- Use it as inspiration for workflow categories
- Create original trend intelligence workflow structures
- Add attribution if content is adapted

Avoid:

- Copying workflow JSON files directly without attribution
- Copying README sections directly
- Copying template descriptions directly
- Removing original author credit
- Presenting adapted templates as fully original

### Repository Rule

TrendPilot AI should treat Awesome n8n Templates as:

```text
External workflow inspiration and reference library
```

Not as:

```text
Source of copied workflow exports
```

---

## 8. Google Sheets

### Role in TrendPilot AI

Google Sheets is referenced as a lightweight data storage and review layer.

It may be used to:

- Store trend signals
- Track product scores
- Review AI-generated ideas
- Share simple dashboards
- Export CSV files

### Risk Level

Low

### Main Risks

- Storing sensitive information
- Exposing shared sheet links publicly
- Accidentally publishing private data
- API quota limitations
- Weak access control

### Safe Use

Allowed:

- Store public trend records
- Store opportunity scores
- Store source logs
- Share reviewed reports

Avoid:

- Storing private personal data
- Storing API keys
- Making private sheets public accidentally
- Storing scraped personal contact lists

---

## 9. Notion

### Role in TrendPilot AI

Notion is referenced as a knowledge base and report archive tool.

It may be used to:

- Archive weekly reports
- Store product ideas
- Organize research notes
- Create simple dashboards
- Share pages with a team or clients

### Risk Level

Low

### Main Risks

- Access permission mistakes
- Publishing private pages
- Storing sensitive data
- API setup issues

### Safe Use

Allowed:

- Store public research summaries
- Store internal report drafts
- Build a public knowledge base
- Archive trend reports

Avoid:

- Storing sensitive personal data
- Sharing private dashboards accidentally
- Storing API keys or tokens

---

## 10. Telegram and Email

### Role in TrendPilot AI

Telegram and email are referenced as report delivery channels.

They may be used to:

- Send daily trend alerts
- Send weekly report summaries
- Notify a team
- Deliver opt-in newsletters
- Send paid community updates

### Risk Level

Low to Medium

### Main Risks

- Spam
- Unsolicited mass messaging
- Poor unsubscribe handling
- Deliverability issues
- Telegram group abuse
- Leaking private report links

### Safe Use

Allowed:

- Send reports to opt-in users
- Send internal team alerts
- Send personal research digests
- Send paid community updates

Avoid:

- Mass unsolicited email
- Scraped email lists
- Automated cold DM spam
- Fake sender identity
- No unsubscribe option
- Sending misleading claims

---

## License-Safe Content Types

TrendPilot AI can safely focus on original content such as:

- System architecture diagrams
- Prompt templates
- Report templates
- Data schemas
- Scoring models
- Risk checklists
- Tool comparison tables
- Integration notes
- Pseudo workflows
- Educational documentation
- Example reports using fictional or public-safe data

---

## Content Types to Avoid

TrendPilot AI should avoid including:

- Third-party source code
- Third-party workflow exports without permission
- Third-party API keys or tokens
- Modified external project files
- Copied README sections
- Copied documentation pages
- Third-party logos without permission
- Marketplace data dumps
- Personal contact databases
- Private scraped data
- Creator content copied from social platforms

---

## Attribution Rules

When referencing an external project:

1. Include the project name.
2. Include the official URL.
3. Explain its role.
4. State that it is external.
5. Avoid implying official partnership.
6. Do not copy its code unless license review allows it.
7. Preserve required attribution when adapting licensed material.
8. Link to the original license when needed.

Recommended wording:

```text
This project references [Tool Name] as an external tool. TrendPilot AI does not include or redistribute its source code.
```

---

## Practical Repository Rules

Before adding a new file to TrendPilot AI, check:

- Is this file original?
- Does it copy third-party code?
- Does it copy third-party workflow exports?
- Does it include private data?
- Does it include API keys?
- Does it use third-party branding?
- Does it make income guarantees?
- Does it encourage unsafe automation?
- Does it require attribution?
- Is the source linked clearly?

If unsure, do not add the file until reviewed.

---

## Final Recommendation

The safest path is to build TrendPilot AI as:

```text
Original documentation
+ Original prompts
+ Original templates
+ Original scoring models
+ Original pseudo workflows
+ External links
+ Clear attribution
```

Not as:

```text
Copied code collection
+ Repackaged external tools
+ Scraping farm
+ Auto-money bot
+ License-risky bundle
```

TrendPilot AI should remain useful, ethical, source-aware, and license-safe.
