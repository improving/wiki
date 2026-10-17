---
title: "Embeddings Find the Meaning and Lose the Noun"
type: "Source Summary"
description: "Dense embeddings excel at concepts but fail on identifiers and proper nouns, so retrieval needs keyword search combined with semantic search."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/embeddings-find-the-meaning-and-lose-the-noun/embeddings-find-the-meaning-and-lose-the-noun.md"
---

# Embeddings Find the Meaning and Lose the Noun — Summary

**Original source**: `references/devlinliles.com/embeddings-find-the-meaning-and-lose-the-noun/embeddings-find-the-meaning-and-lose-the-noun.md`

## Summary

Embeddings place "cancel my membership" near "terminate subscription," solving the vocabulary mismatch that keyword search could not. But meaning-based vectors are genuinely bad at things without meaning behind them: part numbers differing by one character, statute citations, and rare proper nouns, which share no semantic content and appear thinly in training data. This is not a bug a bigger model fixes, it is what an embedding is built to do. Because neither method alone is trustworthy, serious retrieval builds converge on combining them.

## Key Claims

- Dense embeddings handle concepts well but cannot distinguish strings whose meaning is identical, such as part 4471-B versus 4471-C or citation 26 U.S.C. § 501(c)(3).
- Rare proper nouns, internal product codenames, and non-public entity names have thin representations, sometimes barely distinguishable from noise.
- Compressing something that has no semantic content produces a less useful compression, not an error a larger model eventually closes.
- On mixed enterprise content, keyword search alone lands around 65% recall at ten results; dense embeddings alone around 75-80%.
- Neither alone reaches trustworthy retrieval because they cover different failure surfaces; tuning to close one gap does nothing for the other.
- Single-method systems return confidently ranked but factually wrong documents for exact-string queries.

## Relevance

Informs [dense embeddings](/concepts/dense-embeddings.md), [semantic search](/concepts/semantic-search.md), [keyword search](/concepts/keyword-search.md), and [hybrid retrieval](/concepts/hybrid-retrieval.md).

## Quality

Practitioner blog post by Devlin Liles. Clear conceptual framing with recall figures drawn from secondary sources; the numbers are approximate and cited rather than measured here.

## Entities Mentioned

- None.

## Concepts Covered

- [dense embeddings](/concepts/dense-embeddings.md) — strong at concepts, weak at identifiers
- [semantic search](/concepts/semantic-search.md) — the promise and the gap it leaves
- [keyword search](/concepts/keyword-search.md) — the mirror-image strengths it covers
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the combination the post argues for
