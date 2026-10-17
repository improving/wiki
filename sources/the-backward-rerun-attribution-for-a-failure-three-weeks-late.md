---
title: "The Backward Rerun - Attribution for a Failure Three Weeks Late"
type: "Source Summary"
description: "Per-node scores are snapshots that miss delayed failures; causal replay with checkpointing identifies the true node retroactively."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/the-backward-rerun-attribution-for-a-failure-three-weeks-late/the-backward-rerun-attribution-for-a-failure-three-weeks-late.md"
---

# The Backward Rerun - Attribution for a Failure Three Weeks Late — Summary

**Original source**: `references/devlinliles.com/the-backward-rerun-attribution-for-a-failure-three-weeks-late/the-backward-rerun-attribution-for-a-failure-three-weeks-late.md`

## Summary

In a three-agent inventory-reordering chain run over a sixty-day simulation, the supplier-selection agent chose a cheaper supplier with a longer lead time on day twelve. Every node scored well at the moment it acted, yet the longer lead time caused a stockout on day thirty-four. Because the pipeline never re-examined an earlier decision once a delayed failure appeared, the true causal node was named zero percent of the time across ten scenarios. Liles' fix is causal replay: when an outcome is flagged, re-execute the chain backward from checkpointed states, substituting or removing candidate nodes, and rank candidates by how much each swap changes the outcome.

## Key Claims

- A per-node score is a snapshot that cannot see forward in time; "correct by the standard available in the moment" and "actually the cause of a downstream failure" are different claims.
- Backward causal replay with checkpointing raised delayed-cause identification to 80%+ across the same ten scenarios, against a zero percent baseline.
- He logs a `replay_compute_cost` metric — the number of counterfactual re-runs needed to converge — on the same dashboard as the benefit.
- The pattern tests candidates one at a time, so it cannot distinguish a jointly necessary cause from an alternative singleton cause; that gap is unfixed.

## Relevance

Extends [per-node scoring](/concepts/per-node-scoring.md) by pairing it with [checkpointing](/concepts/checkpointing.md) for retrospective attribution in observability and agentic-delivery work.

## Quality

Practitioner blog post by Devlin Liles. Strength: explicit numbers plus a named cost metric and a candid statement of the pattern's formal limitation; caveat: results come from a bounded sixty-day simulation with documented ground truth.

## Entities Mentioned

- None.

## Concepts Covered

- [Per-Node Scoring](/concepts/per-node-scoring.md) — the snapshot grading the post argues is insufficient on its own.
- [Checkpointing](/concepts/checkpointing.md) — state captured at every node-day enables the backward replay.
