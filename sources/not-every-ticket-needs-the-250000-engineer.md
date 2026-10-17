---
title: "Not Every Ticket Needs the $250,000 Engineer"
type: "Source Summary"
description: "Route AI work by capability and cost per solved task, the way leaders staff people, instead of defaulting every request to the flagship model."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/not-every-ticket-needs-the-250000-engineer/not-every-ticket-needs-the-250000-engineer.md"
---

# Not Every Ticket Needs the $250,000 Engineer — Summary

**Original source**: `references/devlinliles.com/not-every-ticket-needs-the-250000-engineer/not-every-ticket-needs-the-250000-engineer.md`

## Summary

Leaders staff human work by the seniority a ticket actually requires, then abandon that discipline for AI and default every request to the most capable model. The post prices model tiers as seniority bands using mid-2026 numbers and argues the right unit is cost per solved task across a full harness, not benchmark score or token price alone. It adds [time horizon](/concepts/time-horizon.md) as the dimension that decides which tier can carry a long task, and concludes [model routing](/concepts/model-routing.md) is a staffing decision.

## Key Claims

- On [SWE-bench](/entities/swe-bench.md) Verified (June 2026), [Claude Fable 5](/entities/claude-fable-5.md) scores 95.0% at $50/M output; [Opus 4.8](/entities/claude-opus-4-8.md) 88.6% at $25; [Sonnet 4.6](/entities/claude-sonnet-4-6.md) 79.6% at $15; open-weights near 80.5% at $1.20.
- Cost per solved task, with retries and a measured cache mix, is $5.25 (Sonnet), $7.86 (Opus), $14.66 (Fable) against an $89 loaded senior hour.
- [METR](/entities/metr.md)'s 50% time horizon grew from 59 minutes (Feb 2025) to 16+ hours (May 2026), doubling about every 4.3 months.
- Two teams with identical-looking days billed $12,000 vs $338,000 per developer a year, a 28x spread driven by workload shape and parallelism.
- At 50% reliability a model finishes half its long tasks, and SWE-bench scores are vendor-reported on a contested benchmark.

## Relevance

Central to AI economics: it prices model tiers as hiring bands, tying [model routing](/concepts/model-routing.md) to [time horizon](/concepts/time-horizon.md) and [token cost](/concepts/token-cost.md).

## Quality

Practitioner blog post by Devlin Liles. Unusually detailed bottom-up cost math with stated assumptions; figures depend on a self-measured cache mix and vendor-reported benchmarks.

## Entities Mentioned

- [SWE-bench](/entities/swe-bench.md) — benchmark used to order model tiers
- [METR](/entities/metr.md) — source of the time-horizon metric
- [Claude Fable 5](/entities/claude-fable-5.md) — frontier tier, 95.0% at $50/M output
- [Claude Opus 4.8](/entities/claude-opus-4-8.md) — senior tier
- [Claude Sonnet 4.6](/entities/claude-sonnet-4-6.md) — mid tier, cheapest solved task

## Concepts Covered

- [model routing](/concepts/model-routing.md) — matching capability and price to each ticket
- [time horizon](/concepts/time-horizon.md) — the longest task a tier can actually carry
- [token cost](/concepts/token-cost.md) — the pricing input behind cost per solved task

## Related Sources

- [Checking the Math on the $500 Million AI Spend Story](/sources/checking-the-math-on-the-500-million-ai-spend-story.md)
- [Cost-Adjusted Capacity: When Tokens Stop Converting to Mergeable PRs](/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md)
