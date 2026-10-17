---
title: "Quality Gates at Every Transition - Stopping a Bad Value Before It Becomes the Next Step's Input"
type: "Source Summary"
description: "A pipeline of individually accurate steps can still be confidently wrong; a cheap gate at every handoff stops bad values propagating."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md"
---

# Quality Gates at Every Transition - Stopping a Bad Value Before It Becomes the Next Step's Input — Summary

**Original source**: `references/devlinliles.com/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md`

## Summary

Using an eight-step insurance claims pipeline, the post shows how a system built entirely from individually accurate steps can still produce a confidently wrong answer. Each step is measured against a narrow question — did I do my own job — while the question that matters, whether the value crossing a boundary is sane, is never measured. The fix is a cheap, narrow gate at every handoff that stops a malformed value before it becomes the next step's input.

## Key Claims

- In a run of 200 synthetic claims, every step scored 90–96% on its own, yet one smudged OCR amount read $4,800 as $48,000 and produced a payout wrong by $43,200 with no step catching it.
- A gate only has to ask one specific, testable question at one seam; on failure the item routes to a held-for-review queue and the pipeline continues.
- Gates force a pipeline to branch (pass/continue vs. fail/route), logic a straight sequence cannot express.
- Gates should query ground truth rather than trust a step's self-reported success — reported success and actual success are different signals.
- Limits: a gate sees one item at one seam, so it cannot catch slow aggregate decline; an unreviewed held queue is worse than no gate.

## Relevance

Informs [quality gates](/concepts/quality-gates.md), [error propagation](/concepts/error-propagation.md), [end-to-end success rate](/concepts/end-to-end-success-rate.md), and [compounding error](/concepts/compounding-error.md).

## Quality

Practitioner blog post by Devlin Liles. The synthetic experiment (200 claims, planted defects) is illustrative rather than published data, but the post is explicit about the mechanism and honest about the gate's scope limits.

## Entities Mentioned

- None.

## Concepts Covered

- [Quality Gates](/concepts/quality-gates.md) — the central mechanism
- [Error Propagation](/concepts/error-propagation.md) — what gates prevent
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — the metric that matters over per-step accuracy
- [Compounding error](/concepts/compounding-error.md) — cost grows with every step a defect survives

## Related Sources

- [Unidirectional Quality Gates in AI-Assisted Development: The Ratchet Pattern](/sources/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern.md)
