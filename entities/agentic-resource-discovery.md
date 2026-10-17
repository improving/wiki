---
title: "Agentic Resource Discovery"
type: "Entity"
description: "Open specification for federated agent capability discovery via domain-owned ai-catalog.json files, distinct from a governed registry."
created: '2026-10-17'
updated: '2026-10-17'
tags: [discovery, agents, specification]
sources:
  - "/sources/off-the-shelf-gets-you-partway-there.md"
  - "/sources/publishing-a-catalog-is-not-the-same-as-running-a-registry.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
---

# Agentic Resource Discovery

Agentic Resource Discovery (ARD) is an open specification for finding agent capabilities across organizational boundaries. It works by crawling domain-owned `ai-catalog.json` files, federating self-reported metadata so one domain can discover another's tools. In this corpus it is framed as a genuine solution to cross-boundary discovery that stops short of being a registry.

## Key Claims

- ARD federates self-reported metadata but verifies no health, so it answers discovery without answering trust ([off the shelf](/sources/off-the-shelf-gets-you-partway-there.md))
- Federation solves cross-boundary discovery but is not a [registry](/concepts/skill-registry.md): crawled catalogs are static, self-reported metadata needing enrichment ([publishing a catalog](/sources/publishing-a-catalog-is-not-the-same-as-running-a-registry.md))
- Over 2,500 Claude Code plugin marketplaces exist with no trust authority; documents and skills fail discovery for the same structural reason.
- Google ships a proprietary governance layer the open spec omits, and the goal is one governed catalog answering current, owned, safe-to-use.
- Discovery is one gate in enterprise retrieval, which needs distinct stages each owning a specific failure mode ([enterprise ai retrieval](/sources/the-architecture-of-enterprise-ai-retrieval.md))

## Related

- [federation](/concepts/federation.md) — ARD's cross-boundary mechanism
- [Skill Registry](/concepts/skill-registry.md) — the governed layer ARD lacks
- [Skill Discovery](/concepts/skill-discovery.md) — the problem it addresses
- [Data Catalog](/concepts/data-catalog.md) — the analogous data-side pattern
- [Google](/entities/google.md) — ships the proprietary governance layer
