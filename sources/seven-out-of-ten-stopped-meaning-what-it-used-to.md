---
title: "Seven Out of Ten Stopped Meaning What It Used To"
type: "Source Summary"
description: "Why an LLM judge's 7/10 auto-approve threshold broke after a silent model swap, and the calibration gate that fixes it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/seven-out-of-ten-stopped-meaning-what-it-used-to/seven-out-of-ten-stopped-meaning-what-it-used-to.md"
---

# Seven Out of Ten Stopped Meaning What It Used To — Summary

**Original source**: `references/devlinliles.com/seven-out-of-ten-stopped-meaning-what-it-used-to/seven-out-of-ten-stopped-meaning-what-it-used-to.md`

## Summary

A marketing-copy pipeline auto-approved AI copy whenever an LLM judge scored it 7/10 or higher, a threshold never checked against humans. Measured against 120 samples and five human raters, the judge's agreement was already mediocre (Cohen's kappa under 0.5); after a silent judge-model swap it worsened and misapproved copy passed 15% with no alert. The author's fix is a calibration pass plus a calibration gate, and he notes current practice recalibrates on a schedule because vendor swaps can be invisible.

## Key Claims

- The judge's agreement with human consensus was a Cohen's kappa under 0.5 before any model change.
- After an unannounced judge-model swap with no recalibration, misapproved copy climbed past 15% and nothing in the system detected it.
- The fix combines an isotonic-regression calibration mapping judge scores to human-consensus scores with a gate requiring kappa at or above 0.65 before any auto-approval.
- A new judge version never inherits the old version's calibration mapping, since a replacement may score on a different internal scale.
- Scheduled recalibration (the author settled on monthly for customer-facing auto-approval) is needed because a vendor can update a judge silently, making calibration drift a moving target.
- Calibration only ever matches its gold set: a calibrated judge can faithfully reproduce its raters' shared blind spots.

## Relevance

Informs [Model-as-judge](/concepts/model-as-judge.md) reliability, [Calibration](/concepts/calibration.md), [Golden Dataset](/concepts/golden-dataset.md) construction, and [Model Drift Detection](/concepts/model-drift-detection.md).

## Quality

Practitioner account by Devlin Liles built on a concrete pilot (120 samples, five raters). Figures come from one small, narrow panel and are illustrative rather than published research; the author flags the panel-size limitation directly.

## Entities Mentioned

- None.

## Concepts Covered

- [Model-as-judge](/concepts/model-as-judge.md) — the scoring component that failed
- [Calibration](/concepts/calibration.md) — the correction and gating mechanism
- [Golden Dataset](/concepts/golden-dataset.md) — the human-rated set calibration depends on
- [Model Drift Detection](/concepts/model-drift-detection.md) — silent judge swaps as a drift source
