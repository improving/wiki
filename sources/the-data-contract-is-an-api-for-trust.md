---
title: "The Data Contract Is an API for Trust"
type: "Source Summary"
description: "Data contracts treat data like a versioned service interface, and their real consequence is forcing organizational ownership."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-data-contract-is-an-api-for-trust/the-data-contract-is-an-api-for-trust.md"
---

# The Data Contract Is an API for Trust — Summary

**Original source**: `references/devlinliles.com/the-data-contract-is-an-api-for-trust/the-data-contract-is-an-api-for-trust.md`

## Summary

Andrew Jones at GoCardless reframed data quality by asking what if data had an interface the way services do. A [data contract](/concepts/data-contract.md) is an enforceable specification — schema, ownership, SLOs, compatibility guarantees — that the system validates, not documentation anyone can ignore. Enforcement moves accountability to the producer. The governance consequence is organizational: a contract cannot exist without an owner. Ascend's modernization shows ownership as the prerequisite, and the pattern fits [data mesh](/concepts/data-mesh.md) because "data as a product" needs an enforceable commitment.

## Key Claims

- A data contract contains schema, ownership, SLOs, and compatibility guarantees, and some implementations add lineage and quality expectations.
- At GoCardless, a pipeline violating its declared contract failed at the producer, not the consumer; within six months contracts covered roughly 50% of asynchronous inter-service events.
- Chad Sanderson at Convoy built a parallel Protobuf/Kafka implementation, Microsoft documented an internal one, and ThoughtWorks placed the Data Contract CLI in its Technology Radar Trial ring.
- For Ascend, the first governance move was establishing [data ownership](/concepts/data-ownership.md); dbt models declare schemas that are tested at build time, before anything reaches production.
- Contracts require maturity — analytics data is harder to contract than event streams, and contracts are a milestone, not a starting point for governance.

## Relevance

Defines [data contract](/concepts/data-contract.md), links it to [data ownership](/concepts/data-ownership.md) and [data mesh](/concepts/data-mesh.md), and exemplifies [embedded governance](/concepts/embedded-governance.md) where policy runs in the build pipeline rather than a committee.

## Quality

Practitioner blog post by Devlin Liles. Well-sourced with named implementations and dates; strong on sequencing, lighter on quantified business outcomes.

## Entities Mentioned

- [Ascend](/entities/ascend.md) — case study where ownership was the first governance move
- [ThoughtWorks](/entities/thoughtworks.md) — placed the Data Contract CLI on its Technology Radar
- [dbt](/entities/dbt.md) — transformation layer whose build-time tests enforce the contracts

## Concepts Covered

- [data contract](/concepts/data-contract.md) — the enforceable interface between producer and consumer
- [data ownership](/concepts/data-ownership.md) — the prerequisite a contract forces
- [data mesh](/concepts/data-mesh.md) — "data as a product" made an enforceable commitment
- [embedded governance](/concepts/embedded-governance.md) — policy enforced by the build pipeline, not a committee
