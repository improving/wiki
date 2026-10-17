---
title: "cross-encoder reranker"
type: "Concept"
description: "A model that reads query and candidate together to rescore retrieval results; the single largest lift in retrieval quality."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, search, ranking]
sources:
  - "/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/the-six-vectors-and-the-reranker-that-actually-matters.md"
---

# cross-encoder reranker

A cross-encoder reranker reads a query and a candidate document jointly — unlike bi-encoders that embed them separately — and rescores a candidate list after first-stage retrieval. Across this corpus it is named the single largest contributor to retrieval quality: the differentiator once hybrid search has become table stakes.

## Key Claims

- Combining keyword and dense retrieval lifts recall from roughly 65–80% to 88–92%, but hybrid search is now the floor, not the ceiling.
- A cross-encoder reads query and candidate together and contributes more than any other single addition.
- Extra retrieval signals can bury the answer through lost-in-the-middle degradation, so more vectors are not automatically better.
- Filter on what you know before searching on what you infer; permissions must hard-exclude before scoring.
- Hybrid search plus a cross-encoder reranker is baseline in enterprise retrieval — the remaining work is the gates around it.
- Naive RAG fails the same five ways: permissions, authority, oversaturation, time, and structure.

## Related

- [Reranking](/concepts/reranking.md) — the stage a cross-encoder implements
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the first stage the reranker refines
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — fuses differently scaled scores by rank position
- [Dense Embeddings](/concepts/dense-embeddings.md) and [Keyword Search](/concepts/keyword-search.md) — the two signals combined upstream
- [Hybrid Retrieval Is the Floor, Not the Ceiling](/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md) — primary source
