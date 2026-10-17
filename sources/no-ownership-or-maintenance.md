---
title: "Top 10 Reasons AI Projects Fail #8: No Ownership or Maintenance"
type: "Source Summary"
description: "Argues AI models are living systems that decay without ownership, MLOps, telemetry, and SLAs, and prescribes lifecycle practices to sustain them."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, data, improving.com]
sources:
  - "references/improving.com/no-ownership-or-maintenance/no-ownership-or-maintenance.md"
---

# Top 10 Reasons AI Projects Fail #8: No Ownership or Maintenance — Summary

**Original source**: `references/improving.com/no-ownership-or-maintenance/no-ownership-or-maintenance.md`

## Summary

Devlin Liles argues that AI systems are living entities that require ongoing care, and treating them like static software guarantees decline. When data, regulations, or user behavior shift, an unmaintained model loses accuracy and trust, and adoption quietly dies. The failure comes from structure rather than laziness — unclear accountability, no lifecycle plan, hidden decay, and operational blind spots — and the remedy is disciplined ownership, monitoring, and refresh rhythms.

## Key Claims

- Most teams assume a model that works in testing will keep working, but data patterns, user intent, third-party tools, and processes keep changing.
- Without monitoring, feedback loops, and ownership, decay goes unnoticed until the system is no longer trusted and adoption drops.
- Four structural causes: unclear accountability, no lifecycle plan, hidden decay (metrics focus on initial accuracy), and operational blind spots (no SLAs, telemetry, or review cadences).
- Prevention starts with assigning a Product Owner accountable for business value, performance, and lifecycle decisions.
- Define an MLOps or GenAIOps framework from day one, including drift detection, feedback loops, prompt evaluation, and refresh cycles.
- Track telemetry and health metrics — accuracy, latency, and confidence scores — with alerts when thresholds decline.
- Publish SLAs for uptime, retraining frequency, and data freshness, and list every deployed model's dependencies, cadence, and owner on an internal AI Services page.
- One Improving client's policy Q&A bot used monthly prompt-pack refreshes and quarterly drift evaluations against gold questions, preventing confidence erosion in an HR system.

## Relevance

Directly informs [model drift detection](/concepts/model-drift-detection.md) and [AI monitoring](/concepts/ai-monitoring.md), with [prompt evaluation](/concepts/prompt-evaluation.md) and [data ownership](/concepts/data-ownership.md) as supporting practices.

## Quality

Series installment by Devlin Liles; practical and prescriptive, though largely anecdotal and promotional.

## Entities Mentioned

- [Improving](/entities/improving.md) — publisher
- [Devlin Liles](/entities/devlin-liles.md) — author

## Concepts Covered

- [model drift detection](/concepts/model-drift-detection.md) — monitoring for behavior change
- [AI monitoring](/concepts/ai-monitoring.md) — telemetry for accuracy and latency
- [prompt evaluation](/concepts/prompt-evaluation.md) — monthly prompt-pack refreshes
- [data ownership](/concepts/data-ownership.md) — named accountability for models
- [service level objective](/concepts/service-level-objective.md) — SLAs for retraining and freshness
