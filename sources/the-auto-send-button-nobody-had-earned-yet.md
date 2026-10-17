---
title: "The Auto-Send Button Nobody Had Earned Yet"
type: "Source Summary"
description: "Exposing auto-send as a feature flag gives every user unearned autonomy; gate it behind per-user demonstrated approval history."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-auto-send-button-nobody-had-earned-yet/the-auto-send-button-nobody-had-earned-yet.md"
---

# The Auto-Send Button Nobody Had Earned Yet — Summary

**Original source**: `references/devlinliles.com/the-auto-send-button-nobody-had-earned-yet/the-auto-send-button-nobody-had-earned-yet.md`

## Summary

Liles built a sales-proposal drafting tool with a suggest mode (a human approves before sending) and an auto-send mode (no review at all), and shipped both to every user from day one. Running twenty synthetic scenarios, a zero-history account had the same access to auto-send as a veteran and flipped it on immediately, sending a proposal with a pricing error straight to a client. The mistake was predictable from the access model: a feature flag tracks whether the code shipped, not whether any given person earned the faster path. The fix hides auto-send per user until a reveal gate confirms at least ten approved suggest-mode drafts.

## Key Claims

- Uniform rollout treats a team's aggregate readiness and an individual user's demonstrated readiness as identical, though they are different claims.
- With the reveal gate, the unearned-autonomy incident rate went to zero across the same twenty scenarios, while users who had cleared ten approvals kept auto-send unchanged.
- Approval count is a proxy for clicks, not scrutiny: a user can rubber-stamp ten drafts and clear the gate without reading any.
- The threshold is not universal; ten is cheap to measure but the right number depends on how expensive a single bad higher-autonomy action is.

## Relevance

Informs agentic delivery and trust design, touching [human approval points](/concepts/human-approval-points.md), [human-in-the-loop](/concepts/human-in-the-loop.md), and [progressive deployment](/concepts/progressive-deployment.md) by making autonomy access individually earned.

## Quality

Practitioner blog post by Devlin Liles. Strength: a crisp, reproducible access-model failure with a clear before/after; caveat: single synthetic case set, and the author openly flags that the gating metric is a proxy.

## Entities Mentioned

- None.

## Concepts Covered

- [human approval points](/concepts/human-approval-points.md) — the per-user approval history the reveal gate checks.
- [human-in-the-loop](/concepts/human-in-the-loop.md) — suggest mode keeps a person in the loop; auto-send removes it.
- [progressive deployment](/concepts/progressive-deployment.md) — the reveal gate reveals capability per user as trust accrues.
