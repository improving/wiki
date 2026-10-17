---
title: "AI monitoring"
type: "Concept"
description: "Continuously observing deployed models for drift and quality, which carries a real, budgetable compute cost."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, operations, governance]
sources:
  - "/sources/openai-ai-monitoring-budgets.md"
  - "/sources/no-ownership-or-maintenance.md"
  - "/sources/the-watched-workforce.md"
  - "/sources/complexity-never-goes-away-ai-systems-engineering.md"
  - "/sources/the-role-of-ai-in-modern-managed-services.md"
---

# AI monitoring

AI monitoring is the continuous observation of deployed models for drift and quality, and the sources argue it carries a real, budgetable compute cost that most enterprises treat as zero until something breaks. Because AI systems are living entities that decay as data, regulations, and user behavior shift, monitoring needs a baseline, a threshold, an escalation path, and periodic human review — plus governance attention to the second-order effects of watching workers.

## Key Claims

- OpenAI disclosed that AI monitoring costs roughly 20% of the compute being monitored; that figure is a floor because OpenAI owns the infrastructure, model, and evaluation designers.
- Teams that have never priced confidence have almost always never defined what a confidence failure looks like — no threshold, no protocol — and find out via user escalation or an unattributable downstream failure.
- A baseline (accuracy, latency, and output distribution on representative production inputs) is required before drift can be measured.
- Monitoring components: evaluation runs on a held-out production sample, a defined deviation threshold, an escalation path, and periodic independent human review.
- AI systems are living entities: assign a product owner, define an MLOps/GenAIOps framework, and publish SLAs for uptime, retraining frequency, and data freshness.
- One client's policy Q&A bot used monthly prompt-pack refreshes and quarterly drift evaluations against gold questions to prevent confidence erosion.
- Workplace monitoring is itself a governance question: 78% of US employers use monitoring tools and 61% deploy AI analytics, which suppress dissent and creativity when broadly scoped and opaque.
- AI monitoring is the LLMOps half of the systems-around-models loop, paired with harness engineering on the input side.

## Related

- [Model Drift Detection](/concepts/model-drift-detection.md) — catching behavior change
- [LLM evaluation](/concepts/llm-evaluation.md) — measuring output quality
- [AI Governance](/concepts/ai-governance.md) — thresholds and escalation protocols
- [token cost](/concepts/token-cost.md) — the budget monitoring consumes
- [Quality Gates](/concepts/quality-gates.md) — pass criteria that trigger escalation
- [runtime governance](/concepts/runtime-governance.md) — controls enforced at execution time
