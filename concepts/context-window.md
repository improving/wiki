---
title: "Context Window"
type: "Concept"
description: "The bounded span of text a model can attend to at once — a limit on knowledge, not a substitute for memory."
created: '2026-10-17'
updated: '2026-10-17'
tags: [llm, retrieval, memory]
sources:
  - "/sources/a-bigger-context-window-is-not-working-memory.md"
  - "/sources/the-model-can-only-know-whats-in-the-window.md"
  - "/sources/your-models-beliefs-are-frozen-rag-is-the-workaround.md"
---

# Context Window

The context window is the span of tokens a model can attend to in a single inference call. Across this corpus it is treated as the hard epistemic boundary of a model's knowledge: nothing outside the window can be reasoned over, and a larger window does not by itself make a system remember.

## Key Claims

- Epistemic closure holds only within the window; unseen information cannot be reasoned about.
- Attention dilutes across long contexts — the "lost in the middle" effect drops accuracy by more than 30 points when the answer moves mid-context.
- RoPE decay and softmax concentrate attention at primacy and recency positions, so placement matters as much as inclusion.
- A wider window is not working memory: gated [working memory](/concepts/working-memory.md) matched long-context scores with a quarter of the gradient steps.
- Model weights do not update at inference, so priors stay frozen at the training cutoff; [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) injects current evidence as a workaround.
- At enterprise scale, memory becomes an orchestration layer with permissions and expiry.

## Related

- [Working Memory](/concepts/working-memory.md) — the retention mechanism a big window does not provide
- [Lost in the middle](/concepts/lost-in-the-middle.md) — the attention failure that makes placement critical
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — injects fresh evidence into the window
- [fine-tuning](/concepts/fine-tuning.md) — real belief revision, slower and costlier than retrieval
- [A Bigger Context Window Is Not Working Memory](/sources/a-bigger-context-window-is-not-working-memory.md) — primary source
