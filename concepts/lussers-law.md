---
title: "Lusser's Law"
type: "Concept"
description: "A series system's reliability is the product of its components' reliabilities, so chained steps compound errors."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, error-math, agents]
sources:
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
  - "/sources/your-agent-is-probably-less-reliable-than-you-think.md"
---

# Lusser's Law

Lusser's Law states that the reliability of a system whose components act in series is the product of their individual reliabilities, not their average. Applied to AI agents, it explains why long autonomous chains fail far more often than per-step accuracy suggests: reliability decays multiplicatively with each additional step.

## Key Claims

- Ten steps at 95% accuracy yield only about 60% end-to-end reliability.
- A 98%-per-step agent at 20 steps succeeds only about 67% of the time.
- System reliability is the product of component reliabilities, never their mean.
- Quality gates between steps are the governance infrastructure that makes autonomy reliable — a capability enabler, not overhead friction.
- Shorter, gated pipelines beat long autonomous chains; adversarial inspector agents can break error chains without raising per-step accuracy.
- Errors left in context recruit the model to defend them.

## Related

- [Stacking Errors](/concepts/stacking-errors.md) — the phenomenon Lusser's Law quantifies
- [Compounding error](/concepts/compounding-error.md) — the multiplicative failure mode
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — the metric this law predicts
- [Quality Gates](/concepts/quality-gates.md) — the mitigation
- [Robert Lusser](/entities/robert-lusser.md) — namesake of the law
- [Stacking Errors: The Compounding Math Behind AI Governance](/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md) — primary source
- [Your Agent Is Probably Less Reliable Than You Think](/sources/your-agent-is-probably-less-reliable-than-you-think.md) — primary source
