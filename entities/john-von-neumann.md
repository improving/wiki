---
title: "John von Neumann"
type: "Entity"
description: "Mathematician whose work on reliable computation from unreliable components underlies the reliability math of chained agents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [mathematician, reliability, systems]
sources:
  - "/sources/engineering-reliability-into-autonomous-ai-agents.md"
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
  - "/sources/your-agent-is-probably-less-reliable-than-you-think.md"
---

# John von Neumann

John von Neumann is the mathematician whose work on reliable computation from unreliable components underlies the reliability math this corpus applies to AI agents.

## Overview

The posts treat sequential reliability as multiplication: ten steps at 95% accuracy yield only about 60% end-to-end reliability, and a 98%-per-step agent at 20 steps succeeds only about 67% of the time. That is Lusser's law applied to agents, and it reframes governance as a capability enabler rather than overhead. The von Neumann tradition — building dependable systems out of undependable parts through structure and redundancy — anchors the argument that defense layers, quality gates, and recovery pipelines, not higher per-step accuracy alone, make autonomy trustworthy.

## Key Claims

- End-to-end reliability is the product of component reliabilities, not their average
- Ten steps at 95% accuracy yield only about 60% end-to-end reliability
- Six independent defense layers sit between a model call and a trusted output
- A seven-phase recovery pipeline replaces retry with evidence-based diagnosis and prevention
- Errors left in context recruit the model to defend them

## Related

- [Lusser's Law](/concepts/lussers-law.md) — the reliability math at the core of the argument
- [Compounding error](/concepts/compounding-error.md) — the failure mode it predicts
- [Stacking Errors](/concepts/stacking-errors.md) — the governance consequence
- [Robert Lusser](/entities/robert-lusser.md) — formulated the series-reliability law
- [Stacking Errors: The Compounding Math Behind AI Governance](/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md) — primary source
