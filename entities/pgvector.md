---
title: "pgvector"
type: "Entity"
description: "Postgres extension for vector similarity search, cited here as a way to keep semantic memory inside a relational store."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, databases, agent-memory]
sources:
  - "/sources/building-agent-memory-systems.md"
---

# pgvector

pgvector is a Postgres extension for vector similarity search that appears in this corpus as one option for implementing the semantic layer of agent memory. Its appeal is architectural: it keeps embeddings inside a relational database the team may already run, rather than adding a dedicated vector store.

## Role in the Corpus

- In a layered [agent memory](/concepts/agent-memory.md) design, semantic memory is implemented in vector stores with top-k retrieval, re-ranking, recency bias, and scope filtering; pgvector is named as one such store alongside [Milvus](/entities/milvus.md).
- The source treats the vector store as a replaceable component — the memory patterns matter more than the specific engine.

## Related

- [agent memory](/concepts/agent-memory.md) — the capability pgvector supports
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — the retrieval pattern it serves
- [Milvus](/entities/milvus.md) — the dedicated vector database alternative
