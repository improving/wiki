---
title: "Per-Node Scoring"
type: "Concept"
description: "Grading each agent step locally at handoff, which cannot see forward in time and so misses delayed causal faults."
created: '2026-10-17'
updated: '2026-10-17'
tags: [attribution, observability, agents]
sources:
  - "/sources/the-attribution-budget-why-telemetry-never-answers-why.md"
  - "/sources/the-backward-rerun-attribution-for-a-failure-three-weeks-late.md"
---

# Per-Node Scoring

Per-node scoring grades each step of an agent chain locally, at the moment of handoff, based on what is visible there. It is the default attribution approach in most pipelines, and this corpus argues it is fundamentally limited: a step can score well and still be the true cause of a failure that only surfaces weeks later.

## Key Claims

- Per-node scores grade only what is visible at the moment of handoff, so they cannot see forward in time.
- Pointwise attribution cannot distinguish jointly necessary causes from alternative singleton causes.
- A day-twelve cost-optimal supplier choice caused a day-thirty-four stockout — invisible to per-node scoring.
- Counterfactual replay from checkpoints raised delayed-cause identification from 0% to 80%.
- Complete telemetry spans answer what happened, not why; attribution coverage stayed under 50% on ten documented incidents despite complete telemetry.
- Attribution needs its own data model, eval set, and budget line item; the Who&When benchmark shows best methods name the responsible agent only 53.5% of the time and the step 14.2%.

## Related

- [Causal Lineage Map](/concepts/causal-lineage-map.md) — the forward-and-backward model scoring lacks
- [checkpointing](/concepts/checkpointing.md) — enables counterfactual replay
- [Runtime Lineage](/concepts/runtime-lineage.md) — the trace that feeds attribution
- [Compounding error](/concepts/compounding-error.md) — why local scores mislead across steps
- [The Attribution Budget - Why Telemetry Never Answers Why](/sources/the-attribution-budget-why-telemetry-never-answers-why.md) — primary source
- [The Backward Rerun - Attribution for a Failure Three Weeks Late](/sources/the-backward-rerun-attribution-for-a-failure-three-weeks-late.md) — primary source
