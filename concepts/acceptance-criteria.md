---
title: "acceptance criteria"
type: "Concept"
description: "Explicit, testable conditions a task must satisfy, separating done from merely coherent and catching defects at definition time."
created: '2026-10-17'
updated: '2026-10-17'
tags: [requirements, agentic-development, planning]
sources:
  - "/sources/code-without-requirements-is-just-expensive-guessing.md"
  - "/sources/coherent-but-wrong-the-case-for-a-second-planning-checkpoint.md"
  - "/sources/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md"
  - "/sources/the-defect-is-in-the-definition.md"
---

# acceptance criteria

Acceptance criteria are the explicit, testable conditions that tell an agent or team when a task is actually done. In this corpus they are the antidote to a specific failure: work that is internally coherent but resolves the wrong goal.

## Key Claims

- Most agentic development failures trace back to definition, not execution; a well-defined task states the goal, done criteria, out-of-scope items, and assumptions.
- Coherence only asks whether steps follow each other, not whether they satisfy the goal, so a separate goal-validation checkpoint should diff plans against independently extracted acceptance criteria.
- The retry loop for that checkpoint is capped at one attempt to avoid the checker and planner converging on the same wrong answer.
- Requirements act as constraints that keep agents from optimizing in the wrong direction; the blast radius of a vague spec grew by an order of magnitude with AI.
- Around day 60, velocity peaks while delivery of correct work flattens or declines — the "velocity wall."
- One artifact doing spec, documentation, and tests at once does none of them well; distribution shift can drop accuracy up to 54% with no spec change.

## Related

- [Definition of Done](/concepts/definition-of-done.md) — the shared completion bar
- [Task Decomposition](/concepts/task-decomposition.md) — breaking work into checkable units
- [Specification pattern](/concepts/specification-pattern.md) — criteria as composable predicates
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — measuring against real completion
- [The Defect Is in the Definition](/sources/the-defect-is-in-the-definition.md) — primary source
