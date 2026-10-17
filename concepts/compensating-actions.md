---
title: "Compensating actions"
type: "Concept"
description: "Pairing every forward action with a reverse action, unwound in order on failure, so multi-step transactions can roll back."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, agents, transactions]
sources:
  - "/sources/book-three-cancel-two-the-saga-compensation-chain.md"
  - "/sources/how-to-stop-an-agent-thats-gone-wrong.md"
---

# Compensating actions

A compensating action pairs every forward action with a reverse action, unwound in strict reverse order when a later step fails. It gives multi-step transactions across independent systems something like atomicity, and it is the mechanism the saga pattern relies on when actions cannot be rolled back outright.

## Key Claims

- Multi-step transactions across independent systems have no built-in atomicity.
- Author compensating actions alongside forward actions, before either runs.
- Unwind the compensation stack in strict reverse order, confirming each cancellation.
- Compensation depends on vendor-side idempotency to be safe.
- Reversibility determines where oversight gates belong in a workflow.
- Approving before irreversible actions is the right default for production systems.
- LangGraph interrupt-and-resume is the most powerful production intervention mechanism.

## Related

- [Saga Pattern](/concepts/saga-pattern.md) — the orchestration that drives the compensation chain
- [checkpointing](/concepts/checkpointing.md) — resume where possible; compensate where it is not
- [circuit breakers](/concepts/circuit-breakers.md) — bound failure before it spreads
- [human approval points](/concepts/human-approval-points.md) — gates placed by reversibility
- [LangGraph](/entities/langgraph.md) — interrupt-and-resume implementation
- [Book Three, Cancel Two - The Saga Compensation Chain](/sources/book-three-cancel-two-the-saga-compensation-chain.md) — primary source
- [How to Stop an Agent That's Gone Wrong](/sources/how-to-stop-an-agent-thats-gone-wrong.md) — primary source
