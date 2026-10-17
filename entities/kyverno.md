---
title: "Kyverno"
type: "Entity"
description: "Kubernetes policy engine used for admission control, prompt-injection defense, and AI tool authorization."
created: '2026-10-17'
updated: '2026-10-17'
tags: [policy-as-code, kubernetes, security]
sources:
  - "/sources/mcp-authorization-policy-driven-tool-invocation-control.md"
  - "/sources/kubernetes-prompt-injection.md"
  - "/sources/platform-security-governance-ai-agents.md"
  - "/sources/platform-engineering-service-organizations.md"
  - "/sources/internal-developer-portal-what-reduces-cognitive-load.md"
---

# Kyverno

Kyverno is a Kubernetes-native policy engine that enforces rules in the admission path through validating and mutating webhooks. Across the corpus it is the recurring enforcement layer for policy as code — used to defend clusters against prompt injection, authorize AI tool calls, and explain platform rules rather than block them silently.

## Enforcement Patterns

- Kyverno sits in the admission path and can inspect arbitrary JSON; validating webhooks accept or block, and mutating webhooks annotate before a call proceeds.
- In an MCP authorization design, tool invocations are modeled as `MCPToolInvocation` custom resources; Kyverno writes five annotations the agent cannot alter, and the Kubernetes audit log retains the creation record even if the resource is later deleted.
- It serves as the second, independent guardrail layer in prompt-injection defense, alongside least-privilege RBAC and NetworkPolicy plus Falco runtime detection.
- In platform security, Kyverno (with OPA) is the mechanism for dynamic policy enforcement — the "WHAT" of agent governance.

## As a Platform Pattern

- OPA/Kyverno policy templates are part of the capability layer a service organization standardizes instead of the environment.
- A Kyverno policy that blocks without explanation drives workarounds; one that explains what it enforced enables action.

## Related

- [policy as code](/concepts/policy-as-code.md) — the discipline Kyverno implements
- [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) — stopping disallowed actions before execution
- [prompt injection](/concepts/prompt-injection.md) — an attack it helps contain
- [agent identity](/concepts/agent-identity.md) — the principal it scopes policies to
