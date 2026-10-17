---
title: "Milvus"
type: "Entity"
description: "Open-source vector database used here as the memory store behind an AI SRE agent and a vector-store option for agent memory."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, databases, agent-memory]
sources:
  - "/sources/how-to-build-ai-agents-with-memory.md"
  - "/sources/building-agent-memory-systems.md"
---

# Milvus

Milvus is an open-source vector database that appears in this corpus as the concrete storage layer behind agent memory. It is used in a working build of an AI SRE assistant and named as one of the vector-store options for implementing semantic memory.

## Role in the Corpus

- OpsAgent, a worked AI SRE assistant, uses a Milvus vector store with recency-reranked retrieval: over-fetch candidates, then blend cosine similarity with an exponential time-decay score so recent incidents outrank older but similar ones.
- Milvus Lite can be swapped for Pinecone while the memory patterns stay the same, illustrating that the vector store is a replaceable component of [agent memory](/concepts/agent-memory.md).
- In the layered memory architecture, Milvus is named alongside [pgvector](/entities/pgvector.md) as a way to implement semantic memory with top-k retrieval, re-ranking, recency bias, and scope filtering.

## Related

- [agent memory](/concepts/agent-memory.md) — the capability Milvus stores
- [temporal retrieval](/concepts/temporal-retrieval.md) — recency-aware ranking over stored memories
- [reranking](/concepts/reranking.md) — the second scoring pass over candidates
- [pgvector](/entities/pgvector.md) — the Postgres-native alternative
