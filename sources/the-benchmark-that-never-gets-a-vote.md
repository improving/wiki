---
title: "The Benchmark That Never Gets a Vote"
type: "Source Summary"
description: "Certifying a model on a public benchmark misses the real task distribution; only a stratified internal set should gate releases."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-benchmark-that-never-gets-a-vote/the-benchmark-that-never-gets-a-vote.md"
---

# The Benchmark That Never Gets a Vote — Summary

**Original source**: `references/devlinliles.com/the-benchmark-that-never-gets-a-vote/the-benchmark-that-never-gets-a-vote.md`

## Summary

A team picking a model for support-ticket triage certified it on a generic public text-classification benchmark and topped the chart in an afternoon. Liles built the set that actually mattered — 150 tickets sampled from the company's own queue, weighted to its real category mix — and ran the winning model against both. Public accuracy was above 85%; accuracy on the company's own distribution was under 65%. The fix is not a better model but a change in which measurement decides: the stratified internal set becomes the only gating metric, while the public benchmark is logged beside it, badged reference only.

## Key Claims

- No one lied: the public score was real, and it still failed to answer whether the model sorts this company's tickets reliably.
- The internal set must be built by a documented, stratified procedure matching the organization's actual task-category frequencies.
- An internal set inherits a staleness risk on a clock the organization controls; a documented refresh cadence is part of the pattern.
- Stratification is a judgment call about which dimensions matter — a bad choice (e.g. ignoring ticket length) leaves the rigor cosmetic.

## Relevance

Core to [benchmark validity](/concepts/benchmark-validity.md) and eval practice; it treats the internal set as a [golden dataset](/concepts/golden-dataset.md) subject to [distribution shift](/concepts/distribution-shift.md) and applies to [model selection](/concepts/model-selection.md).

## Quality

Practitioner blog post by Devlin Liles. Strength: a concrete, quantified gap between two eval sets with an honest "nobody lied" framing; caveat: single-case example and illustrative internal numbers.

## Entities Mentioned

- None.

## Concepts Covered

- [Benchmark Validity](/concepts/benchmark-validity.md) — a public score measuring a different question than production asks.
- [Golden Dataset](/concepts/golden-dataset.md) — the documented internal set that gates releases.
- [Distribution shift](/concepts/distribution-shift.md) — the ticket mix drifting from what the set was stratified against.
- [Model selection](/concepts/model-selection.md) — choosing a model against the measurement that actually decides.
