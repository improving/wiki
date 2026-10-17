---
title: "Confidence Calibration"
type: "Concept"
description: "Making a model's stated confidence match its actual accuracy, and disclosing that evidence so trust is inspectable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, trust, reliability]
sources:
  - "/sources/94-percent-confidence-exact-match-auto-resolved.md"
  - "/sources/getting-the-right-answer-for-the-wrong-reason.md"
  - "/sources/the-chinese-room-is-running-in-production.md"
---

# Confidence Calibration

Confidence calibration is the alignment between a model's stated confidence and its actual accuracy, together with the disclosure of that confidence and its evidence. This corpus argues that accuracy alone is a misleading score: correctness and confidence are only weakly coupled in LLMs, so evaluations and user interfaces must target calibration, not just the answer.

## Key Claims

- Borderline auto-resolutions carried a 40%+ error rate when confidence stayed hidden; disclosing confidence and evidence turns faith-based trust into inspectable trust.
- Disclosure is necessary but insufficient without calibration behind the number, and the autonomy threshold remains a policy decision disclosure cannot make.
- Correctness and confidence are only weakly coupled: medical reference generation showed hallucination rates of roughly 28–40%, and an 85% accuracy score hides how many correct answers were lucky.
- LLMs produce Gettier cases — correct answers reached for unrelated reasons — so [calibration](/concepts/calibration.md)-aware evals and adversarial testing must probe the justification, not just the output.
- Behavioral benchmark scores and causal reliability on novel inputs are diverging; [distribution-shifted](/concepts/distribution-shift.md) evaluations expose the gap standard accuracy tests hide.
- Graceful incompetence, calibration, and abstention are distinct architectural goals, connected to [epistemic humility](/concepts/epistemic-humility.md) and [hallucination](/concepts/hallucination.md).

## Related

- [Calibration](/concepts/calibration.md) — the broader reliability property
- [Confidence Thresholds](/concepts/confidence-thresholds.md) — the policy gate on the number
- [Distribution shift](/concepts/distribution-shift.md) — where calibration breaks down
- [94 Percent Confidence, Exact Match, Auto-Resolved](/sources/94-percent-confidence-exact-match-auto-resolved.md) — primary source
