---
title: "Cost Observability in AI-Assisted Development: Understanding What Your Agents Spend"
type: "Source Summary"
description: "Argues AI token costs need per-task, per-role instrumentation to make agent spend legible and optimizable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/cost-observability-in-ai-assisted-development-understanding-what-your-agents/cost-observability-in-ai-assisted-development-understanding-what-your-agents.md"
---

# Cost Observability in AI-Assisted Development: Understanding What Your Agents Spend — Summary

**Original source**: `references/devlinliles.com/cost-observability-in-ai-assisted-development-understanding-what-your-agents/cost-observability-in-ai-assisted-development-understanding-what-your-agents.md`

## Summary

The post argues that AI token costs scale with context complexity more than output volume, making agent spend hard to predict and impossible to optimize without instrumentation. Provider dashboards show the total bill but not the per-task, per-role, and per-activity breakdown that enables meaningful decisions, so teams must build that measurement layer themselves.

## Key Claims

- A task reading 20 files of context consumes 10–20x the tokens of a narrow-scope task with similar output length.
- Running a large model on work a smaller one handles costs 4–10x more, depending on pricing tiers.
- Production cost distributions are skewed: a small fraction of large-context synthesis tasks dominates spend.
- Four dimensions are worth instrumenting: per-task, per-agent-role, per-model-tier, and per-activity-category cost.
- Session budgets double as diagnostics: consistent budget hits on comparable tasks signal underspecified tasks, over-broad context, or tier mismatch.
- Recommendations from cost data are evidence for evaluation, never automatic routing changes.

## Relevance

Informs [token cost](/concepts/token-cost.md) and [model selection](/concepts/model-selection.md), positioning cost observability as the prerequisite for empirical routing decisions.

## Quality

Practitioner blog post by Devlin Liles. Strength: a concrete instrumentation taxonomy tied to business outcomes. Caveat: relies on illustrative multipliers and an analogy to cloud rightsizing rather than measured datasets.

## Entities Mentioned

- None.

## Concepts Covered

- [token cost](/concepts/token-cost.md) — the spend behavior the post wants made visible
- [model selection](/concepts/model-selection.md) — the optimization cost observability enables
