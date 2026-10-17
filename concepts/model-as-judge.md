---
title: "Model-as-judge"
type: "Concept"
description: "Using a language model to score outputs, powerful but untrustworthy unless calibrated to human consensus and cost-ordered."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, llm, quality]
sources:
  - "/sources/seven-out-of-ten-stopped-meaning-what-it-used-to.md"
  - "/sources/sixty-snippets-a-rule-check-could-have-caught.md"
  - "/sources/the-engineers-evolution-stage-4-designing-and-governing-the-workflow.md"
  - "/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# Model-as-judge

Model-as-judge (LLM-as-judge) uses a language model to score outputs against criteria, sitting in an evaluation stack above cheap deterministic checks and below human review. Across this corpus it is powerful but untrustworthy by default: judges carry documented bias, their thresholds drift silently, and they add value only when calibrated to human consensus and ordered by cost.

## Key Claims

- A judge agreed with human raters at a Cohen's kappa under 0.5 before a model swap; the swap pushed misapproved copy past 15%.
- Calibration maps raw scores to human consensus and should gate approval at kappa 0.65; silent vendor drift means it must run on a schedule, not only on swaps.
- Layer graders: structural, code-validator, LLM-as-judge, process reward models, then human — calibrating the judge to 80% rank-order agreement with humans.
- Sixty of two hundred snippets had violations a deterministic rule check catches instantly, so stages must run in strict cost order, cheapest first.
- Only genuinely ambiguous cases should escalate to human review; tiering pays off only when the cost gap between stages is large.
- Evals-as-code version-controls graders and test cases and wires them into CI; A/B routing requires pre-registered sample sizes and 95% confidence.
- A protection harness is only as good as its weakest gate.

## Related

- [Calibration](/concepts/calibration.md) — the step that makes a judge trustworthy
- [deterministic validation](/concepts/deterministic-validation.md) — the cheapest stage before the judge
- [evals-as-code](/concepts/evals-as-code.md) — versioning graders into CI
- [evaluation harness](/concepts/evaluation-harness.md) — the structure the judge sits in
- [human-in-the-loop](/concepts/human-in-the-loop.md) — the escalation tier above the judge
- [Seven Out of Ten Stopped Meaning What It Used To](/sources/seven-out-of-ten-stopped-meaning-what-it-used-to.md) — primary source
