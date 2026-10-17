---
title: "Stop Building Agents That Forget. Here's How to Fix It."
type: "Source Summary"
description: "Building OpsAgent shows agent memory as vector retrieval, context pruning, cross-session persistence, and skill loading."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, engineering, improving.com]
sources:
  - "references/improving.com/how-to-build-ai-agents-with-memory/how-to-build-ai-agents-with-memory.md"
---

# Stop Building Agents That Forget. Here's How to Fix It. — Summary

**Original source**: `references/improving.com/how-to-build-ai-agents-with-memory/how-to-build-ai-agents-with-memory.md`

## Summary

Sudhanshu Prajapati walks through building OpsAgent, an AI SRE assistant with a real memory system: a Milvus vector store with recency-reranked retrieval, rolling-summary context pruning, cross-session persistence via user profiles and episodic injection, and just-in-time skill loading. The lesson is that remembering comes from deliberate memory design, not a bigger context window.

## Key Claims

- The agent loop is Read → Retrieve → Assemble → Act → Write-back, and each memory feature maps to a stage.
- Plain nearest-neighbor retrieval is insufficient: over-fetch candidates and rerank by blending cosine similarity with an exponential time-decay score, so recent incidents outrank older but similar ones.
- Context stuffing degrades attention and wastes tokens; use rolling summaries every six messages, token-budget pruning, and structured memory extraction back into the vector store.
- Cross-session persistence has two scopes — user-level profile facts (fuzzy-deduplicated) and thread-level session history — and "silent summarization" injects the previous session's summary to solve the cold-start problem.
- Progressive disclosure loads only matched skills from an index (capped at three), following Anthropic's open Agent Skills format, instead of loading every runbook.
- Each piece is replaceable — swap Milvus Lite for Pinecone, Gemini for any embedding API, the JSON profile store for a database — while the patterns stay the same.

## Relevance

A working implementation of [agent memory](/concepts/agent-memory.md) as [context management](/concepts/context-management.md), deliberately not relying on a larger [context window](/concepts/context-window.md). Recency reranking relates to [temporal retrieval](/concepts/temporal-retrieval.md) and skill loading to [skill discovery](/concepts/skill-discovery.md).

## Quality

Hands-on engineering walkthrough by Sudhanshu Prajapati with a cloneable repo; concrete and code-level, though it is a reference demo rather than a production system.

## Entities Mentioned

- [Milvus](/entities/milvus.md) — the vector store used
- [Gemini](/entities/gemini.md) — embedding and generation model
- [LangChain](/entities/langchain.md) — a production library implementing these patterns
- [LangGraph](/entities/langgraph.md) — stateful agent orchestration option
- [Argo CD](/entities/argo-cd.md) — example of a stored user preference
- [Datadog](/entities/datadog.md) — monitoring tool in the example profile
- [Anthropic](/entities/anthropic.md) — originator of the Agent Skills format
- [Kubernetes](/entities/kubernetes.md) — infrastructure in the example context

## Concepts Covered

- [agent memory](/concepts/agent-memory.md) — the main topic
- [context management](/concepts/context-management.md) — pruning and assembly
- [context window](/concepts/context-window.md) — the limit being worked around
- [temporal retrieval](/concepts/temporal-retrieval.md) — recency-aware ranking
- [skill discovery](/concepts/skill-discovery.md) — progressive skill loading
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — memory as retrieval
