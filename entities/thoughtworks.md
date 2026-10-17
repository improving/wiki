---
title: "ThoughtWorks"
type: "Entity"
description: "Software consultancy whose data-mesh and data-contract practice work anchors much of this corpus's data governance writing."
created: '2026-10-17'
updated: '2026-10-17'
tags: [consultancy, data-governance, data-mesh]
sources:
  - "/sources/the-data-contract-is-an-api-for-trust.md"
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
---

# ThoughtWorks

A global software consultancy known for agile and continuous-delivery practice, and in this corpus the source of the data-contract and data-mesh framing that treats governance as an engineering artifact rather than a committee process. Its writers supply the recurring argument that data trust is built by enforceable specifications, not documentation.

## Work

ThoughtWorks practice writing frames the [data contract](/concepts/data-contract.md) as "an API for trust": a specification the system validates, not a document. It forces ownership and accountability as a precondition and moves enforcement to the producer, shifting accountability away from consumers. On [data mesh](/concepts/data-mesh.md), the same practice argues that domain ownership and data-as-a-product are tractable, while federated computational governance is the principle most organizations skip — and the one requiring enforcement at runtime. A related case study describes [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) encoding governance into a Databricks medallion platform with Unity Catalog and an onboarding framework.

## Key Claims

- A data contract is a specification the system validates, not documentation
- Contracts require data maturity and are a milestone, not a starting point
- Domain engineers often don't know which data are protected or regulated
- Governance must be enforced computationally at runtime, not through committees

## Related

- [Data Contract](/concepts/data-contract.md) — ThoughtWorks's core governance artifact
- [Data Mesh](/concepts/data-mesh.md) — the architecture its federated-governance writing addresses
- [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) — case study in embedded governance
- [The Data Contract Is an API for Trust](/sources/the-data-contract-is-an-api-for-trust.md) — primary source
