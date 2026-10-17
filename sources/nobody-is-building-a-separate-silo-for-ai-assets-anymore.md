---
title: "Nobody Is Building a Separate Silo for AI Assets Anymore"
type: "Source Summary"
description: "Four platform vendors independently converged on governing AI assets through the same identity, governance, and discovery layers as data assets."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/nobody-is-building-a-separate-silo-for-ai-assets-anymore/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md"
---

# Nobody Is Building a Separate Silo for AI Assets Anymore — Summary

**Original source**: `references/devlinliles.com/nobody-is-building-a-separate-silo-for-ai-assets-anymore/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md`

## Summary

The market answered the AI-asset discovery question by accident: four vendors that do not coordinate all decided AI assets should live inside the same governance estate as data assets. Databricks widened Unity Catalog's namespace to cover models, functions, vector indexes, agents, and MCP services; Microsoft gave agents identity via Entra Agent ID and governance via Purview; AWS Bedrock and Google shipped registries the same year. The post lays out a layered reference architecture and argues prompts deserve the same registry discipline as models.

## Key Claims

- Nobody serious builds a separate silo for AI assets next to the one for data assets; the winning shape is one identity, governance, and discovery layer holding both.
- An agent and a table are the same governance problem: something to locate, trust, and authorize.
- The architecture has swappable layers: identity/namespace, a [metadata knowledge graph](/concepts/metadata-knowledge-graph.md), per-asset registries, a gateway/broker, and a hybrid search experience layer.
- Governance objects such as scenario lineage and audit logs belong as first-class nodes in the graph from day one, extending OpenLineage's run/job/dataset model to run, agent, prompt, and model.
- Prompts get underbuilt most: they need versioning, evaluation-gated promotion, and an audit trail showing which version produced which output.

## Relevance

Central to enterprise AI retrieval and [Data Governance](/concepts/data-governance.md), describing how catalogs like [Unity Catalog](/entities/unity-catalog.md) and [Microsoft Purview](/entities/microsoft-purview.md) absorb AI assets.

## Quality

Practitioner blog post by Devlin Liles. Strong vendor-convergence survey with concrete products; some 2026 roadmap claims rest on vendor announcements.

## Entities Mentioned

- [Unity Catalog](/entities/unity-catalog.md) — Databricks namespace widened to govern AI assets
- [Databricks](/entities/databricks.md) — vendor whose namespace widening leads the convergence
- [Microsoft Purview](/entities/microsoft-purview.md) — extends governance to agent activity, prompts, and tool calls

## Concepts Covered

- [metadata knowledge graph](/concepts/metadata-knowledge-graph.md) — the active discovery substrate linking assets, owners, and lineage
- [Data Governance](/concepts/data-governance.md) — the discipline agents and data assets are now governed under alike
