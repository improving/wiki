---
title: "Eighteen Percent, Two Models Ago"
type: "Source Summary"
description: "A DrugQA abstention gate rested on a launch-era 18% error figure that nobody re-measured across two model swaps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/eighteen-percent-two-models-ago/eighteen-percent-two-models-ago.md"
---

# Eighteen Percent, Two Models Ago — Summary

**Original source**: `references/devlinliles.com/eighteen-percent-two-models-ago/eighteen-percent-two-models-ago.md`

## Summary

DrugQA shipped with an abstention gate justified by one number: on a 50-question held-out set of ambiguous interaction questions, the launch model gave confidently wrong answers 18% of the time. The gate ran unchanged for two model generations because nothing in the system ever asked whether 18% was still true. The fix is a scheduled job re-running the identical eval against the currently deployed model, storing model version, measured rate, and timestamp, and plotting the live rate against the frozen baseline.

## Key Claims

- The gate's added latency, occasional over-abstention, and escalation routing all rest on a single launch-era measurement of 18%.
- The inherited dashboard showed "18% (measured at launch)," a staleness counter with no ceiling, and a "current rate: unknown" field that never filled itself in.
- A system can carry a mechanism for checking its own assumptions and still never check them, if invoking that mechanism depends on someone remembering to.
- The fix is one recurring job: the same eval, the same failure definition, re-run against whichever model is actually deployed, with the baseline-minus-current gap stored alongside each run.
- The pattern only answers whether a specific guarded failure rate changed; it says nothing about whether the gate's design still fits a model with a genuinely different error profile.
- The eval set itself can drift out of representativeness as the underlying domain changes, so re-running a stale eval still yields a stale answer.

## Relevance

Informs [model drift detection](/concepts/model-drift-detection.md) and [golden dataset](/concepts/golden-dataset.md) practice in evaluation and abstention systems.

## Quality

Practitioner blog post by Devlin Liles. A strong single-case narrative with one concrete figure and an honest account of the pattern's limits; evidence is a single system, not a study.

## Entities Mentioned

- None.

## Concepts Covered

- [model drift detection](/concepts/model-drift-detection.md) — the recurring job that tracks a guarded failure rate as models change
- [golden dataset](/concepts/golden-dataset.md) — the frozen 50-question held-out set re-run each cycle
