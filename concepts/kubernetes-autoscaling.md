---
title: "Kubernetes autoscaling"
type: "Concept"
description: "Scaling workloads to demand, including to zero with event-driven scalers such as KEDA, and its cost and telemetry bill."
created: '2026-10-17'
updated: '2026-10-17'
tags: [kubernetes, platform, cloud-cost]
sources:
  - "/sources/keda-the-gold-standard-for-kubernetes-autoscaling.md"
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md"
  - "/sources/cost-optimization-in-amazon-ecs.md"
---

# Kubernetes autoscaling

Kubernetes autoscaling adjusts the number of running workloads to match demand, and its limits show up first on event-driven systems. The native Horizontal Pod Autoscaler scales only on container CPU and memory, which is a poor signal for a Kafka consumer whose load is really consumer lag. Event-driven scalers such as [KEDA](/entities/keda.md) close that gap and can scale workloads to zero when idle, but elasticity also carries hidden costs in observability billing and in stateful tiers that cannot be treated as interchangeable.

## Key Claims

- Kubernetes HPA natively scales only on container CPU and memory, which is unsuitable for event-driven workloads like Kafka consumers.
- The HPA-plus-adapter approach requires separately deployed, chained components and breaks when the metrics backend changes.
- [KEDA](/entities/keda.md) — a [CNCF](/entities/cncf.md) graduate — uses an Operator and Metrics Server with ScaledObjects and TriggerAuthentication to scale from any number of event sources, including Kafka, RabbitMQ, and cloud sources.
- KEDA can scale workloads to zero when idle, cutting idle cost.
- Scaling has a hidden bill: autoscaling multiplies nodes, sidecars, and label cardinality, so [Datadog](/entities/datadog.md)-style observability charges scale with topology while compute scales with traffic.
- Stateful tiers scale differently from stateless ones: a media relay cannot be treated as interchangeable servers, so autoscaling must be session-aware — which is why the control plane is split from the data plane.
- The other cost lever is capacity purchasing: [Amazon ECS](/entities/amazon-ecs.md) blends an On-Demand baseline with Spot scale-out for up to 90% savings, accepting a two-minute reclaim warning.

## Related

- [container orchestration](/concepts/container-orchestration.md) — the substrate being scaled
- [cloud cost management](/concepts/cloud-cost-management.md) — where the scaling bill lands
- [observability](/concepts/observability.md) — the telemetry cost elasticity multiplies
- [KEDA](/entities/keda.md) — event-driven autoscaling with scale-to-zero
- [Kubernetes](/entities/kubernetes.md) — the platform being scaled
- [CNCF](/entities/cncf.md) — the foundation that graduated KEDA
