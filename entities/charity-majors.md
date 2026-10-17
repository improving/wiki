---
title: "Charity Majors"
type: "Entity"
description: "Engineer and Honeycomb co-founder cited on wide events, eBPF, and the limits of AIOps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, engineer, aiops]
sources:
  - "/sources/observability-arc-04-wide-events-ebpf.md"
  - "/sources/observability-arc-06-aiops-rca.md"
---

# Charity Majors

Charity Majors is an engineer and [Honeycomb](/entities/honeycomb.md) co-founder invoked in this corpus as the voice behind the argument that observability should be built from wide, high-cardinality events rather than the traditional [three pillars](/concepts/three-pillars-of-observability.md).

## Work

- One post argues three-pillar stacks store the same HTTP request three times, a structural tax, and that wide events in a columnar store remove the cardinality ceiling Prometheus imposes.
- It presents eBPF as giving full L4/L7 visibility with no code changes or sidecars, and frames the pillar choice as a data governance decision disguised as infrastructure.
- The companion post traces the humbling arc of AIOps: pre-LLM systems underdelivered because they leaned on clean topology and telemetry, and LLMs add hypothesis generation, not autonomous action.

## Key Claims

- The pillar choice is a data governance decision disguised as infrastructure.
- 90% alert noise reduction is a marketing claim, not an independent benchmark.
- LLMs generate ranked natural-language hypotheses over high-cardinality telemetry.
- Output quality is bounded by telemetry quality, so instrumentation comes first.

## Related

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the model she argues against
- [alert fatigue](/concepts/alert-fatigue.md) — the failure mode AIOps claims to solve
- [anomaly detection](/concepts/anomaly-detection.md) — the detection layer AIOps builds on
- [Honeycomb](/entities/honeycomb.md) — the vendor she co-founded
- [OpenTelemetry](/entities/opentelemetry.md) — the instrumentation standard in the same space
- [Wide Events, eBPF, and Why the Three Pillars Are a Tax](/sources/observability-arc-04-wide-events-ebpf.md) — primary source
- [From Alert Storms to Answers: The Long, Humbling Arc of AIOps](/sources/observability-arc-06-aiops-rca.md) — companion source
