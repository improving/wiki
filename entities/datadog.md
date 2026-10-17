---
title: "Datadog"
type: "Entity"
description: "Observability vendor whose host-based pricing and OTel GenAI adoption anchor this corpus's observability and FinOps arcs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, vendor, telemetry]
sources:
  - "/sources/agentic-development-is-eleven-problems-not-one.md"
  - "/sources/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md"
  - "/sources/observability-arc-02-opentelemetry-standardization.md"
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/observability-arc-04-wide-events-ebpf.md"
  - "/sources/observability-arc-06-aiops-rca.md"
  - "/sources/observability-arc-07-self-healing-remediation.md"
  - "/sources/observability-arc-08-finops-agentic.md"
---

# Datadog

Datadog is a dominant observability platform whose host-based pricing model and early adoption of OpenTelemetry GenAI conventions make it a recurring case in this corpus's observability-cost and agent-telemetry arcs.

## Key Claims

- Datadog's host-based billing punishes Kubernetes autoscaling, so the observability bill scales with topology rather than traffic.
- Metric cardinality grows combinatorially with label and pod combinations, making it the real cost driver.
- Datadog adopted OpenTelemetry GenAI semantic conventions natively from version 1.37 in December 2025.
- AI workloads generate 10 to 100 times more telemetry than traditional applications.
- Most production AI failures are capacity limits, not model quality.

## Related

- [OpenTelemetry](/entities/opentelemetry.md) — the standard it adopted
- [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md) — the agent-telemetry spec
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the stack its pricing exposes
- [Audit Trail](/concepts/audit-trail.md) — the reconstruction requirement it serves
- [anomaly detection](/concepts/anomaly-detection.md) — the AIOps capability it hosts
- [Datadog, Dynatrace, and the Bill That Ate Your Engineering Budget](/sources/observability-arc-03-apm-boom-observability-tax.md) — primary source
