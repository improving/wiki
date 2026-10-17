---
title: "OneLake"
type: "Entity"
description: "Microsoft Fabric's unified, governed data lake that organizes data into business domains with endorsement."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, microsoft, governance]
sources:
  - "/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md"
  - "/sources/business-transformation-through-microsoft-fabric-new-era-of-data.md"
---

# OneLake

OneLake is the unified data lake at the foundation of [Microsoft Fabric](/entities/microsoft-fabric.md), built on ADLS Gen2. It combines files and structured sources with the users who can access them, and its organizing idea is governance: data lives in business domains where security and endorsement apply.

## Key Claims

- OneLake is Fabric's shared data foundation, minimizing redundant copies across analytics workloads.
- It can link external sources such as Azure Data Lake, Databricks, and AWS to virtualize access and eliminate moving data.
- Data is organized into domains (Finance, Sales, Operations) where governance, security, and endorsement apply.
- Without governance, data lakes become chaotic — the author's "library without librarians" analogy.
- OneLake's Data Hub, in the Power BI/Fabric portal, lets users find, filter, and explore items they can access.
- [Power BI](/entities/power-bi.md) queries OneLake via Direct Lake without moving data.

## Related

- [Microsoft Fabric](/entities/microsoft-fabric.md) — the platform OneLake underpins
- [lakehouse](/concepts/lakehouse.md) — the unified lake architecture
- [data governance](/concepts/data-governance.md) — domains and endorsement
- [data integration](/concepts/data-integration.md) — virtualizing external sources
