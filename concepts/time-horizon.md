---
title: "time horizon"
type: "Concept"
description: "The length of task an AI model can complete reliably; it doubles roughly every four to seven months."
created: '2026-10-17'
updated: '2026-10-17'
tags: [capability, forecasting, agents]
sources:
  - "/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
  - "/sources/not-every-ticket-needs-the-250000-engineer.md"
---

# time horizon

The time horizon is how long a task a model can complete reliably — the yardstick [METR](/entities/metr.md) uses to measure frontier capability. It matters across this corpus because it sets the ceiling on what [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) any team can actually convert into merged work.

## Key Claims

- Frontier capability time horizons double roughly every seven months, accelerating to about 4.3 months since 2023.
- Past roughly 30-minute tasks, token spend stops converting into mergeable pull requests — a conversion wall.
- Halving the verification fraction buys 46% throughput; doubling the horizon buys only 2%.
- Roughly 80% of issue resolution is nearly free; premium tiers buy the last 15 points.
- Cost per solved task prices retries and the whole agent harness, so better models are not automatically cheaper.

## Related

- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — what a horizon is worth once verification is priced in
- [verification tax](/concepts/verification-tax.md) — the cost that limits returns from a longer horizon
- [Task Decomposition](/concepts/task-decomposition.md) — how teams work below the conversion wall
- [Cost-Adjusted Capacity](/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md) — primary source
