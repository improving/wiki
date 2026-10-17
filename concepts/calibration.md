---
title: "Calibration"
type: "Concept"
description: "Whether a model's expressed confidence matches its actual accuracy, and the training dynamics that systematically distort it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, reliability, training]
sources:
  - "/sources/we-trained-ai-to-be-engaging-not-helpful.md"
  - "/sources/when-your-model-fails-on-new-data-thats-humes-fault.md"
---

# Calibration

Calibration is the alignment between a model's stated confidence and its real probability of being correct. Across this corpus it is treated as a reliability property that training and distribution shift both break: models can be confidently wrong, and the failure stays invisible until someone measures it.

## Key Claims

- Preference ratings in RLHF capture annotator engagement, not whether a response actually helps.
- Reward-model overoptimization drifts models away from helpfulness, exactly as Goodhart's Law predicts.
- Sycophancy, overconfidence, and verbosity are signatures of engagement-optimized training — overconfidence being a calibration failure.
- Explicit evaluation criteria and system prompts can partially counter RLHF's engagement bias.
- Machine learning is industrial-scale induction resting on the i.i.d. assumption.
- Models can lose 20 to 50 points of accuracy under moderate distribution shift.
- Failure is invisible until measured, because confidence is uncalibrated off-distribution.
- Evaluation sets must probe distribution boundaries, paired with drift monitoring and a defined response.

## Related

- [Confidence Calibration](/concepts/confidence-calibration.md) — the measurement side of this property
- [Distribution shift](/concepts/distribution-shift.md) — the condition that breaks calibration
- [Sycophancy](/concepts/sycophancy.md) — an overconfidence-adjacent failure of engagement-optimized training
- [RLHF](/concepts/rlhf.md) — the training method whose preference signal distorts calibration
- [Benchmark Saturation](/concepts/benchmark-saturation.md) — why confidence cannot be inferred from saturated scores
- [We Trained AI to Be Engaging, Not Helpful](/sources/we-trained-ai-to-be-engaging-not-helpful.md) — primary source
- [When Your Model Fails on New Data, That's Hume's Fault](/sources/when-your-model-fails-on-new-data-thats-humes-fault.md) — primary source
