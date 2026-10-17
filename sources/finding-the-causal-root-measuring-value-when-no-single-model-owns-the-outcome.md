---
title: "Finding the Causal Root: Measuring Value When No Single Model Owns the Outcome"
type: "Source Summary"
description: "Argues model accuracy is not value, and that measuring AI's causal contribution requires counterfactuals designed before training."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md"
---

# Finding the Causal Root: Measuring Value When No Single Model Owns the Outcome — Summary

**Original source**: `references/devlinliles.com/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome/finding-the-causal-root-measuring-value-when-no-single-model-owns-the-outcome.md`

## Summary

Liles argues that model accuracy is not value: value is a causal question about whether the model changed an outcome the business cares about, and whether that change would have happened anyway. He separates three layers — model verification, causal lift, and systemic monitoring — that enterprises routinely conflate, and insists the counterfactual be designed before training. Because modern systems are compound, he adds methods for resolving lift to individual components and warns that composition-level Goodhart compounds fastest.

## Key Claims

- RAND (2024) found over 80% of AI projects fail, roughly 2x non-AI IT projects, mostly from misframed problems and missing measurement; McKinsey (2025) found only ~39% of organizations could attribute any EBIT impact to AI.
- The counterfactual does not exist in your data unless you build it; designs ordered by strength run from RCTs through holdback and stepped-wedge to difference-in-differences and synthetic control.
- Measure-later makes randomization impossible and turns a defensible number into a marketing number; every value claim must be net of full cost.
- In compound systems, component, composition, and interaction lift have different durability — composition value travels with your engineering.
- Goodhart's law, tied to reward hacking, compounds faster at the composition level, so pair leading with lagging metrics and refuse to auto-tune on proxies.

## Relevance

Central to [stepped-wedge design](/concepts/stepped-wedge-design.md), [compound AI systems](/concepts/compound-ai-systems.md), [Goodhart's law](/concepts/goodharts-law.md), [synthetic control](/concepts/synthetic-control.md), and the [causal lineage map](/concepts/causal-lineage-map.md).

## Quality

Practitioner blog post by Devlin Liles. Dense and heavily sourced with named studies; the statistics measure different things and Liles flags that explicitly.

## Entities Mentioned

- [McKinsey & Company](/entities/mckinsey-company.md) — 2025 State of AI survey on attributable EBIT impact
- [Google CausalImpact](/entities/google-causalimpact.md) — Bayesian structural time series for clean intervention windows
- [NIST AI RMF](/entities/nist-ai-rmf.md) — cited governance framework

## Concepts Covered

- [stepped-wedge design](/concepts/stepped-wedge-design.md) — phased randomized rollout fitting AI deployment
- [compound AI systems](/concepts/compound-ai-systems.md) — why the causal root is distributed across components
- [Goodhart's law](/concepts/goodharts-law.md) — compositional Goodhart and proxy-tuning degradation
- [synthetic control](/concepts/synthetic-control.md) — a quasi-experiment when randomization is impossible
- [causal lineage map](/concepts/causal-lineage-map.md) — directed graph from model outputs to reported outcomes
