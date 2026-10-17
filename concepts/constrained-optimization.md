---
title: "constrained optimization"
type: "Concept"
description: "Choosing the best option under explicit constraints, expressed through decision variables, an objective, and a solver."
created: '2026-10-17'
updated: '2026-10-17'
tags: [engineering, data, mathematics]
sources:
  - "/sources/introduction-to-constrained-optimization.md"
---

# constrained optimization

Constrained optimization finds the values that minimize or maximize a function while satisfying a set of constraints, with the outputs being decision variables. This corpus introduces it as a reusable alternative to hand-rolled quantity logic, using a worked e-commerce example, and notes it is deliberately lighter on code than on vocabulary.

## Key Claims

- Constrained optimization minimizes or maximizes an objective function subject to constraints; the outputs are the decision variables.
- The paint example minimizes total price (Σqᵢpᵢ) subject to coverage meeting the project area (Σqᵢcᵢ ≥ a) plus stock limits.
- Favoring the largest container first is not always cheapest — sales, limited stock, or pricing structure can break that assumption.
- Solver choice matters: linear, nonlinear, and integer solvers suit different problem classes, and some packages expect you to supply a solver.
- Some problems are too hard to solve optimally; a feasible (not optimal) solution may be the practical best available.
- Many real problems are constrained optimization problems in disguise, so a packaged solver usually beats bespoke logic.

## Related

- [over-engineering](/concepts/over-engineering.md) — reuse a solver rather than writing bespoke quantity logic
- [design patterns](/concepts/design-patterns.md) — reusable solutions to recurring design problems
