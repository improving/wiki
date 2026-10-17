---
title: "Microsoft Fabric"
type: "Entity"
description: "Microsoft's unified SaaS analytics platform built on OneLake, consolidating Synapse, Data Factory, and Power BI."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, microsoft, analytics]
sources:
  - "/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md"
  - "/sources/business-transformation-through-microsoft-fabric-new-era-of-data.md"
  - "/sources/how-to-tell-if-your-data-platform-is-actually-modern.md"
  - "/sources/co-development-in-power-bi-version-control-and-continuous-integration.md"
  - "/sources/closing-the-sap-data-gap-a-cios-guide-to-clear-connected-data.md"
---

# Microsoft Fabric

Microsoft Fabric is Microsoft's unified SaaS analytics platform, consolidating data engineering, real-time analytics, machine learning, and business intelligence into one experience. Improving's writing frames it as an answer to fragmented data estates — separate tools, skills, and billing — and as a modern, interoperable data platform.

## Key Claims

- Fabric absorbs capabilities from [Azure Synapse](/entities/azure-synapse.md) (querying) and Azure Data Factory (ETL) into a single SaaS ecosystem, reducing the need for specialized infrastructure skills.
- [OneLake](/entities/onelake.md) is the shared data foundation, built on ADLS Gen2, minimizing redundant copies across analytics workloads.
- Data engineering supports lakehouses through Spark notebooks (Python/R); data warehousing offers SQL for structured data; Data Factory handles movement via data flows and pipelines.
- [Power BI](/entities/power-bi.md) integrates via Direct Lake to query the lakehouse without moving data, and [Microsoft Copilot](/entities/microsoft-copilot.md) assists with data wrangling, report generation, and data-science coding.
- Real-Time Hub plus Data Activator manages streaming events and triggers alerts or actions for manufacturing, logistics, and IoT monitoring.
- Fabric's Git integration and deployment pipelines bring version control and CI/CD to Power BI reports, but require a Premium workspace.
- Pricing starts at about $292 per month for the smallest capacity and is not tied to user count, though Power BI Pro is still required per user.
- SAP's Business Data Cloud includes standard connectors to Fabric, Databricks, and Snowflake, and Fabric is cited (with Snowflake and Databricks) as a platform that helps break vendor lock-in.

## Related

- [OneLake](/entities/onelake.md) — Fabric's unified, governed data lake
- [Power BI](/entities/power-bi.md) — the integrated reporting layer
- [lakehouse](/concepts/lakehouse.md) — lake storage with warehouse semantics
- [modern data platform](/concepts/modern-data-platform.md) — separated storage and compute with governance
