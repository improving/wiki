---
title: "cost-adjusted capacity"
type: "Concept"
description: "The rate at which token spend converts into mergeable work, which collapses past roughly 30-minute tasks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [economics, agents, verification]
sources:
  - "/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
  - "/sources/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md"
---

# cost-adjusted capacity

Cost-adjusted capacity is the measure of how much mergeable work a given amount of token spend actually buys, rather than how much capability a model theoretically has. It matters because the two diverge sharply: token spend stops converting into mergeable pull requests past roughly 30-minute tasks, so improving verification beats upgrading models.

## Key Claims

- Frontier capability time horizons double roughly every seven months, accelerating to 4.3 months since 2023.
- Automated graders overstate mergeable capability by up to 6.25x versus human maintainers.
- Halving the verification fraction buys 46% throughput, while doubling the horizon buys only 2%.
- Decompose tasks below the ~30-minute conversion wall, then route execution to cheaper models.
- In a controlled 216-run evaluation, all 25 mergeability failures were test-additions that passed automated tests.
- LLM pull-request failures split into capability-gap and scope-discipline haircuts requiring opposite remediation: better models fix the former and worsen the latter.

## Related

- [time horizon](/concepts/time-horizon.md) — the capability dimension this adjusts
- [verification tax](/concepts/verification-tax.md) — the cost that dominates returns
- [Task Decomposition](/concepts/task-decomposition.md) — the response to the conversion wall
- [model routing](/concepts/model-routing.md) — sending bounded tasks to cheaper models
- [Cost-Adjusted Capacity](/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md) — primary source
- [Two Failure Modes in LLM-Generated Pull Requests](/sources/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md) — controlled evaluation
