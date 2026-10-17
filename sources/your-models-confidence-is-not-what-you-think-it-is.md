---
title: "Your Model's Confidence Is Not What You Think It Is"
type: "Source Summary"
description: "Argues RLHF makes models overconfident and decouples expressed confidence from accuracy, so confidence needs its own evaluation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/your-models-confidence-is-not-what-you-think-it-is/your-models-confidence-is-not-what-you-think-it-is.md"
---

# Your Model's Confidence Is Not What You Think It Is — Summary

**Original source**: `references/devlinliles.com/your-models-confidence-is-not-what-you-think-it-is/your-models-confidence-is-not-what-you-think-it-is.md`

## Summary

The post defines [calibration](/concepts/calibration.md) — a model is well-calibrated when its stated confidence matches its accuracy — and argues most production systems fail it. Base models track near-perfect calibration, but [RLHF](/concepts/rlhf.md) skews them toward overconfidence because human raters prefer confident-sounding answers, rewarding the register of confidence independent of correctness. The author calls for treating expressed confidence as a signal requiring its own evaluation, not ground truth, and for triggering [human-in-the-loop](/concepts/human-in-the-loop.md) checkpoints by risk rather than by model confidence.

## Key Claims

- A base model before instruction tuning tracks fairly close to perfect calibration; RLHF then decouples confidence from accuracy toward overconfidence.
- 2025 research found that in [GPT-4o](/entities/gpt-4o.md), 15% of responses with strong epistemic markers ("certainly," "definitely") were incorrect.
- Confidently wrong output creates legal exposure, medical liability, and wasted engineering time when failures are not immediately obvious.
- Temperature scaling — especially adaptive, per-input scaling — improves calibration but does not fully solve it; calibration varies by domain and question type.
- Expected Calibration Error belongs alongside accuracy in eval suites, and review gates should be triggered by output type and risk level, not model confidence.

## Relevance

Informs [epistemic humility](/concepts/epistemic-humility.md), [RLHF](/concepts/rlhf.md), and confidence-based design choices such as [confidence thresholds](/concepts/confidence-thresholds.md) and [human-in-the-loop](/concepts/human-in-the-loop.md) review.

## Quality

Practitioner blog post by Devlin Liles. Clearly argued and grounded in a named 2025 finding, but cites no source link and leans on qualitative risk claims.

## Entities Mentioned

- [GPT-4o](/entities/gpt-4o.md) — the model in the cited 2025 overconfidence finding

## Concepts Covered

- [Epistemic Humility](/concepts/epistemic-humility.md) — the philosophical frame for appropriate confidence
- [RLHF](/concepts/rlhf.md) — the training phase that skews calibration
- [Calibration](/concepts/calibration.md) — the measurable property the post centers on
- [human-in-the-loop](/concepts/human-in-the-loop.md) — risk-triggered checkpoints instead of confidence-triggered

## Related Sources

- [Agentic Systems That Don't Improve Are Just Expensive Software](/sources/agentic-systems-that-dont-improve-are-just-expensive-software.md)
- [Sycophancy Is a Gricean Failure. It Was Baked In by the Training Signal.](/sources/sycophancy-is-a-gricean-failure-it-was-baked-in-by-the-training-signal.md)
