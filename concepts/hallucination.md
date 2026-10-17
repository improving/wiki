---
title: "Hallucination"
type: "Concept"
description: "Confidently asserted model output that is unsupported or false; one of several categories of AI mistruth, not the only one."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, reliability, evaluation, mistruth]
sources:
  - "/sources/getting-the-right-answer-for-the-wrong-reason.md"
  - "/sources/lies-lies-and-statistics-the-five-ways-ai-gets-things-wrong.md"
  - "/sources/llms-dont-reason-they-hypothesize.md"
---

# Hallucination

Hallucination is a confidently stated model output that is unsupported or false. Across this corpus it is treated less as random noise and more as a structural property of systems that generate the most plausible continuation — and as only one of several ways AI misleads.

## Key Claims

- Hallucination is a defeated hypothesis, not random noise: models perform abductive inference, so errors arrive as confident hypotheses rather than proofs.
- Models score better on abductive tasks than on multi-hop deductive chains, so deductive verification must be a separate pipeline step.
- Hallucination is only one of five categories of AI mistruth (commission, omission, perspective, bias, frame); the other four survive plain fact-checking.
- Medical reference generation showed hallucination rates of roughly 28 to 40 percent.
- Correctness and confidence are only weakly coupled, so an 85 percent accuracy score hides how many correct answers were lucky — see the [confidence-correctness gap](/concepts/confidence-correctness-gap.md).
- [Calibration](/concepts/calibration.md)-aware evals and adversarial testing probe the justification, not just the answer.

## Related

- [Confidence-Correctness Gap](/concepts/confidence-correctness-gap.md) — why accuracy hides lucky answers
- [Calibration](/concepts/calibration.md) — the property evals should measure
- [Cascading hallucination](/concepts/cascading-hallucination.md) — how errors compound downstream
- [Lies, Lies, and Statistics](/sources/lies-lies-and-statistics-the-five-ways-ai-gets-things-wrong.md) — primary source
