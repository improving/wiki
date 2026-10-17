---
title: "CNCF"
type: "Entity"
description: "Cloud Native Computing Foundation, the neutral home for projects like Kubernetes and OpenTelemetry that shaped observability and platform engineering."
created: '2026-10-17'
updated: '2026-10-17'
tags: [organization, standards, cloud-native, observability]
sources:
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-02-opentelemetry-standardization.md"
  - "/sources/observability-arc-05-platform-engineering-idp.md"
---

# CNCF

The Cloud Native Computing Foundation is the vendor-neutral foundation behind many cloud-native projects, and the governance context for much of this corpus's observability and platform-engineering discussion. Its standardization work — especially around [OpenTelemetry](/entities/opentelemetry.md) — is credited with ending vendor capture of instrumentation.

## Overview

- Tool availability led actual adoption by three to five years; the ecosystem shipped observability tooling long before most teams ran it.
- OpenTracing and OpenCensus merged into [OpenTelemetry](/entities/opentelemetry.md) on May 7, 2019 under neutral governance.
- The Collector made "instrument once, export anywhere" concrete, decoupling the instrumentation market from the analytics market.
- Standardized telemetry pipelines are described as the durable payoff of platform engineering, even when internal developer platforms lift individual productivity 8% while dropping stability 14%.

## Related

- [OpenTelemetry](/entities/opentelemetry.md) — its flagship observability project
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — metrics, logs, and traces
- [DORA](/entities/dora.md) — the research program measuring delivery outcomes
- [encoded standards](/concepts/encoded-standards.md) — the value of neutral specifications
- [Metrics, Logs, Traces — and the War That Standardization Won](/sources/observability-arc-02-opentelemetry-standardization.md) — primary source
