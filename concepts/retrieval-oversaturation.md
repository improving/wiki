---
title: "Retrieval oversaturation"
type: "Concept"
description: "Adding more retrieval signals degrades relevance as corpora grow; sharper filtering and a fixed passage budget beat piling on vectors."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, rag, search]
sources:
  - "/sources/skill-sprawl-is-the-shared-drive-again.md"
  - "/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md"
---

# Retrieval oversaturation

Retrieval oversaturation is the failure mode where adding more search signals, overlapping candidates, or larger context budgets makes retrieval *worse* rather than better. Across this corpus it is treated as a structural property of growing corpora: a signal being correct is not the same as a signal being discriminative, and once too many plausible passages crowd the context, the model's attention spreads thin and the right answer gets buried.

## Key Claims

- Overlapping or duplicate items (skills, passages, vectors) cause retrieval oversaturation and unreliable selection.
- Lost-in-the-middle degrades mid-context recall by more than thirty percent, so extra signals can actively hurt.
- "A signal being correct is not the same as a signal being discriminative" — extra vectors often add noise, not lift.
- The fix is not more retrieval but sharper metadata filtering and a fixed passage budget.
- Retrieve broadly, fuse with reciprocal rank fusion, rerank, then keep only three to ten passages.
- Each retrieval method must answer a specific failure mode; no method should be default-on.

## Related

- [Lost in the middle](/concepts/lost-in-the-middle.md) — the attention effect that makes oversaturated context fail
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — how broad candidates are merged before trimming
- [Reranking](/concepts/reranking.md) — the stage that enforces the passage budget
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the multi-signal baseline oversaturation argues against over-extending
- [Skill Registry](/concepts/skill-registry.md) — where overlapping, unreviewed entries cause the same effect
- [The Oversaturation Problem: Why More Search Vectors Make Retrieval Worse](/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md) — primary source
