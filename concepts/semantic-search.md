---
title: "Semantic Search"
type: "Concept"
description: "Retrieval by meaning via embeddings, which complements but never replaces exact-string keyword search."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, embeddings, search]
sources:
  - "/sources/embeddings-find-the-meaning-and-lose-the-noun.md"
  - "/sources/keyword-search-knows-the-word-not-the-meaning.md"
  - "/sources/name-resolution-was-never-enough.md"
  - "/sources/the-catalog-already-learned-to-talk-to-machines.md"
---

# Semantic Search

Semantic search retrieves documents by meaning using [dense embeddings](/concepts/dense-embeddings.md) rather than by matching literal terms. Across this corpus it is treated as one half of a retrieval architecture, not a replacement for [keyword search](/concepts/keyword-search.md): the two methods cover different failure surfaces, so serious enterprise retrieval combines them.

## Key Claims

- Embeddings compress meaning, so they cannot distinguish part numbers or citations that differ only by string; proper nouns and rare codenames get thin, noise-like representations in broadly trained models.
- Keyword search alone lands around 65% recall; dense embeddings reach 75–80%; neither suffices alone, which is why [hybrid retrieval](/concepts/hybrid-retrieval.md) is the floor rather than the ceiling.
- BM25 is right for part numbers, error codes, and citations but fails under [vocabulary mismatch](/concepts/vocabulary-mismatch.md), when query and document share no vocabulary.
- Static keyword catalogs are only as current as the last human edit; active metadata wired into source systems keeps descriptions continuously current.
- A [metadata knowledge graph](/concepts/metadata-knowledge-graph.md) models prompt–model–data relationships that flat entries cannot, and retrieval over catalog metadata differs from retrieval over prompt content.
- Name resolution (DNS, Consul, etcd) never answered health, version, or authorization; AI asset discovery should be capability-first, with a capability registry and semantic search reading one shared [knowledge graph](/concepts/knowledge-graph.md).

## Related

- [Keyword Search](/concepts/keyword-search.md) — the exact-string complement
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the combined architecture
- [Dense Embeddings](/concepts/dense-embeddings.md) — the underlying representation
- [Embeddings Find the Meaning and Lose the Noun](/sources/embeddings-find-the-meaning-and-lose-the-noun.md) — primary source
