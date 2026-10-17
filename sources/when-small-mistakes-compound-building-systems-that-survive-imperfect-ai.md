---
title: "When Small Mistakes Compound: Building Systems That Survive Imperfect AI"
type: "Source Summary"
description: "Small AI errors compound across long workflows, so systems need selective autonomy, checkpoints, grounding, ownership, and end-to-end success metrics."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai.md"
---

# When Small Mistakes Compound: Building Systems That Survive Imperfect AI — Summary

**Original source**: `references/devlinliles.com/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai.md`

## Summary

The post argues that because every AI system errs, the differentiator is what happens to a small error once made. In multi-step processes each output feeds the next, so a 1 percent per-step error rate produces a compounded error in roughly two of five fifty-step runs. The author frames this as a leadership problem — deciding where autonomy is acceptable, inserting [quality gates](/concepts/quality-gates.md), grounding against external reality, and assigning explicit human ownership — rather than a model-quality problem.

## Key Claims

- A 1 percent per-step error rate yields ~40 percent of 50-step runs with a compounded error, and a majority at 100 steps; a 98 percent per-step tool is closer to 36 percent reliable across 50 steps.
- Autonomy belongs where errors are cheap and reversible; expensive or irreversible steps need a [human in the loop](/concepts/human-in-the-loop.md) positioned at the decision, not rubber-stamping a batch.
- Break long processes into checked segments ([checkpointing](/concepts/checkpointing.md)) so errors are caught near their origin, and re-ground the system against authoritative data regularly.
- Measure [end-to-end success rate](/concepts/end-to-end-success-rate.md) at production length and watch the decay curve, not isolated-step accuracy.
- Accountability without visibility, a stop button, and an escalation path is a name on an org chart, not governance.

## Relevance

A governance playbook for deploying AI into long processes, connecting [compounding error](/concepts/compounding-error.md), [Lusser's Law](/concepts/lussers-law.md), and [human-in-the-loop](/concepts/human-in-the-loop.md) design.

## Quality

Practitioner blog post by Devlin Liles. Clear, well-argued leadership framing with concrete arithmetic; illustrative examples are hypothetical rather than from named deployments.

## Entities Mentioned

- None.

## Concepts Covered

- [Compounding error](/concepts/compounding-error.md) — the central risk the post defines
- [human-in-the-loop](/concepts/human-in-the-loop.md) — placement of human judgment on high-consequence steps
- [Quality Gates](/concepts/quality-gates.md) — checkpoints between process segments
- [Checkpointing](/concepts/checkpointing.md) — breaking processes into verified segments
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — the metric the post recommends
- [Lusser's Law](/concepts/lussers-law.md) — the arithmetic of per-step reliability decay

## Related Sources

- [From CI/CD to the Intelligence Operating System](/sources/from-ci-cd-to-the-intelligence-operating-system.md)
- [One Clause at a Time - Previewing Every Edit Before It Commits](/sources/one-clause-at-a-time-previewing-every-edit-before-it-commits.md)
- [The 8-Stage AI Trust Evolution: A Map for the Journey](/sources/the-8-stage-ai-trust-evolution-a-map-for-the-journey.md)
