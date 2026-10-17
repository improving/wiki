---
title: "Ten Days of Miscalibrated Sensors Before the Calendar Noticed"
type: "Source Summary"
description: "A firmware recalibration shifted sensor features and a fixed retrain calendar missed it for ten days; drift triggers plus champion-challenger gates fix it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/ten-days-of-miscalibrated-sensors-before-the-calendar-noticed/ten-days-of-miscalibrated-sensors-before-the-calendar-noticed.md"
---

# Ten Days of Miscalibrated Sensors Before the Calendar Noticed — Summary

**Original source**: `references/devlinliles.com/ten-days-of-miscalibrated-sensors-before-the-calendar-noticed/ten-days-of-miscalibrated-sensors-before-the-calendar-noticed.md`

## Summary

A predictive-maintenance model scored vibration and temperature from forty machines to predict failure seven days out. On day twenty a firmware update recalibrated the vibration sensors, shifting the feature distribution without changing what normal vibration meant physically, and the model misread every reading afterward. Retraining on a fixed monthly schedule left a ten-day blind spot and redeployed automatically without validating against the previous model.

## Key Claims

- A fixed calendar cannot distinguish "nothing changed, retrain anyway" from "something changed ten days ago, retrain now."
- The fix composes two existing mechanisms: a daily Population Stability Index drift check triggers retraining on demand, and a champion-versus-challenger holdout comparison gates promotion.
- Days-to-remediation came in under ten, against the ten-day gap the fixed schedule leaves open by construction.
- Chip Huyen separates stateless (full) from stateful (fine-tune) retraining; a reported Grubhub case cut training cost by a factor of forty-five with stateful retraining.
- The drift threshold needs calibration: too sensitive chases noise, too loose recreates the calendar problem.
- Drift-triggered retraining does not fix closed-loop feedback contamination, where a model's own predictions corrupt future labels.

## Relevance

Informs observability and [model drift detection](/concepts/model-drift-detection.md), showing how [distribution shift](/concepts/distribution-shift.md) interacts with retraining triggers and promotion gates.

## Quality

Practitioner blog post by Devlin Liles. First-person, concrete scenario with a described fix; the reported improvement is a single-case account, and the author is candid about what the pattern does not cover.

## Entities Mentioned

- None.

## Concepts Covered

- [Model Drift Detection](/concepts/model-drift-detection.md) — drift-triggered retraining
- [Distribution shift](/concepts/distribution-shift.md) — the sensor recalibration
