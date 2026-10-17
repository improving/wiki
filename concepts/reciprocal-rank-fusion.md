---
title: "Reciprocal Rank Fusion"
type: "Concept"
description: "Merging ranked retrieval lists by rank position instead of raw score, the standard way to fuse hybrid search results."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, search, ranking]
sources:
  - "/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md"
  - "/sources/the-six-vectors-and-the-reranker-that-actually-matters.md"
---

# Reciprocal Rank Fusion

Reciprocal rank fusion (RRF) merges several ranked retrieval lists into one by combining each document's rank position rather than its raw score. Across this corpus it is the standard way to fuse hybrid keyword and vector results, because scores from BM25 and embeddings live on incomparable scales while ranks do not.

## Key Claims

- RRF fuses scores on different scales by rank position, avoiding the calibration problem of combining raw BM25 and cosine similarities.
- The recommended enterprise shape is retrieve broadly, fuse with RRF, rerank, then keep three to ten passages.
- Combining keyword and dense retrieval lifts recall from ~65–80% to 88–92%; fusion is the step that realizes the gain.
- More retrieval vectors degrade relevance as corpora grow: lost-in-the-middle cuts mid-context recall by more than 30%, so each method must answer a specific failure mode rather than be default-on.
- A signal being correct is not the same as a signal being discriminative; extra vectors can bury the answer.
- Fusion is only the floor: the cross-encoder reranker that follows is the single largest contributor to retrieval quality.

## Related

- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the strategy RRF fuses
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the stage after fusion
- [Reranking](/concepts/reranking.md) — refining fused results
- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — the failure more vectors cause
- [Lost in the middle](/concepts/lost-in-the-middle.md) — why a fixed passage budget matters
- [The Six Vectors and the Reranker That Actually Matters](/sources/the-six-vectors-and-the-reranker-that-actually-matters.md) — primary source
