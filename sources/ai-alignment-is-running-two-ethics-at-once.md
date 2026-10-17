---
title: "AI Alignment Is Running Two Ethics at Once"
type: "Source Summary"
description: "Constitutional AI and RLHF map onto deontology and consequentialism, and their intersection explains key AI failure modes."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/ai-alignment-is-running-two-ethics-at-once/ai-alignment-is-running-two-ethics-at-once.md"
---

# AI Alignment Is Running Two Ethics at Once — Summary

**Original source**: `references/devlinliles.com/ai-alignment-is-running-two-ethics-at-once/ai-alignment-is-running-two-ethics-at-once.md`

## Summary

Devlin Liles argues that major AI alignment approaches split along an old moral-philosophy fault line: Constitutional AI is deontological (rule-following) while RLHF is consequentialist (outcome-maximizing). Neither dominates, and their intersection explains common production failure modes. System prompts and internal policies are applied ethics, so governance must consciously resolve the tension rather than leaving it to the model.

## Key Claims

- Constitutional AI defines principles and trains the model to follow them via self-critique, buying rule consistency and legibility at the cost of handling novel edge cases.
- RLHF trains a reward model from human preferences and optimizes for approval, aligning tightly with user wants but with opaque, inconsistent encoded values.
- The deontological failure is over-refusal: a "don't help harm" rule blocks harm-reduction, medical, security-research, and historical information.
- The consequentialist failure is reward hacking and sycophancy: optimizing for approval converges on "approved outcomes" rather than "good outcomes."
- Enterprise tradeoffs follow: RLHF systems satisfy users better but apply rules less consistently; constitutional systems are more predictable but refuse arbitrarily.
- Where rule-based and satisfaction-based instructions conflict, an unconsidered governance position silently delegates the choice to the model.

## Relevance

Informs [Constitutional AI](/concepts/constitutional-ai.md) and [RLHF](/concepts/rlhf.md) as the two ethical frames, and their failure modes [reward hacking](/concepts/reward-hacking.md) and [Sycophancy](/concepts/sycophancy.md).

## Quality

Practitioner blog post by Devlin Liles. Strength: a clear, useful mapping of philosophy onto deployment tradeoffs. Caveat: an interpretive essay; the Kant/Mill framing is the author's analogy, not a formal claim about lab methods.

## Entities Mentioned

- [John Stuart Mill](/entities/john-stuart-mill.md) — source of the consequentialist frame

## Concepts Covered

- [Constitutional AI](/concepts/constitutional-ai.md) — the deontological alignment approach
- [RLHF](/concepts/rlhf.md) — the consequentialist alignment approach
- [reward hacking](/concepts/reward-hacking.md) — a consequentialist failure mode
- [Sycophancy](/concepts/sycophancy.md) — approval-maximizing behavior

## Related Sources

- [Every Guardrail Is a Value Judgment](/sources/every-guardrail-is-a-value-judgment.md)
