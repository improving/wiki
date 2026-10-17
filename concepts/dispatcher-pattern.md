---
title: "dispatcher pattern"
type: "Concept"
description: "A routing layer that decouples agent logic from model providers, making model selection a configuration decision."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai-agents, architecture, reliability]
sources:
  - "/sources/decoupling-ai-agent-logic-from-model-providers-the-dispatcher-pattern.md"
  - "/sources/engineering-reliability-into-autonomous-ai-agents.md"
---

# dispatcher pattern

The dispatcher pattern inserts a routing layer between an agent's logic and the model providers it calls, so the choice of model becomes configuration rather than code. Across this corpus it is both an independence mechanism — protecting against provider change — and a reliability mechanism that lets a system fail over or specialize without an emergency rewrite.

## Key Claims

- Coupling agent logic to a specific model creates migration costs when models change.
- A routing table maps task classifications to model selections as configuration.
- Prompt adapters and output normalization deliver per-model independence.
- The dispatcher enables provider failover without emergency code changes.
- Ten steps at 95% accuracy yield only about 60% end-to-end pipeline reliability, so decoupling alone is not enough.
- Specialized agents, adversarial tracks, and a dispatcher overcome the [single-agent ceiling](/concepts/single-agent-ceiling.md).

## Related

- [model routing](/concepts/model-routing.md) — the general mechanism the dispatcher implements
- [Model selection](/concepts/model-selection.md) — the decision the routing table encodes
- [orchestration layer](/concepts/orchestration-layer.md) — where a dispatcher typically lives
- [Single-Agent Ceiling](/concepts/single-agent-ceiling.md) — the limit specialization and dispatch address
- [Decoupling AI Agent Logic from Model Providers: The Dispatcher Pattern](/sources/decoupling-ai-agent-logic-from-model-providers-the-dispatcher-pattern.md) — primary source
- [Engineering Reliability into Autonomous AI Agents](/sources/engineering-reliability-into-autonomous-ai-agents.md) — primary source
