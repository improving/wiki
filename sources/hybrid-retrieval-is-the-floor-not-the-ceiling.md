---
title: "Hybrid Retrieval Is the Floor, Not the Ceiling"
type: "Source Summary"
description: "Argues hybrid keyword-plus-embedding retrieval is now baseline, with differentiation moving downstream to reranking—and more signals often hurting."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/hybrid-retrieval-is-the-floor-not-the-ceiling/hybrid-retrieval-is-the-floor-not-the-ceiling.md"
---

# Hybrid Retrieval Is the Floor, Not the Ceiling — Summary

**Original source**: `references/devlinliles.com/hybrid-retrieval-is-the-floor-not-the-ceiling/hybrid-retrieval-is-the-floor-not-the-ceiling.md`

## Summary

Liles argues keyword and dense retrieval fail in almost perfectly complementary places, so combining them is now a baseline rather than a differentiator. On mixed enterprise corpora, hybrid recall lands at 88–92% versus roughly 65% for keyword and 75–80% for embeddings, and the real differentiation has moved downstream to reranking.

## Key Claims

- Naive score averaging fails because BM25 and cosine scores live on different scales; reciprocal rank fusion combines by rank position instead and is table stakes in 2026.
- Anthropic's contextual retrieval research: context-aware chunking cuts top-20 retrieval failures 35%; adding keyword search, 49%; adding a cross-encoder reranker, 67%—the single largest contributor, coming after the hybrid combination rather than instead of it.
- Adding more retrieval signals (metadata filters, knowledge graphs, click data) often loses ground, because of the "lost in the middle" effect: mid-context information degrades by more than 30%.
- A signal must be discriminative in the cases a system currently gets wrong, not merely another accurate-but-redundant vote.
- The same discovery problem will reappear for agents, prompts, and tools once organizations start building their own.

## Relevance

Informs [hybrid retrieval](/concepts/hybrid-retrieval.md), [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md), [cross-encoder reranker](/concepts/cross-encoder-reranker.md), and [lost in the middle](/concepts/lost-in-the-middle.md); the headline figures come from [Anthropic](/entities/anthropic.md) research. The complementary failure modes rest on [keyword search](/concepts/keyword-search.md) and [semantic search](/concepts/semantic-search.md).

## Quality

Practitioner blog post by Devlin Liles. Specific figures and a named vendor study give it weight; the benchmark numbers are drawn from secondary analyses and one vendor's published research rather than the author's own measurements.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — source of the contextual retrieval failure-reduction figures

## Concepts Covered

- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the baseline the post argues is now table stakes
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — the standard way to combine the two methods
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the largest downstream contributor
- [Lost in the middle](/concepts/lost-in-the-middle.md) — why more retrieval signals can hurt
- [Keyword Search](/concepts/keyword-search.md) — catches part numbers and citations
- [Semantic Search](/concepts/semantic-search.md) — catches paraphrase and conceptual matches
