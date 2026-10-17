---
title: "real-time data streaming"
type: "Concept"
description: "Processing events continuously as they occur, with delivery guarantees, ordering, and replay."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, streaming, platform]
sources:
  - "/sources/real-time-data-done-right.md"
  - "/sources/real-time-is-the-easy-part.md"
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/designing-a-gcp-cloud-etl-pipeline.md"
  - "/sources/simplify-stream-processing-with-serverless-apache-flink.md"
  - "/sources/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic.md"
---

# real-time data streaming

Real-time data streaming processes events continuously as they occur, giving systems fresh state instead of overnight batches. Getting streaming running has never been easier, but "real time is the easy part" — the day-two-and-beyond problems of observability, delivery guarantees, ordering, replay, and governance burn runway, so a successful platform is planned around four pillars: scalability and resilience, governance and security, observability, and developer experience.

## Key Claims

- Point-to-point connections between sources and consumers become a fragile tangle as they multiply; event-driven architecture fixes this, but without planning can recreate the same complexity.
- Standard metrics (throughput, latency, broker health, consumer lag) can all look green while data is silently missing; supplement them with black-box signals (what users see) and white-box signals (internal state) such as dead-letter-queue buildup, unreconciled events, and entity staleness.
- Delivery guarantees are at-most-once, at-least-once, and exactly-once; "effectively once" via an at-least-once producer plus an idempotent consumer serves roughly 80% of use cases.
- A dead letter queue stores a problem rather than solving it, so plan replay as a routine operation with idempotency, ordering, and filtering.
- Sub-second, high-volume pipelines are achievable on-prem: one Kafka/Spark/Hive design handles 10TB/day and 100K+ events/sec with sub-second latency, and a serverless GCP pipeline lands 10TB/day in BigQuery at roughly 600ms end to end.
- Setting MQTT QoS to 1 is not enough for at-least-once delivery into Kafka; the fix combines `cleanStart: false` with a positive `sessionExpiryInterval` and manual acknowledgements.
- Governance at scale means picking one center of gravity for schema and lineage, encoding access control and schema changes as code via GitOps with CI/CD validation, and building self-service templates on top.

## Related

- [event-driven architecture](/concepts/event-driven-architecture.md) — decoupled producers and consumers
- [stream processing](/concepts/stream-processing.md) — computing over unbounded streams
- [data lineage](/concepts/data-lineage.md) — visibility from source to destination
- [latency budget](/concepts/latency-budget.md) — the end-to-end delay target
