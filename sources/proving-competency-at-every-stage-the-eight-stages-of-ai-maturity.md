---
title: "Proving Competency at Every Stage: The Eight Stages of AI Maturity"
type: "Source Summary"
description: "An eight-stage AI maturity model where each stage demands demonstrable proof, used as a diagnostic not a race."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity.md"
---

# Proving Competency at Every Stage: The Eight Stages of AI Maturity — Summary

**Original source**: `references/devlinliles.com/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity.md`

## Summary

This is a measurement guide for an eight-stage AI maturity model, where each stage carries artifacts an organization either can or cannot produce. It runs from Stage 1 (Zero AI) through Off the Shelf, Task, Workflow, Delegate, Coordinate, to aspirational Supervise and Orchestrate. The point is diagnostic honesty rather than progression: most organizations sit at Stage 2 while believing they are at Stage 4, and the gap closes only by producing the artifact.

## Key Claims

- Each stage has explicit proof criteria, green/red signals, and gap questions — e.g. Stage 4 requires an end-to-end success rate, deterministic validation at transitions, tested human punch-out points, and an audit trail.
- Per-step accuracy compounds: at 95% per step a 20-step pipeline succeeds about 36% of the time; at 85% it drops below 5%.
- Stage 5 adds adversarial agents with rejection logs and a measurable, improving ratio of self-caught to escaped errors.
- Stages 7–8 (supervision and orchestration) are aspirational — no organization runs them reliably in production today.
- The blunt diagnostic: ask what happens on an unexpected input. No quality gates with a human still watching continuously means Stage 2, however sophisticated the agents look.

## Relevance

Informs the [AI maturity model](/concepts/ai-maturity-model.md), [quality gates](/concepts/quality-gates.md), [end-to-end success rate](/concepts/end-to-end-success-rate.md), [audit trails](/concepts/audit-trail.md), [adversarial validators](/concepts/adversarial-validators.md), [human punch-out points](/concepts/human-punch-out-points.md), [deterministic validation](/concepts/deterministic-validation.md), and [Lusser's law](/concepts/lussers-law.md).

## Quality

Practitioner blog post by Devlin Liles. Strong as a structured diagnostic with explicit artifacts; the pipeline-percentage math is illustrative rather than a measured result, and the framework is the author's own.

## Entities Mentioned

- None.

## Concepts Covered

- [AI maturity model](/concepts/ai-maturity-model.md) — the post's central framework
- [Quality Gates](/concepts/quality-gates.md) — required at every workflow transition
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — the defining Stage 4 measurement
- [Audit Trail](/concepts/audit-trail.md) — needed to trace failures to their origin step
- [adversarial validators](/concepts/adversarial-validators.md) — Stage 5 rejection-log agent
- [human punch-out points](/concepts/human-punch-out-points.md) — must be tested for bypass attempts
- [deterministic validation](/concepts/deterministic-validation.md) — automatic check before each handoff
- [Lusser's Law](/concepts/lussers-law.md) — per-step accuracy compounding across a pipeline

## Related Sources

- [Unidirectional Quality Gates in AI-Assisted Development: The Ratchet Pattern](/sources/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern.md)
