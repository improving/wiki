---
title: "KEDA"
type: "Entity"
description: "Kubernetes Event-Driven Autoscaling, a CNCF-graduated scaler that can scale workloads to zero."
created: '2026-10-17'
updated: '2026-10-17'
tags: [kubernetes, autoscaling, cloud-cost]
sources:
  - "/sources/keda-the-gold-standard-for-kubernetes-autoscaling.md"
---

# KEDA

KEDA (Kubernetes Event-Driven Autoscaling) is a CNCF-graduated autoscaler that scales Kubernetes workloads on event sources rather than only CPU and memory. The corpus treats it as the gold standard for autoscaling because it handles event-driven workloads natively and can scale to zero.

## Key Facts

- Kubernetes' native Horizontal Pod Autoscaler scales only on container CPU and memory, which is unsuitable for event-driven workloads like Kafka consumers.
- KEDA scales on event sources such as Kafka consumer lag, RabbitMQ, and cloud events, using ScaledObjects and TriggerAuthentication.
- It installs as a single pair — an Operator and a Metrics Server — whereas the HPA-plus-adapter approach requires separately deployed, chained components and breaks when the metrics backend changes.
- KEDA can scale workloads to zero when idle, cutting idle cost.

## Related

- [Kubernetes autoscaling](/concepts/kubernetes-autoscaling.md) — the capability KEDA provides
- [container orchestration](/concepts/container-orchestration.md) — the platform it scales
- [cloud cost management](/concepts/cloud-cost-management.md) — the savings from scale-to-zero
- [CNCF](/entities/cncf.md) — the foundation that graduated KEDA
