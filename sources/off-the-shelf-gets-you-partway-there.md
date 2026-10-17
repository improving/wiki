---
title: "Off the Shelf Gets You Partway There"
type: "Source Summary"
description: "Federation distributes skills across boundaries but is only a feed into a graph; the goal is one governed catalog with authority to say no."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/off-the-shelf-gets-you-partway-there/off-the-shelf-gets-you-partway-there.md"
---

# Off the Shelf Gets You Partway There — Summary

**Original source**: `references/devlinliles.com/off-the-shelf-gets-you-partway-there/off-the-shelf-gets-you-partway-there.md`

## Summary

Skill distribution is solved — 2,500+ [Claude Code](/entities/claude-code.md) plugin marketplaces exist and ~40 products support the open Agent Skills spec — but trust is not. The series' recurring failure is a discovery problem with no authority behind it: a shared drive, a folksonomy, keyword and semantic search, and now skill sprawl all fail for the same structural reason. [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) federation solves cross-boundary lookup, but it is self-reported, batch-published metadata — a feed into a graph, not the graph itself.

## Key Claims

- Federation answers how an agent finds a capability across a boundary neither party controls, and is precisely as far as it goes.
- A crawled federation entry is self-reported metadata, exactly the kind [Active Metadata](/concepts/active-metadata.md) replaced inside a single catalog, and it hands off without confirming health, live version, or authorization.
- The goal is one governed catalog answering "is this current, owned, and safe right now" for every asset and consumer.
- Documents and skills are the same problem; a person and a pipeline should read one shared record, not two descriptions that drift.
- Cross-boundary capabilities should be treated like a newly authored internal skill: verified, [version-pinned](/concepts/version-pinning.md), and logged.

## Relevance

Informs [Skill Discovery](/concepts/skill-discovery.md), [federation](/concepts/federation.md), and [Active Metadata](/concepts/active-metadata.md), and points toward the catalog-as-control-plane thesis.

## Quality

Practitioner blog post by Devlin Liles. Synthesizes a multi-post series with a clear architectural argument; marketplace and adoption figures are cited secondhand and the framing is opinion.

## Entities Mentioned

- [Claude Code](/entities/claude-code.md) — ecosystem whose marketplaces illustrate solved distribution
- [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) — the federation spec for cross-boundary capability lookup

## Concepts Covered

- [Skill Discovery](/concepts/skill-discovery.md) — the authority problem federation does not solve
- [federation](/concepts/federation.md) — cross-boundary lookup as a feed into a graph
- [Active Metadata](/concepts/active-metadata.md) — what self-reported federation entries fall short of
- [Version Pinning](/concepts/version-pinning.md) — applied to inbound cross-boundary skills
- [Data Catalog](/concepts/data-catalog.md) — the one governed catalog as goal state
- [Control plane](/concepts/control-plane.md) — catalog as control plane for data and AI governance
