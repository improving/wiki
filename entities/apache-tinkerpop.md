---
title: "Apache TinkerPop"
type: "Entity"
description: "Open-source graph computing framework whose Gremlin traversal language is the SQL of graph databases."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, open-source, graph]
sources:
  - "/sources/unit-testing-apache-tinkerpop-transactions-from-tinkergraph-to-amazon.md"
  - "/sources/showcasing-women-in-tech-yang-xia-and-apache-tinkerpop.md"
---

# Apache TinkerPop

Apache TinkerPop is an open-source graph computing framework for both graph databases (OLTP) and graph analytics (OLAP), modeling data as vertices (objects) connected by edges (relationships). Its Gremlin traversal language plays the role SQL plays for relational databases, and the framework lets developers add graph capabilities without building their own APIs, graph processing engines, or algorithms.

## Key Claims

- Gremlin is TinkerPop's graph traversal language, analogous to SQL for relational databases.
- TinkerPop's project management committee (PMC) governs the project under the [Apache Software Foundation](/entities/apache-software-foundation.md), holding sole authority to vote on formal releases and to add committers.
- TinkerTransactionGraph, introduced in Apache TinkerPop 3.7.0, makes transactional unit testing feasible in embedded Java mode.
- TinkerTransactionGraph offers only read-committed isolation and optimistic locking (retry on exception), so some scenarios still need a full suite against production graph databases.
- Improving consultant [Yang Xia](/entities/yang-xia.md) became the firm's first Apache PMC member through her TinkerPop work, moving from a Gremlin-based JDBC driver to a Go implementation of Gremlin.

## Related

- [Amazon Neptune](/entities/amazon-neptune.md) — the managed graph database these workloads target
- [knowledge graph](/concepts/knowledge-graph.md) — the vertices-and-edges data model
- [automated testing](/concepts/automated-testing.md) — transactional unit testing with TinkerGraph
