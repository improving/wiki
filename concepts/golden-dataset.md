---
title: "Golden Dataset"
type: "Concept"
description: "A fixed, representative set of labeled cases used to score prompts and models reproducibly over time."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, testing, model-selection]
sources:
  - "/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md"
  - "/sources/using-evaluation-data-to-match-model-capability-to-task-requirements.md"
---

# Golden Dataset

A golden dataset is a curated set of representative inputs with known-good outputs, used as the stable yardstick for evaluating prompts, models, and pipelines. In this corpus it is the foundation of both the [evaluation harness](/concepts/evaluation-harness.md) and the data-driven routing that matches model capability to task requirements.

## Key Claims

- Prompts degrade from model updates, context drift, and input distribution shift, so a fixed dataset is needed to detect regressions.
- Golden datasets must represent the real input distribution, including edge cases, not just easy examples.
- Multi-dimension rubrics beat single similarity scores when scoring outputs against the dataset.
- Regression gates convert measurement into enforcement by failing changes that drop below a bar.
- Benchmark performance diverges from task-specific performance, so the dataset must reflect the actual task.
- Tasks should be segmented by context window and reasoning depth, with routing maps versioned, reviewed, and re-evaluated quarterly.
- Quality-proxy signals should be monitored for about 30 days after a routing change.

## Related

- [evaluation harness](/concepts/evaluation-harness.md) — the runner that scores against the dataset
- [model routing](/concepts/model-routing.md) — the routing map built from evaluation data
- [Model selection](/concepts/model-selection.md) — choosing models using dataset evidence
- [Distribution shift](/concepts/distribution-shift.md) — the drift a golden dataset guards against
- [Building an Evaluation Harness for Prompt Engineering: Moving Beyond Intuition](/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md) — primary source
