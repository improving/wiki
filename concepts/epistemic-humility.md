---
title: "Epistemic Humility"
type: "Concept"
description: "Treating model capability and expressed confidence as uncertain, bounded by scale thresholds and training artifacts rather than stable truth."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai-capability, calibration, risk]
sources:
  - "/sources/the-capabilities-nobody-predicted.md"
  - "/sources/your-models-confidence-is-not-what-you-think-it-is.md"
---

# Epistemic Humility

Epistemic humility is the stance that neither a model's capabilities nor its stated confidence can be taken at face value. Across this corpus it recurs as a design principle: pilots and evals measure only what current models, under current prompting, happen to reveal.

## Key Claims

- Emergent abilities appeared as phase transitions at critical model-scale thresholds, so smaller-model pilots are a lower bound rather than a forecast.
- One account (Schaeffer et al.) argues apparent emergence is often an artifact of discontinuous metrics, making even the phenomenon itself contested.
- A non-ergodic framing warns that aggregate capability can mask per-use-case variability, so averages hide the cases that fail.
- [Calibration](/concepts/calibration.md) requires stated confidence to match actual accuracy; [RLHF](/concepts/rlhf.md) skews base-model calibration toward overconfidence.
- Human raters prefer confident-sounding answers, rewarding register over correctness and manufacturing a [confidence-correctness gap](/concepts/confidence-correctness-gap.md).
- Safety evals on current models may not predict future capability jumps, so reviews should trigger on risk rather than expressed confidence.

## Related

- [Capability Forecasting](/concepts/capability-forecasting.md) — predicting what models will do beyond today's pilots
- [Confidence Calibration](/concepts/confidence-calibration.md) — measuring whether stated confidence is trustworthy
- [Emergent Capabilities](/concepts/emergent-capabilities.md) — the scale-threshold jumps that defeat extrapolation
- [Sycophancy](/concepts/sycophancy.md) — the rater preference that inflates confidence
- [The Capabilities Nobody Predicted](/sources/the-capabilities-nobody-predicted.md) — primary source
