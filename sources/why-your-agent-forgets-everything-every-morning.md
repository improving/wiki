---
title: "Why Your Agent Forgets Everything Every Morning"
type: "Source Summary"
description: "Agent memory fails because retention isn't designed; the CoALA taxonomy names four memory types teams must choose between deliberately."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/why-your-agent-forgets-everything-every-morning/why-your-agent-forgets-everything-every-morning.md"
---

# Why Your Agent Forgets Everything Every Morning — Summary

**Original source**: `references/devlinliles.com/why-your-agent-forgets-everything-every-morning/why-your-agent-forgets-everything-every-morning.md`

## Summary

Liles diagnoses the common complaint that deployed agents "keep making the same mistakes": retention isn't designed, so agents have nowhere to put what they learn. He walks through the CoALA taxonomy's four memory types — working, episodic, semantic, and procedural — noting most systems implement only the first. MemoryAgentBench's central finding is that no system masters retrieval, test-time learning, long-range understanding, and selective forgetting; selective forgetting is hardest, so memory systems stockpile stale beliefs rather than lose facts. The practical advice is to name the memory type you need before picking a tool.

## Key Claims

- Working memory is the finite context window; every other memory type extends effective working memory beyond the context limit.
- Episodic memory records events ("I've seen this error before"), semantic memory stores atemporal facts, and procedural memory encodes learned strategies — the hardest and highest-leverage type.
- MemoryAgentBench probes four competencies and finds no current system masters all four; selective forgetting is the hardest.
- Without selective forgetting, an agent told "Postgres" in January and "CockroachDB" in April holds both beliefs and chooses unpredictably.
- Mem0 (~48K GitHub stars, $24M raised October 2025) is the most widely deployed production memory system; LangMem, Zep/Graphiti, and Letta each cover different memory types.

## Relevance

Informs [context management](/concepts/context-management.md) and [working memory](/concepts/working-memory.md) design for production agents.

## Quality

Practitioner blog post by Devlin Liles. Useful, well-structured survey of memory frameworks and benchmarks; adoption and funding figures are cited but not independently verified.

## Entities Mentioned

- [MemoryAgentBench](/entities/memoryagentbench.md) — the primary memory evaluation benchmark cited

## Concepts Covered

- [Working Memory](/concepts/working-memory.md) — the first of the four CoALA memory types
- [Context Management](/concepts/context-management.md) — the broader discipline of extending effective context
