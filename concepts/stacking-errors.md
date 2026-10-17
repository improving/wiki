---
title: "Stacking Errors"
type: "Concept"
description: "Chained steps multiply error rates, so end-to-end reliability falls far below per-step accuracy without gates."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, ai-governance, math]
sources:
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
  - "/sources/the-vocabulary-of-ai-native-organizations.md"
  - "/sources/vocabulary-is-a-force-multiplier-why-naming-things-precisely-matters.md"
---

# Stacking Errors

Stacking errors is the compounding failure of chained steps: when each step is imperfect, the reliability of the whole series falls far below the accuracy of any single step. The corpus argues this math is why [AI Governance](/concepts/ai-governance.md) is non-optional — quality gates between steps are the infrastructure that makes autonomy reliable, not overhead friction.

## Key Claims

- Ten steps at 95% accuracy yield only about 60% end-to-end reliability.
- [Lusser's Law](/concepts/lussers-law.md): series-system reliability is the product of component reliabilities, not their average.
- A 99% per-step model succeeds end to end only 37% of the time across a hundred steps; a 98% agent at 20 steps succeeds roughly 67% of the time.
- Prefer shorter, gated pipelines over long autonomous chains; governance is a capability enabler.
- Precise shared vocabulary — stage numbers and named failure mechanisms — gives strategy a language for these failures; naming a recurring pattern makes it discussable and actionable.

## Related

- [Lusser's Law](/concepts/lussers-law.md) — the math behind stacking errors
- [Compounding error](/concepts/compounding-error.md) — the same phenomenon at the model level
- [Quality Gates](/concepts/quality-gates.md) — the mitigation between steps
- [Task Decomposition](/concepts/task-decomposition.md) — shorter pipelines that reduce stacking
- [Shared vocabulary](/concepts/shared-vocabulary.md) — naming the pattern so teams can act on it
- [Stacking Errors: The Compounding Math Behind AI Governance](/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md) — primary source
