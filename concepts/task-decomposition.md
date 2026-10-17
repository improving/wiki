---
title: "Task Decomposition"
type: "Concept"
description: "Breaking agent work into shorter, gated steps to counter compounding error and stale world state."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agent-reliability, orchestration, architecture]
sources:
  - "/sources/ai-agents-dont-know-what-changed-thats-a-1969-problem.md"
  - "/sources/the-compounding-tax-why-small-model-errors-become-large-system-failures.md"
  - "/sources/your-agent-is-probably-less-reliable-than-you-think.md"
---

# Task Decomposition

Task decomposition is the practice of breaking agent work into shorter, independently verified steps so that errors cannot compound across a long autonomous chain. Across this corpus it is the architectural answer to two failure modes: autoregressive error accumulation and silent operation on stale world state.

## Key Claims

- The 1969 frame problem explains why production agents fail silently, operating on stale world state; 65% of enterprise AI failures trace to [context drift](/concepts/context-drift.md) or memory loss.
- Verification steps act as frame-reset operations before consequential actions, making explicit state management a first-class architectural component.
- Per-step accuracy compounds catastrophically over long horizons; decomposition, grounding, verification, [checkpointing](/concepts/checkpointing.md), and observability bend the curve.
- Adversarial inspector agents break error chains without raising per-step accuracy, because errors left in context recruit the model to defend them.
- Single-turn benchmarks hide compounding because they measure per-step accuracy rather than end-to-end outcomes.

## Related

- [context drift](/concepts/context-drift.md) — the stale-state failure decomposition mitigates
- [Compounding error](/concepts/compounding-error.md) — why long horizons fail
- [checkpointing](/concepts/checkpointing.md) — a decomposition tactic
- [Stacking Errors](/concepts/stacking-errors.md) — the reliability math behind shorter pipelines
- [The Compounding Tax: Why Small Model Errors Become Large System Failures](/sources/the-compounding-tax-why-small-model-errors-become-large-system-failures.md) — primary source
