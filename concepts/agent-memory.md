---
title: "agent memory"
type: "Concept"
description: "Giving agents durable long-term context through vector stores, summaries, and cross-session persistence."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, agents, context]
sources:
  - "/sources/why-your-agent-forgets-everything-every-morning.md"
  - "/sources/how-to-build-ai-agents-with-memory.md"
  - "/sources/building-agent-memory-systems.md"
  - "/sources/rethinking-intelligence-from-brains-to-systems.md"
---

# agent memory

Agent memory gives agents durable long-term context through vector stores, summaries, and cross-session persistence, turning a one-shot chatbot into something that maintains state, learns from outcomes, and stays aligned with constraints. The sources stress that memory is a designed mechanism, not a bigger [context window](/concepts/context-window.md): retrieval, pruning, and write-back must be deliberate, and selective forgetting is the hardest part.

## Key Claims

- Memory splits into working (the finite context window), episodic (past events and outcomes), semantic (stable facts and preferences), and procedural (runbooks and learned strategies); most systems implement only the first.
- MemoryAgentBench probes retrieval, test-time learning, long-range understanding, and selective forgetting and finds no current system masters all four — forgetting is hardest.
- Without selective forgetting, an agent told "Postgres" in January and "CockroachDB" in April holds both beliefs and chooses unpredictably.
- RAG is stateless external knowledge retrieval; memory is stateful, personalized internal context — the best systems use both.
- Plain nearest-neighbor retrieval is insufficient: over-fetch candidates and rerank by blending cosine similarity with an exponential time-decay score so recent incidents outrank older but similar ones.
- Context stuffing degrades attention and wastes tokens; use rolling summaries (e.g., every six messages), token-budget pruning, and structured write-back into the store.
- Cross-session persistence has two scopes — user-level profile facts and thread-level session history — and "silent summarization" injects the prior session summary to solve the cold-start problem.

## Related

- [Working Memory](/concepts/working-memory.md) — the first of the memory types
- [Context Management](/concepts/context-management.md) — the broader discipline of extending context
- [Context Window](/concepts/context-window.md) — the limit memory works around
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — stateless external retrieval, contrasted
- [temporal retrieval](/concepts/temporal-retrieval.md) — recency-aware ranking
- [Reranking](/concepts/reranking.md) — re-scoring retrieved memories
- [skill discovery](/concepts/skill-discovery.md) — progressive skill loading
- [knowledge graph](/concepts/knowledge-graph.md) — a structured store for semantic memory
