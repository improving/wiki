---
title: "Unidirectional Quality Gates in AI-Assisted Development: The Ratchet Pattern"
type: "Source Summary"
description: "Proposes enforcing quality metrics as monotonically non-decreasing floors to stop invisible AI-accelerated drift."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern.md"
---

# Unidirectional Quality Gates in AI-Assisted Development: The Ratchet Pattern — Summary

**Original source**: `references/devlinliles.com/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern.md`

## Summary

Liles observes that quality regression in AI-assisted development is gradual and invisible — coverage drifting down, lint warnings accumulating, type errors reappearing — and that parallel AI agents compress a quarter's drift into two weeks. His remedy is the "ratchet pattern": quality metrics are enforced to be monotonically non-decreasing, with a checked-in floor file that blocks any merge lowering a measured metric. The post covers the mechanism, a pre-session constraint layer, calibration, audit value, and limitations.

## Key Claims

- Ratchet state lives in a checked-in file recording the current floor for each metric (branch coverage, lint violations, type-check errors, import-boundary violations); it is updated on improvement and never downward.
- Before every merge, the pipeline measures the incoming change against each floor and blocks any regression with an explicit report of which metric fell and by how much.
- The approach needs no human reviewer to notice a drop, no remembered team norm, and no per-PR configuration.
- A pre-session layer checks structural constraints (import boundaries, type exports, dependency direction) before an agent writes any code.
- Calibrate the initial floor by measuring the current state; support per-directory or per-module floors for legacy, generated, or experimental code.
- Limitations: hard-to-quantify qualities (clarity, architectural coherence, API design) are not covered; intentional regressions need manual floor updates with explanatory commits; Goodhart's law applies to whatever is measured.

## Relevance

Implements [quality gates](/concepts/quality-gates.md) for AI-assisted delivery and explicitly invokes [Goodhart's law](/concepts/goodharts-law.md); its per-module floors are a response to [technical debt](/concepts/technical-debt.md).

## Quality

Practitioner post by Devlin Liles. Concrete mechanism and honest tradeoff section; it is a design proposal with illustrative reasoning rather than measured results.

## Entities Mentioned

- None.

## Concepts Covered

- [quality gates](/concepts/quality-gates.md) — the ratchet as a specific gate design
- [Goodhart's law](/concepts/goodharts-law.md) — the caveat that a measure targeted stops being a good measure
- [technical debt](/concepts/technical-debt.md) — acknowledged debt in legacy and experimental modules handled via per-module floors

## Related Sources

- [Proving Competency at Every Stage: The Eight Stages of AI Maturity](/sources/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity.md)
- [Quality Gates at Every Transition - Stopping a Bad Value Before It Becomes the Next Step's Input](/sources/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md)
