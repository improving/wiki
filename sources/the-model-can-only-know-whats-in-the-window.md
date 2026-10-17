---
title: "The Model Can Only Know What's in the Window"
type: "Source Summary"
description: "Bigger context windows don't remove the reasoning limit: attention and retrieval quality bound what the model can actually use."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/the-model-can-only-know-whats-in-the-window/the-model-can-only-know-whats-in-the-window.md"
---

# The Model Can Only Know What's in the Window — Summary

**Original Source**: `references/devlinliles.com/the-model-can-only-know-whats-in-the-window/the-model-can-only-know-whats-in-the-window.md`

## Summary

Longer [context windows](/concepts/context-window.md) were pitched as engineering away context constraints, but a basic logical principle explains why the problem persists. The post applies epistemic closure — knowledge is closed under known entailment — to show a model can only reason over what sits, usable, inside its window. It then argues that attention and retrieval quality, not raw window size, determine whether the model can close a reasoning chain, so teams should engineer context construction rather than wait.

## Key Claims

- The model's epistemic closure holds only within the window; information outside it is simply unavailable for reasoning.
- The "lost in the middle" effect (Liu et al., 2023; TACL 2024) is a reliable U-curve: accuracy dropped more than 30 percentage points when the answer document moved from position 1 to position 10 in a 20-document context.
- The architectural cause is RoPE positional encoding's long-term decay plus softmax concentration on primacy and recency positions.
- Critical instructions and key passages belong at the beginning or end; the middle of a long context is not reliably accessible.
- Dumping a whole knowledge base into context is a category error; retrieval quality (not quantity) determines whether the chain closes, and enterprise teams routinely underinvest in context construction.

## Relevance

Central to [context window](/concepts/context-window.md) and [lost in the middle](/concepts/lost-in-the-middle.md), and directly informs [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) and [context management](/concepts/context-management.md).

## Quality

Practitioner blog post by Devlin Liles. Concise and well-grounded, citing a named study with a specific figure; the architectural explanation is accurate if simplified, and the enterprise underinvestment claim is asserted rather than measured.

## Entities Mentioned

- None.

## Concepts Covered

- [context window](/concepts/context-window.md) — the boundary of what the model can access per inference
- [lost in the middle](/concepts/lost-in-the-middle.md) — the U-shaped attention effect the post explains
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — the pipeline that positions relevant chunks where the model attends
- [context management](/concepts/context-management.md) — context construction as the primary lever on closure

## Related Sources

- [A Bigger Context Window Is Not Working Memory](/sources/a-bigger-context-window-is-not-working-memory.md)
- [Your Model's Beliefs Are Frozen. RAG Is the Workaround.](/sources/your-models-beliefs-are-frozen-rag-is-the-workaround.md)
