---
title: "token cost"
type: "Concept"
description: "The per-token expense of LLM inference, which scales with context complexity and demands per-task observability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [economics, observability, operations]
sources:
  - "/sources/built-for-demand-that-hasnt-arrived.md"
  - "/sources/checking-the-math-on-the-500-million-ai-spend-story.md"
  - "/sources/cost-observability-in-ai-assisted-development-understanding-what-your-agents.md"
  - "/sources/the-bottleneck-isnt-the-fix-its-finding-what-to-fix.md"
---

# token cost

Token cost is the per-token price of model inference and the central unit of AI economics in this corpus. It scales with context complexity more than output volume, so teams need per-task measurement rather than blunt caps — and the broader market, not just a single bill, is where the demand limit shows up.

## Key Claims

- Token costs scale with context complexity more than with output volume; instrument per-task, per-agent-role, per-model-tier, and per-activity-category cost.
- Budget enforcement doubles as a diagnostic signal for misconfigured tasks, and [cost observability](/concepts/cost-adjusted-capacity.md) is the prerequisite for empirical [model-tier selection](/concepts/model-selection.md).
- A viral $500M Claude bill fails arithmetic — that is $193 per second for 30 days, needing 2–3.3 million developer seats — but the underlying spend-control anxiety is real; token cost is under-instrumented.
- Splitting repository exploration from repair (FastContext) cut tokens up to 60% and improved resolution 5.5%, showing architecture beats model upgrades for cost.
- Cheaper narrow models handle breadth while frontier models reserve context for depth, which is the practical basis of [model routing](/concepts/model-routing.md).
- At the market level, IBM's Together AI inference cluster won't go live until early 2027, and Nvidia posted an earnings beat only to be sold off: more capability does not create demand, and capital markets no longer fund buildout on forecasts alone.

## Related

- [model routing](/concepts/model-routing.md) — spending the right model per task
- [model selection](/concepts/model-selection.md) — empirical tier choice
- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — when tokens stop converting to PRs
- [Cost Observability in AI-Assisted Development](/sources/cost-observability-in-ai-assisted-development-understanding-what-your-agents.md) — primary source
