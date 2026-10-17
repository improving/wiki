---
title: "Fine-Tune or Orchestrate: The Architecture Decision Every Agent Engagement Skips"
type: "Source Summary"
description: "Argues that fine-tune-versus-orchestrate is an explicit architecture decision engagements skip, governed by workflow stability and drift."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/fine-tune-or-orchestrate-the-architecture-decision-every-agent-engagement-skips/fine-tune-or-orchestrate-the-architecture-decision-every-agent-engagement-skips.md"
---

# Fine-Tune or Orchestrate: The Architecture Decision Every Agent Engagement Skips — Summary

**Original source**: `references/devlinliles.com/fine-tune-or-orchestrate-the-architecture-decision-every-agent-engagement-skips/fine-tune-or-orchestrate-the-architecture-decision-every-agent-engagement-skips.md`

## Summary

Liles argues that agent engagements rarely make the fine-tune-versus-orchestrate decision explicitly; it gets defaulted to whatever the demo used. Borrowing the post-training vs. in-context-reasoning split from a 29-author agentic-reasoning survey, he maps it to a quadrant: narrow, stable workflows suit a fine-tuned specialist, while workflows whose steps, tools, or edge cases drift suit an orchestration layer edited overnight. The call must be revisited whenever the workflow's shape changes.

## Key Claims

- The governing choice: bake capability into weights (RL or supervised fine-tuning) versus assemble it at runtime via prompts, tools, and a pipeline.
- Fine-tuning wins outright only in the narrow-and-stable quadrant; broaden the task or let requirements drift and the math flips toward orchestration.
- Fine-tuning looks cheap on the SOW because it shows a one-time training cost — really a bet that the workflow holds still long enough to pay off.
- Each requirement change is a jump on the fine-tuned cost curve (re-label, retrain, re-validate); orchestration absorbs the same change with near-flat cost.
- A narrow specialist out of its depth answers confidently anyway, forcing the problem into the shape of its training data.

## Relevance

Frames the [fine-tuning](/concepts/fine-tuning.md) versus [orchestration layer](/concepts/orchestration-layer.md) architecture decision for agent systems.

## Quality

Practitioner blog post by Devlin Liles. Strong decision framing; both charts are explicitly illustrative and not measured data.

## Entities Mentioned

- None.

## Concepts Covered

- [fine-tuning](/concepts/fine-tuning.md) — the specialist option, favored only for narrow, stable workflows
- [orchestration layer](/concepts/orchestration-layer.md) — the adaptable option for drifting requirements
