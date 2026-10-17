---
title: "Short, Bounded Pipelines - Trading a Seamless Run for a Shorter Leash on Drift"
type: "Source Summary"
description: "Break long agent runs into short stages ending in real checkpoints, so errors are caught before they compound downstream."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift.md"
---

# Short, Bounded Pipelines - Trading a Seamless Run for a Shorter Leash on Drift — Summary

**Original source**: `references/devlinliles.com/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift.md`

## Summary

Using a travel-planning agent run against twenty seeded trip requests, the post argues that a single uninterrupted chain of seven or eight steps is [compounding error](/concepts/compounding-error.md) dressed up as autonomy. A small misread near the start (dates off by a day, a budget in the wrong currency) goes unchecked until final reconciliation, by which point fixing it means unwinding four or five downstream choices. The fix is to break the run into short stages, each ending in a real [checkpoint](/concepts/checkpointing.md) that passes state explicitly before the next stage may start.

## Key Claims

- Every step looks reasonable in isolation; the problem appears early and is discovered late, once an early error has become load-bearing.
- Four bounded stages (confirm preferences/dates/budget; search flights and hotel; car and activities; final reconciliation) cut how far drift travels before inspection.
- Reliability degrades as a smooth function of run length, and long runs fall into repetitive loops rather than failing cleanly at one identifiable step.
- The pattern narrows the blast radius but does not fix within-stage accuracy; four bounded stages of two steps each still compound internally.
- Draw the boundary where the cost of discovering a mistake jumps; "a bigger model can still drift over twenty uninterrupted steps — it just drifts more competently."

## Relevance

Informs [checkpointing](/concepts/checkpointing.md), [compounding error](/concepts/compounding-error.md), and agent working-memory limits in agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. Grounded in a stated twenty-request experiment, but reports no raw numbers, only the qualitative direction of the result; the reliability-vs-length finding is cited rather than shown.

## Entities Mentioned

- None.

## Concepts Covered

- [checkpointing](/concepts/checkpointing.md) — the stage boundary that inspects explicit, passed state before the next stage runs.
- [Compounding error](/concepts/compounding-error.md) — the central failure mode of one long unchecked chain.
- [Working Memory](/concepts/working-memory.md) — long uninterrupted runs lose track of the original objective and loop.
