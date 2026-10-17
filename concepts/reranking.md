---
title: "Reranking"
type: "Concept"
description: "A second scoring pass that reorders a broad candidate set before a small passage budget is spent."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, search, ranking]
sources:
  - "/sources/the-context-window-is-not-a-filing-cabinet.md"
  - "/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md"
---

# Reranking

Reranking is the reordering step that follows broad retrieval: pull many candidates cheaply, fuse the signals, then score them carefully so only a small, high-quality passage set reaches the model. It matters because relevance degrades as corpora grow, and because a signal being correct is not the same as a signal being discriminative.

## Key Claims

- Retrieve broadly, fuse with reciprocal rank fusion, rerank, then keep three to ten passages.
- Each retrieval method must answer a specific failure mode, not be default-on.
- A signal being correct is not the same as a signal being discriminative.
- Lost-in-the-middle degrades mid-context recall by more than thirty percent.
- RAG shifts the failure from a window too full to a window filled with the wrong things; being explicit about what each step needs makes retrieval bounded and reliable.

## Related

- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the model class used for the second pass
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — merges the broad candidate lists first
- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — the failure mode a fixed passage budget addresses
- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — the hard gate that runs before scoring
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the broad first pass reranking refines
- [The Oversaturation Problem: Why More Search Vectors Make Retrieval Worse](/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md) — primary source
