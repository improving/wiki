---
title: "One Clause at a Time - Previewing Every Edit Before It Commits"
type: "Source Summary"
description: "Previewing every agent-proposed edit as a clause-level diff before commit catches wrong edits, at the cost of review fatigue."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/one-clause-at-a-time-previewing-every-edit-before-it-commits/one-clause-at-a-time-previewing-every-edit-before-it-commits.md"
---

# One Clause at a Time - Previewing Every Edit Before It Commits — Summary

**Original source**: `references/devlinliles.com/one-clause-at-a-time-previewing-every-edit-before-it-commits/one-clause-at-a-time-previewing-every-edit-before-it-commits.md`

## Summary

A contract-redlining agent's first version auto-applied every proposed edit with no preview, so all five deliberately-seeded wrong edits (a misread defined term, a liability figure on the wrong section) landed in the working document alongside the correct ten. The damage wasn't the error rate but the invisibility: once legal-ops saw wrong edits auto-applied, distrust spread over the correct edits too. The fix stops any edit from writing directly to the document — each surfaces as a clause-level diff shown before commit, with drafting and committing separated by an explicit [human-in-the-loop](/concepts/human-in-the-loop.md) approval.

## Key Claims

- With preview, all five injected-wrong edits are caught and rejected before reaching the document; the post-hoc correction rate drops to zero.
- The correct ten clauses still move through in roughly the same time, since approving a correct diff is fast; a rejection is cheap because nothing happened yet.
- Trust in an autonomous system isn't decided once at go-live; it's earned one visible action at a time, so each action must be visible before it's final.
- Success creates a new failure: [review fatigue](/concepts/review-bottleneck.md) — someone who has approved two hundred correct diffs may reflexively approve the two hundred and first.
- At volume, per-clause approval becomes the bottleneck; the pattern says nothing about when to graduate to batching or sampling.

## Relevance

Informs [human-in-the-loop](/concepts/human-in-the-loop.md) and [human approval points](/concepts/human-approval-points.md), and the wiki's review-bottleneck and trust themes in agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. Concrete before/after on fifteen synthetic clauses; the sample is small and illustrative, and the review-fatigue and volume caveats are argued from observation rather than measured.

## Entities Mentioned

- None.

## Concepts Covered

- [human-in-the-loop](/concepts/human-in-the-loop.md) — explicit approval before any edit commits
- [human approval points](/concepts/human-approval-points.md) — clause-level diffs as commit gates
- [Review Bottleneck](/concepts/review-bottleneck.md) — review fatigue and volume friction the pattern creates

## Related Sources

- [The 8-Stage AI Trust Evolution: A Map for the Journey](/sources/the-8-stage-ai-trust-evolution-a-map-for-the-journey.md)
- [When Small Mistakes Compound: Building Systems That Survive Imperfect AI](/sources/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai.md)
