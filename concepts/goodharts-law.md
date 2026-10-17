---
title: "Goodhart's Law"
type: "Concept"
description: "When a measure becomes a target it ceases to be a good measure — the recurring failure mode of AI evaluation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [metrics, measurement, evaluation]
sources:
  - "/sources/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md"
  - "/sources/inside-the-system-boundary.md"
  - "/sources/p-o-s-t-four-dimensions-of-ai-native-delivery.md"
  - "/sources/we-trained-ai-to-be-engaging-not-helpful.md"
---

# Goodhart's Law

Goodhart's law holds that when a measure becomes a target, it ceases to be a good measure. Across this corpus it is the recurring failure mode of AI measurement: optimizing a proxy — annotator preference, component accuracy, a single dimension — improves the proxy while degrading the outcome it was meant to represent.

## Key Claims

- RLHF reward models optimize annotator engagement rather than helpfulness; sycophancy, overconfidence, and verbosity are the signatures, exactly as Goodhart's law predicts.
- Reward model overoptimization drifts models from helpfulness as training pushes further along the proxy.
- Goodhart's law compounds across interacting components in compound AI systems, so measurement must pair leading and lagging metrics.
- Model accuracy creates zero value without changing an action; most AI projects fail from misframed problems and missing measurement.
- Component, composition, and interaction lift must be separated — via ablation, shadow routing, specialist isolation, and critic gating — to make value claims defensible.
- The P.O.S.T. dimensions (productivity, outcomes, satisfaction, time to market) guard each other against gaming, because a dimension tells a team what to measure rather than what to sacrifice.

## Related

- [reward hacking](/concepts/reward-hacking.md) — the mechanism this law describes
- [Sycophancy](/concepts/sycophancy.md) — a signature of engagement-optimized training
- [RLHF](/concepts/rlhf.md) — the training regime where the drift appears
- [compound AI systems](/concepts/compound-ai-systems.md) — where the effect compounds
- [Causal Lineage Map](/concepts/causal-lineage-map.md) — causal measurement that resists proxy gaming
- [We Trained AI to Be Engaging, Not Helpful](/sources/we-trained-ai-to-be-engaging-not-helpful.md) — primary source
