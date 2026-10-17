---
title: "Service Discovery"
type: "Concept"
description: "Resolving which capability to use at runtime — now applied to AI assets, not just network services."
created: '2026-10-17'
updated: '2026-10-17'
tags: [distributed-systems, agents, discovery]
sources:
  - "/sources/a-person-and-a-pipeline-are-asking-the-same-question.md"
  - "/sources/name-resolution-was-never-enough.md"
---

# Service Discovery

Service discovery is the machinery that answers "which capability should I use, and is it healthy?" Historically that meant DNS names; today it means resolving AI assets — models, agents, tools, skills — for both people and pipelines. The corpus argues the human search box and the machine resolver are the same question asked on different clocks, and staffing them as two systems guarantees their descriptions drift apart.

## Key Claims

- DNS solved naming but never answered health, version, or authorization.
- Consul, etcd, and Zookeeper added live, health-checked service indexes — the pattern AI assets now need.
- People and pipelines resolve capabilities on different clocks with different error tolerance, yet both are lenses over one asset object: identity, capability, version, owner, health.
- MCP, A2A, and NANDA AgentFacts converge on capability-first descriptions.
- A capability registry and semantic search should read one shared knowledge graph.
- Design the shared capability contract once, then expose it through an index and a resolver.

## Related

- [Semantic Search](/concepts/semantic-search.md) — the query interface over a capability registry
- [knowledge graph](/concepts/knowledge-graph.md) — the shared source of truth both lenses read
- [Model Context Protocol](/entities/model-context-protocol.md) — one converging capability-first description format
- [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) — federated metadata for AI assets
- [A Person and a Pipeline Are Asking the Same Question](/sources/a-person-and-a-pipeline-are-asking-the-same-question.md) — primary source
- [Name Resolution Was Never Enough](/sources/name-resolution-was-never-enough.md) — primary source
