---
title: "Data Mesh"
type: "Concept"
description: "A decentralized data architecture with domain ownership, data-as-a-product, and federated computational governance."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data-architecture, governance, decentralization]
sources:
  - "/sources/publishing-a-catalog-is-not-the-same-as-running-a-registry.md"
  - "/sources/the-data-contract-is-an-api-for-trust.md"
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
---

# Data Mesh

Data mesh decentralizes data ownership to domains, treats data as a product, and replaces central committees with federated computational governance. Across this corpus the first principles are tractable; the fourth — federated computational governance — is the one organizations skip, because domains often lack the knowledge to comply and enforcement must be computational.

## Key Claims

- Domain ownership and data-as-a-product are tractable; federated computational governance is the principle most organizations skip.
- Domain engineers often don't know which data are protected or regulated, creating an accountability gap.
- Governance must be enforced computationally at runtime, not through committees and review.
- BCBSM encoded governance into a Databricks medallion platform with Unity Catalog and an onboarding framework.
- A data contract is a specification the system validates, not documentation, and forces ownership and accountability as a precondition.
- Contracts require data maturity: they are a milestone, not a starting point.
- Federated capability discovery via published catalogs solves cross-boundary discovery but is not a registry; crawled catalogs are static, self-reported metadata needing enrichment.

## Related

- [Data Contract](/concepts/data-contract.md) — the enforceable interface between domains
- [Data Ownership](/concepts/data-ownership.md) — the principle that shifts accountability to producers
- [Embedded Governance](/concepts/embedded-governance.md) and [runtime governance](/concepts/runtime-governance.md) — computational enforcement at runtime
- [federation](/concepts/federation.md) — cross-boundary discovery between domains
- [Data Catalog](/concepts/data-catalog.md) — the discovery surface domains publish
- [Unity Catalog](/entities/unity-catalog.md) — the platform BCBSM used to encode governance
- [The Fourth Principle: Federated Governance and the Hardest Problem in Data Mesh](/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md) — primary source
