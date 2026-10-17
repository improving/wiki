---
title: "metadata knowledge graph"
type: "Concept"
description: "A graph model of asset relationships and active metadata that lets people and models discover prompts, agents, and data."
created: '2026-10-17'
updated: '2026-10-17'
tags: [metadata, catalog, discovery]
sources:
  - "/sources/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md"
  - "/sources/the-catalog-already-learned-to-talk-to-machines.md"
---

# metadata knowledge graph

A metadata knowledge graph models the relationships among assets — prompts, models, agents, functions, and data — as a connected graph rather than flat catalog entries. It is the discovery layer that lets both humans and models retrieve AI assets and understand how they relate, and it converges with the identity and governance layer that platform vendors now apply to data and AI alike.

## Key Claims

- Static keyword catalogs fail because they are only as current as the last human update.
- Active metadata wired into source systems keeps catalog descriptions continuously current.
- A graph models prompt–model–data relationships that flat entries cannot express.
- Retrieval over catalog metadata is a different problem from retrieval over prompt content.
- Platform vendors converged on one layer: Databricks widened Unity Catalog to govern models, functions, agents, and MCP services; Microsoft gives agents identity via Entra Agent ID and governance via Purview.
- Prompts need versioning, evaluation-gated promotion, and audit trails like models do.

## Related

- [knowledge graph](/concepts/knowledge-graph.md) — the underlying model
- [Active Metadata](/concepts/active-metadata.md) — what keeps descriptions current
- [Data Catalog](/concepts/data-catalog.md) — the catalog this extends to AI assets
- [Skill Registry](/concepts/skill-registry.md) — a related discovery surface for agents
- [Unity Catalog](/entities/unity-catalog.md) — vendor implementation
- [Microsoft Purview](/entities/microsoft-purview.md) — vendor governance layer
- [Nobody Is Building a Separate Silo for AI Assets Anymore](/sources/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md) — primary source
- [The Catalog Already Learned to Talk to Machines](/sources/the-catalog-already-learned-to-talk-to-machines.md) — primary source
