---
title: "AI Agents Don't Know What Changed. That's a 1969 Problem."
type: "Source Summary"
description: "The 1969 frame problem explains why production agents fail on stale world state, and points to context engineering as scaffolding."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/ai-agents-dont-know-what-changed-thats-a-1969-problem/ai-agents-dont-know-what-changed-thats-a-1969-problem.md"
---

# AI Agents Don't Know What Changed. That's a 1969 Problem. — Summary

**Original source**: `references/devlinliles.com/ai-agents-dont-know-what-changed-thats-a-1969-problem/ai-agents-dont-know-what-changed-thats-a-1969-problem.md`

## Summary

Devlin Liles argues the most common production agent failure is not hallucination but stale world state: the agent doesn't know what it already did, what is still true, and what changed. This is the frame problem, named by John McCarthy and Patrick Hayes in 1969, and never solved. Modern frameworks manage it with explicit state, checkpointing, and verification, and the post maps those workarounds onto a precise vocabulary for agent design.

## Key Claims

- A 2026 analysis attributed roughly 65% of enterprise AI failures to context drift or memory loss during multi-step reasoning, not raw context window exhaustion.
- Agents fail silently, producing plausible output from degraded or incorrect world state.
- Naive re-verification after every action solves correctness but creates prohibitive performance overhead.
- Task decomposition is a frame-management strategy: splitting work into sub-tasks with handoff state summaries resets the frame at each boundary.
- State schemas are frame definitions and verification steps are frame reset operations.
- The same management strategy recurs from the symbolic AI era through today's memory architectures and context engineering: don't solve the problem, build scaffolding that constrains it.

## Relevance

Central to [context drift](/concepts/context-drift.md) and the [Task Decomposition](/concepts/task-decomposition.md) used to manage it.

## Quality

Practitioner blog post by Devlin Liles. Strength: connects a classic AI problem to concrete production patterns and a single supporting statistic. Caveat: the 65% figure is cited without a linked source.

## Entities Mentioned

- None.

## Concepts Covered

- [context drift](/concepts/context-drift.md) — the second-largest failure category described
- [Task Decomposition](/concepts/task-decomposition.md) — a frame-management strategy
- [checkpointing](/concepts/checkpointing.md) — structured state persistence
- [Working Memory](/concepts/working-memory.md) — explicit read/write state instead of context history
- [cognitive scaffolding](/concepts/cognitive-scaffolding.md) — building constraints around an unsolved problem
