---
title: "OpenTelemetry"
type: "Entity"
description: "The vendor-neutral telemetry standard that decoupled instrumentation from analytics and now covers AI agent traces."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, standard, telemetry, cncf]
sources:
  - "/sources/observability-arc-02-opentelemetry-standardization.md"
  - "/sources/observability-arc-08-finops-agentic.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
---

# OpenTelemetry

OpenTelemetry (OTel) is the vendor-neutral instrumentation standard for metrics, logs, and traces. In this corpus it is both the resolution of the observability vendor wars and the emerging substrate for AI agent telemetry.

## Overview

OpenTracing and OpenCensus merged into OpenTelemetry on May 7, 2019, and the Collector made "instrument once, export anywhere" concrete — turning the backend into a configuration change rather than a rewrite, which decoupled the instrumentation market from the analytics market. With AI workloads generating 10 to 100 times more telemetry than traditional apps, OTel GenAI conventions standardize how agent telemetry is captured across backends, and observability becomes a managed cost center with per-inference unit economics.

## Key Claims

- OpenTracing and OpenCensus merged into OpenTelemetry on May 7, 2019
- The Collector makes instrument-once, export-anywhere concrete
- OTel decoupled the instrumentation market from the analytics market
- AI workloads generate 10 to 100 times more telemetry than traditional apps
- OTel GenAI conventions standardize AI telemetry capture across backends

## Related

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — metrics, logs, and traces
- [Audit Trail](/concepts/audit-trail.md) — durable decision records
- [token cost](/concepts/token-cost.md) — per-inference unit economics
- [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md) — the AI-specific profile
- [Datadog](/entities/datadog.md) — adopted the conventions natively
- [Metrics, Logs, Traces — and the War That Standardization Won](/sources/observability-arc-02-opentelemetry-standardization.md) — primary source
