---
title: "How to Stop an Agent That's Gone Wrong"
type: "Source Summary"
description: "Frames agent intervention as a reversibility spectrum: interrupt-and-resume, approval gates, sagas, and pool- or session-level controls."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/how-to-stop-an-agent-thats-gone-wrong/how-to-stop-an-agent-thats-gone-wrong.md"
---

# How to Stop an Agent That's Gone Wrong — Summary

**Original source**: `references/devlinliles.com/how-to-stop-an-agent-thats-gone-wrong/how-to-stop-an-agent-thats-gone-wrong.md`

## Summary

Liles argues the question is not whether agents will go wrong but what you can do when they do, and whether you built that capability before you needed it. He frames intervention as a spectrum from graceful pause-and-hand-off to full rollback, with placement determined by one factor: how reversible the action already taken is.

## Key Claims

- Gate placement follows reversibility: the more irreversible the action, the earlier oversight must happen; "approve before irreversible" is the right default and avoids overhead on reversible steps.
- LangGraph's interrupt-and-resume is the most powerful mechanism—pausing at any node, exposing state, accepting edits, and resuming—because it checkpoints state at every node.
- Approval gates are coarser, firing at phase boundaries, but far simpler; HumanLayer adds them to any framework with a decorator, routing requests to Slack, email, or a custom UI.
- The saga pattern defines a compensating action for each non-rollbackable step; teams that skip this design work discover the gap during an incident.
- Error recovery and course correction are different problems: in course correction the agent did nothing wrong, the world changed, so you adapt rather than roll back.

## Relevance

Details [human approval points](/concepts/human-approval-points.md), the [Saga Pattern](/concepts/saga-pattern.md), and [compensating actions](/concepts/compensating-actions.md); the mechanisms are grounded in [LangGraph](/entities/langgraph.md), [HumanLayer](/entities/humanlayer.md), and [Augment Code](/entities/augment-code.md)'s pattern catalog.

## Quality

Practitioner blog post by Devlin Liles. Clear taxonomy tied to named tools and literature; the recommendations are experience-based and the post cites vendor documentation rather than measured incident data.

## Entities Mentioned

- [LangGraph](/entities/langgraph.md) — interrupt-and-resume, the "gold standard" mechanism
- [HumanLayer](/entities/humanlayer.md) — decorator-based approval gates
- [Augment Code](/entities/augment-code.md) — source for the intervention pattern catalog

## Concepts Covered

- [human approval points](/concepts/human-approval-points.md) — phase-boundary gates versus per-step control
- [Saga Pattern](/concepts/saga-pattern.md) — handling actions that cannot be rolled back
- [Compensating actions](/concepts/compensating-actions.md) — the per-step reversal defined up front
- [checkpointing](/concepts/checkpointing.md) — the state persistence that makes interrupt-and-resume possible

## Related Sources

- [Agentic Development Is Eleven Problems, Not One](/sources/agentic-development-is-eleven-problems-not-one.md)
