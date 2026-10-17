---
title: "model-agnostic architecture"
type: "Concept"
description: "Abstracting the model behind a provider-neutral interface so models can be swapped without rewriting applications."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, architecture, platform]
sources:
  - "/sources/designing-ai-systems-for-change.md"
  - "/sources/when-mcp-is-not-the-right-choice.md"
  - "/sources/ai-sovereignty-escaping-the-single-vendor-trap.md"
  - "/sources/own-the-interface-why-enterprise-ai-needs-a-governed-gateway.md"
  - "/sources/switch-from-openai-to-amazon-bedrock.md"
---

# model-agnostic architecture

Model-agnostic architecture abstracts model access behind a provider-neutral interface so models, prompts, and orchestration can change without rewriting applications. It is the structural answer to the fact that AI models age faster than the software around them: tying business logic to specific models, providers, or frameworks accumulates technical debt and makes future migrations slower, riskier, and more expensive.

## Key Claims

- A seemingly simple model upgrade can affect prompt behavior, retrieval quality, latency, cost, workflows, and evaluation baselines all at once.
- Behavior changes come from rapid model evolution, prompt drift caused by RLHF and safety tuning, retrieval/embedding upgrades, data drift, and expanding regulation such as the EU AI Act and GDPR Article 22.
- Build abstraction layers (LiteLLM, Portkey, internal proxy), keep prompts in managed systems (Langfuse, PromptLayer), and isolate orchestration (LangChain, LlamaIndex).
- Version and evaluate models, prompts, embeddings, and datasets, upgrading only after testing and approval, and monitor quality, retrieval accuracy, and latency continuously.
- Manage embedding lifecycles with multiple coexisting versions, phased migration, parallel indexes, and automated regeneration; keep raw documents model-independent.
- MCP is itself a model-agnostic protocol that decouples AI applications from individual model providers, though it adds an operational complexity tax and an enlarged security blast radius when adopted without need.
- The interface can be owned via a hyperscaler surface (Bedrock's Converse API, Azure AI Foundry, Vertex AI) or a governed gateway, so model-sunset migrations move to configuration rather than application code.

## Related

- [AI sovereignty](/concepts/ai-sovereignty.md) — the vendor-exposure problem it addresses
- [governed AI gateway](/concepts/governed-ai-gateway.md) — where the abstraction is enforced
- [dispatcher pattern](/concepts/dispatcher-pattern.md) — a shared access layer routing to providers
- [version pinning](/concepts/version-pinning.md) — tracking each swappable component
