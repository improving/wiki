---
title: "Hybrid Retrieval"
type: "Concept"
description: "Combining keyword and dense vector search so each covers the other's failure surface; the baseline for serious retrieval."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, search, rag]
sources:
  - "/sources/embeddings-find-the-meaning-and-lose-the-noun.md"
  - "/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/the-six-vectors-and-the-reranker-that-actually-matters.md"
---

# Hybrid Retrieval

Hybrid retrieval combines keyword search and dense vector search so each covers the other's failure surface. Across this corpus it is treated as the baseline every serious retrieval system must clear: embeddings find meaning but lose the noun, keyword search knows the word but not the meaning, and fusing them lifts recall well above either alone.

## Key Claims

- Keyword search alone lands around 65% recall and dense embeddings 75–80%; combining them lifts recall to 88–92%.
- Embeddings compress meaning, so they cannot distinguish part numbers or citations that differ only by string; proper nouns and rare codenames get thin, noise-like representations.
- BM25 and dense vectors each miss what the other catches, so hybrid search is table stakes rather than a differentiator.
- Reciprocal rank fusion merges scores on different scales by rank position.
- The cross-encoder reranker is the single largest contributor to retrieval quality — not piling on more signals.
- Enterprise retrieval should be a sequence of gates, each owning a specific failure mode; naive RAG fails the same five ways: permissions, authority, oversaturation, time, and structure.
- Filter on what you know before searching on what you infer; extra signals can bury the answer via lost-in-the-middle degradation.

## Related

- [Keyword Search](/concepts/keyword-search.md) — the lexical half of the pair
- [Dense Embeddings](/concepts/dense-embeddings.md) — the semantic half
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — how the two ranked lists are merged
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the largest downstream quality lever
- [Reranking](/concepts/reranking.md) — the stage after fusion
- [Hybrid Retrieval Is the Floor, Not the Ceiling](/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md) — primary source
