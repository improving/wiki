---
title: "Data Contract"
type: "Concept"
description: "An enforceable specification of a dataset's schema, ownership, and SLOs, validated by the system rather than documented in a committee."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data-governance, data-engineering, contracts]
sources:
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/the-data-contract-is-an-api-for-trust.md"
  - "/sources/the-policy-binder-didnt-change-anyones-behavior.md"
  - "/sources/your-stakeholders-are-your-data-quality-system.md"
---

# Data Contract

A data contract applies API-contract thinking to data: schema, ownership, and service levels become a specification the system validates at build and runtime, rather than documentation a committee maintains. In this corpus it is the mechanism that shifts accountability from consumers to producers and makes governance the default.

## Key Claims

- A data contract is a specification the system validates, not a document; enforcement at the producer shifts accountability upstream.
- Contracts force ownership and accountability as a precondition — you cannot contract data nobody owns.
- Contracts require data maturity and are a milestone, not a starting point.
- dbt Core v1.5 access, contracts, and versions enforce governance at build time.
- 74% of data professionals say stakeholders catch data quality issues before the data team, which is the symptom contracts and ownership address.
- Observability without defined ownership turns a fifteen-hour incident into a week.

## Related

- [Data Governance](/concepts/data-governance.md) — the program contracts operationalize
- [Policy as Code](/concepts/policy-as-code.md) — contracts are policy expressed on data
- [Embedded Governance](/concepts/embedded-governance.md) — governance inside the platform
- [Data Ownership](/concepts/data-ownership.md) — the precondition contracts force
- [dbt](/entities/dbt.md) — tooling that enforces contracts at build time
- [The Data Contract Is an API for Trust](/sources/the-data-contract-is-an-api-for-trust.md) — primary source
