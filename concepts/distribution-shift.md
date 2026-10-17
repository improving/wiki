---
title: "Distribution shift"
type: "Concept"
description: "When production inputs diverge from training data, degrading model accuracy in ways confidence cannot reveal."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, reliability, ml]
sources:
  - "/sources/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md"
  - "/sources/the-chinese-room-is-running-in-production.md"
  - "/sources/when-your-model-fails-on-new-data-thats-humes-fault.md"
---

# Distribution shift

Distribution shift is the divergence between the data a model was trained or evaluated on and the data it meets in production. Across this corpus it is the central reason benchmark scores mislead: models are industrial-scale induction resting on an i.i.d. assumption, and reliability on novel inputs can fall far below behavioral benchmark results.

## Key Claims

- Machine learning is industrial-scale induction resting on the i.i.d. assumption; out-of-distribution failure is Hume's problem of induction at scale.
- Models can lose 20–50 points of accuracy under moderate distribution shift, with drops up to 54% reported with no spec change.
- Failure is invisible until measured, because confidence is uncalibrated off-distribution.
- Behavioral benchmark scores and causal reliability on novel inputs are diverging; distribution-shifted evaluations expose the gap.
- Evaluation sets must probe distribution boundaries, paired with drift monitoring and a defined response.
- Graceful incompetence, calibration, and abstention are distinct architectural goals.

## Related

- [Calibration](/concepts/calibration.md) — why off-distribution confidence cannot be trusted
- [Model Drift Detection](/concepts/model-drift-detection.md) — monitoring the boundary over time
- [Benchmark Validity](/concepts/benchmark-validity.md) — why standard accuracy tests hide the gap
- [Epistemic Humility](/concepts/epistemic-humility.md) — abstention and graceful incompetence
- [evaluation harness](/concepts/evaluation-harness.md) — where boundary evaluation is operationalized
- [When Your Model Fails on New Data, That's Hume's Fault](/sources/when-your-model-fails-on-new-data-thats-humes-fault.md) — primary source
