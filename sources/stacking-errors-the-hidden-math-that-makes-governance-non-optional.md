---
title: "Stacking Errors: The Compounding Math Behind AI Governance"
type: "Source Summary"
description: "Chained agent steps multiply error rates; quality gates and thresholds are what make autonomy reliable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/stacking-errors-the-hidden-math-that-makes-governance-non-optional/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
---

# Stacking Errors: The Compounding Math Behind AI Governance — Summary

**Original source**: `references/devlinliles.com/stacking-errors-the-hidden-math-that-makes-governance-non-optional/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md`

## Summary

Trust in autonomous agents is an infrastructure question, and the reason comes down to one piece of math. A 10-step pipeline where each step is 95% accurate produces correct end-to-end results only about 60% of the time (`0.95^10`); 20 steps drops to roughly 36%. Because chained steps multiply their error probabilities, governance is not friction but the mechanism that lets autonomy reach the reliability an organization needs.

## Key Claims

- `0.95^10 ≈ 0.60` and `0.95^20 ≈ 0.36`: per-step accuracy does not equal end-to-end reliability.
- Robert Lusser formalized this in the 1940s (Lusser's law): series-system reliability is the product of component reliabilities.
- John von Neumann's 1956 work on reliable organisms from unreliable components is the intellectual ancestor of the quality gate.
- Governance mechanisms belong at each transition: automated quality gates, structured output validation, confidence thresholds, and human approval points reserved for irreversible steps.
- The autonomy paradox: longer, fewer-touchpoint pipelines are less reliable and harder to debug than shorter, gated ones.

## Relevance

Reframes [AI Governance](/concepts/ai-governance.md) as a capability enabler rather than overhead, and grounds [stacking errors](/concepts/stacking-errors.md) and [Lusser's law](/concepts/lussers-law.md) in concrete pipeline design.

## Quality

Practitioner blog post by Devlin Liles. The math is exact and verifiable; the reliability figures are illustrative models, and the author openly flags the independence assumption as a simplification.

## Entities Mentioned

- [Robert Lusser](/entities/robert-lusser.md) — formalized series-system reliability
- [John von Neumann](/entities/john-von-neumann.md) — carried the idea into computing

## Concepts Covered

- [Stacking Errors](/concepts/stacking-errors.md) — central argument
- [Lusser's Law](/concepts/lussers-law.md) — the underlying math
- [Quality Gates](/concepts/quality-gates.md) — the proposed fix
- [Confidence Thresholds](/concepts/confidence-thresholds.md) — per-step routing mechanism
- [human approval points](/concepts/human-approval-points.md) — reserved for irreversible steps
