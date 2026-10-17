---
title: "Unity Catalog"
type: "Entity"
description: "Databricks governance layer that puts policy and lineage inside the platform rather than beside it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data-governance, catalog, databricks]
sources:
  - "/sources/ai-governance-is-data-governance-with-consequences.md"
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/the-catalog-is-now-the-control-plane.md"
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
  - "/sources/why-80-of-governance-programs-fail-and-what-the-other-20-do-differently.md"
---

# Unity Catalog

Unity Catalog is Databricks' governance layer for data and AI assets. It appears throughout this corpus as the example of governance embedded in the platform rather than bolted on beside it.

## Key Claims

- Unity Catalog and MLflow Model Registry gave Blue Cross Blue Shield of Minnesota auditable training-data lineage.
- Databricks widened Unity Catalog to govern models, functions, agents, and MCP services under one identity, governance, and discovery layer.
- Runtime-captured lineage stays accurate where manual lineage documentation drifts.
- BCBSM encoded governance into a Databricks medallion platform with Unity Catalog and an onboarding framework.
- The catalog becomes the control plane, so policy follows data across engines; multi-engine estates still lack cross-catalog policy synchronization.

## Related

- [Embedded Governance](/concepts/embedded-governance.md) — the pattern it exemplifies
- [Runtime Lineage](/concepts/runtime-lineage.md) — the lineage it captures automatically
- [Data Catalog](/concepts/data-catalog.md) — the category it belongs to
- [Control plane](/concepts/control-plane.md) — what the catalog becomes
- [Databricks](/entities/databricks.md) — its vendor
- [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) — the reference implementation
- [Governance Belongs in the Platform, Not Next to It](/sources/governance-belongs-in-the-platform-not-next-to-it.md) — primary source
