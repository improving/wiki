---
title: "The Attribution Budget - Why Telemetry Never Answers Why"
type: "Source Summary"
description: "Complete telemetry answers what happened, not why; attribution must be built and budgeted as its own component."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/the-attribution-budget-why-telemetry-never-answers-why/the-attribution-budget-why-telemetry-never-answers-why.md"
---

# The Attribution Budget - Why Telemetry Never Answers Why — Summary

**Original source**: `references/devlinliles.com/the-attribution-budget-why-telemetry-never-answers-why/the-attribution-budget-why-telemetry-never-answers-why.md`

## Summary

Drawing on an agentic ETL-repair system he built, Liles argues that complete, well-structured telemetry answers what a trace is designed to answer (which node ran, with what inputs, in what order, at what cost) but does not compute a causal verdict about which node caused a downstream failure. He treated good telemetry as sufficient and was wrong: a patch that fixed one job caused a data-quality incident in another two days later. The fix was to build attribution as its own component, with its own data model, eval set, and budget line, consuming existing trace propagation and per-node scoring rather than reinventing them.

## Key Claims

- Across a ten-incident set with documented ground-truth causes, attribution coverage (a definitive cause within a capped review budget) landed under 50% even though the telemetry was genuinely complete.
- Rebuilt as a dedicated service, the same ten-incident set reached 90%+ coverage with mean time-to-attribution near-instant.
- The Who&When benchmark found frontier reasoning models and purpose-built attribution methods name the responsible agent only about 53.5% of the time and the responsible step only about 14.2%.
- The hardest cost is organizational: arguing for attribution as its own budget line before the first incident is harder than after.

## Relevance

Informs observability and failure-attribution practice, and treats [per-node scoring](/concepts/per-node-scoring.md) as a reusable building block; adjacent to the [three pillars of observability](/concepts/three-pillars-of-observability.md).

## Quality

Practitioner blog post by Devlin Liles. Strength: concrete ten-incident numbers paired with an external published benchmark; caveat: the headline 90% figure comes from a bounded, synthetic eval set with documented ground truth and may not generalize.

## Entities Mentioned

- None.

## Concepts Covered

- [Per-Node Scoring](/concepts/per-node-scoring.md) — reused as an input the attribution service consumes rather than rebuilds.
