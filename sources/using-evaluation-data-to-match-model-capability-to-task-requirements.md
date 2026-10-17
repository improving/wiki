---
title: "Using Evaluation Data to Match Model Capability to Task Requirements"
type: "Source Summary"
description: "Shows how to route tasks to the cheapest adequate model tier using an existing evaluation harness."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/using-evaluation-data-to-match-model-capability-to-task-requirements/using-evaluation-data-to-match-model-capability-to-task-requirements.md"
---

# Using Evaluation Data to Match Model Capability to Task Requirements — Summary

**Original source**: `references/devlinliles.com/using-evaluation-data-to-match-model-capability-to-task-requirements/using-evaluation-data-to-match-model-capability-to-task-requirements.md`

## Summary

Liles argues that uniformly applying one or two benchmark-selected models mismatches capability to task requirements in both directions, because benchmark performance and task-specific performance diverge. He describes using an existing evaluation harness to test lower-tier candidates against each task segment and build a versioned routing map, so cheaper models handle the tasks they can and frontier models handle the rest.

## Key Claims

- Pricing varies roughly 5–15x between frontier and smaller models in a provider's line, and most development pipelines skew toward simpler, higher-volume task types, creating optimization headroom.
- Task segmentation splits the task population into four to seven natural groups by context-window size, reasoning depth, and output format; the current model's harness scores are the baseline.
- Candidate evaluation runs the existing golden dataset and rubric against lower-tier models, asking whether each meets the segment's quality floor.
- Routing-map construction assigns each segment the minimum tier that met its floor; segments with no passing candidate keep their current model.
- Re-evaluate quarterly; running a new cheaper model against the existing dataset yields a comparability assessment in hours, and candidate evaluation often reveals the quality floor was set too loosely.
- Post-change monitoring should track behavioral quality proxies (user correction rate, downstream failure rate, output length, error rate) over a 30-day window.
- Caveats: dataset and rubric quality is the binding constraint, and smaller models may need their own prompt variant to be fairly evaluated.

## Relevance

Operationalizes [model routing](/concepts/model-routing.md) and the [golden dataset](/concepts/golden-dataset.md) within an [evaluation harness](/concepts/evaluation-harness.md).

## Quality

Practitioner guide by Devlin Liles. Concrete three-stage process with real-world observations and explicit caveats; the pricing ratios are given as shifting approximations rather than fixed figures.

## Entities Mentioned

- None.

## Concepts Covered

- [model routing](/concepts/model-routing.md) — the routing map mapping segments to the cheapest adequate tier
- [golden dataset](/concepts/golden-dataset.md) — the per-segment evaluation set compared against a quality floor
- [evaluation harness](/concepts/evaluation-harness.md) — the infrastructure that makes substitution testing practical

## Related Sources

- [Building an Evaluation Harness for Prompt Engineering: Moving Beyond Intuition](/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md)
- [Read the Accuracy Number Next to the Cost Number](/sources/read-the-accuracy-number-next-to-the-cost-number.md)
