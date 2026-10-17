---
title: "Lost in the middle"
type: "Concept"
description: "The degradation of recall for information placed mid-context, so retrieved passages buried in the middle get ignored."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, context, llm-behavior]
sources:
  - "/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md"
  - "/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md"
---

# Lost in the middle

Lost in the middle describes a failure mode in which language models attend less reliably to information positioned in the middle of a long context. In retrieval pipelines it is the hidden cost of "more is better": piling on signals can push the answer out of the model's effective attention and degrade relevance even when the right passage was retrieved.

## Key Claims

- Mid-context recall degrades by more than thirty percent, so position within the context matters as much as presence.
- Extra retrieval signals can bury the answer, which is why hybrid retrieval's gains flatten beyond a point.
- A signal being correct is not the same as a signal being discriminative; adding signals adds noise.
- The remedy is discipline, not volume: retrieve broadly, fuse with reciprocal rank fusion, rerank, then keep only three to ten passages.
- Each retrieval method should answer a specific failure mode rather than being left default-on.

## Related

- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — the corpus-level symptom of the same problem
- [Reranking](/concepts/reranking.md) — the lever that counteracts burying
- [Context Window](/concepts/context-window.md) — the space in which position degrades
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — where the degradation shows up
- [Hybrid Retrieval Is the Floor, Not the Ceiling](/sources/hybrid-retrieval-is-the-floor-not-the-ceiling.md) — primary source
- [The Oversaturation Problem: Why More Search Vectors Make Retrieval Worse](/sources/the-oversaturation-problem-why-more-search-vectors-make-retrieval-worse.md) — primary source
