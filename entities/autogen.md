---
title: "AutoGen"
type: "Entity"
description: "Event-driven multi-agent orchestration framework whose decoupled agents trade debuggability for flexibility."
created: '2026-10-17'
updated: '2026-10-17'
tags: [framework, multi-agent, orchestration]
sources:
  - "/sources/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md"
  - "/sources/your-multi-agent-system-has-a-coordination-problem.md"
---

# AutoGen

AutoGen (also referenced as AG2) is a multi-agent orchestration framework discussed in this corpus as one of the hard-to-reverse architecture choices teams make when building agent systems. Its event-driven model decouples agents from one another, which buys flexibility at the cost of debuggability.

## Overview

- One post argues orchestration framework choice fixes error handling, state ownership, and debuggability — making it an architecture decision you can't undo.
- In that comparison, AG2's event-driven model decouples agents but hurts debuggability, while [LangGraph](/entities/langgraph.md)'s checkpointed DAGs are framed as the production-grade option for complex workflows.
- The companion post locates most failures at the boundaries between agents, arguing that [state isolation](/concepts/state-isolation.md) and standardized protocols matter more than the framework label.

## Key Claims

- Chained 95%-reliable steps yield only 36% end-to-end success across twenty steps.
- Coordination problems are distinct from execution problems and usually surface in production.
- Supervisor/worker is the most debuggable and most common enterprise coordination model.
- Shared state corruption is the most common multi-agent failure mode.

## Related

- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — the problem AutoGen addresses
- [orchestration layer](/concepts/orchestration-layer.md) — the architectural layer it occupies
- [state isolation](/concepts/state-isolation.md) — the mitigation the corpus recommends
- [LangGraph](/entities/langgraph.md) — the contrasting production-grade option
- [The Orchestration Model You Pick Is the Architecture Decision You Can't Undo](/sources/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md) — primary source
- [Your Multi-Agent System Has a Coordination Problem](/sources/your-multi-agent-system-has-a-coordination-problem.md) — companion source
