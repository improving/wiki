---
title: "Real Time Is the Easy Part: Lessons from Building Data Streaming Platforms at Scale"
type: "Source Summary"
description: "Argues real-time streaming is easy to start and hard to run, covering observability, delivery guarantees, ordering, replay, governance, and agents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, platform, improving.com]
sources:
  - "references/improving.com/real-time-is-the-easy-part/real-time-is-the-easy-part.md"
---

# Real Time Is the Easy Part: Lessons from Building Data Streaming Platforms at Scale — Summary

**Original source**: `references/improving.com/real-time-is-the-easy-part/real-time-is-the-easy-part.md`

## Summary

Getting real-time streaming running has never been easier, but "real time is the easy part" — the day-two-and-beyond problems burn runway. The post walks through the concerns that break production streaming systems: observability that reveals silent failures, delivery guarantees, ordering and causality, dead-letter-queue replay, governance at scale, and running AI agents on fresh event streams.

## Key Claims

- Standard metrics (throughput, latency, broker health, consumer lag) can all look green while data is silently missing; supplement them with black-box signals (what users see) and white-box signals (internal state).
- Advanced signals: dead-letter-queue buildup, unreconciled events, entity staleness, and canary heartbeat events.
- Delivery guarantees: at-most-once, at-least-once, exactly-once; "effectively once" via an at-least-once producer plus an idempotent consumer serves roughly 80% of use cases, even when the stated requirement is exactly once.
- Ordering breaks on partition rebalancing, and message keys don't guarantee business causality (an "out for delivery" event can arrive before "label created"); strategies are hold-and-wait with watermarks, accept provisionally, or restructure as a state-transition workflow.
- A dead letter queue stores a problem rather than solving it; plan replay as a routine operation with idempotency, ordering, and filtering, and use an error store with automated replay at high volume.
- Pick one governance center of gravity (Confluent Cloud Schema Registry/Stream Lineage/Data Portal vs Collibra or DataHub), encode access control and schema changes as code via GitOps with CI/CD validation, and build self-service templates on top.
- Agents can use input/output topics as a communication backbone, giving auditability, access control, integration, and fresh context; the need is context engineering, not just RAG or prompt engineering.

## Relevance

Frames [real-time data streaming](/concepts/real-time-data-streaming.md) and [event-driven architecture](/concepts/event-driven-architecture.md) as operations problems, requiring [observability](/concepts/observability.md), [data quality](/concepts/data-quality.md), and [GitOps](/concepts/gitops.md) at scale.

## Quality

Practitioner field guide by Mark Soule; concrete and experience-based, with few quantified outcomes.

## Entities Mentioned

- [Mark Soule](/entities/mark-soule.md) — author
- [Apache Kafka](/entities/apache-kafka.md) — the streaming substrate
- [Confluent](/entities/confluent.md) — managed streaming and governance tooling
- [Apache Flink](/entities/apache-flink.md) — stream-processing engine cited
- [Collibra](/entities/collibra.md) — catalog option for governance center of gravity

## Concepts Covered

- [real-time data streaming](/concepts/real-time-data-streaming.md) — continuous event processing
- [event-driven architecture](/concepts/event-driven-architecture.md) — decoupled producers and consumers
- [stream processing](/concepts/stream-processing.md) — computing over unbounded streams
- [observability](/concepts/observability.md) — seeing silent failures
- [data quality](/concepts/data-quality.md) — freshness and completeness signals
- [GitOps](/concepts/gitops.md) — governance as reviewable code
- [context engineering](/concepts/context-engineering.md) — keeping agents on fresh state
