---
title: "The Right Experiment for the Right Claim"
type: "Source Summary"
description: "A navigation guide to eight causal designs for attributing enterprise AI value, chosen by deployment constraints."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-right-experiment-for-the-right-claim/the-right-experiment-for-the-right-claim.md"
---

# The Right Experiment for the Right Claim — Summary

**Original source**: `references/devlinliles.com/the-right-experiment-for-the-right-claim/the-right-experiment-for-the-right-claim.md`

## Summary

Most enterprise AI ROI cases are pre/post analyses, which can prove a metric moved but not that the model moved it. Devlin Liles frames eight experimental designs, each supporting a different level of causal claim, and argues the design must be chosen before deployment because randomization is impossible once the model is live. The organizing question is simply: can you randomize?

## Key Claims

- An RCT randomizes treatment at the decision level (customer, claim, transaction); randomizing by batch, day, or region measures the rollout, not the model.
- Holdback testing is an RCT in production and is standard for recommenders, search, fraud, and pricing; holdback size is a power calculation, not a gut call.
- The [stepped-wedge design](/concepts/stepped-wedge-design.md) randomizes rollout sequence across clusters; letting readiness or urgency drive the sequence degrades it to observational.
- Regression discontinuity exploits a hard threshold in the assignment rule and is often the cleanest after-the-fact option for decisioning systems.
- Difference-in-differences assumes parallel pre-treatment trends, almost always partly violated, so estimates read as lower bounds on positive effects.
- [Synthetic Control](/concepts/synthetic-control.md) suits one treated unit with many long-history controls; interrupted time series is the weakest design and should not anchor a business case.
- The measurement design conversation belongs in discovery, before architecture, training, and vendor selection.

## Relevance

Central to [stepped-wedge design](/concepts/stepped-wedge-design.md) and [Synthetic Control](/concepts/synthetic-control.md) as tools for AI value attribution.

## Quality

Practitioner blog post by Devlin Liles. Well-organized and grounded in named academic methods (Hussey & Hughes; Abadie et al.; Pearl & Mackenzie); it is a survey, not new evidence.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author

## Concepts Covered

- [stepped-wedge design](/concepts/stepped-wedge-design.md) — randomized rollout sequence
- [Synthetic Control](/concepts/synthetic-control.md) — weighted control composite for one treated unit
