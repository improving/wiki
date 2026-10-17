---
title: "Braintrust"
type: "Entity"
description: "Evaluation platform cited in posts on eval-driven development and layered agentic grading."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, tooling, agents]
sources:
  - "/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md"
  - "/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# Braintrust

Braintrust is an evaluation platform referenced in this corpus as the tooling layer for treating AI behavior as something you specify and test rather than inspect by hand. The two posts argue evaluation is a discipline teams are missing, not a dashboard they are missing.

## Overview

- One post frames an eval as an automated test suite that serves as the specification for AI behavior, with three tiers run in sequence: deterministic, model-graded, then human review.
- The other argues for a layered grader stack — structural, code-validator, [LLM-as-judge](/concepts/model-as-judge.md), [process reward models](/concepts/process-reward-models.md), then human — version-controlled as code and wired into CI.
- Both treat eval-first development as what lets teams swap models in days with automated proof of safety.

## Key Claims

- 57% of organizations run agents in production, and quality is the top barrier.
- Evals-as-code version-controls graders and test cases and wires them into CI.
- LLM-as-judge carries documented bias; calibrate to 80% rank-order agreement with humans.
- A/B routing requires pre-registered sample sizes and 95% confidence before deciding.

## Related

- [evals-as-code](/concepts/evals-as-code.md) — the practice the platform supports
- [evaluation harness](/concepts/evaluation-harness.md) — the surrounding infrastructure
- [Model-as-judge](/concepts/model-as-judge.md) — a grader tier with documented bias
- [Process Reward Models](/concepts/process-reward-models.md) — a deeper grader layer
- [Golden Dataset](/concepts/golden-dataset.md) — the test corpus evals run against
- [Eval-Driven Development](/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md) — primary source
- [You Can't Improve What You Can't Measure](/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md) — companion source
