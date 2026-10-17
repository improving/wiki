---
title: "End-to-End Success Rate"
type: "Concept"
description: "The probability a whole multi-step pipeline succeeds, which falls far below per-step accuracy as steps multiply."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, pipelines, evaluation]
sources:
  - "/sources/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity.md"
  - "/sources/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md"
---

# End-to-End Success Rate

End-to-end success rate is the probability that an entire multi-step pipeline produces a correct result, as opposed to the accuracy of any single step. It matters across this corpus because per-step accuracy is a poor proxy for system reliability: individually competent stages still compose into fragile pipelines.

## Key Claims

- Reliability compounds multiplicatively, so end-to-end success is the product of per-step accuracies, not their average.
- At 85% per-step accuracy, a 20-step pipeline drops below 5% end-to-end success.
- Individually accurate steps can still yield a confidently wrong pipeline output when a bad value passes between them.
- A cheap validation [quality gate](/concepts/quality-gates.md) at every handoff catches defects while they are cheap, before cost compounds downstream.
- The metric exposes overestimation: organizations often believe they operate at a maturity stage their true end-to-end results do not support.

## Related

- [Error Propagation](/concepts/error-propagation.md) — the mechanism that erodes end-to-end success
- [Quality Gates](/concepts/quality-gates.md) — handoff checks that protect the aggregate rate
- [Lusser's Law](/concepts/lussers-law.md) — the multiplicative reliability arithmetic behind the number
- [AI maturity model](/concepts/ai-maturity-model.md) — stages judged by demonstrated end-to-end competency
- [Proving Competency at Every Stage: The Eight Stages of AI Maturity](/sources/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity.md) — primary source
