---
title: "AI Pipeline Reliability Governance for Multi-Step Accuracy Failures"
type: "Source Summary"
description: "Per-step accuracy multiplies across a pipeline, so long agent chains need quality gates rather than better models."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, reliability, improving.com]
sources:
  - "references/improving.com/ai-pipeline-reliability-governance/ai-pipeline-reliability-governance.md"
---

# AI Pipeline Reliability Governance for Multi-Step Accuracy Failures — Summary

**Original source**: `references/improving.com/ai-pipeline-reliability-governance/ai-pipeline-reliability-governance.md`

## Summary

Devlin Liles argues that per-step accuracy multiplies rather than averages across a pipeline, so a ten-step chain at 95% per step is only about 60% reliable end to end and a twenty-step chain about 36%. The fix is a real quality gate at each transition, not a better model, because the failures are architectural rather than capability gaps.

## Key Claims

- Accuracy multiplies down a chain (0.95^10 ≈ 0.60; 0.95^20 ≈ 0.36), which is Lusser's law, first diagnosed for 1940s German rocket programs.
- Improving built a contract-extraction pipeline for a one-person general counsel's office; a rolling comparison of production vs. test output caught a model upgrade silently failing four of eighteen risk constraints.
- Teams typically chase a better model: lifting per-step accuracy from 95% to 97% moves ten-step reliability only to about 74%, leaving the compounding structure untouched.
- As programs mature from task agents to workflow agents to agent teams, chaining more steps cuts reliability — the "autonomy paradox": the most autonomous-looking pipelines are often least trustworthy.
- Once workflows cross team and vendor boundaries, nobody owns the full chain, so stacking errors become an organizational visibility problem.
- Two objections are answered: steps aren't fully independent but the curve's shape holds, and a verifier model or self-consistency check *is* a quality gate, so the case is for checking machinery, not committees.

## Relevance

The central argument for [quality gates](/concepts/quality-gates.md) between steps, explained by [Lusser's law](/concepts/lussers-law.md) and [stacking errors](/concepts/stacking-errors.md). It connects to [compounding error](/concepts/compounding-error.md) and [end-to-end success rate](/concepts/end-to-end-success-rate.md).

## Quality

Practitioner essay by Improving's Devlin Liles; clear reliability math and honest treatment of objections, with a self-interested nudge toward Improving assessments.

## Entities Mentioned

- [Robert Lusser](/entities/robert-lusser.md) — originator of the series-reliability law
- [Lakeshore Learning](/entities/lakeshore-learning.md) — three-step pipeline case study
- [Devlin Liles](/entities/devlin-liles.md) — author
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [quality gates](/concepts/quality-gates.md) — the main prescription
- [Lusser's law](/concepts/lussers-law.md) — the reliability math
- [stacking errors](/concepts/stacking-errors.md) — errors multiplying across steps
- [compounding error](/concepts/compounding-error.md) — the same effect over long horizons
- [end-to-end success rate](/concepts/end-to-end-success-rate.md) — the number that ships
- [error propagation](/concepts/error-propagation.md) — a bad value flowing downstream
- [AI governance](/concepts/ai-governance.md) — the broader control context
