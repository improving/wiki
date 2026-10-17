---
title: "Power BI"
type: "Entity"
description: "Microsoft's business intelligence and reporting tool, central to BI, visualization, and Fabric reporting."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, microsoft, analytics]
sources:
  - "/sources/why-your-power-bi-reports-are-slow.md"
  - "/sources/data-analysis-and-visualization-with-microsoft-power-bi.md"
  - "/sources/microsoft-copilot-for-power-bi.md"
  - "/sources/co-development-in-power-bi-version-control-and-continuous-integration.md"
  - "/sources/enterprise-business-intelligence-guide-to-strategy-adoption-impact.md"
  - "/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md"
---

# Power BI

Power BI is Microsoft's business intelligence and reporting tool, covering data cleansing, modeling, relationships, visualization, and publishing in one product with monthly updates. It is the recurring reference point in Improving's BI writing, from report performance to Copilot-assisted authoring and Fabric integration.

## Key Claims

- Desktop components are Power Query Editor, Model View, and Report View; a web service version also exists.
- Three standout visuals are Q&A (natural-language queries), Key Influencers (e.g. age 47–90 makes high income 11.96x more likely), and Smart Narratives (natural-language summaries).
- Query folding pushes transformations and aggregations down to the data source; standard connectors that cannot fold make Power BI pull all rows and inflate memory, processing, and storage costs.
- Copilot translates natural-language questions into Power BI queries and builds reports, but it needs a usable data model — Improving finds nearly 100% of clients seeking report help actually have a data model problem.
- Power BI Project (PBIP) files split reports and datasets into diffable text files trackable in Git; Fabric adds workspace Git integration and deployment pipelines requiring a Premium workspace.
- In [Microsoft Fabric](/entities/microsoft-fabric.md), Power BI integrates via Direct Lake to query [OneLake](/entities/onelake.md) without moving data; Fabric pricing is capacity-based but still requires Power BI Pro per user.

## Related

- [business intelligence](/concepts/business-intelligence.md) — decision-ready reporting
- [query folding](/concepts/query-folding.md) — pushing work to the source
- [Microsoft Fabric](/entities/microsoft-fabric.md) — the platform integrating Power BI
- [Microsoft Copilot](/entities/microsoft-copilot.md) — natural-language report generation
