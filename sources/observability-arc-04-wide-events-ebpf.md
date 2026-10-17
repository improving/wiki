---
title: "Wide Events, eBPF, and Why the Three Pillars Are a Tax You're Still Paying"
type: "Source Summary"
description: "Argues wide events, columnar storage, and eBPF can replace the three-pillar stack with a unified CNCF-native Datadog alternative."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-04-wide-events-ebpf/observability-arc-04-wide-events-ebpf.md"
---

# Wide Events, eBPF, and Why the Three Pillars Are a Tax You're Still Paying — Summary

**Original source**: `references/devlinliles.com/observability-arc-04-wide-events-ebpf/observability-arc-04-wide-events-ebpf.md`

## Summary

Most Kubernetes shops run three separate systems — Prometheus, a log indexer, and a trace backend — and pay to store the same request three times, a data architecture accident the author calls the [three pillars of observability](/concepts/three-pillars-of-observability.md). Two responses emerged around 2021: [Charity Majors](/entities/charity-majors.md) and [Honeycomb](/entities/honeycomb.md) argue for a single arbitrarily-wide event per request in a columnar store, while eBPF instruments the kernel at L4/L7 with no code changes. Together they make a disciplined [OpenTelemetry](/entities/opentelemetry.md) and [Grafana Labs](/entities/grafana-labs.md) LGTM stack a credible alternative to [Datadog](/entities/datadog.md).

## Key Claims

- A columnar wide-event store avoids pre-aggregation, sampling, and the cardinality ceiling that makes high-cardinality labels a footgun in Prometheus.
- eBPF runs sandboxed kernel programs attached to syscall, cgroup, socket, and traffic-control hooks, giving full topology and latency visibility without per-service instrumentation.
- Cilium shipped Hubble in November 2019; [CNCF](/entities/cncf.md) accepted Cilium as incubating in October 2021, and it graduated in 2023.
- The CNCF-native stack (OTel Collector, Prometheus Operator, Grafana LGTM, [Kubernetes](/entities/kubernetes.md) Cilium) is 5–7 components and can take three months to tune, but usually costs less than Datadog above roughly 200 nodes.
- Wide events demand schema and naming discipline — a data governance decision disguised as an infrastructure one.

## Relevance

Informs [three pillars of observability](/concepts/three-pillars-of-observability.md) and the observability arc's argument that platform capability, not per-team tool choice, closes the gap.

## Quality

Practitioner blog post by Devlin Liles. Strong on architecture tradeoffs and dated project milestones; cost figures are illustrative and the Datadog comparison is a reasoned claim, not a benchmark.

## Entities Mentioned

- [Charity Majors](/entities/charity-majors.md) — coined "Observability 1.0/2.0"; leads the wide-event argument
- [Honeycomb](/entities/honeycomb.md) — vendor behind the wide-event storage model
- [Datadog](/entities/datadog.md) — the commercial alternative being weighed
- [OpenTelemetry](/entities/opentelemetry.md) — collection and routing layer
- [Grafana Labs](/entities/grafana-labs.md) — LGTM storage and visualization stack
- [CNCF](/entities/cncf.md) — hosts Cilium, Pixie, and the profiling signal
- [Kubernetes](/entities/kubernetes.md) — target environment for eBPF instrumentation

## Concepts Covered

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the model being critiqued as a cost multiplier

## Related Sources

- [The Cost of Knowing: Observability in the Age of AI Agents](/sources/observability-arc-08-finops-agentic.md)
