---
title: "Working Memory"
type: "Concept"
description: "The active, retained context an agent holds during a task — a designed mechanism, not a bigger context window."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, memory, context]
sources:
  - "/sources/a-bigger-context-window-is-not-working-memory.md"
  - "/sources/why-your-agent-forgets-everything-every-morning.md"
---

# Working Memory

Working memory is the information an agent actively retains and reasons over during a task. This corpus insists it is not the same as a larger [Context Window](/concepts/context-window.md): retention needs deliberate mechanisms for keeping, folding, compacting, and carrying knowledge forward, and at enterprise scale it becomes an orchestration layer with permissions and expiry.

## Key Claims

- Attention dilutes across long contexts; a wider window does not retain.
- A gated working memory hit comparable long-context scores with a quarter of the gradient steps.
- Self-timed compaction ran 30–70% cheaper and scored higher than fixed schedules.
- The CoALA taxonomy maps agent memory onto working, episodic, semantic, and procedural types, which must be chosen deliberately.
- [MemoryAgentBench](/entities/memoryagentbench.md) finds no current system masters retrieval, learning, long-range understanding, and selective forgetting; selective forgetting is hardest.

## Related

- [Context Window](/concepts/context-window.md) — the capacity that is not memory
- [Context Management](/concepts/context-management.md) — the compaction and folding mechanisms
- [orchestration layer](/concepts/orchestration-layer.md) — where enterprise memory lives
- [A Bigger Context Window Is Not Working Memory](/sources/a-bigger-context-window-is-not-working-memory.md) — primary source
