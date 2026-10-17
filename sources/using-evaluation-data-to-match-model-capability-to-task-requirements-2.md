---
title: "Using Evaluation Data to Match Model Capability to Task Requirements"
type: "Source Summary"
description: "Argues teams should pick production models from their own evaluation data instead of defaulting to the largest model."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/using-evaluation-data-to-match-model-capability-to-task-requirements-2/using-evaluation-data-to-match-model-capability-to-task-requirements-2.md"
---

# Using Evaluation Data to Match Model Capability to Task Requirements — Summary

**Original source**: `references/devlinliles.com/using-evaluation-data-to-match-model-capability-to-task-requirements-2/using-evaluation-data-to-match-model-capability-to-task-requirements-2.md`

## Summary

This companion post argues that once an evaluation harness is running, the resulting data should drive which model runs in production, replacing the default instinct to use the largest model. Because "more capable" is measured on general benchmarks rather than your task, teams overpay for unused capability and may miss a smaller model that fits better. Liles walks through reading scores, task-model fit, sampling, validation, and cost optimization, and stresses the discipline of letting data override intuition.

## Key Claims

- The default of picking the largest model pays for capability measured against general benchmarks, not your specific task.
- A raw score hides dimensions that matter: cost per token (a candidate might be 10x cheaper), latency (5x faster), availability across vendors, and consistency (fewer catastrophic failures can beat a higher average).
- Task-model fit: run the test set across models to see where each wins or fails by case type (legacy vs. modern code, simple vs. complex) and by failure-mode category.
- Sampling strategy: baseline one model on the full set, run two or three candidates on a 20–30 case representative subset, and only run full coverage if still uncertain.
- Respect the validation-vs-production boundary: shadow-deploy the top candidate and score its real-input outputs before promoting, because the test set is not the full distribution.
- Cost example: a 92%-correct model at $0.005 per execution versus an 89% candidate at 60% cheaper — decide by the cost of an error, which many teams overpay to avoid.
- The hard part is discipline: when intuition says "use the latest model" but your data says it does not perform better, the data should win.

## Relevance

Founds [model selection](/concepts/model-selection.md) on [evaluation harness](/concepts/evaluation-harness.md) data and connects to [prompt engineering](/concepts/prompt-engineering.md) as an iterative loop.

## Quality

Practitioner post by Devlin Liles. Practical and concrete, with a clear sampling and validation recipe; the numeric examples (scores, prices, savings) are illustrative rather than empirical findings.

## Entities Mentioned

- None.

## Concepts Covered

- [model selection](/concepts/model-selection.md) — choosing production models from task-specific evaluation data
- [evaluation harness](/concepts/evaluation-harness.md) — the source of the scores and the mechanism for comparison
- [prompt engineering](/concepts/prompt-engineering.md) — the iterative loop between prompt tuning and model choice

## Related Sources

- [Building an Evaluation Harness for Prompt Engineering: Moving Beyond Intuition](/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md)
- [The Evaluation-Governance Flywheel: Neither Works Without the Other](/sources/the-evaluation-governance-flywheel-neither-works-without-the-other.md)
