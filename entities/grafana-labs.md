---
title: "Grafana Labs"
type: "Entity"
description: "Observability vendor behind the LGTM stack, cited in this corpus's APM-cost and AIOps arcs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, vendor, telemetry]
sources:
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/observability-arc-06-aiops-rca.md"
---

# Grafana Labs

Grafana Labs is an observability vendor known for the Grafana dashboards and the LGTM stack (Loki, Grafana, Tempo, Mimir). In this corpus it appears as an alternative to host-based APM pricing and as part of the telemetry foundation that AIOps depends on.

## Overview

One post traces the observability tax: the market will reach $14.2 billion by 2028, and Datadog's host-based billing punishes Kubernetes autoscaling because metric cardinality grows combinatorially with label and pod combinations. Edge Collector pipelines with tail-based sampling and filtering are the cost levers, and self-hosted or usage-flexible stacks like Grafana's are the implied counter-position.

The other post revisits AIOps. Pre-LLM AIOps broke when architecture changed because its models learned from history, and the "90% alert noise reduction" figure is a marketing claim, not an independent benchmark. LLMs generate ranked natural-language hypotheses over high-cardinality telemetry, but output quality is bounded by telemetry quality — so instrumentation comes first.

## Key Claims

- The observability market will reach $14.2 billion by 2028.
- Metric cardinality grows combinatorially with label and pod combinations, making it the real cost driver.
- Edge Collector pipelines with tail-based sampling and filtering are the cost levers.
- Pre-LLM AIOps broke when architecture changed because models learned from history.
- LLM output quality is bounded by telemetry quality, so instrumentation comes first.

## Related

- [Datadog](/entities/datadog.md) — the pricing model it counters
- [Dynatrace](/entities/dynatrace.md) — the other APM incumbent
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the stack it implements
- [anomaly detection](/concepts/anomaly-detection.md) — the AIOps capability it hosts
- [Datadog, Dynatrace, and the Bill That Ate Your Engineering Budget](/sources/observability-arc-03-apm-boom-observability-tax.md) — primary source
