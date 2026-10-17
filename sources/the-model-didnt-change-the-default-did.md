---
title: "The Model Didn't Change. The Default Did."
type: "Source Summary"
description: "Anthropic's Claude Code regression lived in a moved product default; clients must pin parameters and run their own production eval suites."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-model-didnt-change-the-default-did/the-model-didnt-change-the-default-did.md"
---

# The Model Didn't Change. The Default Did. — Summary

**Original Source**: `references/devlinliles.com/the-model-didnt-change-the-default-did/the-model-didnt-change-the-default-did.md`

## Summary

[Anthropic](/entities/anthropic.md)'s April 23 postmortem never says the model got worse because it didn't: the regression lived in a moved default and two other changes, not the weights. The post reads the episode as a lesson in where failures hide. Reasoning effort is a parameter the API accepts directly, but [Claude Code](/entities/claude-code.md) chose a default and sent it on your behalf — so anyone on the product surface inherited whatever Anthropic decided that week, with no way to know it had changed. The remedy is to pin what you can and monitor what you can't.

## Key Claims

- On March 4 Anthropic changed Claude Code's default reasoning effort from high to medium to cut latency; the effort change ran for thirty-four days before the April 7 revert, and no explanation was published until April 23.
- Two other changes blurred the signal: a caching bug (March 26) cleared reasoning history every turn, and a system-prompt length cap (April 16) later measured at three eval points.
- The API was never touched; the regression sat entirely in the product layer that picks a default — direct-API callers with an explicit effort value never saw it.
- Anthropic's own evals and telemetry failed to reproduce a live regression in its own flagship product for over a month, and its internal evals missed all three regressions on first pass.
- Fixes: pin parameters, then build a fixed, versioned suite of ~100 representative production tasks graded against a rubric and run on a schedule, tracking reasoning traces (chain-of-thought length, tool calls) before final answers.

## Relevance

Central to [version pinning](/concepts/version-pinning.md), [quiet drift](/concepts/quiet-drift.md), [model drift detection](/concepts/model-drift-detection.md), and [evaluation harness](/concepts/evaluation-harness.md).

## Quality

Practitioner blog post by Devlin Liles. Tightly grounded in Anthropic's own published postmortem with specific dates and figures; the proposed production suite and illustrative baseline chart are recommendations rather than demonstrated results.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — author of the postmortem and the moving default
- [Claude Code](/entities/claude-code.md) — the product whose default change caused the regression

## Concepts Covered

- [version pinning](/concepts/version-pinning.md) — set explicit parameters rather than accept vendor defaults
- [quiet drift](/concepts/quiet-drift.md) — silent behavioral change without a version bump
- [model drift detection](/concepts/model-drift-detection.md) — independent, scheduled evaluation to catch regressions
- [evaluation harness](/concepts/evaluation-harness.md) — a versioned production-workload suite with a locked baseline
