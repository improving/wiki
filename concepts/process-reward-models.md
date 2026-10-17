---
title: "Process Reward Models"
type: "Concept"
description: "Models that score each step of a trajectory, approximating per-move feedback where only an end-of-run reward exists."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, evaluation, agents, reinforcement-learning]
sources:
  - "/sources/agentic-systems-that-dont-improve-are-just-expensive-software.md"
  - "/sources/running-the-experiment-was-never-the-hard-part.md"
  - "/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# Process Reward Models

Process reward models (PRMs) score each step of a trajectory rather than only the final outcome. They appear in this corpus as an attempt to give agentic systems the dense, per-move feedback that made reinforcement learning work in games, where a single end-of-run reward leaves the credit assignment problem unsolved.

## Key Claims

- Without a feedback loop, agentic systems are just expensive software; PRMs are one of the loops (with reflection, RLVR, and trajectory memory) that let systems compound.
- [AlphaGo](/entities/alphago.md)'s MCTS gave a graded target on every move, sidestepping credit assignment; LLM agents instead get one reward at the end of a hundred-thousand-token trajectory.
- Process reward models approximate per-step targets, but open-ended judgment remains unsolved.
- Agentic evaluation should layer graders: structural, code-validator, [LLM-as-judge](/concepts/model-as-judge.md), process reward models, then human.
- [Evals-as-code](/concepts/evals-as-code.md) version-controls graders and test cases and wires them into CI.
- Harness simplification often beats model upgrades.

## Related

- [Model-as-judge](/concepts/model-as-judge.md) — the grader layer beneath PRMs
- [evals-as-code](/concepts/evals-as-code.md) — how graders are versioned and run
- [reward hacking](/concepts/reward-hacking.md) — the failure a step-level signal can invite
- [You Can't Improve What You Can't Measure](/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md) — primary source
