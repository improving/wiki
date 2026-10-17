---
title: "Axiom Disclosure - Naming Whose Preferences Your Model Actually Optimizes For"
type: "Source Summary"
description: "A disclosure record that names whose preferences a vendor model's alignment tuning optimizes for, reviewed before deployment."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/axiom-disclosure-naming-whose-preferences-your-model-actually-optimizes-for/axiom-disclosure-naming-whose-preferences-your-model-actually-optimizes-for.md"
---

# Axiom Disclosure - Naming Whose Preferences Your Model Actually Optimizes For — Summary

**Original source**: `references/devlinliles.com/axiom-disclosure-naming-whose-preferences-your-model-actually-optimizes-for/axiom-disclosure-naming-whose-preferences-your-model-actually-optimizes-for.md`

## Summary

An HR policy assistant built on an off-the-shelf "helpful and harmless" vendor model gave confident, plausible answers that contradicted the company's own written policy on boundary cases, because nobody had recorded what the vendor's alignment tuning optimized for. Devlin proposes an "axiom disclosure record" that names whose preferences the tuning was built from and what aggregation method produced the reward signal, reviewed against company policy before launch. Known-divergence areas are routed to human reviewers rather than shipped as raw vendor answers.

## Key Claims

- On a 100-question seeded set with 12 boundary cases, the assistant gave a conservative but policy-contradicting parental-leave answer that no review step caught.
- The disclosure record surfaced known divergence areas in advance, producing a 100% disclosed-and-routed rate on boundary cases.
- Disclosure only covers what the vendor chooses to publish; most omit rater demographics, aggregation methods, and deliberate edge-case tradeoffs.
- Every alignment method bottoms out at an unjustified stopping point — RLHF at raters, constitutional approaches at the constitution — and documenting it makes the choice visible, not resolved.
- Vendor model updates can silently invalidate a disclosure record, so re-review should be tied to model version changes.

## Relevance

Informs [AI governance](/concepts/ai-governance.md) practice, the trade-offs of [RLHF](/concepts/rlhf.md) and [Constitutional AI](/concepts/constitutional-ai.md), and the risk of [sycophancy](/concepts/sycophancy.md) collapsing value choices to whoever is in the chat window.

## Quality

Practitioner blog post by Devlin Liles. Illustrative single-case figures (100 questions, 12 boundary cases) with cited arXiv preprints; opinionated and explicit about what the pattern cannot resolve.

## Entities Mentioned

- None.

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — the pattern is a governance artifact for adopting vendor models
- [RLHF](/concepts/rlhf.md) — named as one alignment method with an arbitrary stopping point
- [Constitutional AI](/concepts/constitutional-ai.md) — contrasted as moving the stopping point up one level
- [Sycophancy](/concepts/sycophancy.md) — cited as a common practical failure mode of the trilemma
