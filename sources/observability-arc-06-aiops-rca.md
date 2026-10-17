---
title: "From Alert Storms to Answers: The Long, Humbling Arc of AIOps"
type: "Source Summary"
description: "AIOps overpromised root-cause analysis; LLMs added narrative hypothesis generation, but telemetry quality still bounds every outcome."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-06-aiops-rca/observability-arc-06-aiops-rca.md"
---

# From Alert Storms to Answers: The Long, Humbling Arc of AIOps — Summary

**Original source**: `references/devlinliles.com/observability-arc-06-aiops-rca/observability-arc-06-aiops-rca.md`

## Summary

[Gartner](/entities/gartner.md) coined AIOps in 2016 around five layers, but the market heard a two-line pitch about eliminating alert storms and automating root cause — and got less than promised. Pre-LLM tools relied on static rules and supervised models that broke whenever architecture changed, built atop CMDBs most organizations never had. LLMs added something qualitatively new: natural-language hypothesis generation and narrative explanation, as in [Honeycomb](/entities/honeycomb.md)'s Query Assistant. But output quality is bounded by telemetry quality, so [alert fatigue](/concepts/alert-fatigue.md) and slow diagnosis remain foundation problems before they are analysis problems.

## Key Claims

- Gartner estimated the 2019 AIOps market at $300–500M and projected ~$3.4B by 2025, with observability heading toward $14.2B by 2028.
- The "90% alert noise reduction" claim is marketing selected from best-case engagements, not an independent benchmark.
- Pre-LLM tools were good at exactly one of the five layers — event correlation — while sales targeted root-cause analysis and remediation.
- One 200-person engineering org cut page volume ~30% with no MTTR improvement until the underlying telemetry was fixed.
- [Anomaly detection](/concepts/anomaly-detection.md) is maturing, root-cause analysis is emerging (hypotheses, not truth), and autonomous remediation is early-stage; a Grafana Labs 2024 survey found AI in observability "largely aspirational."

## Relevance

Informs [alert fatigue](/concepts/alert-fatigue.md) and [anomaly detection](/concepts/anomaly-detection.md), and sets up the arc's self-healing and FinOps follow-ons.

## Quality

Practitioner blog post by Devlin Liles. Strong on the gap between vendor claims and capability; the 30% page-reduction case is single-case evidence and the era charts are illustrative.

## Entities Mentioned

- [Gartner](/entities/gartner.md) — coined AIOps and produced the market figures
- [Honeycomb](/entities/honeycomb.md) — Query Assistant and BubbleUp, the LLM-era marker
- [Dynatrace](/entities/dynatrace.md) — Davis AI anomaly and root-cause tooling
- [Datadog](/entities/datadog.md) — anomaly detection in the AIOps category
- [Charity Majors](/entities/charity-majors.md) — quoted on observability preceding AI observability
- [Grafana Labs](/entities/grafana-labs.md) — 2024 Observability Survey on AI aspirations

## Concepts Covered

- [anomaly detection](/concepts/anomaly-detection.md) — maturing first-tier triage capability
- [alert fatigue](/concepts/alert-fatigue.md) — the noise problem AIOps exists to reduce
