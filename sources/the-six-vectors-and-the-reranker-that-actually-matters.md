---
title: "The Six Vectors and the Reranker That Actually Matters"
type: "Source Summary"
description: "Enterprise semantic search is really six retrieval vectors fused then reranked; the cross-encoder does most of the work."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/the-six-vectors-and-the-reranker-that-actually-matters/the-six-vectors-and-the-reranker-that-actually-matters.md"
---

# The Six Vectors and the Reranker That Actually Matters — Summary

**Original source**: `references/devlinliles.com/the-six-vectors-and-the-reranker-that-actually-matters/the-six-vectors-and-the-reranker-that-actually-matters.md`

## Summary

Argues that what enterprises call "semantic search" actually requires six retrieval methods running in parallel, fused into one ranked list, then re-scored by a cross-encoder whose only job is to tell the others when they're wrong. Drawing on three builds (pipeline compliance, healthcare documentation, contract analysis), the post shows the architecture is nearly identical across domains, and that the reranker — the step nobody budgets for — contributes more than any other addition. Hybrid search plus a reranker is now the baseline, not a nice-to-have.

## Key Claims

- BM25 keyword search alone lands around 65% recall@10; dense vectors alone 75 to 80%; the two combined 88 to 92%.
- Anthropic's contextual retrieval numbers: context-aware chunking cuts top-20 failures 35%, adding BM25 via RRF takes it to 49%, adding a cross-encoder reranker to 67%.
- A bare vector search scores around 0.16 MRR@5; adding a cross-encoder reranking pass climbs to roughly 0.75.
- The standard shape: retrieve top-1000 across all vectors, fuse with RRF at k=60, rerank the top 100 down to the 3 to 10 passages that reach the prompt.
- Behavioral/usage signal should be deprioritized for most internal knowledge bases, which lack the query volume to make it a real signal.

## Relevance

The clearest statement of the [hybrid retrieval](/concepts/hybrid-retrieval.md) stack: [dense embeddings](/concepts/dense-embeddings.md) plus [keyword search](/concepts/keyword-search.md) fused by [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) and lifted by a [cross-encoder reranker](/concepts/cross-encoder-reranker.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: concrete production figures and a clear mechanism for why the reranker works. Caveat: recall and MRR figures are presented as production/benchmark observations with limited provenance.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — source of the published contextual-retrieval numbers
- [SharePoint](/entities/sharepoint.md) — document store in the healthcare case

## Concepts Covered

- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the combined-vector architecture
- [dense embeddings](/concepts/dense-embeddings.md) — semantic search and its proper-noun weakness
- [keyword search](/concepts/keyword-search.md) — BM25 covering the gap dense vectors leave
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — the fusion mechanism across incompatible score scales
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the step doing most of the work
- [reranking](/concepts/reranking.md) — re-scoring a narrowed candidate set
- [temporal retrieval](/concepts/temporal-retrieval.md) — document dates as a proxy for validity
- [knowledge graph](/concepts/knowledge-graph.md) — graph retrieval for multi-hop and equivalency questions
