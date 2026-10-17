---
title: "Confidence Thresholds"
type: "Concept"
description: "Routing decisions by how confident or cheap each check is, escalating only ambiguous cases to expensive review."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, review, reliability]
sources:
  - "/sources/sixty-snippets-a-rule-check-could-have-caught.md"
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
---

# Confidence Thresholds

Confidence thresholds are the decision rules that determine how far a piece of work progresses through a tiered pipeline before it is accepted, escalated, or rejected. They matter across this corpus because both cost and reliability are governed by where those gates sit: cheap deterministic checks should catch the easy cases, and only genuinely ambiguous work should reach expensive human review.

## Key Claims

- Sixty of two hundred snippets had violations a deterministic rule check catches instantly, so ordering stages matters.
- Stages must run in strict cost order — cheapest check first — to cut cost without lowering the catch rate.
- Tiering only pays off when the cost gap between stages is large; otherwise the extra hops add latency for little gain.
- Because chained steps multiply error rates (ten steps at 95% yield roughly 60% end-to-end reliability), gates between steps are the infrastructure that makes autonomy reliable.
- Prefer shorter, gated pipelines over long autonomous chains.

## Related

- [Stacking Errors](/concepts/stacking-errors.md) — why gates between steps are required
- [Quality Gates](/concepts/quality-gates.md) — the enforcement points thresholds feed
- [Model-as-judge](/concepts/model-as-judge.md) — the middle, model-based tier
- [Sixty Snippets a Rule Check Could Have Caught](/sources/sixty-snippets-a-rule-check-could-have-caught.md) — primary source
- [Stacking Errors](/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md) — compounding math
