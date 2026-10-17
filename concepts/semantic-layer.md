---
title: "semantic layer"
type: "Concept"
description: "A governed business-meaning layer over physical data that keeps metrics consistent across tools."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, analytics, governance]
sources:
  - "/sources/enterprise-business-intelligence-guide-to-strategy-adoption-impact.md"
  - "/sources/achieving-self-service-and-data-independence-in-an-sap-world.md"
  - "/sources/closing-the-sap-data-gap-how-ceos-get-clear-business-insight.md"
  - "/sources/closing-the-sap-data-gap-how-chros-turn-people-data-into-informed-action.md"
---

# semantic layer

A semantic layer sits between physical data and the tools that consume it, translating tables into governed business concepts — metrics, dimensions, relationships — so that "revenue" or "headcount" means the same thing in a dashboard, a CRM, and an AI agent. In this corpus it is the ingredient that separates trusted insight from executives who are buried in dashboards yet still argue over which number is correct.

## Key Claims

- The semantic layer keeps "revenue" meaning the same thing across Power BI, CRM, and AI agents; Snowflake's Open Semantic Interchange pushes a vendor-neutral standard for these definitions ([BI guide](/sources/enterprise-business-intelligence-guide-to-strategy-adoption-impact.md)).
- Metric ownership should be explicit and tool-agnostic — the guide recommends starting with 10–15 metrics and naming a business owner for each, such as the CFO owning revenue ([BI guide](/sources/enterprise-business-intelligence-guide-to-strategy-adoption-impact.md)).
- SAP Datasphere provides a business data fabric that preserves business context and logic over physical data, with a knowledge graph expressing semantic relationships between datasets ([self-service in SAP](/sources/achieving-self-service-and-data-independence-in-an-sap-world.md)).
- Staging and joining data in SAP Business Data Cloud makes it queryable as a specific, structured dataset; Joule then points natural-language questions at a verifiable logical dataset rather than wide-open data ([CEO's guide](/sources/closing-the-sap-data-gap-how-ceos-get-clear-business-insight.md)).
- A unified model standardizes metrics such as headcount and FTE across HR and finance, letting the CHRO and CFO work from one definition ([CHRO's guide](/sources/closing-the-sap-data-gap-how-chros-turn-people-data-into-informed-action.md)).
- AI needs unified data with the right semantics; without that foundation, natural-language querying returns hallucinations or irrelevant answers ([CEO's guide](/sources/closing-the-sap-data-gap-how-ceos-get-clear-business-insight.md)).

## Related

- [business intelligence](/concepts/business-intelligence.md) — the decision-ready output the layer serves
- [data governance](/concepts/data-governance.md) and [data quality](/concepts/data-quality.md) — the trust the layer encodes
- [master data management](/concepts/master-data-management.md) — consistent core entities under the metrics
- [SAP Datasphere](/entities/sap-datasphere.md), [SAP Business Data Cloud](/entities/sap-business-data-cloud.md), [Power BI](/entities/power-bi.md)
