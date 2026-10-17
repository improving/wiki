---
title: "Amazon Neptune"
type: "Entity"
description: "AWS managed graph database, used as the production target for Apache TinkerPop and Gremlin workloads."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, cloud, graph, aws]
sources:
  - "/sources/unit-testing-apache-tinkerpop-transactions-from-tinkergraph-to-amazon.md"
---

# Amazon Neptune

Amazon Neptune is AWS's managed graph database, appearing in Improving's writing as the production database that [Apache TinkerPop](/entities/apache-tinkerpop.md) and Gremlin workloads are tested against and deployed on.

## Key Claims

- Neptune provides stronger transactional guarantees than a local TinkerTransactionGraph: it prevents phantom and non-repeatable reads, where TinkerTransactionGraph offers only read-committed isolation.
- TinkerTransactionGraph uses optimistic locking (retry on exception) while Neptune uses a pessimistic wait-lock.
- Unit testing directly against Neptune requires internet access and a VPC connection, which is why a local TinkerGraph is preferred for unit tests.
- Neptune Serverless is recommended for the infrequent staging/integration portion of the test pipeline, matching production semantics cost-effectively.
- Embedded TinkerGraph testing requires Java but removes the need for a separate server process.

## Related

- [Apache TinkerPop](/entities/apache-tinkerpop.md) — the graph framework and Gremlin query language
- [automated testing](/concepts/automated-testing.md) — where the local-versus-Neptune tradeoff is made
- [AWS](/entities/aws.md) — the platform vendor
