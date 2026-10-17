---
title: "PageRank"
type: "Entity"
description: "Link-analysis algorithm the corpus adapts to propagate source authority through a knowledge graph cheaply."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, graphs, algorithms]
sources:
  - "/sources/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md"
  - "/sources/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval.md"
---

# PageRank

PageRank is the link-analysis algorithm this corpus borrows to propagate trust through a knowledge graph. Where the original ranked web pages by incoming links, these sources use it to let structural authority flow between connected documents and facts, distinct from mere relevance.

## Overview

The authority post argues relevance doesn't measure believability. Authority is a property of the source, mostly free from existing metadata, and graph centrality propagates trust the way PageRank propagates web importance. Crucially, corroboration across independent witnesses differs from structural authority, and a static trust score can confidently suppress a stale-but-correct source — so contradictions should be surfaced rather than auto-resolved.

The temporal-retrieval post adds the graph context: document dates are a proxy, validity belongs to the fact, and recency decay should be the fallback rather than the strategy. Graph retrieval pays off for multi-hop and cross-document questions, not single-fact lookups. A lighter personalized PageRank approach costs ten to thirty times less than full GraphRAG, making it the pragmatic default.

## Key Claims

- Authority is a property of the source, mostly free from existing metadata.
- Graph centrality propagates trust like PageRank propagates web importance.
- Corroboration across independent witnesses differs from structural authority.
- A static trust score can confidently suppress a stale-but-correct source.
- A lighter personalized PageRank approach costs ten to thirty times less than full GraphRAG.

## Related

- [knowledge graph](/concepts/knowledge-graph.md) — the structure PageRank traverses
- [Corroboration](/concepts/corroboration.md) — the signal distinct from centrality
- [trusted signals](/concepts/trusted-signals.md) — what centrality helps establish
- [temporal retrieval](/concepts/temporal-retrieval.md) — the validity problem it complements
- [Policy Doc or Teams Message](/sources/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md) — primary source
