---
title: "three pillars of observability"
type: "Concept"
description: "The metrics/logs/traces split for observability, and the storage and cardinality tax its separation imposes."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, telemetry, architecture]
sources:
  - "/sources/observability-arc-02-opentelemetry-standardization.md"
  - "/sources/observability-arc-04-wide-events-ebpf.md"
---

# three pillars of observability

The three pillars — metrics, logs, and traces — are the conventional decomposition of observability data. This corpus traces how standardization made the pillars portable, then argues the separation itself has become a structural tax: the same request is stored three times, and newer approaches replace the pillars with wide events in a columnar store.

## Key Claims

- Running four separate APM agents in production was vendor capture, not differentiation.
- OpenTracing and OpenCensus merged into OpenTelemetry on May 7, 2019.
- The OpenTelemetry Collector makes "instrument once, export anywhere" concrete, decoupling the instrumentation market from the analytics market.
- Three-pillar stacks store the same HTTP request three times — a structural tax.
- Wide events in a columnar store remove the cardinality ceiling Prometheus imposes.
- eBPF gives full L4/L7 visibility with no code changes or sidecars.
- The pillar choice is a data governance decision disguised as infrastructure.

## Related

- [OpenTelemetry](/entities/opentelemetry.md) — the standard that made instrumentation portable across pillars
- [alert fatigue](/concepts/alert-fatigue.md) — the operational cost of pillar-shaped signal noise
- [anomaly detection](/concepts/anomaly-detection.md) — analysis that benefits from unified wide events
- [Data Governance](/concepts/data-governance.md) — the real decision behind choosing pillars
- [Metrics, Logs, Traces — and the War That Standardization Won](/sources/observability-arc-02-opentelemetry-standardization.md) — primary source
- [Wide Events, eBPF, and Why the Three Pillars Are a Tax You're Still Paying](/sources/observability-arc-04-wide-events-ebpf.md) — primary source
