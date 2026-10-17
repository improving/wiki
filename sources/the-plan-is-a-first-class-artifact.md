---
title: "The Plan Is a First-Class Artifact"
type: "Source Summary"
description: "Planning is the upstream domain of agentic development; separating plans from execution creates the approval gates production systems require."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-plan-is-a-first-class-artifact/the-plan-is-a-first-class-artifact.md"
---

# The Plan Is a First-Class Artifact — Summary

**Original source**: `references/devlinliles.com/the-plan-is-a-first-class-artifact/the-plan-is-a-first-class-artifact.md`

## Summary

Argues that planning sits upstream of every other domain in agentic development, and that a wrong plan propagates: it is executed confidently in the wrong direction, consumes budget, and creates artifacts that must be unwound. The post contrasts planning patterns — ReAct, Plan-then-Execute, Tree of Thought/LATS, and hierarchical planning — and argues teams should match the pattern to the reversibility of the work. A plan must exist as a reviewable artifact to be auditable and approvable, and human oversight should be a dial positioned by undo difficulty rather than a switch.

## Key Claims

- ReAct reasons one step at a time and drifts on complex tasks: by step fifteen of a fifty-step task, no single step was wrong but the accumulated path has left the goal.
- Plan-then-Execute inserts a decision point between intent and consequence; you cannot audit or approve something that does not exist as an artifact.
- Tree of Thought explores multiple candidate plans, and LATS adds Monte Carlo tree search with an LLM value function — state of the art under uncertainty, at real inference cost.
- Match pattern to reversibility: ReAct for cheap rollbacks, Plan-then-Execute at minimum for anything irreversible, ToT when the cost of a bad path justifies the overhead.
- Set the gate by asking how hard a wrong result is to undo; if it means a support ticket, compensating transaction, or customer conversation, the gate goes before that step.

## Relevance

Informs [plan-then-execute](/concepts/plan-then-execute.md), [human-in-the-loop](/concepts/human-in-the-loop.md), and [human approval points](/concepts/human-approval-points.md) within agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. Synthesizes several patterns and vendor docs into a decision guide; illustrative rather than empirical, with no measurements of its own.

## Entities Mentioned

- [HumanLayer](/entities/humanlayer.md) — open-source library wrapping workflows with approval gates
- [LangGraph](/entities/langgraph.md) — interrupt-and-resume pausing execution at a graph node
- [ReAct](/entities/react.md) — the default reason-then-act loop discussed as the non-scaling baseline

## Concepts Covered

- [Plan-then-Execute](/concepts/plan-then-execute.md) — the production pattern the post recommends
- [human-in-the-loop](/concepts/human-in-the-loop.md) — oversight treated as a dial, not a switch
- [human approval points](/concepts/human-approval-points.md) — where to place gates based on reversibility
