---
title: "Keyword Search Knows the Word, Not the Meaning"
type: "Source Summary"
description: "BM25 remains right for exact strings like part numbers, while semantic search closes the vocabulary-mismatch gap it cannot."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/keyword-search-knows-the-word-not-the-meaning/keyword-search-knows-the-word-not-the-meaning.md"
---

# Keyword Search Knows the Word, Not the Meaning — Summary

**Original source**: `references/devlinliles.com/keyword-search-knows-the-word-not-the-meaning/keyword-search-knows-the-word-not-the-meaning.md`

## Summary

Two different problems share one search box: finding the document containing an exact string like a CVE identifier, and finding something that satisfies a question like "how do I cancel my membership." Liles argues BM25 keyword search is still the right tool for the first — part numbers, error codes, statute citations, proper nouns — and that its mechanical failure on the second is the vocabulary-mismatch problem appearing at the retrieval layer. The instinct to retire BM25 for vectors gets the relationship backwards; semantic search finds the idea near the string, and the two methods are complementary rather than competing.

## Key Claims

- BM25 scores by term frequency, discounts common terms, and slightly penalizes long documents — no embeddings, no GPU, single-digit-millisecond answers, and fully inspectable scoring.
- For exact strings, nothing about "conceptual similarity" improves on exact match; cleverness produces slightly-off rankings that are hard to debug.
- BM25 sees "cancel my membership" and "terminate subscription" as sharing zero words, so author and searcher using different words for one idea never meet.
- The synonym-list fix hits diminishing returns fast, because language does not fail in the tidy way a thesaurus assumes.
- Every serious enterprise retrieval build of the last three years has added embeddings on top of keyword search rather than replacing it.

## Relevance

Core to [keyword search](/concepts/keyword-search.md), [semantic search](/concepts/semantic-search.md), and [vocabulary mismatch](/concepts/vocabulary-mismatch.md); motivates [hybrid retrieval](/concepts/hybrid-retrieval.md).

## Quality

Practitioner blog post by Devlin Liles. Clear, mechanical explanation with a good worked contrast; it is a conceptual overview that defers production detail to cited sources and to the next post in the series.

## Entities Mentioned

- None.

## Concepts Covered

- [Keyword search](/concepts/keyword-search.md) — BM25's mechanics, strengths, and exact-match fit
- [Semantic search](/concepts/semantic-search.md) — built to close the intent gap
- [Vocabulary mismatch](/concepts/vocabulary-mismatch.md) — the same failure as tagging, one layer deeper
- [Hybrid retrieval](/concepts/hybrid-retrieval.md) — embeddings added on top of keyword search, not instead of it
