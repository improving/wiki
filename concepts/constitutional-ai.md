---
title: "Constitutional AI"
type: "Concept"
description: "Rule-based alignment against a written constitution, which this corpus critiques as relocating rather than resolving arbitrary axioms."
created: '2026-10-17'
updated: '2026-10-17'
tags: [alignment, governance, philosophy]
sources:
  - "/sources/every-ai-value-system-bottoms-out-somewhere.md"
  - "/sources/godels-warning-to-symbolic-ai.md"
  - "/sources/you-can-train-a-character-not-just-rules.md"
---

# Constitutional AI

Constitutional AI aligns a model by having it follow a written set of principles. This corpus is critical of it as a complete solution: like [RLHF](/concepts/rlhf.md), it does not escape the problem of unjustified foundations, and as a rule-based approach it inherits the incompleteness that [Gödel](/sources/godels-warning-to-symbolic-ai.md) proved cannot be closed by adding more rules.

## Key Claims

- The Munchhausen Trilemma forces every justification chain into regress, circularity, or an axiomatic halt; RLHF bottoms out at human preferences, and Constitutional AI merely moves the arbitrary axiom up one level to the chosen constitution.
- Adopting a provider's model means adopting a non-value-neutral value structure, so the constitution's authorship is a governance question, not a technical one.
- Any consistent formal system expressive enough for arithmetic is incomplete; symbolic AI inherits this, and Constitutional AI's principle boundaries are Gödel sentences in that system.
- Neural approaches trade formal provability for probabilistic coverage, which is why rule-following produces arbitrary refusals while consequentialist optimization converges on [sycophancy](/concepts/sycophancy.md) and [reward hacking](/concepts/reward-hacking.md).
- Character-based alignment is offered as an alternative: training first-person identity declarations raised trait correlation from 0.44 to 0.87, generalizing better than rules or approval optimization.
- Whether models can achieve Aristotelian phronesis — practical wisdom beyond rules — remains unresolved.

## Related

- [RLHF](/concepts/rlhf.md) — the consequentialist counterpart
- [Symbolic AI](/concepts/symbolic-ai.md) — the rule-based tradition it belongs to
- [reward hacking](/concepts/reward-hacking.md) — a failure at the intersection
- [Every AI Value System Bottoms Out Somewhere](/sources/every-ai-value-system-bottoms-out-somewhere.md) — primary source
