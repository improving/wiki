---
title: "Keyword Search"
type: "Concept"
description: "Lexical retrieval such as BM25 that matches exact terms, excelling on identifiers but failing on meaning."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, search, bm25]
sources:
  - "/sources/embeddings-find-the-meaning-and-lose-the-noun.md"
  - "/sources/keyword-search-knows-the-word-not-the-meaning.md"
---

# Keyword Search

Lexical retrieval, canonically BM25, that scores documents by term overlap. It matters because it is the half of retrieval that [dense embeddings](/concepts/dense-embeddings.md) cannot replace: exact identifiers, error codes, and citations survive keyword matching and dissolve in a compressed vector.

## Key Claims

- BM25 scores term frequency, discounts common words, and penalizes long documents.
- Keyword search is the right tool for part numbers, error codes, and citations.
- BM25 fails when query and document share no vocabulary — the [vocabulary mismatch](/concepts/vocabulary-mismatch.md) problem.
- Embeddings compress meaning, so they cannot distinguish part numbers or citations differing only by string.
- Proper nouns and rare codenames get thin, noise-like representations in broadly trained models.
- Keyword search alone lands around 65% recall and dense embeddings 75–80%; neither suffices alone, so serious retrieval combines them in [hybrid retrieval](/concepts/hybrid-retrieval.md).

## Related

- [Dense Embeddings](/concepts/dense-embeddings.md) — the complementary semantic half
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — combining lexical and semantic signals
- [Vocabulary mismatch](/concepts/vocabulary-mismatch.md) — keyword search's failure mode
- [knowledge graph](/concepts/knowledge-graph.md) — another structure for exact, linked entities
- [Embeddings Find the Meaning and Lose the Noun](/sources/embeddings-find-the-meaning-and-lose-the-noun.md) — primary source
- [Keyword Search Knows the Word, Not the Meaning](/sources/keyword-search-knows-the-word-not-the-meaning.md) — primary source
