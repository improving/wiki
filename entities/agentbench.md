---
title: "AgentBench"
type: "Entity"
description: "An agentic evaluation benchmark used as a reference point in this corpus's writing on eval-driven development."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, agents, benchmarks]
sources:
  - "/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md"
  - "/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# AgentBench

An agentic evaluation benchmark referenced in this corpus as part of the emerging discipline of measuring agent behaviour rather than trusting it.

## Overview

AgentBench sits in a family of agent evaluations — alongside harnesses like [SWE-bench](/entities/swe-bench.md), [SkillsBench](/entities/skillsbench.md), and [MemoryAgentBench](/entities/memoryagentbench.md) — whose central lesson is that a benchmark is only as good as the grader behind it.

## Key Claims

- An eval is best understood as an automated test suite that serves as the specification for AI behaviour, which is why the corpus argues teams should write evals before writing agents.
- Grading should layer in sequence: deterministic checks, then model-graded judgments, then human review — with [process reward models](/concepts/process-reward-models.md) approximating per-step targets where end-to-end scores are too coarse.
- [LLM-as-judge](/concepts/model-as-judge.md) carries documented bias and should be calibrated to roughly 80% rank-order agreement with humans before it is trusted.
- Evaluation should be versioned and wired into CI as [evals-as-code](/concepts/evals-as-code.md), so that models can be swapped in days with automated proof of safety.
- Reported context: 57% of organizations run agents in production, and quality is the top barrier to further adoption.

## Related

- [evaluation harness](/concepts/evaluation-harness.md) — the machinery a benchmark like this requires
- [evals-as-code](/concepts/evals-as-code.md) — practice for versioning graders and cases
- [Model-as-judge](/concepts/model-as-judge.md) — a grader tier in the stack
- [Eval-Driven Development: The Discipline Agent Teams Are Missing](/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md) — primary source
