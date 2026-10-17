---
title: "Datadog, Dynatrace, and the Bill That Ate Your Engineering Budget"
type: "Source Summary"
description: "The observability boom produced a cost crisis: billing scales with topology, not traffic, and the bill is really an architecture signal."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-03-apm-boom-observability-tax/observability-arc-03-apm-boom-observability-tax.md"
---

# Datadog, Dynatrace, and the Bill That Ate Your Engineering Budget — Summary

**Original source**: `references/devlinliles.com/observability-arc-03-apm-boom-observability-tax/observability-arc-03-apm-boom-observability-tax.md`

## Summary

The third observability post turns from tooling to the bill. [Gartner](/entities/gartner.md) projects the market at $14.2 billion by 2028, and [Datadog](/entities/datadog.md) alone reported $3.43 billion in FY2025 revenue, up 27.68%. The argument is that multi-dimensional pricing meets elastic architecture badly: [Kubernetes](/entities/kubernetes.md) autoscaling multiplies nodes, sidecars, and label cardinality, so the observability bill scales with topology while the compute bill scales with traffic. The author reads an oversized bill as an architecture failure, not a procurement problem.

## Key Claims

- Datadog pricing (Q2 2026) is multi-dimensional: roughly $15/host for infrastructure, $31 for APM, $0.10/GB log ingest plus $1.70 per million indexed events, and about $0.05 per custom metric per month.
- Grafana Labs' 2023 survey found 52% of organizations use six or more observability tools and 11% use sixteen or more; Datadog research puts teams at twelve or more.
- Scaling a cluster from ten to fifty nodes multiplies host-based charges, sidecar log streams, and metric cardinality faster than the workload grows.
- The ingestion-versus-indexing split means teams keep logs they cannot query — "a filing cabinet with a lock on it."
- The levers are not exotic: an edge [OpenTelemetry](/entities/opentelemetry.md) Collector pipeline with tail-based sampling, log exclusion filters, and instrumentation-time cardinality governance.

## Relevance

Extends the observability arc into cost: it argues multi-dimensional pricing meeting Kubernetes elasticity makes [three pillars of observability](/concepts/three-pillars-of-observability.md) tooling an architecture and budget problem, not merely a technical one.

## Quality

Practitioner blog post by Devlin Liles. Concrete pricing and revenue figures with named sources; the pricing is a snapshot and the architecture-signal framing is the author's opinion.

## Entities Mentioned

- [Datadog](/entities/datadog.md) — central example of multi-dimensional pricing and growth
- [Dynatrace](/entities/dynatrace.md) — commercial platform bringing AI-assisted anomaly detection
- [Gartner](/entities/gartner.md) — source of the $14.2B market projection
- [Kubernetes](/entities/kubernetes.md) — elastic runtime that multiplies observability cost
- [Grafana Labs](/entities/grafana-labs.md) — source of the tool-sprawl survey data
- [Charity Majors](/entities/charity-majors.md) — argues good teams spend most time governing cardinality

## Concepts Covered

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the model whose adoption created the cost crisis

## Related Sources

- [Closing the Loop: The Graduated Case for Self-Healing Systems](/sources/observability-arc-07-self-healing-remediation.md)
