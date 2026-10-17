---
title: "stepped-wedge design"
type: "Concept"
description: "A phased-rollout causal design in which groups switch to treatment in randomized sequence, yielding within- and between-group comparisons."
created: '2026-10-17'
updated: '2026-10-17'
tags: [causal-inference, experimentation, measurement]
sources:
  - "/sources/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md"
  - "/sources/the-right-experiment-for-the-right-claim.md"
---

# stepped-wedge design

A stepped-wedge design rolls an intervention out to groups in a randomized sequence, so every group eventually receives treatment but at different times. It is the causal design this corpus recommends when a rollout must be phased for operational reasons but the organization still needs to claim that the model, not the calendar, moved the metric.

## Key Claims

- Stepped-wedge designs fit phased rollouts when the order of adoption is randomized.
- Pre/post analysis proves a metric moved, not that the model moved it; a design must isolate the model's contribution.
- Randomize at the decision level, not by batch, day, or region.
- The strongest designs require choices made before any data is collected — counterfactual structure cannot be bolted on after training.
- Measure-later approaches produce marketing numbers rather than causal lift.
- Model verification, causal lift, and systemic monitoring are three distinct measurement layers, and compound systems require separating component, composition, and interaction lift.

## Related

- [Synthetic Control](/concepts/synthetic-control.md) — a complementary counterfactual method when full randomization is impossible
- [Causal Lineage Map](/concepts/causal-lineage-map.md) — traces which component contributed the measured effect
- [compound AI systems](/concepts/compound-ai-systems.md) — the setting where component and interaction lift must be separated
- [Capability vs Activity](/concepts/capability-vs-activity.md) — the framing that keeps measurement tied to actions, not model scores
- [Finding the Causal Root](/sources/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md) — primary source
- [The Right Experiment for the Right Claim](/sources/the-right-experiment-for-the-right-claim.md) — primary source
