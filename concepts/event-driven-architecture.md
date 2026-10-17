---
title: "event-driven architecture"
type: "Concept"
description: "Systems that communicate through streams of events, decoupling producers from consumers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, architecture, streaming]
sources:
  - "/sources/real-time-data-done-right.md"
  - "/sources/designing-distributed-systems.md"
  - "/sources/real-time-is-the-easy-part.md"
  - "/sources/designing-a-gcp-cloud-etl-pipeline.md"
  - "/sources/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md"
---

# event-driven architecture

Event-driven architecture communicates through streams of events so producers and consumers are decoupled, rather than wiring point-to-point connections that become a fragile tangle as they multiply. It rests on asynchronous messaging — modeled on the postal service rather than the phone call — which scales because messages queue instead of requiring an immediate answer, and most robust real systems blend synchronous and asynchronous communication.

## Key Claims

- Synchronous communication ("phone calls") underlies the web and suits customized real-time experiences; asynchronous messaging ("postal service") scales because messages queue.
- Large-scale commerce such as Ticketmaster or Hasbro card drops uses async requests to temporarily lock inventory so seats are never sold twice; streaming services deliver the last mile synchronously per consumer while running asynchronously internally.
- Sync costs compute and network while async adds per-message overhead, so the design should match the business goal.
- Event-driven platforms (Apache Kafka, Confluent Cloud) address the tangle of direct connections, but without planning can recreate the same complexity.
- Platform pillars are scalability and resilience (Kubernetes, Terraform, tiered storage, Kafka self-healing), governance and security (schema validation, RBAC, field-level encryption), observability, and developer experience.
- In a serverless GCP pipeline, GCS object-finalized events trigger a Cloud Function that publishes to Pub/Sub, which buffers and decouples, enabling horizontal scaling, replay on downstream failure, and backpressure via flow control.
- An event-driven orchestration model decouples agents, easing the addition of new agents but making failures across an event chain hard to trace, so observability is not optional.

## Related

- [real-time data streaming](/concepts/real-time-data-streaming.md) — continuous event processing
- [stream processing](/concepts/stream-processing.md) — computing over the resulting streams
- [reactive systems](/concepts/reactive-systems.md) — message-driven, elastic, resilient systems
- [data integration](/concepts/data-integration.md) — connecting and consolidating data across sources
