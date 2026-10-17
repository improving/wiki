---
title: "evaluation harness"
type: "Concept"
description: "A structured test rig — golden dataset, rubric, runner, and regression gate — that replaces intuition in AI evaluation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, testing, model-selection]
sources:
  - "/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md"
  - "/sources/the-evaluation-governance-flywheel-neither-works-without-the-other.md"
  - "/sources/using-evaluation-data-to-match-model-capability-to-task-requirements-2.md"
---

# evaluation harness

An evaluation harness is the scaffolding that makes AI quality measurable: a representative golden dataset, a scoring rubric, an automated runner, and a regression gate. Across this corpus it is the mechanism that turns prompt engineering from intuition into engineering, and the baseline that production monitoring and governance depend on.

## Key Claims

- Prompts degrade from model updates, context drift, and input distribution shift, so evaluation must be continuous.
- Golden datasets must represent the real input distribution, including edge cases; a task-representative test set establishes the production baseline.
- Multi-dimension rubrics beat single similarity scores.
- Regression gates convert measurement into enforcement.
- METR found automated graders overstated PR mergeability by about 24 points, and harness quality explains 17–21 points of task-completion variance.
- A 20–30 case subset can rank candidate models cheaply, and candidates should be shadow-deployed before promotion.
- Defaulting to the largest model buys capability the task does not need; raw scores miss cost, latency, availability, and consistency tradeoffs.

## Related

- [Golden Dataset](/concepts/golden-dataset.md) — the representative test set at the harness's core
- [evals-as-code](/concepts/evals-as-code.md) — harnesses kept under version control
- [Model-as-judge](/concepts/model-as-judge.md) — automated grading and its overstatement risk
- [Model selection](/concepts/model-selection.md) — matching capability to task requirements
- [Quality Gates](/concepts/quality-gates.md) — the regression gate in CI
- [Distribution shift](/concepts/distribution-shift.md) — the failure mode harnesses must probe
- [Building an Evaluation Harness for Prompt Engineering: Moving Beyond Intuition](/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md) — primary source
