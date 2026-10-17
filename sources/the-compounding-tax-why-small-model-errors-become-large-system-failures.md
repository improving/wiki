---
title: "The Compounding Tax: Why Small Model Errors Become Large System Failures"
type: "Source Summary"
description: "Per-step accuracy compounds across horizons, so trajectory reliability — not single-step benchmarks — is the metric that matters."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-compounding-tax-why-small-model-errors-become-large-system-failures/the-compounding-tax-why-small-model-errors-become-large-system-failures.md"
---

# The Compounding Tax — Summary

**Original source**: `references/devlinliles.com/the-compounding-tax-why-small-model-errors-become-large-system-failures/the-compounding-tax-why-small-model-errors-become-large-system-failures.md`

## Summary

A model that is right 99% of the time succeeds end to end only about 37% of the time across a hundred sequential steps, because error-free runs scale as `p^N`. The post separates two mechanisms: autoregressive error accumulation (exposure bias, where inference runs on the model's own flawed prefixes) and agentic loop drift (wrong actions corrupt the environment away from the agent's belief). Benchmarks hide this by measuring single-turn accuracy. Containment means shortening horizons, grounding, verifying between steps, and checkpointing.

## Key Claims

- At `p = 0.99`, ten steps give 90% end-to-end reliability, fifty give 61%, and a hundred drop to 37%; even `p = 0.999` collapses back to 37% at a thousand steps.
- Errors are correlated in practice, so `p^N` is the optimistic bound — one confidently wrong premise poisons every downstream inference.
- Exposure bias: models train on ground-truth prefixes but infer on their own generated prefixes, and they show no internal signal that they have left the training distribution.
- In agents, a slightly wrong action mutates the environment into a state that no longer matches the agent's mental model, and the divergence grows without a correction mechanism.
- A demo that looks like 98% per-step accuracy can behave like 94% in the wild, turning a fifty-step task into 36% versus 5% end-to-end.

## Relevance

Foundational for [compounding error](/concepts/compounding-error.md) and [error propagation](/concepts/error-propagation.md); the fixes map to [task decomposition](/concepts/task-decomposition.md), [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md), [checkpointing](/concepts/checkpointing.md), and [human-in-the-loop](/concepts/human-in-the-loop.md) placement.

## Quality

Practitioner blog post by Devlin Liles. Clear, well-structured arithmetic and a useful taxonomy; the numeric examples are illustrative and the independence assumption is explicitly flagged as optimistic.

## Entities Mentioned

- None.

## Concepts Covered

- [compounding error](/concepts/compounding-error.md) — the core `p^N` failure mode
- [error propagation](/concepts/error-propagation.md) — correlated errors and drift through a trajectory
- [task decomposition](/concepts/task-decomposition.md) — shortening the effective horizon
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — grounding each step against external truth
- [checkpointing](/concepts/checkpointing.md) — persisting state so a derailed run can roll back
- [human-in-the-loop](/concepts/human-in-the-loop.md) — routing high-consequence steps through review
