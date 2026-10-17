---
title: "fine-tuning"
type: "Concept"
description: "Updating model weights to specialize behavior or revise beliefs, traded against orchestration based on workflow stability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [architecture, adaptation, model-selection]
sources:
  - "/sources/fine-tune-or-orchestrate-the-architecture-decision-every-agent-engagement-skips.md"
  - "/sources/your-models-beliefs-are-frozen-rag-is-the-workaround.md"
---

# fine-tuning

Fine-tuning updates a model's weights to specialize it for a task or revise what it "believes." Across this corpus it appears as one side of an architecture decision — fine-tune versus orchestrate — and as the slower, costlier alternative to retrieval when the problem is stale knowledge.

## Key Claims

- Narrow, stable workflows favor fine-tuned specialists; evolving ones favor orchestration.
- Fine-tuning's one-time cost is a bet that requirements hold still; the architecture decision must be revisited as the workflow's shape shifts.
- Orchestration absorbs requirement changes cheaply, while fine-tuning pays per change.
- Model weights do not update at inference, so priors stay frozen at the training cutoff.
- Fine-tuning is real belief revision, but it is slower and costlier than injecting current evidence via [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md).
- Models sometimes ignore retrieved evidence that contradicts a strongly encoded prior, a failure retrieval alone cannot fix.

## Related

- [orchestration layer](/concepts/orchestration-layer.md) — the adaptive alternative to fine-tuning
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — the cheaper workaround for frozen priors
- [Targeted Fine-Tuning](/concepts/targeted-fine-tuning.md) — a focused form of weight update
- [model routing](/concepts/model-routing.md) — deciding which adapted model handles which task
- [Fine-Tune or Orchestrate: The Architecture Decision Every Agent Engagement Skips](/sources/fine-tune-or-orchestrate-the-architecture-decision-every-agent-engagement-skips.md) — primary source
