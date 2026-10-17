---
title: "state isolation"
type: "Concept"
description: "Keeping each agent's working state separate so shared mutable context cannot corrupt concurrent multi-agent work."
created: '2026-10-17'
updated: '2026-10-17'
tags: [multi-agent, architecture, reliability]
sources:
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
  - "/sources/your-multi-agent-system-has-a-coordination-problem.md"
---

# state isolation

State isolation is the practice of giving each agent its own working state instead of letting several agents read and write one shared, mutable context. In this corpus it is presented as the primary defense against the most common multi-agent failure mode — shared state corruption — and as one of a small set of coordination decisions that determine whether a multi-agent system survives production.

## Key Claims

- Shared state corruption is the most common multi-agent failure mode.
- Coordination problems are distinct from execution problems and usually surface only in production, at the boundaries between agents.
- Supervisor/worker is the most debuggable and most common enterprise coordination model.
- Most agent systems implement only working memory, so they reset every session; durable state must be isolated and externalized deliberately.
- Protocols split the remaining seams: MCP standardizes agent-to-tool communication while A2A targets agent-to-agent.
- Reliability is a property of the architecture connecting layers, and a governance loop breaks at its weakest stage, not its average.

## Related

- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — the broader problem state isolation addresses
- [Context Pollution](/concepts/context-pollution.md) — the single-agent analogue of corrupted shared state
- [Working Memory](/concepts/working-memory.md) — the state that must persist rather than reset each session
- [checkpointing](/concepts/checkpointing.md) — how isolated state is durably saved and resumed
- [task agents](/concepts/task-agents.md) — scoped agents whose state is easiest to keep isolated
- [Model Context Protocol](/entities/model-context-protocol.md) — the tool-facing half of the coordination protocol story
- [The Twelve Problems of Agentic Software Delivery](/sources/the-twelve-problems-of-agentic-software-delivery.md) — primary source
- [Your Multi-Agent System Has a Coordination Problem](/sources/your-multi-agent-system-has-a-coordination-problem.md) — primary source
