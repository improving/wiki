---
title: "Vocabulary mismatch"
type: "Concept"
description: "When a query and a document mean the same thing but share no words, defeating keyword search and manual tags."
created: '2026-10-17'
updated: '2026-10-17'
tags: [search, retrieval, taxonomy]
sources:
  - "/sources/keyword-search-knows-the-word-not-the-meaning.md"
  - "/sources/tags-are-a-promise-nobody-enforces.md"
---

# Vocabulary mismatch

Vocabulary mismatch is the failure where a searcher and a document describe the same idea in different words, so exact-term matching finds nothing. It is why [Keyword Search](/concepts/keyword-search.md) cannot stand alone and why retrieval systems add [Semantic Search](/concepts/semantic-search.md); it is also the steady-state outcome of any tagging scheme that depends on human upkeep.

## Key Claims

- [Keyword Search](/concepts/keyword-search.md) (BM25) scores term frequency, discounts common words, and penalizes long documents.
- BM25 is right for part numbers, error codes, and citations, but fails when query and document share no vocabulary.
- Semantic search adds [Dense Embeddings](/concepts/dense-embeddings.md) on top; the two methods are complementary.
- Folksonomies scale but produce vocabulary mismatch; ontologies are powerful but expensive to build and maintain.
- Tags generated as a pipeline side effect survive; manual tags decay.

## Related

- [Keyword Search](/concepts/keyword-search.md) — the method most exposed to mismatch
- [Semantic Search](/concepts/semantic-search.md) — the complementary fix
- [shared vocabulary](/concepts/shared-vocabulary.md) — the organizational remedy
- [Keyword Search Knows the Word, Not the Meaning](/sources/keyword-search-knows-the-word-not-the-meaning.md) — primary source
