---
title: "temporal retrieval"
type: "Concept"
description: "Retrieval that reasons about when a fact was true, treating validity as a property of the fact rather than the document."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, rag, search]
sources:
  - "/sources/the-six-vectors-and-the-reranker-that-actually-matters.md"
  - "/sources/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval.md"
---

# temporal retrieval

Temporal retrieval answers questions about what was true at a given time, rather than ranking documents by their timestamps. This corpus argues that document dates are only a proxy: validity belongs to the individual fact, so temporal correctness must be resolved before graph traversal or reranking runs, and recency decay should be a fallback rather than the whole strategy.

## Key Claims

- Document dates are a proxy; validity belongs to the fact, not the document.
- Recency decay should be the fallback, not the strategy, for temporal retrieval.
- Graph retrieval pays off for multi-hop and cross-document questions, not single-fact lookups.
- A lighter personalized PageRank approach costs ten to thirty times less than full GraphRAG.
- Enterprise retrieval needs six fused vectors plus a cross-encoder reranker, and the reranker contributes more than any other single addition.
- Hybrid search is table stakes; filter on what you know before searching on what you infer.

## Related

- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the fused-vector foundation temporal filtering sits on
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the highest-value single addition to a retrieval stack
- [knowledge graph](/concepts/knowledge-graph.md) — the structure multi-hop and temporal queries traverse
- [Reranking](/concepts/reranking.md) — the stage that follows temporal filtering
- [PageRank](/entities/pagerank.md) — the basis for the cheaper personalized graph approach
- [The Six Vectors and the Reranker That Actually Matters](/sources/the-six-vectors-and-the-reranker-that-actually-matters.md) — primary source
- [Time Is Not a Timestamp](/sources/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval.md) — primary source
