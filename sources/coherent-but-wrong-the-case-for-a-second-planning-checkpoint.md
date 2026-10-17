---
title: "Coherent But Wrong - The Case for a Second Planning Checkpoint"
type: "Source Summary"
description: "A support agent's coherent plan issued the wrong resolution, motivating a separate goal-validation checkpoint after the coherence check."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/coherent-but-wrong-the-case-for-a-second-planning-checkpoint/coherent-but-wrong-the-case-for-a-second-planning-checkpoint.md"
---

# Coherent But Wrong - The Case for a Second Planning Checkpoint — Summary

**Original source**: `references/devlinliles.com/coherent-but-wrong-the-case-for-a-second-planning-checkpoint/coherent-but-wrong-the-case-for-a-second-planning-checkpoint.md`

## Summary

Devlin Liles built a support agent that resolves refund tickets against an order database and a policy ruleset. Given a ticket asking for a card refund, the agent produced a coherent plan, passed a self-review coherence check, and then issued store credit. His argument: coherence is an embarrassingly weak bar because it asks only whether each step follows from the last, never whether the plan lands on what the customer asked for or what policy entitles them to. The fix is a second, separate checkpoint — a Goal-Validation Checkpoint.

## Key Claims

- On twenty-five seeded tickets, acceptance-criteria satisfaction (resolution matched both the stated ask and the applicable policy rule) landed well below the coherence check's own pass rate.
- The fix is a second checkpoint, not a better first one: it independently extracts the ticket's stated acceptance criteria and the applicable policy rule, then diffs the plan against both, capped at one retry.
- It must be a separate pass because of the self-correction illusion: models catch errors flagged in others' reasoning but reliably fail to act on the same error inside their own reasoning trace.
- The retry loop is deliberately narrow — one re-plan with the specific discrepancy handed back — to avoid plan and checker converging on agreement.
- The pattern assumes the checker is trustworthy, and it cannot rescue genuinely ambiguous policy.

## Relevance

Informs [acceptance criteria](/concepts/acceptance-criteria.md) satisfaction in agentic delivery, and the gap between plan adherence and task completion in agent evaluation.

## Quality

Practitioner blog post by Devlin Liles. Grounded in a concrete twenty-five-ticket experiment and linked to 2026 evaluation literature; the single-agent case and the untrusted-checker gap remain open limitations he states plainly.

## Entities Mentioned

- None.

## Concepts Covered

- [acceptance criteria](/concepts/acceptance-criteria.md) — extracted and diffed by the Goal-Validation Checkpoint

## Related Sources

- [Spec-Driven Development for AI: What Works, What Doesn't, and What to Do About It](/sources/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md)
- [The Defect Is in the Definition](/sources/the-defect-is-in-the-definition.md)
