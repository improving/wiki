---
title: "Saga Pattern"
type: "Concept"
description: "Pairing each forward action with a compensating action, unwound in reverse order, to remove orphaned cost from multi-step transactions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, reliability, transactions]
sources:
  - "/sources/book-three-cancel-two-the-saga-compensation-chain.md"
  - "/sources/how-to-stop-an-agent-thats-gone-wrong.md"
---

# Saga Pattern

The saga pattern manages multi-step transactions that span independent systems and therefore have no built-in atomicity: when a later step fails, earlier steps cannot simply be rolled back. The remedy is to pair every forward action with a compensating action, authored *before* either runs, and to unwind the compensation stack in strict reverse order on failure, confirming each cancellation. In this corpus the saga pattern is the answer for agent actions that are irreversible — where the alternative, an approval gate before the action, is not enough because the action has already begun.

## Key Claims

- Multi-step transactions across independent systems have no built-in atomicity.
- Author compensating actions alongside forward actions before either runs.
- Unwind the compensation stack in strict reverse order, confirming each cancellation.
- Compensation depends on vendor-side idempotency to be safe.
- Reversibility determines where oversight gates belong; approve before irreversible actions is the production default.
- The saga pattern handles actions that cannot be rolled back, complementing rather than replacing approval gates.

## Related

- [Compensating actions](/concepts/compensating-actions.md) — the unit a saga unwinds
- [Unit of work](/concepts/unit-of-work.md) — the transaction boundary a saga spans
- [human approval points](/concepts/human-approval-points.md) — the pre-action alternative for reversible steps
- [checkpointing](/concepts/checkpointing.md) — resuming instead of redoing long agent runs
- [circuit breakers](/concepts/circuit-breakers.md) — stopping a failing chain before more damage
- [LangGraph](/entities/langgraph.md) — the runtime whose interrupt-and-resume powers production intervention
- [Book Three, Cancel Two - The Saga Compensation Chain](/sources/book-three-cancel-two-the-saga-compensation-chain.md) — primary source
