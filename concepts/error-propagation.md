---
title: "Error Propagation"
type: "Concept"
description: "How a single bad value or mistake flows through a multi-step pipeline, compounding cost and corrupting later outputs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, pipelines, agents]
sources:
  - "/sources/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md"
  - "/sources/your-agent-is-probably-less-reliable-than-you-think.md"
---

# Error Propagation

Error propagation describes how a defect introduced at one step becomes the input to the next, so a small local error is amplified into a large system failure. It is central to this corpus because agentic pipelines are sequential, and their reliability is a property of the connections between steps.

## Key Claims

- System reliability is the product of component reliabilities, not their average, so errors compound rather than cancel.
- A 98%-per-step agent at 20 steps succeeds only about 67% of the time.
- Individually accurate steps can still produce a confidently wrong pipeline output when nothing checks the value between them.
- Errors left in context recruit the model to defend them, turning a transient mistake into a persistent one.
- Adversarial inspector agents break error chains without raising per-step accuracy, by catching bad values at the handoff.
- Catching defects early is cheap; catching them late compounds cost across every downstream stage.

## Related

- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — the metric error propagation erodes
- [Quality Gates](/concepts/quality-gates.md) — handoff checks that stop propagation
- [Compounding error](/concepts/compounding-error.md) — the arithmetic of accumulated mistakes
- [adversarial validators](/concepts/adversarial-validators.md) — inspector agents that break the chain
- [Quality Gates at Every Transition - Stopping a Bad Value Before It Becomes the Next Step's Input](/sources/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md) — primary source
