---
title: "Compounding error"
type: "Concept"
description: "How small per-step model errors multiply across long horizons, making end-to-end success a function of run length."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, agents, mathematics]
sources:
  - "/sources/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift.md"
  - "/sources/the-compounding-tax-why-small-model-errors-become-large-system-failures.md"
  - "/sources/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai.md"
---

# Compounding error

Compounding error is the tendency of small, tolerable per-step model mistakes to multiply into large system failures over long horizons. Across this corpus it reframes reliability: end-to-end success at production length, not per-step accuracy, is the metric that matters, so systems must be engineered — through decomposition, grounding, verification, and checkpoints — to survive imperfect AI.

## Key Claims

- A 99% per-step model succeeds end to end only 37% of the time across a hundred steps; a 1% per-step error rate compounds to failures in most hundred-step runs.
- Autoregressive error accumulation and agentic loop drift drive the effect, which single-turn benchmarks hide because they measure per-step accuracy.
- Reliability degrades with run length regardless of per-step accuracy, so [Lusser's Law](/concepts/lussers-law.md) and [error propagation](/concepts/error-propagation.md) describe the same arithmetic.
- Breaking long runs into short bounded stages with explicit checkpoints catches errors before they compound; draw stage boundaries where unwinding a downstream decision becomes expensive.
- [Checkpointing](/concepts/checkpointing.md), re-grounding in verified data, [task decomposition](/concepts/task-decomposition.md), and observability bend the curve.
- Autonomy should be granted only where mistakes are cheap and reversible, with explicit ownership at each stage.

## Related

- [checkpointing](/concepts/checkpointing.md) — bounding error by stage
- [error propagation](/concepts/error-propagation.md) — how a bad value spreads
- [Lusser's Law](/concepts/lussers-law.md) — the underlying arithmetic
- [The Compounding Tax](/sources/the-compounding-tax-why-small-model-errors-become-large-system-failures.md) — primary source
