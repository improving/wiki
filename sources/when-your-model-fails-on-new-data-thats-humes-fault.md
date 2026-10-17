---
title: "When Your Model Fails on New Data, That's Hume's Fault"
type: "Source Summary"
description: "Production AI failures are the problem of induction at scale, so teams should monitor distribution shift and define out-of-distribution responses."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/when-your-model-fails-on-new-data-thats-humes-fault/when-your-model-fails-on-new-data-thats-humes-fault.md"
---

# When Your Model Fails on New Data, That's Hume's Fault — Summary

**Original source**: `references/devlinliles.com/when-your-model-fails-on-new-data-thats-humes-fault/when-your-model-fails-on-new-data-thats-humes-fault.md`

## Summary

The post reframes the common explanation that "the model saw different data" as a structural, philosophical problem rather than an operational one. Machine learning is industrial-scale induction resting on the i.i.d. assumption, which rarely holds in deployment; David Hume's 1748 problem of induction shows the leap can't be closed by more data. The author argues the responsible response is to measure [distribution shift](/concepts/distribution-shift.md) exposure, monitor it, and define what happens when out-of-distribution inputs appear.

## Key Claims

- A model strong on its held-out test set can lose 20 to 50 percentage points of accuracy under moderate-to-large distribution shift, with abrupt degradation under severe shifts.
- Failure is invisible until measured: models generate tokens with the same surface confidence whether in- or out-of-distribution, and the [calibration](/concepts/calibration.md) problem hides the gap.
- Evaluation sets should probe distribution boundaries, not just resample the training distribution.
- [Model drift detection](/concepts/model-drift-detection.md) is not optional — track production input statistics and alert on divergence.
- Define a response to out-of-distribution detection: who reviews it, and when it triggers retraining versus a human fallback.
- Vendor benchmark numbers show in-distribution performance and say little about your tasks; the gap is Hume's gap made concrete.

## Relevance

Grounds [distribution shift](/concepts/distribution-shift.md) and evaluation practice in the problem of induction, informing eval design and production monitoring.

## Quality

Practitioner blog post by Devlin Liles. Philosophically framed with concrete figures and practical prescriptions; the 20–50 point range is cited generically rather than to a specific study.

## Entities Mentioned

- None.

## Concepts Covered

- [Distribution shift](/concepts/distribution-shift.md) — the central technical phenomenon
- [Calibration](/concepts/calibration.md) — why confident output hides out-of-distribution failure
- [Model Drift Detection](/concepts/model-drift-detection.md) — the monitoring discipline the post recommends
