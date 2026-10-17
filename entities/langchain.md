---
title: "LangChain"
type: "Entity"
description: "LLM application framework whose routing and context tooling anchor this corpus's cost and context-management arguments."
created: '2026-10-17'
updated: '2026-10-17'
tags: [framework, llm, tooling]
sources:
  - "/sources/read-the-accuracy-number-next-to-the-cost-number.md"
  - "/sources/the-context-window-is-not-a-filing-cabinet.md"
---

# LangChain

LangChain is a widely used framework for building LLM applications, spanning chains, retrieval, and agent orchestration. This corpus references it as the layer where model routing and context management get implemented — and where their costs and failure modes surface.

## Key Claims

- A routing savings percentage without an accuracy delta is half an experiment.
- Routing accuracy is a property of a router paired with a specific workload.
- Saturation, pollution, and retrieval latency are the three context window problems.
- Context pollution misleads agents even when there is technically enough room.
- RAG shifts failure from window too full to window filled with wrong things.

## Work

As the orchestration layer, LangChain is where routing decisions and retrieval get wired in. One post argues savings claims must be paired with accuracy measured on the client's actual workload, and that aggregate accuracy can hide worse failure rates on the hardest requests. Context management, not raw window size, is the discipline that keeps agents reliable.

## Related

- [MemoryAgentBench](/entities/memoryagentbench.md) — the benchmark for the memory problem LangChain's tooling addresses
- [model routing](/concepts/model-routing.md) — the cost lever its stack exposes
- [Context Management](/concepts/context-management.md) — the discipline its retrieval tooling serves
- [Context Pollution](/concepts/context-pollution.md) — a failure mode of naive retrieval
- [The Context Window Is Not a Filing Cabinet](/sources/the-context-window-is-not-a-filing-cabinet.md) — primary source
