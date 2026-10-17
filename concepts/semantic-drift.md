---
title: "semantic drift"
type: "Concept"
description: "A gradual, exception-free accumulation of off-target output that stack traces never surface."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, agents, failure-modes]
sources:
  - "/sources/the-error-your-stack-trace-will-never-catch.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
---

# semantic drift

Semantic drift is the slow divergence of an agentic system from its intended target without any error being raised. Nothing throws; the output stays plausible and well-formed while drifting away from what was asked. It matters because it defeats the usual observability reflex — you cannot catch it with a stack trace, only with evaluation, lineage, and gates that check meaning rather than syntax.

## Key Claims

- Agentic errors fall into five types: REG, BUG, SEC, INF, and DAT — semantic drift is the one that raises no exception.
- Drift accumulates gradually and off-target rather than failing at a single point.
- Pre-execution gates — test sufficiency, scope validation, pre-flight checks — catch drift before it runs.
- Runtime safeguards include circuit breakers, timeouts, and token budgets.
- In layered agentic delivery, failure in one layer surfaces as a symptom in another, so drift is often misdiagnosed.
- The governance loop breaks at its weakest stage, not its average, so a single unchecked stage lets drift compound.

## Related

- [context drift](/concepts/context-drift.md) — the context-window analogue of the same slow divergence
- [Compounding error](/concepts/compounding-error.md) — how small off-target steps accumulate
- [Quiet Drift](/concepts/quiet-drift.md) — a related silent-failure pattern
- [Error Propagation](/concepts/error-propagation.md) — how drift spreads across layers
- [The Error Your Stack Trace Will Never Catch](/sources/the-error-your-stack-trace-will-never-catch.md) — primary source
- [The Twelve Problems of Agentic Software Delivery](/sources/the-twelve-problems-of-agentic-software-delivery.md) — primary source
