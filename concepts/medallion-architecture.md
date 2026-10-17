---
title: "medallion architecture"
type: "Concept"
description: "Layering data into bronze, silver, and gold zones of increasing refinement."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, architecture, databricks]
sources:
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
  - "/sources/etl-modernization-informatica-to-confluent-databricks.md"
---

# medallion architecture

The medallion architecture is a layered data pattern — commonly described as bronze (raw), silver (cleansed/conformed), and gold (curated, business-ready) zones — that refines data progressively as it moves through a lakehouse. It appears in this corpus as the Databricks layout chosen for a large, governed data-mesh implementation; coverage is otherwise thin, and the pattern is best read as the layered counterpart to a [lakehouse](/concepts/lakehouse.md).

## Key Claims

- Improving built the BCBSM data platform on a Databricks medallion architecture with Unity Catalog enforcing access and lineage at the storage layer ([federated governance](/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md)).
- That platform spanned 11 domains, 133 subdomains, and 88-plus data suppliers, with governance encoded into the platform rather than trained into domain teams ([federated governance](/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md)).
- The layered approach pairs with embedded governance: lineage and access controls are enforced as data moves between zones, not documented afterward ([federated governance](/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md)).
- Databricks' lakehouse, the substrate medallion layering runs on, supports advanced analytics, AI/ML, and secure data collaboration ([ETL modernization](/sources/etl-modernization-informatica-to-confluent-databricks.md)).
- Successful layered/federated implementations started small and invested in the self-serve platform first ([federated governance](/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md)).

## Related

- [lakehouse](/concepts/lakehouse.md) — the storage architecture medallion zones sit inside
- [data governance](/concepts/data-governance.md) and [embedded governance](/concepts/embedded-governance.md) — enforcement across the zones
- [data mesh](/concepts/data-mesh.md) — the decentralized model the named case implemented
- [Databricks](/entities/databricks.md), [Unity Catalog](/entities/unity-catalog.md)
