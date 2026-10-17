---
title: "MemoryAgentBench"
type: "Entity"
description: "Benchmark finding that no current agent memory system masters retrieval, learning, long-range understanding, and selective forgetting."
created: '2026-10-17'
updated: '2026-10-17'
tags: [benchmark, memory, agents]
sources:
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
  - "/sources/why-your-agent-forgets-everything-every-morning.md"
---

# MemoryAgentBench

MemoryAgentBench is a benchmark for agent memory. Its headline result — that no current system masters retrieval, learning, long-range understanding, and selective forgetting simultaneously — anchors this corpus's argument that agent memory must be designed deliberately rather than assumed.

## Key Claims

- CoALA maps agent memory onto working, episodic, semantic, and procedural types.
- MemoryAgentBench finds no current system masters retrieval, learning, long-range understanding, and selective forgetting.
- Selective forgetting is hardest; systems stockpile outdated beliefs rather than losing facts.
- Most systems implement only working memory, so they reset every session.
- Pick the memory type first, then the tool, such as Mem0, LangMem, Zep/Graphiti, or Letta.

## Work

The benchmark reframes "the agent forgot" as an architecture gap: because most systems implement only working memory, they lose episodic and procedural knowledge between sessions and repeat mistakes. The prescription is to choose the memory type first — working, episodic, semantic, or procedural — and only then select tooling.

## Related

- [LangChain](/entities/langchain.md) — a framework whose memory tooling implements these types
- [Working Memory](/concepts/working-memory.md) — the only type most systems implement
- [Context Management](/concepts/context-management.md) — the related discipline of what stays in the window
- [context drift](/concepts/context-drift.md) — a symptom of undesigned memory
- [Why Your Agent Forgets Everything Every Morning](/sources/why-your-agent-forgets-everything-every-morning.md) — primary source
