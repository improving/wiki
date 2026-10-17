---
title: "governed AI gateway"
type: "Concept"
description: "A single controlled ingress that routes model traffic for cost, vendor risk, and data-residency control."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, platform, governance]
sources:
  - "/sources/own-the-interface-why-enterprise-ai-needs-a-governed-gateway.md"
  - "/sources/your-prompt-is-a-cross-border-data-transfer.md"
  - "/sources/ai-sovereignty-escaping-the-single-vendor-trap.md"
  - "/sources/switch-from-openai-to-amazon-bedrock.md"
---

# governed AI gateway

A governed AI gateway is a single controlled ingress that sits in front of model providers and routes traffic under enterprise policy. Instead of applications calling a vendor API directly, they call the gateway, which issues virtual keys with budgets, inspects prompts for policy violations, strips data that shouldn't leave, routes to cheaper models, and provides cross-provider observability that vendor dashboards won't. It converts vendor dependence into leverage over cost, compliance, and model choice.

## Key Claims

- Direct API calls expose an enterprise to per-token price changes with no counterparty, provider outages it inherits, residency and privacy uncertainty, vendor viability, and fast model deprecation.
- The staged path is: point at a hyperscaler (near one-line change), put a governed gateway in front, then add multiple backends behind it.
- Gateway responsibilities include virtual keys with budgets, policy inspection, data stripping, [model routing](/concepts/model-routing.md), and cross-provider observability.
- The metric that matters shifts from cost per token to cost per successful task, since a model that is a third the price isn't cheaper if it needs twice the tokens.
- A gateway also governs developer tools such as [Claude Code](/entities/claude-code.md) through pushed configuration, and moves model-sunset migrations to the gateway without touching application code.
- Named options include [LiteLLM](/entities/litellm.md), Bifrost, Kong AI, and Portkey; running open-weight models locally is a fourth option outside the gateway architecture.
- A working sovereignty demo wires an AI Gateway, an agent service, an MCP server of region-tagged tools, and an LLM router toggling between local Ollama and cloud Gemini, tracing every call to produce a compliance verdict.

## Related

- [AI sovereignty](/concepts/ai-sovereignty.md) — the vendor-exposure problem it solves
- [model-agnostic architecture](/concepts/model-agnostic-architecture.md) — swapping models without rewrites
- [model routing](/concepts/model-routing.md) — policy-driven cost control
- [data residency](/concepts/data-residency.md) — where inference runs
