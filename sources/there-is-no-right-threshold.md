---
title: "There Is No Right Threshold"
type: "Source Summary"
description: "Classifier thresholds are unresolvable value judgments, so they need explicit ownership, monitoring, and context awareness."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/there-is-no-right-threshold/there-is-no-right-threshold.md"
---

# There Is No Right Threshold — Summary

**Original source**: `references/devlinliles.com/there-is-no-right-threshold/there-is-no-right-threshold.md`

## Summary

Devlin Liles argues that every deployed binary classifier hides an unresolved philosophical decision: at what score does a transaction become fraud, a message hate speech, a scan positive? He connects this to the 2,400-year-old Sorites Paradox, showing that vague categories have no sharp edges in the world, so any threshold is a value judgment about which errors to prefer, not a technical finding. Tuning on a validation set only pushes the paradox one level up. He draws three governance consequences from this.

## Key Claims

- Moving a spam filter threshold from 0.1 to 0.9 trades precision for recall; no threshold "solves" the classification problem.
- A 2024 NeurIPS paper on out-of-distribution detection found the same problem in marginal OOD samples and built the IS-OOD benchmark to expose the gradient structure.
- Thresholds carry moral character and require explicit ownership; a fraud threshold at 0.6 versus 0.7 is a live policy choice the compliance team should own, with the model team surfacing it.
- Thresholds are parameters to monitor, not constants — input distribution drift reshapes the vague region, so threshold monitoring belongs alongside data drift monitoring in MLOps.
- The right threshold is often context-dependent; a model between business banking and consumer credit may need different thresholds even with identical scores.

## Relevance

Informs [confidence thresholds](/concepts/confidence-thresholds.md) and connects to [Model Drift Detection](/concepts/model-drift-detection.md) for threshold monitoring.

## Quality

Practitioner blog post by Devlin Liles. Clear and well-argued, bridging philosophy and MLOps; the governance prescriptions are reasoned opinion rather than tested practice.

## Entities Mentioned

- None.

## Concepts Covered

- [Confidence Thresholds](/concepts/confidence-thresholds.md) — the production threshold as an owned policy choice
- [Model Drift Detection](/concepts/model-drift-detection.md) — threshold monitoring as part of drift practice
- [Calibration](/concepts/calibration.md) — the score-to-decision relationship the threshold governs
