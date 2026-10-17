---
title: "compound AI systems"
type: "Concept"
description: "AI value delivered by composed systems of models and tools rather than any single model acting alone."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai-architecture, measurement, agents]
sources:
  - "/sources/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md"
  - "/sources/inside-the-system-boundary.md"
---

# compound AI systems

A compound AI system composes multiple models, tools, and steps so that the delivered outcome belongs to the whole pipeline rather than to any individual model. This matters across the corpus because modern AI value is created by these compositions, which makes attribution — and therefore defensible measurement — the central problem for teams claiming impact.

## Key Claims

- Modern AI value comes from compound systems, not individual models, so no single model owns the outcome.
- Value must be decomposed into component, composition, and interaction lift; conflating them produces marketing numbers rather than causal evidence.
- Model verification, causal lift, and systemic monitoring are three distinct measurement layers.
- Counterfactual designs and control groups must be built before training; measure-later cannot recover causal attribution.
- Ablation, shadow routing, specialist isolation, and critic gating isolate each component's contribution.
- Goodhart's law compounds across interacting components, so teams should pair leading and lagging metrics.

## Related

- [Causal Lineage Map](/concepts/causal-lineage-map.md) — traces which component drove an outcome
- [Capability Forecasting](/concepts/capability-forecasting.md) — forecasting the whole system, not one model
- [Goodhart's law](/concepts/goodharts-law.md) — metric gaming compounds across components
- [Finding the Causal Root](/sources/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md) — primary source
- [Inside the System Boundary](/sources/inside-the-system-boundary.md) — the three kinds of lift
