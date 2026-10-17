---
title: "Name Resolution Was Never Enough"
type: "Source Summary"
description: "AI asset discovery should follow service discovery's evolution but skip name-first resolution, becoming capability-first registries in a shared graph."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/name-resolution-was-never-enough/name-resolution-was-never-enough.md"
---

# Name Resolution Was Never Enough — Summary

**Original source**: `references/devlinliles.com/name-resolution-was-never-enough/name-resolution-was-never-enough.md`

## Summary

[Service Discovery](/concepts/service-discovery.md) spent two decades learning that a name and address are not enough: DNS solved naming, client- and server-side discovery added location, and registries like Consul and etcd added a live, health-checked index answering whether a thing is safe to call. The post argues AI asset discovery must make the same evolution but skip the slow name-first stage, because prompts, agents, and skills are defined by capability rather than by one deployable endpoint. A registry should be capability-first from day one, resolving what an asset does before how to invoke it.

## Key Claims

- A name cannot tell you whether an instance is healthy, which version runs, or whether you are authorized to call it.
- Services map cleanly to one deployable, so name-first resolution was natural; AI assets do not, so the registry should describe inputs, outputs, and a searchable capability description.
- MCP tool descriptors, A2A Agent Cards, and NANDA's AgentFacts independently converged on the same shape: describe capability first, then identity and invocation.
- These standards are young; commit to the shared pattern, not to betting a platform API on one winning spec.
- A capability registry emitting into a shared [knowledge graph](/concepts/knowledge-graph.md) that a [semantic search](/concepts/semantic-search.md) index reads becomes one graph read two ways, not two systems that may drift.

## Relevance

Connects service discovery to enterprise AI retrieval, arguing that [Model Context Protocol](/entities/model-context-protocol.md)-style capability registries and [semantic search](/concepts/semantic-search.md) should share one [knowledge graph](/concepts/knowledge-graph.md).

## Quality

Practitioner blog post by Devlin Liles. Strong synthesis across standards and citations, but the standards cited are new and untested; the convergence argument is the author's read.

## Entities Mentioned

- [Model Context Protocol](/entities/model-context-protocol.md) — its tool descriptors exemplify capability-first description

## Concepts Covered

- [Service Discovery](/concepts/service-discovery.md) — the two-decade precedent the post maps onto AI assets
- [knowledge graph](/concepts/knowledge-graph.md) — the shared substrate both halves of discovery should emit into
- [Semantic Search](/concepts/semantic-search.md) — the second reader of that same graph
