---
title: "CHARM"
type: "Entity"
description: "A named failure mode: cascading hallucination where an early retrieval error becomes a confidently wrong downstream answer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [hallucination, reliability, evaluation]
sources:
  - "/sources/hallucination-left-the-sentence-and-moved-into-the-chain.md"
  - "/sources/the-benchmark-passed-the-chain-still-failed.md"
---

# CHARM

CHARM is the name this corpus gives to **cascading hallucination**: a failure mode where an ungrounded claim at an early step of a multi-step chain is treated as fact by every later step, producing a confident wrong answer at the end.

## Overview

Where earlier discussion treated hallucination as a sentence-level property of a model, these posts argue it has moved into the chain. Zero hallucination is described as a property a system enforces, not one a model possesses; RAG lowers fabrication rate but leaves the producing mechanism in place.

## Key Claims

- Cascading hallucination (CHARM) names early retrieval errors that yield confident wrong answers
- Ungrounded early claims compound as downstream steps treat them as fact
- Stage-level and span-level checks are needed; code and tool traces are hardest to verify
- GPT-5.5 resolves 69.1% of individual bugs but only 26.0% of full chains
- Standard uncertainty methods ignore doubt inherited across steps
- AgentAuditor audits reasoning-tree divergence points, beating majority vote by up to 5 points

## Related

- [Cascading hallucination](/concepts/cascading-hallucination.md) — the concept CHARM names
- [Compounding error](/concepts/compounding-error.md) — mechanism behind the chain failure
- [Error Propagation](/concepts/error-propagation.md) — how early errors travel downstream
- [GPT-5.5](/entities/gpt-5-5.md) — model measured in the chain benchmark
- [The Benchmark Passed. The Chain Still Failed.](/sources/the-benchmark-passed-the-chain-still-failed.md) — primary source
- [Hallucination Left the Sentence and Moved Into the Chain](/sources/hallucination-left-the-sentence-and-moved-into-the-chain.md) — primary source
