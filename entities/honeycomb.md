---
title: "Honeycomb"
type: "Entity"
description: "An observability vendor associated in this corpus with wide events, high-cardinality analysis, and the shift away from three-pillar stacks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, telemetry, vendor]
sources:
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-04-wide-events-ebpf.md"
  - "/sources/observability-arc-06-aiops-rca.md"
  - "/sources/observability-arc-08-finops-agentic.md"
---

# Honeycomb

Honeycomb is an observability vendor that appears across this corpus as the champion of [wide events](/concepts/three-pillars-of-observability.md) stored in a columnar backend, positioned against the traditional three-pillar stack of metrics, logs, and traces.

## Overview

The posts use the vendor to argue a structural point: three-pillar stacks store the same HTTP request three times, a tax that wide events avoid, and columnar storage removes the cardinality ceiling Prometheus imposes. The 2019 baseline they describe is a gap between what the books recommended and what teams actually ran — monitoring for known unknowns, not observability for unknown unknowns — with tooling leading adoption by three to five years.

## Key Claims

- Monitoring solves known unknowns; observability solves unknown unknowns, and vendor-specific instrumentation was the structural friction.
- Three-pillar stacks store the same request three times; wide events in a columnar store avoid the duplication.
- eBPF gives full L4/L7 visibility with no code changes or sidecars.
- The pillar choice is a data governance decision disguised as infrastructure.
- AI workloads generate 10 to 100 times more telemetry than traditional apps, making observability a FinOps problem with per-inference unit economics.

## Related

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the model Honeycomb argues against
- [Alert fatigue](/concepts/alert-fatigue.md) — the symptom of noisy monitoring
- [OpenTelemetry](/entities/opentelemetry.md) — the instrumentation standard in play
- [Datadog](/entities/datadog.md) — a contrasting observability vendor
- [The 2019 Baseline: What the Books Said vs. What Your Team Actually Ran](/sources/observability-arc-01-the-2019-baseline.md) — primary source
