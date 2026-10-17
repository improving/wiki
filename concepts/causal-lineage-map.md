---
title: "Causal Lineage Map"
type: "Concept"
description: "Tracing how model-level lift becomes P&L, exposing where attribution leaks through cannibalization and window misalignment."
created: '2026-10-17'
updated: '2026-10-17'
tags: [measurement, causal-inference, attribution]
sources:
  - "/sources/from-model-lift-to-the-p-l.md"
  - "/sources/making-measurement-operational.md"
---

# Causal Lineage Map

A causal lineage map traces how a model-level lift actually flows into the P&L, marking the places where naive attribution leaks. It matters because portfolio impact is routinely overstated when individual initiative wins are summed without accounting for interference.

## Key Claims

- Naive summing of initiative lifts can overstate portfolio impact by 30 percent or more.
- Cannibalization, intermediate capture, and window misalignment eat the difference.
- Bayesian structural time series suits short histories; marketing mix modeling suits long ones.
- Shapley value decomposition fairly allocates credit among jointly moving initiatives.
- Value is the increment between what happened and what would have happened.
- Most AI programs stall at the holdback-design stage; measurement needs ownership across ML, analytics, and finance.

## Related

- [Synthetic Control](/concepts/synthetic-control.md) — one method for estimating the counterfactual
- [Runtime Lineage](/concepts/runtime-lineage.md) — the technical trace that grounds causal claims
- [Google CausalImpact](/entities/google-causalimpact.md) — structural time-series tooling
- [SHAP](/entities/shap.md) — attribution method for shared credit
- [From Model Lift to the P&L](/sources/from-model-lift-to-the-p-l.md) — primary source
- [Making Measurement Operational](/sources/making-measurement-operational.md) — primary source
