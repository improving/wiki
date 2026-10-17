---
title: "Golden Paths to Observability: What Platform Engineering Actually Delivers (and What It Doesn't)"
type: "Source Summary"
description: "Platform engineering moved observability into the golden path, but DORA data shows IDPs lift individual productivity while lowering throughput and stability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-05-platform-engineering-idp/observability-arc-05-platform-engineering-idp.md"
---

# Golden Paths to Observability: What Platform Engineering Actually Delivers (and What It Doesn't) — Summary

**Original source**: `references/devlinliles.com/observability-arc-05-platform-engineering-idp/observability-arc-05-platform-engineering-idp.md`

## Summary

Between 2022 and 2025 observability stopped being a tool problem and became a platform problem, with the [CNCF](/entities/cncf.md) framing automatic instrumentation and standard dashboards as core golden-path capabilities. [Spotify](/entities/spotify.md)'s Backstage became the vehicle, and [Gartner](/entities/gartner.md) projected 80% of large engineering organizations would run platform teams by 2026. But [DORA](/entities/dora.md)'s 2024 data shows the same IDPs that lifted individual productivity 8% also dropped change throughput 8% and stability 14% — a coordination cost invisible in the metrics platform teams report about themselves.

## Key Claims

- DORA's ~39,000-respondent 2024 study found IDP adoption raised individual productivity 8% and team performance 10% while dropping change throughput 8% and stability 14%.
- Backstage reached CNCF incubating status in March 2022, with 3,400+ adopting organizations, 1,600+ contributors, and 230+ plugins; Spotify reports ~96% of R&D using it.
- At an insurance carrier with 150+ services, an Improving Backstage build cut new-service onboarding from 2–3 days to under an hour.
- A 25% rise in AI adoption correlated with a 1.5% throughput drop and a 7.2% stability drop.
- Platform teams measuring only tool coverage and adoption optimize for what they provide, not what they deliver.

## Relevance

Informs [DORA](/entities/dora.md) measurement debates and the observability arc's theme that standardized telemetry becomes the substrate for platform capability.

## Quality

Practitioner blog post by Devlin Liles. Well-sourced with dated DORA, Gartner, and CNCF figures and a concrete client case; the causality of the throughput/stability drops is correlation as reported.

## Entities Mentioned

- [CNCF](/entities/cncf.md) — published the Platforms white paper and maturity model
- [DORA](/entities/dora.md) — source of the productivity/stability findings
- [Spotify](/entities/spotify.md) — built and open-sourced Backstage
- [Gartner](/entities/gartner.md) — projected platform-team adoption
- [OpenTelemetry](/entities/opentelemetry.md) — SDKs wired into golden-path templates

## Concepts Covered

- None.

## Related Sources

- [The 2019 Baseline: What the Books Said vs. What Your Team Actually Ran](/sources/observability-arc-01-the-2019-baseline.md)
- [Metrics, Logs, Traces — and the War That Standardization Won](/sources/observability-arc-02-opentelemetry-standardization.md)
