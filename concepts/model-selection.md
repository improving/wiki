---
title: "Model selection"
type: "Concept"
description: "Choosing a model by matching measured capability, cost, latency, and failure profile to a task rather than defaulting to the largest."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, evaluation, cost, security]
sources:
  - "/sources/using-evaluation-data-to-match-model-capability-to-task-requirements-2.md"
  - "/sources/what-a-10-percent-chip-stock-selloff-over-one-model-release-actually-tells-you.md"
  - "/sources/which-failure-mode-can-you-afford-the-security-personality-of-your-model.md"
---

# Model selection

Model selection is the practice of matching a model's measured capability, cost, latency, and failure profile to a specific task instead of defaulting to the largest available model. Across this corpus it is an evaluation-driven decision, and one that headline benchmarks alone cannot make.

## Key Claims

- Defaulting to the largest model buys capability the task does not need; raw scores miss cost, latency, availability, and consistency tradeoffs.
- A 20-30 case subset can rank candidate models cheaply; shadow-deploy a candidate before promoting it to production.
- Models within four SWE-bench points span a 12x range in security-critical defect density, so failure profiles are distinct and uncorrelated.
- [SOC 2](/entities/soc-2-type-ii.md) and EU AI Act Annex III make task-specific model evaluation auditable.
- Static analysis misses semantic correctness; [METR](/entities/metr.md) found half of graded AI PRs unmergeable.
- A 10 percent chip-stock selloff over one open-weight release reflected headline-reactive capital, not a change in fundamentals — integration work and enterprise context, not model weights, are the durable moat.

## Related

- [model routing](/concepts/model-routing.md) — operational counterpart that picks a model per request
- [Open-Weight Models](/concepts/open-weight-models.md) — the class behind the selloff case
- [token cost](/concepts/token-cost.md) — a tradeoff raw scores hide
- [Which Failure Mode Can You Afford?](/sources/which-failure-mode-can-you-afford-the-security-personality-of-your-model.md) — primary source
