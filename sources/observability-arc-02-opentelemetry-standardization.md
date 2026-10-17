---
title: "Metrics, Logs, Traces — and the War That Standardization Won"
type: "Source Summary"
description: "OpenTelemetry's merger ended vendor capture of instrumentation, decoupling the instrumentation market from the analytics market."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-02-opentelemetry-standardization/observability-arc-02-opentelemetry-standardization.md"
---

# Metrics, Logs, Traces — and the War That Standardization Won — Summary

**Original source**: `references/devlinliles.com/observability-arc-02-opentelemetry-standardization/observability-arc-02-opentelemetry-standardization.md`

## Summary

The second observability post traces the [three pillars of observability](/concepts/three-pillars-of-observability.md) — metrics, logs, traces — from Peter Bourgon's 2017 vocabulary through the vendor capture that followed, when a complex team could run four APM agents that never talked to each other. It marks the May 7, 2019 [CNCF](/entities/cncf.md) merger of OpenTracing and OpenCensus into [OpenTelemetry](/entities/opentelemetry.md) as the turning point. The argument is that OTel is a business decision dressed as a technical one: it turns instrumentation into a commodity and restores leverage over vendors.

## Key Claims

- Each pillar does something the others cannot do cheaply: traces locate the break, metrics give affordable scale, logs preserve exact detail.
- Before OTel, the agent was the moat; winning instrumentation meant winning the account.
- OTel has four parts — SDKs/APIs, the Collector pipeline, the OTLP wire protocol, and semantic conventions — summarized as "instrument once, export anywhere."
- Adoption followed a standards curve: 4% in production in 2020, 20% by 2022, 41% in 2025, graduating from CNCF on May 21, 2026 with 12,000+ contributors.
- Portability lets teams negotiate from a position of optionality; those not on OTel accumulate invisible migration debt.

## Relevance

Follows the arc from the 2019 baseline post, showing how [OpenTelemetry](/entities/opentelemetry.md) decoupled instrumentation from [Datadog](/entities/datadog.md)-style backends and reshaped the [three pillars of observability](/concepts/three-pillars-of-observability.md) market.

## Quality

Practitioner blog post by Devlin Liles. Well-sourced with CNCF and Grafana Labs figures; some chart images are placeholders and the business framing is the author's interpretation.

## Entities Mentioned

- [OpenTelemetry](/entities/opentelemetry.md) — the standard at the center of the post
- [CNCF](/entities/cncf.md) — hosted the merger and later graduation
- [Datadog](/entities/datadog.md) — example backend whose lock-in OTel breaks

## Concepts Covered

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the model that gave the market its vocabulary

## Related Sources

- [Golden Paths to Observability: What Platform Engineering Actually Delivers (and What It Doesn't)](/sources/observability-arc-05-platform-engineering-idp.md)
- [The Cost of Knowing: Observability in the Age of AI Agents](/sources/observability-arc-08-finops-agentic.md)
