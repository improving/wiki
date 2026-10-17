---
title: "verification tax"
type: "Concept"
description: "The share of effort spent checking AI output; lowering it buys more throughput than upgrading models."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, review, throughput]
sources:
  - "/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
  - "/sources/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md"
---

# verification tax

The verification tax is the fraction of effort a team spends checking AI-generated work before it can be merged. This corpus argues it — not raw model capability — is the binding constraint on throughput: past roughly 30-minute tasks, tokens stop converting into mergeable pull requests, so improving verification beats upgrading models.

## Key Claims

- Halving the verification fraction buys 46% throughput; doubling the [time horizon](/concepts/time-horizon.md) buys only 2%.
- Automated graders overstate mergeable capability by up to 6.25x versus human maintainers.
- In a 216-run evaluation, all 25 mergeability failures were test-additions that had passed automated tests.
- Token spend was 0.1%–2.3% of the cost per mergeable PR, so generation is cheap and checking is expensive.
- Failures split into capability-gap and scope-discipline haircuts, which need opposite remediation: better models fix the first and worsen the second.

## Related

- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — the metric that prices verification in
- [time horizon](/concepts/time-horizon.md) — capability ceiling the tax limits
- [Quality Gates](/concepts/quality-gates.md) — programmatic checks that shrink the tax
- [Cost-Adjusted Capacity](/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md) — primary source
