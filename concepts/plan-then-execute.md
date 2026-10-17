---
title: "Plan-then-Execute"
type: "Concept"
description: "An agent pattern that drafts a complete plan for approval before any action, trading latency for a reviewable gate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, planning, reliability]
sources:
  - "/sources/the-plan-is-a-first-class-artifact.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
---

# Plan-then-Execute

Plan-then-Execute separates an agent's reasoning from its acting: the model produces a full plan first, a gate approves it, and only then does execution begin. It matters because it inserts an approval point between intent and consequence where ReAct has none, which is the difference between a reviewable artifact and an unreviewable stream of actions.

## Key Claims

- ReAct reasons step by step and drifts on long tasks because it never looks ahead.
- Plan-then-Execute inserts an approval gate between intent and consequence.
- Tree of Thought and LATS explore candidate plans when errors are costly.
- Match the planning pattern to the reversibility of the work.
- Planning answers how and Definition answers what — and the order matters.
- Failure in one layer surfaces as a symptom in a different layer.

## Related

- [ReAct](/entities/react.md) — the reactive alternative it contrasts with
- [human approval points](/concepts/human-approval-points.md) — where the gate lives
- [Task Decomposition](/concepts/task-decomposition.md) — how the plan is structured
- [workflow sequencing](/concepts/workflow-sequencing.md) — ordering of planning and definition
- [The Plan Is a First-Class Artifact](/sources/the-plan-is-a-first-class-artifact.md) — primary source
