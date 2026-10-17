---
title: "Dense Embeddings"
type: "Concept"
description: "Vector representations that compress meaning, strong on concepts but weak on exact identifiers, so retrieval must pair them with keyword search."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, embeddings, search]
sources:
  - "/sources/embeddings-find-the-meaning-and-lose-the-noun.md"
  - "/sources/the-six-vectors-and-the-reranker-that-actually-matters.md"
---

# Dense Embeddings

Dense embeddings map text into continuous vectors that capture meaning, so semantically similar passages land near each other even without shared words. Across this corpus they are treated as one necessary signal in enterprise retrieval rather than a complete solution: they excel at concepts but lose exact identifiers.

## Key Claims

- Embeddings compress meaning, so they cannot reliably distinguish part numbers or citations that differ only by string.
- Proper nouns and rare codenames get thin, noise-like representations in broadly trained models.
- Keyword search alone lands around 65% recall; dense embeddings reach 75–80%; neither suffices alone.
- BM25 and dense vectors each miss what the other catches, so serious retrieval combines them.
- Hybrid search is table stakes; the [cross-encoder reranker](/concepts/cross-encoder-reranker.md) is the differentiator.
- Filter on what you know before searching on what you infer.

## Related

- [Keyword Search](/concepts/keyword-search.md) — the complementary signal dense vectors miss
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — combining dense and lexical retrieval
- [Semantic Search](/concepts/semantic-search.md) — the capability dense embeddings provide
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the differentiator on top of fusion
- [Embeddings Find the Meaning and Lose the Noun](/sources/embeddings-find-the-meaning-and-lose-the-noun.md) — primary source
- [The Six Vectors and the Reranker That Actually Matters](/sources/the-six-vectors-and-the-reranker-that-actually-matters.md) — primary source
