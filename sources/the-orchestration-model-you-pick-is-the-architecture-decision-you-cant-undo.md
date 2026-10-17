---
title: "The Orchestration Model You Pick Is the Architecture Decision You Can't Undo"
type: "Source Summary"
description: "Argues the orchestration framework choice — LangGraph, CrewAI, or AG2 — is a hard-to-reverse architecture decision shaping error handling, state, and debuggability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md"
---

# The Orchestration Model You Pick Is the Architecture Decision You Can't Undo — Summary

**Original source**: `references/devlinliles.com/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md`

## Summary

Devlin Liles argues that teams pick orchestration frameworks casually, then spend months fighting the resulting architectural constraints. He contrasts three dominant models — stateful graph execution (LangGraph), role-based crew execution (CrewAI), and event-driven execution (AG2/AutoGen v0.4) — noting they disagree at the level of state ownership, coordination, and what failure looks like. The supervisor/subagent structure is the dominant deployed pattern and is compatible with any of the three. Picking casually is expensive because the choice governs error handling, checkpointing, and debuggability.

## Key Claims

- LangGraph models workflows as DAGs with typed state, checkpointed per node; interrupt-and-resume lets you pause, modify state, and replay without restarting — the most capable option for complex workflows.
- CrewAI is fastest to a prototype when work maps onto roles with sequential or hierarchical handoffs, but exposes no state machinery to pause, inspect, and resume mid-execution.
- AG2 decouples agents via events, which eases adding agents but makes tracing a failure across an event chain hard — observability is not optional.
- Reliability compounds downward: twenty chained steps at 95% per step give only a 36% chance the whole chain succeeds, making circuit breakers, worktree isolation, and bounded sessions correctness requirements, not optimizations.
- Skill composition — versioned, tested skill definitions — is the unit of reuse that shrinks future failure surface.

## Relevance

Frames [orchestration layer](/concepts/orchestration-layer.md) and [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) choices alongside [checkpointing](/concepts/checkpointing.md), [state isolation](/concepts/state-isolation.md), and [circuit breakers](/concepts/circuit-breakers.md).

## Quality

Practitioner blog post by Devlin Liles. Practical, comparison-driven guidance drawn from documentation and field patterns; recommendations are judgment rather than measured benchmarks.

## Entities Mentioned

- [LangGraph](/entities/langgraph.md) — the production-grade stateful-graph option
- [AutoGen](/entities/autogen.md) — the event-driven model (AG2 / AutoGen v0.4)
- [OpenAI Swarm](/entities/openai-swarm.md) — cited as an experimental/educational reference

## Concepts Covered

- [orchestration layer](/concepts/orchestration-layer.md) — the framework decision itself
- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — supervisor/subagent and handoff patterns
- [checkpointing](/concepts/checkpointing.md) — LangGraph's pause/inspect/resume capability
- [state isolation](/concepts/state-isolation.md) — per-agent git worktrees to prevent conflicts
- [circuit breakers](/concepts/circuit-breakers.md) — containing cascading failures
- [Lusser's Law](/concepts/lussers-law.md) — the 95%^20 ≈ 36% reliability math
