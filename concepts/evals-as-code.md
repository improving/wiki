---
title: "evals-as-code"
type: "Concept"
description: "Treating evaluation graders and test cases as version-controlled artifacts wired into CI, rather than one-off human review."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, ci, agentic-delivery]
sources:
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
  - "/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# evals-as-code

Evals-as-code is the practice of storing evaluation graders and test cases in version control and running them automatically in CI, so agent quality is measured continuously rather than judged ad hoc. It matters here because agentic delivery is described as a stack of compounding problems where reliability is a property of the whole architecture, not of any single model call.

## Key Claims

- Graders should be layered: structural, code-validator, LLM-as-judge, process reward models, and human review last.
- Evals-as-code version-controls graders and test cases and wires them into the CI pipeline, so regressions fail a build.
- [Model-as-judge](/concepts/model-as-judge.md) carries documented bias and should be calibrated to roughly 80% rank-order agreement with humans.
- A/B routing requires pre-registered sample sizes and 95% confidence before a decision is declared.
- Because failures in one layer surface as symptoms in another, evaluation must span the full delivery stack.
- The governance loop breaks at its weakest stage, not its average, so eval coverage must be complete rather than merely broad.

## Related

- [evaluation harness](/concepts/evaluation-harness.md) — the runner and rubric that host graders
- [Golden Dataset](/concepts/golden-dataset.md) — the fixed test cases evals-as-code version-controls
- [Model-as-judge](/concepts/model-as-judge.md) — a biased grader layer requiring calibration
- [Process Reward Models](/concepts/process-reward-models.md) — a step-level grading layer
- [You Can't Improve What You Can't Measure — Agentic Evaluation Done Right](/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md) — primary source
