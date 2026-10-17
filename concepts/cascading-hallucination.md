---
title: "Cascading hallucination"
type: "Concept"
description: "When an ungrounded claim at an early step is treated as fact downstream, producing confident wrong answers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, evaluation, hallucination]
sources:
  - "/sources/hallucination-left-the-sentence-and-moved-into-the-chain.md"
  - "/sources/the-benchmark-passed-the-chain-still-failed.md"
---

# Cascading hallucination

Cascading hallucination is a systemic failure in which a fabricated or ungrounded claim early in a chain is consumed as fact by later steps, yielding a confident wrong answer far from the original error. It matters because it shifts the fix from better models or disclaimers to verification against ground truth at each stage.

## Key Claims

- Zero hallucination is a property a system enforces, not one a model possesses.
- RAG lowers fabrication rate but leaves the producing mechanism in place.
- Ungrounded claims at early steps compound as downstream steps treat them as fact.
- Stage-level and span-level checks are needed; code and tool traces are hardest to verify.
- GPT-5.5 resolves 69.1% of individual bugs but only 26.0% of full chains.
- CHARM names cascading hallucination where early retrieval errors yield confident wrong answers; AgentAuditor audits reasoning-tree divergence points, beating majority vote by up to 5 points.

## Related

- [Hallucination](/concepts/hallucination.md) — the single-step failure that cascades
- [Compounding error](/concepts/compounding-error.md) — the mechanism that amplifies it
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — reduces but does not remove it
- [checkpointing](/concepts/checkpointing.md) — short bounded stages catch errors before they compound
- [CHARM](/entities/charm.md) — names the pattern
- [Hallucination Left the Sentence and Moved Into the Chain](/sources/hallucination-left-the-sentence-and-moved-into-the-chain.md) — primary source
- [The Benchmark Passed. The Chain Still Failed.](/sources/the-benchmark-passed-the-chain-still-failed.md) — primary source
