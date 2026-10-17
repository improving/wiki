---
title: "From Model Lift to the P&L"
type: "Source Summary"
description: "Causal lifts don't sum to a P&L number; portfolio attribution needs a causal lineage map, method-matched estimators, and honest intervals."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/from-model-lift-to-the-p-l/from-model-lift-to-the-p-l.md"
---

# From Model Lift to the P&L — Summary

**Original source**: `references/devlinliles.com/from-model-lift-to-the-p-l/from-model-lift-to-the-p-l.md`

## Summary

Devlin Liles argues that individual causal lift estimates do not roll up to a P&L number by themselves, and that closing that gap is its own discipline. Naively summing four initiative lifts can overstate portfolio impact by 30% or more through cannibalization, intermediate capture, and measurement-window misalignment. The honest approach requires a [causal lineage map](/concepts/causal-lineage-map.md), an estimator matched to the available data history, and always-reported uncertainty intervals.

## Key Claims

- Three error sources (cannibalization, intermediate capture, window misalignment) can overstate a naive portfolio sum by 30% or more.
- Match method to history: Bayesian structural time series (Google's CausalImpact) under six months; difference-in-differences plus BSTS at six to eighteen; marketing mix modeling at eighteen-plus.
- [Synthetic control](/concepts/synthetic-control.md) fits one treated unit with many controls and a long pre-treatment history.
- Shapley value decomposition allocates credit fairly across entangled initiatives, satisfying efficiency, symmetry, dummy, and additivity axioms — the same math as SHAP.
- Every estimate carries error from individual estimates, the additivity assumption, and non-AI factors; a number without an interval is a presentation artifact.

## Relevance

Core to AI value measurement and [causal lineage map](/concepts/causal-lineage-map.md); links model explainability to portfolio attribution.

## Quality

Practitioner blog post by Devlin Liles. Grounded in named statistical methods and academic sources; practical and rigorous, with no proprietary data.

## Entities Mentioned

- [Google CausalImpact](/entities/google-causalimpact.md) — BSTS counterfactual tool for short histories
- [SHAP](/entities/shap.md) — same Shapley math at the model-explainability layer

## Concepts Covered

- [Causal Lineage Map](/concepts/causal-lineage-map.md) — directed graph from model outputs to reported outcome
- [Synthetic Control](/concepts/synthetic-control.md) — weighted control units for single-treated-unit attribution
