---
title: "Kubernetes"
type: "Entity"
description: "Container orchestrator whose autoscaling and self-healing behavior anchors this corpus's observability-cost and remediation arguments."
created: '2026-10-17'
updated: '2026-10-17'
tags: [infrastructure, orchestration, observability]
sources:
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/observability-arc-07-self-healing-remediation.md"
---

# Kubernetes

Kubernetes is the dominant container orchestration platform. It appears throughout this corpus less as a deployment target than as the thing that breaks assumptions in observability pricing and self-healing automation.

## Key Claims

- Datadog host-based billing punishes Kubernetes autoscaling.
- Metric cardinality grows combinatorially with label and pod combinations.
- Kubernetes self-healing is table stakes but automates symptoms, not causes.
- The trust ladder must be climbed with measured confidence gates, not skipped.
- The six-step self-healing cycle ends in Learn, the step teams skip.

## Work

Because pods are ephemeral and autoscaling multiplies hosts, host-based APM pricing makes the observability bill scale with topology rather than traffic. Kubernetes' built-in restarts and rescheduling also make self-healing look solved, but they remediate symptoms; closing the loop requires a Learn step that changes something and a recurring-failure rate measured by root cause.

## Related

- [Michael Nygard](/entities/michael-nygard.md) — stability patterns for the distributed systems Kubernetes runs
- [Datadog](/entities/datadog.md) — the vendor whose billing model its autoscaling exposes
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the telemetry its topology inflates
- [Service Discovery](/concepts/service-discovery.md) — a control-plane concern it automates
- [Datadog, Dynatrace, and the Bill That Ate Your Engineering Budget](/sources/observability-arc-03-apm-boom-observability-tax.md) — primary source
