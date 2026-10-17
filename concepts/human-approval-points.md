---
title: "human approval points"
type: "Concept"
description: "Designed pauses where a human authorizes an agent action, placed by how irreversible that action is."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, oversight, approval]
sources:
  - "/sources/agent-containment-is-losing-the-race-to-capability.md"
  - "/sources/devops-was-always-a-trust-problem.md"
  - "/sources/governance-is-not-overhead-it-is-the-engine-of-trust.md"
  - "/sources/how-to-stop-an-agent-thats-gone-wrong.md"
  - "/sources/one-clause-at-a-time-previewing-every-edit-before-it-commits.md"
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
---

# human approval points

A human approval point is a designed pause where a person authorizes an agent action before it takes effect. Across this corpus, approval points are one of the five governance components, and their placement is governed by reversibility: approve before irreversible actions, and let reversible ones proceed. They are trust infrastructure — the conditions for trusting autonomy, built before the autonomy is deployed.

## Key Claims

- Governance's five components are audit trails, boundary enforcement, quality gates, human approval, and access control.
- Reversibility determines where oversight gates belong; "approve before irreversible actions" is the right default for production systems, with the saga pattern managing actions that cannot be rolled back via compensating actions.
- Separating drafting from committing so every proposed edit is previewed cut five silently-applied wrong edits to zero, but per-action approval risks review fatigue and becomes a bottleneck at volume.
- Containment fails at the action layer, not the prompt: in three July 2026 incidents, sandboxes, proxies, approval prompts, and scopes each had unchecked gaps.
- DevOps adoption stalled on trust rather than tooling — tooling deployed in low-trust environments gets adopted defensively and delivers no ROI — and agentic AI faces the same infrastructure-first requirement.
- LangGraph interrupt-and-resume is the most powerful production intervention mechanism, letting a run pause for approval and continue.

## Related

- [human-in-the-loop](/concepts/human-in-the-loop.md) — the broader oversight pattern
- [Compensating actions](/concepts/compensating-actions.md) — handling actions that cannot be undone
- [Saga Pattern](/concepts/saga-pattern.md) — managing non-rollbackable sequences
- [trust infrastructure](/concepts/trust-infrastructure.md) — the conditions built before deployment
- [Review Gate](/concepts/review-gate.md) — approval as a pipeline stage
- [How to Stop an Agent That's Gone Wrong](/sources/how-to-stop-an-agent-thats-gone-wrong.md) — primary source
