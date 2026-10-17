---
title: "Inside the System Boundary"
type: "Source Summary"
description: "Compound AI systems generate component, composition, and interaction lift, and only the last two are defensible at renewal."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/inside-the-system-boundary/inside-the-system-boundary.md"
---

# Inside the System Boundary — Summary

**Original source**: `references/devlinliles.com/inside-the-system-boundary/inside-the-system-boundary.md`

## Summary

Since Berkeley AI Research argued that state-of-the-art results now come from compound systems rather than single models, the measurement problem has changed. A system-level A/B test tells you whether the whole pipeline beats a baseline, but not which components work, which are deadweight, and which harm results while looking fine on their own metrics. Liles argues for evaluating components inside the system boundary, and warns that Goodhart's law compounds faster when a proxy metric sits upstream of many interacting components.

## Key Claims

- Any compound system produces three simultaneous kinds of lift: component lift, composition lift (the orchestration layer), and interaction lift (proprietary architecture).
- Composition and interaction lift are far more defensible at renewal; component lift travels with the foundation model vendor.
- Four designs for isolating lift: ablation lift, shadow routing, specialist-isolation A/B, and critic-gated evaluation — each with a specific confound.
- Cascade contamination: a second-tier model only sees hard cases, so comparing tiers measures sample composition, not quality.
- Mitigation for compounding Goodhart: pair every leading metric with a lagging outcome metric and recalibrate at least quarterly.

## Relevance

Core to evaluating [compound AI systems](/concepts/compound-ai-systems.md) and to [Goodhart's law](/concepts/goodharts-law.md) in production; touches [model routing](/concepts/model-routing.md) and the [orchestration layer](/concepts/orchestration-layer.md).

## Quality

Practitioner blog post by Devlin Liles. Strong conceptual framing grounded in cited research (Zaharia/Khattab et al. 2024; arXiv Goodhart formalizations; EMNLP Findings 2025); abstract and lightly evidenced, with designs described rather than measured.

## Entities Mentioned

- None.

## Concepts Covered

- [Compound AI systems](/concepts/compound-ai-systems.md) — the measurement unit the post centers on
- [Goodhart's law](/concepts/goodharts-law.md) — how proxy metrics diverge faster across components
- [Model routing](/concepts/model-routing.md) — router value measured at the outcome layer
- [Orchestration layer](/concepts/orchestration-layer.md) — source of composition lift
