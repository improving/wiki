---
title: "data lineage"
type: "Concept"
description: "Tracing where data came from and how it changed, captured at runtime rather than documented after the fact."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, observability, governance]
sources:
  - "/sources/effective-data-lineage-strategies-for-real-time-systems.md"
  - "/sources/data-debt-ai-predictions.md"
  - "/sources/garbage-in-garbage-out.md"
  - "/sources/real-time-data-done-right.md"
  - "/sources/responsible-ai-governance.md"
---

# data lineage

Data lineage tracks what happens to data, how it changes, and where it moves — a chain of custody distinct from system logging or tracing. Real-time streaming makes lineage both harder and more valuable: without it, a wrong dashboard or dropped model accuracy means debugging blind, and AI predictions cannot be traced back to their sources.

## Key Claims

- Lineage answers what happens to data, how it changes, and where it moves — an audit trail distinct from logging, which tracks system behavior and errors.
- A lineage model should capture types and type revisions, datasets and revisions, jobs and transformations, transformation slots, and flows and runs.
- OpenTelemetry can be adapted for lineage, but needs 100% sampling for lineage-tagged traces (traditional 1% sampling is unsuitable), custom span attributes, and custom exporters routing to a lineage backend.
- The ecosystem is fragmented: batch-oriented tools (Apache Atlas, NiFi, Collibra, OpenMetadata, Monte Carlo) and real-time options (Confluent Stream Lineage, Solace, Datorios) that lack message-level granularity, with organizations using 3–20 products and no single pane of glass.
- OpenLineage, a graduated Linux Foundation AI & Data project, offers a standardized, technology-agnostic, real-time-suitable format with growing producer and consumer support.
- Recommendations: start at job level before message level, prioritize coverage over detail, and implement consistent trace ID propagation.
- Lineage is a named fix for data debt — one AI degradation traced to an upstream redefinition of "active users" that a feature pipeline served stale for nearly a month, invisible because pipelines stayed green.

## Related

- [data debt](/concepts/data-debt.md) — the failure mode lineage exposes
- [real-time data streaming](/concepts/real-time-data-streaming.md) — the setting that raises the stakes
- [distributed tracing](/concepts/distributed-tracing.md) — trace propagation reused for lineage
- [data governance](/concepts/data-governance.md) — the discipline lineage serves
