---
title: "You Can't Improve What You Can't Measure — Agentic Evaluation Done Right"
type: "Source Summary"
description: "Agentic evaluation needs a layered grader stack, evals-as-code in CI, task-appropriate benchmarks, and disciplined A/B routing."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# You Can't Improve What You Can't Measure — Agentic Evaluation Done Right — Summary

**Original source**: `references/devlinliles.com/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md`

## Summary

Liles argues that most teams know their agent's quality "by how it feels," which is hope, not evaluation. Real evaluation measures agent behavior against defined criteria rigorously enough to catch regressions before users do. He lays out a layered grader stack — structural, code-validator, LLM-as-judge, process reward models, and human evaluation as ground truth — and stresses evals-as-code stored in version control and run in CI. He also covers using task-appropriate benchmarks, a test-case taxonomy that includes adversarial cases, and A/B routing with pre-registered sample sizes.

## Key Claims

- Human review is the most familiar evaluation mechanism but the most expensive, slowest, and least scalable; it belongs at calibration and high-stakes gates.
- LLM-as-judge risks model-specific, positional, and length bias; Braintrust recommends targeting 80% rank-order agreement with human judges before trusting it.
- Process Reward Models evaluate intermediate reasoning steps and are more reliable than output-level evaluation for long-horizon tasks.
- Evals-as-code run on every prompt change make regression detection free; wiring them into CI stops them being a manual step.
- A test suite without adversarial cases is not production-ready.
- A/B routing should run until at least 95% confidence on a two-tailed test, with sample size pre-registered before launch.

## Relevance

Core to [evals-as-code](/concepts/evals-as-code.md), [Model-as-judge](/concepts/model-as-judge.md), [Process Reward Models](/concepts/process-reward-models.md), and [calibration](/concepts/calibration.md).

## Quality

Practitioner blog post by Devlin Liles. A practical, well-sourced survey of evaluation practice; benchmark and tool claims are cited but the guidance is experience-based.

## Entities Mentioned

- [Braintrust](/entities/braintrust.md) — source of the 80% judge-agreement baseline
- [SWE-bench](/entities/swe-bench.md) — the standard software-engineering benchmark cited
- [AgentBench](/entities/agentbench.md) — multi-environment agent benchmark cited

## Concepts Covered

- [Model-as-judge](/concepts/model-as-judge.md) — the subjective-quality grader and its biases
- [evals-as-code](/concepts/evals-as-code.md) — version-controlled evaluation definitions run in CI
- [Process Reward Models](/concepts/process-reward-models.md) — step-level evaluation for long-horizon tasks
- [Calibration](/concepts/calibration.md) — aligning automated graders with human judgment
