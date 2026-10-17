---
title: "Mark Soule"
type: "Entity"
description: "Improving writer on streaming, KEDA, and security models."
created: '2026-10-17'
updated: '2026-10-17'
tags: [author, data, platform, security]
sources:
  - "/sources/keda-the-gold-standard-for-kubernetes-autoscaling.md"
  - "/sources/a-security-model-for-developers.md"
  - "/sources/effective-data-lineage-strategies-for-real-time-systems.md"
  - "/sources/real-time-is-the-easy-part.md"
  - "/sources/how-a-global-healthcare-manufacturer-transformed-production-lines.md"
---

# Mark Soule

An Improving architect and writer on real-time data streaming, Kubernetes operations, and security. His posts are concrete and field-tested, often drawing on client engagements to argue that starting streaming is easy while running it reliably is the hard part.

## Topics and Work

- Argues KEDA is the gold standard for [Kubernetes autoscaling](/concepts/kubernetes-autoscaling.md), scaling on event sources like Kafka consumer lag and to zero, versus the HPA-plus-adapter approach that breaks when the metrics backend changes.
- In "Real Time Is the Easy Part," catalogs the day-two streaming problems — silent data loss behind green metrics, delivery guarantees, ordering and causality, dead-letter-queue replay, and governance at scale — concluding "effectively once" serves ~80% of use cases.
- Proposes a metadata model and OpenTelemetry-based collection for [data lineage](/concepts/data-lineage.md) in real-time systems, and points to [OpenLineage](/entities/openlineage.md) as the emerging vendor-neutral standard.
- Gives developers a security mental model chaining policy → principle → standard → guideline → requirements → testable user stories, illustrated with TLS and Kafka ACLs.
- Documents [Medtronic](/entities/medtronic.md)'s move from paper-based production tracking to Kafka and Confluent Cloud pipelines across 350 sites, with predictive maintenance and reduced scrap.

## Related

- [real-time data streaming](/concepts/real-time-data-streaming.md) — his primary subject
- [event-driven architecture](/concepts/event-driven-architecture.md) — decoupled producers and consumers
- [observability](/concepts/observability.md) — seeing silent failures
- [application security](/concepts/application-security.md) — his developer security model
