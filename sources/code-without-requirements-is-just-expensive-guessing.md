---
title: "Code Without Requirements Is Just Expensive Guessing"
type: "Source Summary"
description: "Argues that AI coding tools make missing requirements more costly, so specs and acceptance criteria must precede implementation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agile-post, devlinliles.com]
sources:
  - "references/devlinliles.com/code-without-requirements-is-just-expensive-guessing/code-without-requirements-is-just-expensive-guessing.md"
---

# Code Without Requirements Is Just Expensive Guessing — Summary

**Original source**: `references/devlinliles.com/code-without-requirements-is-just-expensive-guessing/code-without-requirements-is-just-expensive-guessing.md`

## Summary

Devlin Liles argues that the fastest way to slow down an AI-enabled team is to let it skip requirements, because the code isn't the expensive part — the rework is. AI coding tools optimize for speed from prompt to code, but they accelerate a sloppy process at machine speed, widening the blast radius of a vague spec by an order of magnitude. Requirements, he contends, are the constraints that stop agents from optimizing in the wrong direction, and the teams that lock them in before the first prompt avoid the "60-day velocity wall."

## Key Claims

- Barry Boehm's research showed defect-fix cost climbs steeply the later a defect is found, and the most expensive are planted at the requirements stage; Fred Brooks made the same point in "No Silver Bullet."
- Around day 60, AI-enabled teams' velocity peaks while delivery flattens or declines — review bottlenecks, architectural drift, and integration failures pile up.
- An agent without requirements will make unauthorized architectural decisions, add unevaluated dependencies, and solve adjacent problems.
- Teams that write acceptance criteria, non-functional constraints, and architectural boundaries before implementation land the first implementation closer to correct and compress review cycles.
- Requirements should flow through the pipeline as data, producing built-in traceability matrices rather than manual bookkeeping — "evidence is the deliverable" in regulated industries.

## Relevance

Informs [acceptance criteria](/concepts/acceptance-criteria.md), workflow sequencing, and AI-era delivery practice; engages the [Agile Manifesto](/entities/agile-manifesto.md) tension.

## Quality

Practitioner blog post by Devlin Liles. Concrete and well-argued with named historical findings; the "60-day wall" is an observed pattern from personal experience, not measured research.

## Entities Mentioned

- [Fred Brooks](/entities/fred-brooks.md) — cited for "the hardest part is deciding what to build"
- [Agile Manifesto](/entities/agile-manifesto.md) — its documentation stance is addressed as an objection

## Concepts Covered

- [acceptance criteria](/concepts/acceptance-criteria.md) — the first of three artifacts to write before prompting

## Related Sources

- [False Dichotomies Are the Enemy of Progress](/sources/false-dichotomies-are-the-enemy-of-progress.md)
- [P.O.S.T.: Four Dimensions of AI-Native Delivery](/sources/p-o-s-t-four-dimensions-of-ai-native-delivery.md)
- [The Manifesto We Forgot We Were Following](/sources/the-manifesto-we-forgot-we-were-following.md)
- [The Three Eras of Agile: Constraint, Synergy, Intent](/sources/the-three-eras-of-agile-constraint-synergy-intent.md)
