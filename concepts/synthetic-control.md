---
title: "Synthetic Control"
type: "Concept"
description: "A causal method that builds a counterfactual from a weighted combination of untreated units to estimate an intervention's effect."
created: '2026-10-17'
updated: '2026-10-17'
tags: [causal-inference, measurement, attribution]
sources:
  - "/sources/from-model-lift-to-the-p-l.md"
  - "/sources/the-right-experiment-for-the-right-claim.md"
---

# Synthetic Control

Synthetic control constructs a counterfactual series by weighting untreated comparison units to mimic what the treated unit would have looked like absent the intervention. This corpus uses it as one of several causal methods for converting model-level lift into a defensible P&L number, especially where a clean randomized experiment is not available.

## Key Claims

- Naive summing of initiative lifts can overstate portfolio impact by 30 percent or more.
- Cannibalization, intermediate capture, and window misalignment eat the difference between summed and real impact.
- Bayesian structural time series suits short histories; marketing mix modeling suits long ones.
- Shapley value decomposition fairly allocates credit among initiatives that move jointly.
- Pre/post analysis only proves a metric moved; isolating the model's contribution needs a counterfactual design chosen before deployment.
- Confidence intervals should be reported honestly rather than as a single headline number.

## Related

- [stepped-wedge design](/concepts/stepped-wedge-design.md) — the phased-rollout alternative when randomization is possible
- [Causal Lineage Map](/concepts/causal-lineage-map.md) — connects measured effect back to the component that caused it
- [Google CausalImpact](/entities/google-causalimpact.md) — a well-known implementation of the Bayesian structural time-series approach
- [From Model Lift to the P&L](/sources/from-model-lift-to-the-p-l.md) — primary source
- [The Right Experiment for the Right Claim](/sources/the-right-experiment-for-the-right-claim.md) — primary source
