---
title: "metrics logs traces"
type: "Concept"
description: "The three telemetry pillars, and the storage and cardinality tax of keeping them in separate systems."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, platform, cloud-cost]
sources:
  - "/sources/observability-arc-02-opentelemetry-standardization.md"
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
  - "/sources/observability-arc-04-wide-events-ebpf.md"
---

# metrics logs traces

Metrics, logs, and traces are the three telemetry pillars that gave the observability market its vocabulary, each doing something the others cannot do cheaply. The pillar model is also a data-architecture accident: most Kubernetes shops run three separate systems and pay to store the same request three times. Standardization through [OpenTelemetry](/entities/opentelemetry.md) decoupled instrumentation from analytics, but the storage and cardinality tax of the split remains, and it is what makes observability a budget conversation as much as a technical one.

## Key Claims

- The pillar vocabulary traces to Peter Bourgon's 2017 writing; each pillar is irreducible — traces locate the break, metrics give affordable scale, logs preserve exact detail.
- Before [OpenTelemetry](/entities/opentelemetry.md), the agent was the moat and a complex team could run four APM agents that never talked to each other.
- The May 7, 2019 [CNCF](/entities/cncf.md) merger of OpenTracing and OpenCensus made instrumentation a commodity: OTel reached 4% production adoption in 2020, 20% by 2022, 41% in 2025, and graduated from CNCF on May 21, 2026 with 12,000+ contributors.
- The cost scales with topology, not traffic: [Datadog](/entities/datadog.md) pricing (Q2 2026) runs roughly $15/host for infrastructure, $31 for APM, $0.10/GB log ingest plus $1.70 per million indexed events, and ~$0.05 per custom metric per month.
- Scaling a cluster from ten to fifty nodes multiplies host charges, sidecar log streams, and metric cardinality faster than the workload grows; an oversized bill reads as an architecture signal.
- The open-source LGTM stack (Prometheus, Grafana, Loki, Tempo, OTel) indexes only log metadata rather than full content, and Loki helped Paytm Insider save 75% of logging and monitoring costs.
- The alternative to the split is a wide event per request in a columnar store, or eBPF instrumentation at the kernel's L4/L7 hooks with no code changes.

## Related

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the split and its storage tax
- [observability](/concepts/observability.md) — the practice the pillars serve
- [distributed tracing](/concepts/distributed-tracing.md) — the pillar teams neglect
- [cloud cost management](/concepts/cloud-cost-management.md) — where the cardinality tax lands
- [OpenTelemetry](/entities/opentelemetry.md) — the standard that commoditized instrumentation
- [Grafana Loki](/entities/grafana-loki.md) — metadata-only log aggregation
