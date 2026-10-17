---
title: "Design Your AI Like You Don't Know Who You Are"
type: "Source Summary"
description: "Applies Rawls's veil of ignorance to AI fairness, arguing proxy features and feedback loops defeat naive demographic removal."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/design-your-ai-like-you-dont-know-who-you-are/design-your-ai-like-you-dont-know-who-you-are.md"
---

# Design Your AI Like You Don't Know Who You Are — Summary

**Original source**: `references/devlinliles.com/design-your-ai-like-you-dont-know-who-you-are/design-your-ai-like-you-dont-know-who-you-are.md`

## Summary

The post applies John Rawls's veil of ignorance to machine learning fairness: design model behavior as if you didn't know which demographic group's queries you'd submit. It argues that naive fairness measures fail — removing demographic features makes bias worse because proxy signals remain — and that feedback loops can quietly erode fairness over time, so genuine fairness needs proxy-aware design and longitudinal monitoring.

## Key Claims

- A November 2025 paper found naively removing demographic features worsened bias by 8.9%, while proxy-aware pruning reduced the demographic parity gap by 32.6%.
- Removing obvious attributes leaves demographic signal encoded in remaining features — a thin curtain, not a veil.
- A Fudan Journal critique identifies a fundamental paradox: Rawlsian-fair systems can grow more disparate over time through feedback loops (documented in healthcare allocation).
- Aggregate metrics hide failure — 87% overall accuracy can mask 94% majority vs. 74% minority accuracy.
- Zip code encodes race and income; browsing history encodes gender; vocabulary patterns encode education and origin.
- Operationalization requires reframing fairness as design intent, disaggregated evaluation, longitudinal monitoring, and proxy modeling.

## Relevance

Informs [distribution shift](/concepts/distribution-shift.md) as the mechanism by which fair-at-deployment systems drift unfair through feedback loops.

## Quality

Practitioner blog post by Devlin Liles. Strength: pairs a philosophical frame with cited empirical results and concrete enterprise practices. Caveat: draws on a few studies and translates a theoretical principle into practice by analogy.

## Entities Mentioned

- None.

## Concepts Covered

- [distribution shift](/concepts/distribution-shift.md) — evolving populations and feedback loops that erode deployment-time fairness
