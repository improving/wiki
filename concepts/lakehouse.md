---
title: "lakehouse"
type: "Concept"
description: "An architecture combining data-lake storage with warehouse-style transactions and governance."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, analytics, architecture]
sources:
  - "/sources/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility.md"
  - "/sources/etl-modernization-informatica-to-confluent-databricks.md"
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md"
  - "/sources/business-transformation-through-microsoft-fabric-new-era-of-data.md"
  - "/sources/business-intelligence-advanced-analytics-companies.md"
---

# lakehouse

A lakehouse combines the cheap, flexible storage of a data lake with the transactional semantics and governance of a warehouse, so the same layer can serve BI, advanced analytics, and AI/ML without a separate copy. In this corpus it is the default landing architecture for modern data platforms, and the recurring lesson is that its value depends on governance embedded in the storage and compute layer rather than a catalog bolted alongside.

## Key Claims

- Databricks' lakehouse supports advanced analytics, AI/ML, and secure data collaboration, and was paired with Confluent managed streaming to replace brittle batch ETL ([etl modernization](/sources/etl-modernization-informatica-to-confluent-databricks.md)).
- An Improving engagement married Databricks lakehouse operational data to S/4HANA financial data using SAP Business Data Cloud's zero-delta copy, giving real-time access without maintaining a stale copy ([COO's guide](/sources/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility.md)).
- Governance must live inside the lake, not beside it: Databricks' Unity Catalog and Snowflake's Horizon enforce access control, runtime lineage, and audit logs below the engines that touch the data ([governance in the platform](/sources/governance-belongs-in-the-platform-not-next-to-it.md)).
- At BCBSM, a single governed lakehouse spanned 11 domains, 133 subdomains, and 88-plus suppliers with column-level PHI/PII control and HIPAA-satisfying audit logs ([governance in the platform](/sources/governance-belongs-in-the-platform-not-next-to-it.md)).
- Microsoft Fabric's OneLake implements a unified lake on ADLS Gen2 that links external sources such as Databricks and AWS to virtualize access and avoid moving data, organizing it into business domains where security and endorsement apply ([OneLake](/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md), [Fabric analytics](/sources/business-transformation-through-microsoft-fabric-new-era-of-data.md)).
- Without governance a lake becomes "a library without librarians" — a Data Hub is needed so users can find, filter, and explore what they are allowed to see ([OneLake](/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md)).
- Most modern analytics programs run a governed lake/warehouse layer — Snowflake, Databricks, or Fabric — feeding self-service dashboards such as Power BI, Tableau, or Looker ([BI buyer's guide](/sources/business-intelligence-advanced-analytics-companies.md)).

## Related

- [modern data platform](/concepts/modern-data-platform.md) — the broader ecosystem a lakehouse anchors
- [medallion architecture](/concepts/medallion-architecture.md) — the layered refinement pattern used inside Databricks lakehouses
- [data governance](/concepts/data-governance.md) and [embedded governance](/concepts/embedded-governance.md) — what keeps a lake trustworthy
- [data platform modernization](/concepts/data-platform-modernization.md) — the migration that lands on a lakehouse
- [Databricks](/entities/databricks.md), [Microsoft Fabric](/entities/microsoft-fabric.md), [OneLake](/entities/onelake.md), [Unity Catalog](/entities/unity-catalog.md)
