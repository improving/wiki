---
title: "Coordination Overhead"
type: "Concept"
description: "The cost of keeping parallel agents or workers aligned, which grows faster than their number."
created: '2026-10-17'
updated: '2026-10-17'
tags: [multi-agent, management, delivery]
sources:
  - "/sources/biological-coordination-patterns-applied-to-multi-agent-software-delivery.md"
  - "/sources/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled.md"
---

# Coordination Overhead

Coordination overhead is the work required to keep parallel agents, workers, or overseers aligned, and it grows faster than the count of participants themselves. It matters because it caps how much parallel capacity actually pays off: adding nodes can reduce total throughput once their mutual alignment cost exceeds the work they add.

## Key Claims

- Coordination overhead grows faster than agent count, echoing Brooks's law.
- Ten nodes yield up to 45 connection pairs, each an unmodeled coordination cost.
- Adding one human overseer per agent lowered throughput below the single-agent baseline.
- A sizing calculator bounds overseers to agent clusters under a connection ceiling.
- Concentrating oversight creates single points of failure and requires periodic resizing.
- Biological primitives — specialization, inhibition, checkpoint synchronization, and convergence — reduce the cost: specialization is interface definition, scope inhibition generalizes file locking, and convergence checks combined outputs for emergent interaction failures.

## Related

- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — the practice this cost constrains
- [Single-Agent Ceiling](/concepts/single-agent-ceiling.md) — why teams add agents at all
- [The Mythical Man-Month](/entities/the-mythical-man-month.md) — the classic statement of the law
- [Biological Coordination Patterns](/sources/biological-coordination-patterns-applied-to-multi-agent-software-delivery.md) — primitives that reduce overhead
- [Ten Nodes, Forty-Five Connections](/sources/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled.md) — measured throughput drop
