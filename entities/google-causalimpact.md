---
title: "Google CausalImpact"
type: "Entity"
description: "Google's Bayesian structural time-series tool for estimating causal lift, cited as a method for turning model gains into P&L numbers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [causal-inference, measurement, tooling]
sources:
  - "/sources/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md"
  - "/sources/from-model-lift-to-the-p-l.md"
---

# Google CausalImpact

Google CausalImpact is a package for estimating the causal effect of an intervention using Bayesian structural time series, constructing a counterfactual from control series. This corpus cites it as part of the measurement stack that turns model-level lift into financial value.

## Overview

One post argues that AI value requires causal measurement, because model accuracy creates zero value without changing an action. It separates three layers — model verification, causal lift, and systemic monitoring — and insists counterfactual designs be built before training, since measuring later yields marketing numbers.

A companion post moves from model lift to the P&L. Naive summing of initiative lifts can overstate portfolio impact by 30 percent or more, because cannibalization, intermediate capture, and window misalignment eat the difference. Bayesian structural time series suits short histories; marketing mix modeling suits long ones. Shapley value decomposition fairly allocates credit among jointly moving initiatives.

## Key Claims

- Model accuracy creates zero value without changing an action.
- Counterfactual designs must be built before training; measure-later yields marketing numbers.
- Naive summing of initiative lifts can overstate portfolio impact by 30 percent or more.
- Bayesian structural time series suits short histories; marketing mix modeling suits long ones.
- Shapley value decomposition fairly allocates credit among jointly moving initiatives.

## Related

- [Causal Lineage Map](/concepts/causal-lineage-map.md) — the lineage the tool feeds
- [Synthetic Control](/concepts/synthetic-control.md) — the counterfactual family it belongs to
- [SHAP](/entities/shap.md) — the attribution counterpart
- [compound AI systems](/concepts/compound-ai-systems.md) — the systems whose lift it separates
- [From Model Lift to the P&L](/sources/from-model-lift-to-the-p-l.md) — primary source
