---
title: "LiteLLM"
type: "Entity"
description: "Provider-neutral LLM proxy that appears here as a mature open-source governed gateway and abstraction layer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, platform, gateway]
sources:
  - "/sources/own-the-interface-why-enterprise-ai-needs-a-governed-gateway.md"
  - "/sources/designing-ai-systems-for-change.md"
  - "/sources/human-cost-security-ai-era.md"
---

# LiteLLM

LiteLLM is a provider-neutral LLM proxy that appears in this corpus as the mature open-source option for a [governed AI gateway](/concepts/governed-ai-gateway.md) and as an abstraction layer that decouples applications from model providers.

## Role in the Corpus

- The "own the interface" argument names LiteLLM (with Bifrost, Kong AI, and Portkey) as gateway options that let an enterprise put a controlled layer in front of model vendors.
- A gateway issues virtual keys with budgets and routing policy, inspects prompts for policy violations, strips data that shouldn't leave, routes to cheaper models, and provides cross-provider observability that provider dashboards won't.
- It also governs developer tools like [Claude Code](/entities/claude-code.md) through pushed configuration and moves model-sunset migrations to the gateway without touching application code.
- The metric that matters shifts from cost per token to cost per successful task, since a model that is a third the price isn't cheaper if it needs twice the tokens.
- The "designing AI systems for change" playbook names LiteLLM (with Portkey or an internal proxy) as the abstraction layer that keeps business logic from binding to a specific model.
- A supply-chain post lists LiteLLM among the downstream victims of the 2026 Trivy compromise, a reminder that shared infrastructure concentrates risk.

## Related

- [governed AI gateway](/concepts/governed-ai-gateway.md) — the pattern LiteLLM implements
- [model-agnostic architecture](/concepts/model-agnostic-architecture.md) — the abstraction it provides
- [model routing](/concepts/model-routing.md) — policy-driven cost control at the gateway
- [dispatcher pattern](/concepts/dispatcher-pattern.md) — the shared access layer
