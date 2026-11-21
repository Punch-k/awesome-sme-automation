# Awesome SME Automation

**Open-source software a small or mid-size business can install and run today, organised by the business process it automates.**
Each entry is a complete product (not a code snippet or a one-off template) and is re-checked against GitHub every week.

**Who it is for:** owners, operations managers and consultants who want to replace manual work or per-seat SaaS fees with
software they control. **What you get per tool:** what it runs end to end, a concrete SME use case, advantages, watch-outs,
licence and live activity.

## Contents

- [Workflow automation engines](#workflow-automation-engines) (5)
- [AI assistants and agent builders](#ai-assistants-and-agent-builders) (4)
- [Finance, invoicing and accounting](#finance-invoicing-and-accounting) (3)
- [All-in-one ERP](#all-in-one-erp) (3)
- [Documents, PDFs and e-signature](#documents-pdfs-and-e-signature) (5)
- [CRM, sales and marketing](#crm-sales-and-marketing) (7)
- [Customer support](#customer-support) (3)
- [Inventory, warehouse and supply chain](#inventory-warehouse-and-supply-chain) (3)
- [HR, time and projects](#hr-time-and-projects) (4)
- [Data, dashboards and internal tools](#data-dashboards-and-internal-tools) (5)
- [Starter stacks](#starter-stacks)
- [Workflow template libraries](#workflow-template-libraries)
- [How tools are chosen](#how-tools-are-chosen)

## What "ready to use" means here

Every tool listed:
1. is a **complete, self-hostable product** with documented installation (most also offer a hosted plan);
2. is **actively maintained**: a commit within the last 180 days, and the repository is not archived;
3. has its **licence shown**. "check terms" means the project uses a source-available, fair-code or custom licence: free to use for
   your own business in most cases, with limits on reselling or hosting it for others. Read it before you build a product on top.

The **Status** column shows licence, GitHub stars, month of the last commit, and **AI** where the tool has built-in AI features. It is refreshed automatically every week by `scripts/build.py`.

## Workflow automation engines

The glue: connect your apps, schedule jobs, add AI steps. Start here if you want to automate across tools.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[n8n](https://n8n.io)**<br>Visual workflows across hundreds of apps, with schedules, webhooks and AI agent steps | A 10-person agency syncs new deals from the CRM to invoicing, Slack and a Google Sheet, and has an AI agent draft first replies to inbound leads. | + Very large integration library and template gallery<br>+ Self-host or use their cloud<br>+ Native AI agent and LLM steps | − Fair-code licence limits reselling it as a service<br>− Self-hosting means you own updates and backups<br>− Big flows get hard to debug | Zapier, Make | check terms<br>★ 211.6k<br>2026-11<br>**AI** |
| **[Huginn](https://github.com/huginn/huginn)**<br>Agents that watch websites, feeds and inboxes and act when something changes | Alert the sales team when a competitor changes a price page or a tender is posted. | + MIT licence, mature<br>+ Excellent for monitoring and alerting<br>+ Fully self-hosted | − Dated interface<br>− Fewer modern SaaS integrations<br>− Ruby stack to maintain | IFTTT | MIT<br>★ 50.6k<br>2026-11 |
| **[Activepieces](https://www.activepieces.com)**<br>No-code automation flows with AI agents and MCP servers | An office manager builds form-to-CRM-to-email flows without code, and exposes them to AI assistants through MCP. | + Simple, friendly builder<br>+ Hundreds of MCP servers for AI agents<br>+ Open-source core | − Fewer integrations than n8n<br>− Some features only in paid editions | Zapier | check terms<br>★ 25.7k<br>2026-11<br>**AI** |
| **[Node-RED](http://nodered.org)**<br>Event-driven flows for devices, APIs and alerts | A small manufacturer sends a text when a machine sensor or warehouse freezer goes out of range. | + Apache-2.0, lightweight<br>+ Great for devices, APIs and events<br>+ Huge library of community nodes | − Interface is technical<br>− Fewer ready-made business-app connectors | Custom integration scripts | Apache-2.0<br>★ 23.9k<br>2026-11 |
| **[Windmill](https://windmill.dev)**<br>Turns scripts into scheduled workflows, internal apps and AI agents | An ops analyst turns Python scripts (price checks, report builds) into scheduled jobs with a simple UI for colleagues. | + Code-first: Python, TypeScript, SQL<br>+ Fast, with schedules, approvals and apps in one place<br>+ Self-hostable | − Needs someone who can code<br>− More than a non-technical team needs | Retool Workflows, Airflow | check terms<br>★ 18.7k<br>2026-11<br>**AI** |

## AI assistants and agent builders

Private assistants over your own documents, and visual builders for AI workflows.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Dify](https://dify.ai)**<br>Build AI assistants, RAG pipelines and agent workflows, then publish them as apps or APIs | Build a quote-drafting assistant that reads the price list and publish it as an internal app. | + Complete AI app platform: RAG, workflows, agents<br>+ Publish as web apps or APIs<br>+ Large community | − Licence restricts some multi-tenant SaaS uses<br>− Heavier stack to self-host | Custom GPTs, Copilot Studio | check terms<br>★ 161.6k<br>2026-11<br>**AI** |
| **[Open WebUI](https://openwebui.com)**<br>A private ChatGPT-style assistant on local (Ollama) or hosted models, with document chat | Give every employee a ChatGPT-style assistant that runs on the company's own server. | + Easy multi-user chat with local or hosted models<br>+ Document chat built in<br>+ Keeps data in-house | − Quality depends on the model and your hardware<br>− Check licence terms for branding conditions | ChatGPT Team | check terms<br>★ 159.2k<br>2026-11<br>**AI** |
| **[Langflow](http://www.langflow.org)**<br>Visual builder for AI agents and workflows, deployable as APIs | A developer prototypes an email-triage agent visually, then serves it as an API. | + MIT licence<br>+ Visual and flexible<br>+ Deploy flows as APIs | − Developer-oriented<br>− Flows can need updates between versions | Custom AI development | MIT<br>★ 156.8k<br>2026-11<br>**AI** |
| **[AnythingLLM](https://anythingllm.com)**<br>A private assistant that answers from your company documents, with agents | Staff ask 'what is our return policy for distributors?' and get answers with sources from company files. | + MIT licence, desktop and server versions<br>+ Point-and-click document Q&A<br>+ Works with local models | − Answers are only as good as the documents loaded<br>− Retrieval needs tuning for large archives | ChatGPT Enterprise knowledge base | MIT<br>★ 68.5k<br>2026-11<br>**AI** |

## Finance, invoicing and accounting

Quote-to-cash and bookkeeping without per-seat fees.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Invoice Ninja](https://invoiceninja.com)**<br>Quotes, invoices, recurring billing, online payments, projects and time tracking | A consultancy sends quotes, converts them to invoices, takes card payments and chases late payers automatically. | + Complete quote-to-cash with client portal<br>+ Many payment gateways<br>+ Recurring billing and time tracking | − Source-available, not OSI open source<br>− Some features tied to hosted plans | FreshBooks, Zoho Invoice | check terms<br>★ 10.6k<br>2026-11 |
| **[Akaunting](https://akaunting.com)**<br>Online accounting: invoices, bills, banking and financial reports | A shop owner records sales, bills and bank transactions and gets monthly P&L reports. | + Simple accounting for non-accountants<br>+ Multi-currency<br>+ App store for add-ons | − Many useful add-ons are paid<br>− Check licence terms before reselling | QuickBooks Online, Xero | check terms<br>★ 10.3k<br>2026-11 |
| **[Bigcapital](https://bigcapital.app)**<br>Double-entry accounting with inventory tracking and financial reporting | A wholesaler keeps double-entry books and stock values in one place. | + AGPL licence<br>+ Accounting plus inventory and reports<br>+ Modern interface | − Younger project, smaller community<br>− Fewer integrations than incumbents | QuickBooks | AGPL-3.0<br>★ 4.2k<br>2026-11 |

## All-in-one ERP

One system for sales, purchasing, stock, accounting and HR. Bigger setup, biggest payoff.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Odoo (Community)](https://www.odoo.com)**<br>Modular business apps: CRM, sales, purchase, inventory, accounting, website | A growing retailer starts with CRM and inventory and adds modules as it grows. | + Polished apps that work together<br>+ Huge module ecosystem<br>+ Large partner network | − Several key modules are Enterprise-only (paid)<br>− Customisation can get expensive | NetSuite, Microsoft Dynamics | check terms<br>★ 56.0k<br>2026-11 |
| **[ERPNext](https://frappe.io/erpnext)**<br>Full ERP: CRM, selling, buying, stock, manufacturing, accounting, projects | A 50-person distributor runs quotes, purchasing, stock, invoicing and HR in one system. | + GPL licence, genuinely full ERP<br>+ Active community and partner ecosystem<br>+ No per-user fees when self-hosted | − Real implementation project, weeks not hours<br>− Learning curve for staff | NetSuite, SAP Business One | GPL-3.0<br>★ 41.5k<br>2026-11 |
| **[Dolibarr](https://www.dolibarr.org)**<br>ERP and CRM for small companies: proposals, orders, invoices, stock, projects | A small trades business manages proposals, orders, invoices and stock without heavy setup. | + GPL licence, light and modular<br>+ Quick to start<br>+ Runs on cheap hosting | − Dated interface<br>− Fewer integrations | Zoho One | GPL-3.0<br>★ 7.9k<br>2026-11 |

## Documents, PDFs and e-signature

Paperless back office: capture, file, search and sign.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Stirling-PDF](https://stirling.com)**<br>Merge, split, convert, OCR and edit PDFs in the browser | Merge delivery notes, split scanned batches, OCR and compress PDFs without uploading them anywhere. | + Dozens of PDF tools in one place<br>+ Runs locally, files stay private<br>+ Very popular, active | − Not a document management system<br>− Check licence terms | Adobe Acrobat | check terms<br>★ 97.1k<br>2026-11 |
| **[Paperless-ngx](http://docs.paperless-ngx.com/)**<br>Scan, OCR, tag and archive every document so it is searchable | Every bill, receipt and contract is scanned or emailed in, read by OCR, tagged and searchable in seconds. | + GPL licence, excellent OCR and search<br>+ Email and scanner intake<br>+ Large community | − You manage storage and backups<br>− Needs initial tagging rules | Filing cabinets, Dropbox folders | GPL-3.0<br>★ 48.4k<br>2026-11 |
| **[DocuSeal](https://www.docuseal.com)**<br>Create fillable forms and collect e-signatures | Send NDAs and service agreements for signature from a template. | + AGPL licence<br>+ Easy form builder with an API<br>+ Self-hostable | − Legal validity of e-signatures varies by country<br>− Some features in paid plans | DocuSign | AGPL-3.0<br>★ 19.1k<br>2026-11 |
| **[Documenso](https://documenso.com)**<br>Send documents for e-signature with signing workflows | Contract signing with an audit trail, embedded in your own workflow through the API. | + AGPL licence<br>+ Modern interface and API<br>+ Self-hostable | − Younger product<br>− Some features in paid cloud plans | DocuSign | AGPL-3.0<br>★ 15.8k<br>2026-11 |
| **[Paperless-AI](https://clusterzx.github.io/paperless-ai/)**<br>AI that titles, tags and files documents in Paperless-ngx, with chat over the archive | New documents are titled, tagged and assigned to a correspondent automatically, and staff can ask questions of the archive. | + MIT licence<br>+ Removes manual filing<br>+ Works with local models | − Requires Paperless-ngx<br>− AI tags still need spot checks | Manual document filing | MIT<br>★ 6.1k<br>2026-11<br>**AI** |

## CRM, sales and marketing

Leads to customers: pipelines, campaigns, newsletters, booking.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Twenty](https://twenty.com)**<br>Modern CRM with pipelines, an API and workflow automation | A B2B startup tracks leads and deals in a clean CRM and automates follow-ups. | + Modern interface, API-first<br>+ Built-in workflows<br>+ Self-hostable | − Younger: fewer integrations than Salesforce or HubSpot<br>− Check licence terms for commercial use | Salesforce, HubSpot CRM | check terms<br>★ 61.3k<br>2026-11<br>**AI** |
| **[Cal (cal.diy)](https://cal.diy)**<br>Online booking pages and scheduling | Prospects book discovery calls from a link that respects your calendar. | + MIT licence<br>+ Booking pages and team scheduling<br>+ Self-hostable | − Project packaging recently changed (now cal.diy): check which features are included<br>− Calendar integrations need setup | Calendly | MIT<br>★ 50.3k<br>2026-11 |
| **[Medusa](https://medusajs.com)**<br>Commerce engine: products, carts, orders and inventory | A brand runs its online store back end (products, orders, inventory) on its own stack. | + Flexible, modular commerce engine<br>+ API-first<br>+ Large community | − Developer-heavy: you build or pick a storefront<br>− Check licence terms | Shopify Plus (back end) | check terms<br>★ 37.3k<br>2026-11 |
| **[listmonk](https://listmonk.app)**<br>Newsletters and mailing lists with analytics | Send the monthly newsletter to 20,000 customers through your own email provider. | + AGPL licence, very fast<br>+ Single binary, easy to run<br>+ Good analytics | − Needs an SMTP or email service<br>− Newsletters only, no automation journeys | Mailchimp | AGPL-3.0<br>★ 24.4k<br>2026-11 |
| **[Krayin CRM](https://krayincrm.com)**<br>Lead, pipeline and sales management | A small sales team runs a simple lead pipeline. | + MIT licence<br>+ Simple and extendable (Laravel)<br>+ Self-hostable | − Smaller ecosystem<br>− Basic reporting | Pipedrive | MIT<br>★ 24.2k<br>2026-11 |
| **[Mautic](https://www.mautic.org)**<br>Marketing automation: segments, campaigns, email and lead scoring | Nurture leads with segmented email campaigns and lead scoring. | + Full marketing automation at no licence cost<br>+ Segments, campaigns, scoring<br>+ Large community | − Complex to set up well<br>− Email deliverability is your responsibility | HubSpot Marketing, ActiveCampaign | check terms<br>★ 11.1k<br>2026-11 |
| **[EspoCRM](https://www.espocrm.com)**<br>CRM: leads, accounts, opportunities, email and workflows | A services firm manages accounts, opportunities and email in a customisable CRM. | + AGPL licence, mature<br>+ Highly customisable<br>+ Light to host | − Advanced extensions are paid<br>− Interface less modern | Zoho CRM | AGPL-3.0<br>★ 3.6k<br>2026-11 |

## Customer support

One inbox for chat, email and messaging, with tickets and SLAs.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Chatwoot](https://www.chatwoot.com/help-center)**<br>One shared inbox for website chat, email and messaging channels, with AI assistance options | Website chat, email and messaging all land in one shared inbox with canned replies and AI help. | + True omni-channel inbox<br>+ Mature, widely used<br>+ AI assistance options | − Some features in paid editions<br>− Check licence terms | Intercom, Zendesk | check terms<br>★ 40.3k<br>2026-11<br>**AI** |
| **[Zammad](https://zammad.org)**<br>Helpdesk ticketing across email, chat, phone and social | Support requests from email, phone and chat become tickets with owners and SLAs. | + AGPL licence, mature ticketing<br>+ Multi-channel<br>+ Good reporting | − Fairly heavy to self-host<br>− Less suited to live chat sales | Zendesk, Freshdesk | AGPL-3.0<br>★ 6.1k<br>2026-11 |
| **[Helpdesk (Frappe)](https://frappe.io/helpdesk)**<br>Ticketing with SLAs and a knowledge base | Ticketing with SLAs and a knowledge base, linked to ERPNext customers. | + AGPL licence<br>+ Modern interface<br>+ Fits the Frappe/ERPNext suite | − Best inside the Frappe ecosystem<br>− Smaller community | Freshdesk | AGPL-3.0<br>★ 3.5k<br>2026-11 |

## Inventory, warehouse and supply chain

Stock, purchasing and planning for companies that move physical goods.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[InvenTree](https://docs.inventree.org)**<br>Inventory, parts, stock locations, purchase and sales orders | A hardware maker tracks parts, stock locations, purchase orders and builds. | + MIT licence<br>+ Strong parts, BOM and stock control<br>+ API and plugins | − Geared to parts and manufacturing<br>− No demand forecasting | Fishbowl, spreadsheets | MIT<br>★ 7.9k<br>2026-11 |
| **[OpenBoxes](https://openboxes.com)**<br>Warehouse and inventory management with stock movement tracking (built for health supply chains) | A distributor tracks lots, expiry dates and stock movements across warehouses. | + EPL licence, proven in health supply chains<br>+ Lot and expiry tracking<br>+ Multi-location | − Niche focus<br>− Java/Grails stack to maintain | Entry-level WMS | EPL-1.0<br>★ 934<br>2026-11 |
| **[frePPLe](https://frepple.com)**<br>Demand forecasting, inventory planning and production planning | A manufacturer forecasts demand and plans purchasing and production against capacity. | + Real planning engine: forecasting, MRP, capacity<br>+ Open-source community edition<br>+ Excel-friendly | − Steep learning curve<br>− Some features only in the paid edition | Kinaxis, o9 (planning) | check terms<br>★ 784<br>2026-11 |

## HR, time and projects

People operations and delivery tracking.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Plane](http://plane.so)**<br>Projects, issues, cycles and docs | A team plans projects, tasks and sprints without per-seat fees. | + AGPL licence, modern<br>+ Issues, cycles and docs<br>+ Self-hostable | − Some features in paid editions<br>− Younger than Jira | Jira, Asana, ClickUp | AGPL-3.0<br>★ 62.9k<br>2026-11 |
| **[Frappe HR](https://frappe.io/hr)**<br>HR and payroll: leave, attendance, expenses, payroll | Leave, attendance, expense claims and payroll for a 40-person company. | + GPL licence<br>+ Payroll included<br>+ Integrates with ERPNext | − Payroll rules need local configuration<br>− Learning curve | BambooHR, Gusto (HR side) | GPL-3.0<br>★ 9.1k<br>2026-11 |
| **[Kimai](https://www.kimai.org)**<br>Time tracking and timesheets, with invoice exports | Consultants log hours per client and export them for invoicing. | + AGPL licence<br>+ Simple, multi-user time tracking<br>+ Plugins and exports | − Some plugins are paid<br>− Time tracking only | Harvest, Toggl | AGPL-3.0<br>★ 5.2k<br>2026-11 |
| **[OrangeHRM](https://github.com/orangehrm/orangehrm)**<br>Employee records, leave, time and recruitment | Keep employee records, leave and recruitment in one place. | + GPL licence, widely used<br>+ Covers core HR<br>+ Self-hostable | − Some modules only in the paid edition<br>− Dated interface | BambooHR | GPL-3.0<br>★ 1.2k<br>2026-11 |

## Data, dashboards and internal tools

See the numbers and build simple internal apps on top of them.

| Tool | Use case | Advantages | Disadvantages | Replaces | Status |
|---|---|---|---|---|---|
| **[Apache Superset](https://superset.apache.org/)**<br>BI dashboards and data exploration | An analyst builds detailed dashboards across several data sources. | + Apache-2.0<br>+ Powerful charts and SQL<br>+ Scales well | − More technical than Metabase<br>− Heavier setup | Tableau, Looker | Apache-2.0<br>★ 75.6k<br>2026-11 |
| **[NocoDB](https://nocodb.com)**<br>A spreadsheet-style database on top of your data, with an API | Turn a messy supplier spreadsheet into a shared database with forms and an API. | + Airtable-style interface<br>+ Works on top of your own database<br>+ API out of the box | − Check licence terms<br>− Not a full app builder | Airtable | check terms<br>★ 65.6k<br>2026-11 |
| **[Metabase](https://metabase.com)**<br>Dashboards and questions on your business data, no SQL required | The owner sees sales, margin and stock dashboards from the company database every Monday. | + Easiest BI for non-technical users<br>+ Alerts and scheduled reports<br>+ Large community | − Embedding, SSO and some features are paid<br>− Check licence terms | Tableau, Power BI (basic) | check terms<br>★ 50.5k<br>2026-11 |
| **[Appsmith](https://www.appsmith.com)**<br>Build admin panels, internal tools and dashboards on your databases and APIs | Build an order-lookup and returns-approval tool on the existing database. | + Apache-2.0<br>+ Many database and API connectors<br>+ Self-hostable | − Needs some JavaScript<br>− Maintenance as apps grow | Retool | Apache-2.0<br>★ 41.3k<br>2026-11 |
| **[ToolJet](https://tooljet.com)**<br>Build internal tools and workflows on your data | Build internal approval workflows and dashboards, with AI help generating the app. | + AGPL licence<br>+ AI-assisted app building<br>+ Many connectors | − Technical setup<br>− Some features in paid editions | Retool | AGPL-3.0<br>★ 41.3k<br>2026-11<br>**AI** |

## Starter stacks

Proven combinations of the tools above, by business need. Each runs on one small server.

| Stack | For | Tools | How it fits together |
|---|---|---|---|
| **Back office in a box** | Service businesses drowning in invoices and paper | Invoice Ninja, Paperless-ngx, Paperless-AI, DocuSeal, n8n | Quote and invoice clients in Invoice Ninja; every receipt, bill and contract is scanned into Paperless-ngx and auto-filed by Paperless-AI; contracts go out for signature through DocuSeal; n8n ties them together (for example, a signed contract creates the client and first invoice). |
| **Sales and support team** | Teams that sell and serve customers online | Twenty, Cal (cal.diy), Chatwoot, listmonk, n8n | Leads land in Twenty; prospects book calls through Cal; conversations from chat, email and messaging arrive in one Chatwoot inbox; listmonk sends the newsletter; n8n syncs contacts and logs conversations to the CRM. |
| **Operations and inventory** | Companies that buy, stock and ship physical goods | InvenTree, frePPLe, Metabase, n8n | Track parts, stock and purchase orders in InvenTree (or run the whole business in ERPNext); plan demand and replenishment in frePPLe; watch stock, service level and spend in Metabase; n8n sends low-stock and late-order alerts. |
| **Private AI for the whole company** | Teams that want ChatGPT-style help without sending data out | Open WebUI, AnythingLLM, Dify | Run models locally with Ollama behind Open WebUI for everyday questions; load policies, price lists and manuals into AnythingLLM so staff get answers with sources; build specific assistants (quote drafting, ticket replies) in Dify. |

## Workflow template libraries

Ready-to-import n8n workflows. Useful starting points, but templates are not tested here and quality varies: check each one, and its licence and source, before using it with real data. n8n's official gallery is at [n8n.io/workflows](https://n8n.io/workflows).

| Library | What it is | Licence | Stars | Updated |
|---|---|---|---|---|
| [awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates) | 280+ ready-to-import n8n workflows (Gmail, Telegram, Slack, Discord...). | check terms | 26.5k | 2026-09-12 |
| [n8n-workflows](https://github.com/Zie619/n8n-workflows) | Thousands of n8n workflows gathered from public sources, including n8n's own gallery. Check provenance before reuse. | MIT | 57.3k | 2026-06-24 |

## How tools are chosen

- Complete products a business can run, not libraries or demos.
- Self-hostable, so you can keep your data, with a documented install.
- Maintained (see the bar above) and with a visible licence.
- Advantages and disadvantages are written for an SME decision-maker: cost, setup effort, lock-in and licence limits.
- Excluded on 2026-11-20: Flowise (repository archived), Automatisch (no recent commits).

**Contributing:** add an entry to `catalog.json` and `data/notes.json`, run `python scripts/build.py`, and open a pull request.
Include a real use case and at least one honest disadvantage.

**Disclaimer:** descriptions are a starting point, not a recommendation for your situation. Check licences, security and
compliance (for example payroll or e-signature rules in your country) before going live.

---
Last refreshed: 2026-11-20 · 42 tools · Maintained by [Prapanch Kokkalemada](https://punch-k.github.io/Portfolio/)
