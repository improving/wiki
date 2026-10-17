---
title: "Robert Lusser"
type: "Entity"
description: "Reliability engineer whose series-system law explains why chained agent steps compound failure multiplicatively."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, engineering, mathematics]
sources:
  - "/sources/engineering-reliability-into-autonomous-ai-agents.md"
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
  - "/sources/your-agent-is-probably-less-reliable-than-you-think.md"
---

# Robert Lusser

Robert Lusser is the reliability engineer whose series-system law this corpus applies to AI agents: end-to-end reliability is the product of component reliabilities, not their average.

## Overview

Lusser's law explains why chained agent steps fail far more often than per-step accuracy suggests — ten steps at 95% accuracy yield only about 60% end-to-end reliability, and a 98%-per-step agent at 20 steps succeeds only about 67% of the time. The posts draw a governance conclusion from it: quality gates between steps are the infrastructure that makes autonomy reliable, so prefer shorter, gated pipelines over long autonomous chains. Adversarial inspector agents can break error chains without raising per-step accuracy.

## Key Claims

- Lusser's law: series-system reliability is the product of component reliabilities
- Ten steps at 95% accuracy yield only about 60% end-to-end reliability
- A 98%-per-step agent at 20 steps succeeds only about 67% of the time
- Governance is a capability enabler, not overhead friction
- Prefer shorter, gated pipelines over long autonomous chains

## Related

- [Lusser's Law](/concepts/lussers-law.md) — the law named for him
- [Compounding error](/concepts/compounding-error.md) — its practical consequence
- [Stacking Errors](/concepts/stacking-errors.md) — the governance response to the math
- [John von Neumann](/entities/john-von-neumann.md) — related reliability framing
- [Your Agent Is Probably Less Reliable Than You Think](/sources/your-agent-is-probably-less-reliable-than-you-think.md) — primary source
