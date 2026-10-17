---
title: "The Accuracy Number That Was True Once"
type: "Source Summary"
description: "A one-time 91% launch eval hid a 15-point decline from corpus churn and query drift; continuous re-scoring with drift alerts caught it in 30 days."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-accuracy-number-that-was-true-once/the-accuracy-number-that-was-true-once.md"
---

# The Accuracy Number That Was True Once — Summary

**Original source**: `references/devlinliles.com/the-accuracy-number-that-was-true-once/the-accuracy-number-that-was-true-once.md`

## Summary

A knowledge-base Q&A agent launched with a one-time 91% accuracy score that nobody re-measured; ninety days later, with six policy-corpus updates and drifted employee queries, real accuracy had fallen at least fifteen points while stale superseded chunks kept getting cited. The fix replaces the launch eval with a runner that re-scores on a fixed cadence (every ten days here), re-anchoring a held-out question set to live policy chunks and sampling realistic production queries, with a drift alert against a rolling baseline.

## Key Claims

- A launch-day 91% figure was never re-run; real accuracy against current queries declined at least 15 points over ninety days.
- Continuous re-scoring combines two inputs: a held-out set re-anchored to currently live content, and a rolling sample of production-style queries.
- The drift alert caught the real decline within thirty simulated days, sixty days earlier than it would otherwise have surfaced.
- Model and prompt stayed pinned; the loop watches whether the world underneath an unchanged system has moved.
- Production 2026 practice: judge-based scoring on 5–10% of live traffic, cheap heuristics on all of it, and calibrated or human review on the 1–5% failing heuristics.

## Relevance

Informs [model drift detection](/concepts/model-drift-detection.md) and [evaluation harnesses](/concepts/evaluation-harness.md), with a [golden dataset](/concepts/golden-dataset.md) as the re-anchored question set.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a concrete drift scenario with a clear cadence fix and honest treatment of label-source bias. Caveats: figures come from a ninety-day simulation.

## Entities Mentioned

- None.

## Concepts Covered

- [Model Drift Detection](/concepts/model-drift-detection.md) — accuracy as a live trend, with a drift alert against a rolling baseline
- [evaluation harness](/concepts/evaluation-harness.md) — a runner that re-scores on a fixed cadence
- [Golden Dataset](/concepts/golden-dataset.md) — the held-out question set re-anchored to live content
