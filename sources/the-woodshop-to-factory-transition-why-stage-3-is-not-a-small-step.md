---
title: "The Woodshop-to-Factory Transition: Why Stage 3 Is Not a Small Step"
type: "Source Summary"
description: "Moving to autonomous agents is a category change requiring factory infrastructure: boundaries, quality gates, audit trails, and error handling."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-woodshop-to-factory-transition-why-stage-3-is-not-a-small-step/the-woodshop-to-factory-transition-why-stage-3-is-not-a-small-step.md"
---

# The Woodshop-to-Factory Transition: Why Stage 3 Is Not a Small Step — Summary

**Original source**: `references/devlinliles.com/the-woodshop-to-factory-transition-why-stage-3-is-not-a-small-step/the-woodshop-to-factory-transition-why-stage-3-is-not-a-small-step.md`

## Summary

Devlin Liles argues that the move from AI-assisted work (Stage 2) to autonomous task agents (Stage 3) is not an increment like manual-to-CI/CD but a category change in operating environment. He uses the woodshop-to-factory analogy: in the woodshop the craftsman is the quality gate, while a factory requires safety systems, codified standards, inspection points, and material specs built explicitly. Teams that scale autonomous agents without this infrastructure see errors compound, then wrongly conclude autonomous AI doesn't work.

## Key Claims

- Stage 2 quality is enforced by the developer's continuous presence; Stage 3 agents execute without continuous human oversight, at speed and scale.
- Walter Shewhart's control charts at Bell Labs in 1924 marked manufacturing's acceptance that inspecting finished goods was too late — quality had to live in the process.
- Stage 3 requires four infrastructure pieces: agent boundaries, quality gates, audit trails, and error handling, all designed before the first production run.
- A boundary assumed implicit in the agent's training is "a hope, and hope is poor infrastructure."
- Counterarguments that self-monitoring replaces infrastructure or that infrastructure-first is waterfall are addressed: run pilot lines small and instrumented before scaling.

## Relevance

Central to [woodshop-to-factory transition](/concepts/woodshop-to-factory-transition.md), and it defines the [quality gates](/concepts/quality-gates.md) and [audit trail](/concepts/audit-trail.md) infrastructure autonomous delivery demands.

## Quality

Practitioner blog post by Devlin Liles. Strong analogy-driven argument with concrete requirements; evidence is historical and illustrative rather than measured.

## Entities Mentioned

- None.

## Concepts Covered

- [Woodshop-to-Factory Transition](/concepts/woodshop-to-factory-transition.md) — the central analogy
- [Quality Gates](/concepts/quality-gates.md) — validation points before output passes forward
- [Audit Trail](/concepts/audit-trail.md) — what the agent did, when, why, and with what outcome
- [Boundary enforcement](/concepts/boundary-enforcement.md) — explicit, enforced agent boundaries
- [human approval points](/concepts/human-approval-points.md) — decisions requiring human sign-off
