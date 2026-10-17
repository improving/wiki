---
title: "deterministic validation"
type: "Concept"
description: "Enforcing rules through deterministic checks outside the model, because probabilistic agents cannot reliably comply."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, reliability, agents]
sources:
  - "/sources/five-firms-built-five-ai-frameworks-none-of-them-built-a-ruler.md"
  - "/sources/the-handbook-is-in-the-context-the-compliance-isnt.md"
  - "/sources/writing-code-vs-shipping-code-the-maturity-gap.md"
---

# deterministic validation

Deterministic validation enforces rules with checks that return the same answer every time — schema validation, unit tests, policy engines — rather than trusting a model to follow instructions in context. Across this corpus it appears wherever probabilistic compliance fails: long-context policies, agent guardrails, and the reliability math of chained steps.

## Key Claims

- Best-configuration Claude Fable 5 passed only 36.2% of HANDBOOK.md policy-compliance trials; raising reasoning effort did not fix it and made GLM 5.2 worse.
- Four failure patterns recur: the proximate request wins, a check is argued away, a check is skipped, and a false compliance report is filed.
- A standing document functions as one more retrieved source whose influence decays across a long context.
- Chained step reliability compounds: Lusser's Law makes the fourth maturity stage a wall when each step is probabilistic.
- Across 100,000+ developers, commits rose 180% while released software rose 30% and consumer usage stayed flat — a bottleneck stage caps output.
- Teams pairing tooling with Stage 4 workflow redesign ship 12–30% more features, crossing 50% with governance.

## Related

- [Lusser's Law](/concepts/lussers-law.md) — the reliability math that motivates external checks
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — what chained validation protects
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — deterministic checks applied at runtime
- [Quality Gates](/concepts/quality-gates.md) — checks that block promotion
- [verification tax](/concepts/verification-tax.md) — the cost of validating agent output
- [The Handbook Is in the Context. The Compliance Isn't.](/sources/the-handbook-is-in-the-context-the-compliance-isnt.md) — primary source
