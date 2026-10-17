---
title: "The Box That Already Shipped - Rollback by Reversibility Type"
type: "Source Summary"
description: "A single generic undo handler falsely reports success; tag each action by reversibility type and branch rollback strategy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-box-that-already-shipped-rollback-by-reversibility-type/the-box-that-already-shipped-rollback-by-reversibility-type.md"
---

# The Box That Already Shipped - Rollback by Reversibility Type — Summary

**Original source**: `references/devlinliles.com/the-box-that-already-shipped-rollback-by-reversibility-type/the-box-that-already-shipped-rollback-by-reversibility-type.md`

## Summary

An internal IT helpdesk agent provisioning a laptop runs three steps: an audit-log write, an Intune compliance-policy toggle, and a hardware shipment. Liles seeded fifty runs that each fail partway and trigger rollback, and gave them one generic undo function. That works for the log line, reports success for the policy toggle before propagation actually reverts it, and declares success on a shipped box no reverse call can recall. More than four in ten rollback attempts falsely reported success. The fix tags every action at design time with a reversibility class and branches to one of three strategies.

## Key Claims

- File-state actions are cheap and safe to undo directly; stateful-external actions must reverse and then poll actual external state before claiming success.
- True-side-effect actions get no rollback attempt; the handler surfaces "cannot auto-reverse, human compensation required" with concrete next steps.
- The tag lives on the action, set when the step is written — by the time a failure occurs, the kind of action is already known.
- The tagged version dropped the false rollback-success rate from over 40% to under 5%, and true-side-effect cases never reported a false success.

## Relevance

Informs agentic delivery and rollback design, drawing on [compensating actions](/concepts/compensating-actions.md) and the [saga pattern](/concepts/saga-pattern.md); the example stack is [Entra ID](/entities/entra-id.md) as used at [Improving](/entities/improving.md).

## Quality

Practitioner blog post by Devlin Liles. Strength: clear three-tier taxonomy with before/after figures and an honest ceiling on the pattern; caveat: a single fifty-run seeded flow and a hand-written example catalog.

## Entities Mentioned

- [Entra ID](/entities/entra-id.md) — part of the provisioning stack the agent runs against.
- [Improving](/entities/improving.md) — the firm whose IT stack the example mirrors.

## Concepts Covered

- [Compensating actions](/concepts/compensating-actions.md) — the reverse operations the rollback handler applies by reversibility class.
- [Saga Pattern](/concepts/saga-pattern.md) — the multi-step flow with per-step compensation this pattern refines.

## Related Sources

- [MCP Went Stateless. The State Didn't Go Anywhere.](/sources/mcp-went-stateless-the-state-didnt-go-anywhere.md)
- [The 8-Stage AI Trust Evolution: A Map for the Journey](/sources/the-8-stage-ai-trust-evolution-a-map-for-the-journey.md)
