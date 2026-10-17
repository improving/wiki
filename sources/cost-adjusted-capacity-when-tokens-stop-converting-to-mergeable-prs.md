---
title: "Cost-Adjusted Capacity: When Tokens Stop Converting to Mergeable PRs"
type: "Source Summary"
description: "Models when extra AI token spend stops producing mergeable PRs, arguing verification beats capability upgrades."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
---

# Cost-Adjusted Capacity: When Tokens Stop Converting to Mergeable PRs — Summary

**Original source**: `references/devlinliles.com/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md`

## Summary

The post builds a cost-adjusted capacity model that joins METR's task-completion time horizons with frontier pricing to locate the point where more token spend stops converting into mergeable pull requests. It argues most AI coding budgets optimize the wrong variable — model tier and token volume — when the real constraint is the gap between passing tests and being mergeable.

## Key Claims

- METR's 50% time horizons have doubled roughly every 7 months since 2019, accelerating to ~4.3 months since 2023 (Claude 3.7 Sonnet ~59 min, GPT-5 ~137 min, Opus 4.5 ~320 min).
- METR found none of 15 reviewed PRs from Claude 3.7 Sonnet were mergeable as-is; fixing them averaged 42 minutes, ~a third of total PR time.
- Sonnet 4.5's grader horizon was ~50 minutes versus ~8 minutes by maintainers — a 6.25x overstatement (mergeability factor D = 6.25).
- Token spend is only 6–11% of the cost of a mergeable PR; the verification tax is everything else.
- Halving the verification fraction buys ~46% more mergeable throughput versus ~2.0% from doubling the horizon — better than 20:1 in favor of fixing the system.

## Relevance

Informs [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md), [time horizon](/concepts/time-horizon.md), the [verification tax](/concepts/verification-tax.md), and [model routing](/concepts/model-routing.md) under an [AI economics](/concepts/token-cost.md) lens.

## Quality

Practitioner blog post by Devlin Liles. Strength: fully stated math with sourced constants and reproducible derivations. Caveat: the conclusion depends on a small number of METR datasets and stated pricing conventions that will drift over time.

## Entities Mentioned

- [METR](/entities/metr.md) — source of the time-horizon and holistic-evaluation datasets
- [SWE-bench](/entities/swe-bench.md) — benchmark whose test-passing results overstate mergeability
- [Anthropic](/entities/anthropic.md) — vendor whose model documentation and pricing supply the cost inputs

## Concepts Covered

- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — the central model the post derives
- [time horizon](/concepts/time-horizon.md) — METR's capability-vs-difficulty measurement
- [verification tax](/concepts/verification-tax.md) — the dominant, non-token cost of a mergeable PR
- [model routing](/concepts/model-routing.md) — decompose first, then pick the tier
- [task decomposition](/concepts/task-decomposition.md) — keep units left of the ~30-minute conversion wall

## Related Sources

- [Direct API Integration for AI Agents: Lessons from Removing the CLI Layer](/sources/direct-api-integration-for-ai-agents-lessons-from-removing-the-cli-layer.md)
- [Not Every Ticket Needs the $250,000 Engineer](/sources/not-every-ticket-needs-the-250000-engineer.md)
- [The Plan Was Right When You Made It](/sources/the-plan-was-right-when-you-made-it.md)
