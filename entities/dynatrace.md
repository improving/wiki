---
title: "Dynatrace"
type: "Entity"
description: "APM vendor used in the corpus to illustrate host-based pricing pressure and the limits of pre-LLM AIOps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, apm, vendor]
sources:
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/observability-arc-06-aiops-rca.md"
---

# Dynatrace

An application performance monitoring (APM) vendor that the corpus uses to describe the observability cost problem and the humbling arc of AIOps. It is grouped with [Datadog](/entities/datadog.md) in a market projected to reach $14.2 billion by 2028.

## Overview

Host-based APM pricing punishes Kubernetes autoscaling, and metric cardinality grows combinatorially with label and pod combinations, so the bill scales with topology rather than traffic. The AIOps post argues pre-LLM tools underdelivered because they leaned on clean topology and telemetry that architecture change invalidated; LLMs add hypothesis generation, not autonomous action.

## Key Claims

- The observability market will reach $14.2 billion by 2028.
- Host-based billing punishes Kubernetes autoscaling; edge collector pipelines with tail-based sampling are the cost lever.
- Pre-LLM AIOps broke when architecture changed because models learned from history.
- 90% alert-noise reduction is a marketing claim, not an independent benchmark; output quality is bounded by telemetry quality.

## Related

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the stack its pricing exposes
- [alert fatigue](/concepts/alert-fatigue.md) — the problem AIOps targets
- [anomaly detection](/concepts/anomaly-detection.md) — the pre-LLM AIOps capability
- [Datadog](/entities/datadog.md) — its closest competitor in the corpus
- [From Alert Storms to Answers](/sources/observability-arc-06-aiops-rca.md) — source
