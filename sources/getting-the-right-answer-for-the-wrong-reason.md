---
title: "Getting the Right Answer for the Wrong Reason"
type: "Source Summary"
description: "LLMs produce Gettier cases: correct, confident answers reached by pattern-matching rather than understanding, which accuracy evals miss."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/getting-the-right-answer-for-the-wrong-reason/getting-the-right-answer-for-the-wrong-reason.md"
---

# Getting the Right Answer for the Wrong Reason — Summary

**Original source**: `references/devlinliles.com/getting-the-right-answer-for-the-wrong-reason/getting-the-right-answer-for-the-wrong-reason.md`

## Summary

Devlin Liles argues you cannot trust an AI system because it got the last ten answers right, because correctness and confidence are weakly coupled. Using Edmund Gettier's 1963 counterexamples to the justified-true-belief definition of knowledge, he shows that an LLM can produce a confident, accurate answer whose reasoning path is coincidental pattern-matching — a Gettier case at inference time. Standard accuracy evals miss this because they measure the score, not the structure of the correct answers.

## Key Claims

- A 2024 JMIR study on medical reference generation found [hallucination](/concepts/hallucination.md) rates of roughly 28–40% depending on model, many delivered in the same confident register as correct answers.
- A model getting 85% on an accuracy eval may include an unknown share of lucky "Gettier" cases that break when the framing, noise, or context shifts.
- Evaluation should be calibration-aware: probe the reasoning path, vary framing, ask follow-ups, and check whether [confidence](/concepts/confidence-calibration.md) tracks actual accuracy.
- Human review checkpoints should target confident outputs, not uncertain ones, since a hedging model at least signals uncertainty.
- Track record is weak evidence: a model that has answered 10,000 questions correctly has not necessarily understood any of them.

## Relevance

Central to AI evaluation practice — [Evaluation harness](/concepts/evaluation-harness.md), [distribution shift](/concepts/distribution-shift.md), and the [Confidence-Correctness Gap](/concepts/confidence-correctness-gap.md).

## Quality

Practitioner blog post by Devlin Liles. Strong conceptual framing grounded in a real study; the philosophy-to-evals bridge is argumentative rather than measured.

## Entities Mentioned

- None.

## Concepts Covered

- [Hallucination](/concepts/hallucination.md) — confident wrong answers in high-stakes domains
- [Confidence Calibration](/concepts/confidence-calibration.md) — checking whether confidence tracks accuracy
- [Confidence-Correctness Gap](/concepts/confidence-correctness-gap.md) — weak coupling between being right and being sure
- [Evaluation harness](/concepts/evaluation-harness.md) — evals that probe reasoning, not just accuracy
- [distribution shift](/concepts/distribution-shift.md) — where the Gettier cases wait

## Related Sources

- [94 Percent Confidence, Exact Match, Auto-Resolved](/sources/94-percent-confidence-exact-match-auto-resolved.md)
- [Lies, Lies, and Statistics: The Five Ways AI Gets Things Wrong](/sources/lies-lies-and-statistics-the-five-ways-ai-gets-things-wrong.md)
