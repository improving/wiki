---
title: "anomaly detection"
type: "Concept"
description: "Finding unusual behavior in telemetry or delivery signals, increasingly augmented by LLMs that rank hypotheses rather than act autonomously."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, aiops, monitoring]
sources:
  - "/sources/every-stage-of-software-delivery-has-an-ai-dimension.md"
  - "/sources/observability-arc-06-aiops-rca.md"
---

# anomaly detection

Anomaly detection is the practice of surfacing behavior that departs from expected patterns, whether in production telemetry or in the signals of a software delivery pipeline. In this corpus it is framed as one AI leverage point among many, and one whose output is only as trustworthy as the data beneath it.

## Key Claims

- Every stage of the Plan-to-Monitor loop has a distinct AI leverage point, and limiting AI to code completion leaves most delivery leverage untouched.
- Defect prevention compounds: catching issues earlier costs less, which makes detection at the earliest stage disproportionately valuable.
- Pre-LLM AIOps underdelivered because it leaned on clean topology and telemetry; it broke whenever architecture changed, since the models learned from history.
- LLMs add hypothesis generation, not autonomous action — they produce ranked natural-language hypotheses over high-cardinality telemetry.
- The often-quoted 90 percent alert-noise reduction is a marketing claim, not an independent benchmark.
- Output quality is bounded by telemetry quality, so instrumentation comes before smarter detection.

## Related

- [alert fatigue](/concepts/alert-fatigue.md) — the failure mode noisy detection produces
- [Model Drift Detection](/concepts/model-drift-detection.md) — a specialized case of detecting behavioral change
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the telemetry that bounds detection quality
- [AI Governance](/concepts/ai-governance.md) — where detection feeds monitoring and enforcement layers
- [Every Stage of Software Delivery Has an AI Dimension](/sources/every-stage-of-software-delivery-has-an-ai-dimension.md) — primary source
- [From Alert Storms to Answers: The Long, Humbling Arc of AIOps](/sources/observability-arc-06-aiops-rca.md) — primary source
