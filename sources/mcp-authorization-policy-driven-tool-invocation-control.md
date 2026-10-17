---
title: "Closing the AuthZ Gap in MCP: Policy-Driven Tool Invocation Control"
type: "Source Summary"
description: "MCP authorizes connectivity but not tool invocation; enforcing Kyverno policy on tool calls modeled as Kubernetes resources closes the gap."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, ai, improving.com]
sources:
  - "references/improving.com/mcp-authorization-policy-driven-tool-invocation-control/mcp-authorization-policy-driven-tool-invocation-control.md"
---

# Closing the AuthZ Gap in MCP: Policy-Driven Tool Invocation Control — Summary

**Original source**: `references/improving.com/mcp-authorization-policy-driven-tool-invocation-control/mcp-authorization-policy-driven-tool-invocation-control.md`

## Summary

MCP has become the de-facto standard for how AI agents connect to external services, but its authorization model covers only connectivity and authentication — once an agent is authenticated, nothing native controls which tools it can call or with what parameters. The post argues for modeling MCP tool invocations as Kubernetes custom resources and enforcing policy in the admission path with Kyverno, so every call becomes a first-class object the platform can inspect, validate, mutate, and audit.

## Key Claims

- Over 17,000 MCP servers exist (Zuplo report), and 50% of professionals find MCP security or access control a big challenge.
- MCP can require OAuth 2.0 tokens and restrict which clients connect, but it lacks a native primitive for authorization at the tool-invocation layer.
- The multi-tenant threat surface: cross-tenant tool calls, phantom agent identity (audit shows a service account, not the human who triggered the chain), unconstrained parameters, and privilege escalation chains where each hop loses context and permission.
- Kubernetes RBAC has no answer because it governs resource-verb pairs at the API surface, while MCP tool calls carry semantic context — which tool, agent, tenant, parameters, and time.
- The solution models each invocation as an `MCPToolInvocation` custom resource and puts a policy engine in the admission path; Kyverno sits there and can inspect arbitrary JSON, with validating webhooks that accept or block and mutating webhooks that annotate before a call proceeds.
- Three patterns: tool allowlisting per agent identity (deny by default), multi-tenant isolation (tenant context must match the agent's namespace or annotation), and human identity injection (a mutating policy annotates `triggered-by`, timestamp, agent chain ID, and policy version).
- In the demo with `kubernetes-mcp-server`, before mutation the CR carries only agent-supplied `triggeredBy`; after, Kyverno writes five annotations the agent cannot alter, and the Kubernetes audit log retains the creation record even if the CR is later deleted.
- Rollout guidance: audit first (Kyverno in Audit mode), model the CRD deliberately with toolName/tenantId/agentId in spec, start with human identity propagation rather than blocking, flip one policy to Enforce at a time with at least two weeks of audit coverage, and propagate human context at the orchestration layer (LangGraph, AutoGen) before agents get production write access.
- Full code is at the `infracloudio/mcp-authz-kyerno-demo` repository.

## Relevance

Informs [policy as code](/concepts/policy-as-code.md), [runtime policy enforcement](/concepts/runtime-policy-enforcement.md), [agent identity](/concepts/agent-identity.md), and [least privilege](/concepts/least-privilege.md).

## Quality

Hands-on security architecture post by Sonali Srivastava; concrete YAML and a demo, candid about the spec's maturity, though vendor-adjacent.

## Entities Mentioned

- [Improving](/entities/improving.md) — the practice behind the post
- [Model Context Protocol](/entities/model-context-protocol.md) — the protocol whose authorization gap is addressed
- [Kyverno](/entities/kyverno.md) — the policy engine in the admission path
- [Kubernetes](/entities/kubernetes.md) — hosts the CRD and admission webhooks
- [LangGraph](/entities/langgraph.md) — an orchestration framework that must stamp human context
- [AutoGen](/entities/autogen.md) — another orchestration framework cited

## Concepts Covered

- [policy as code](/concepts/policy-as-code.md) — the enforcement layer
- [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) — stopping disallowed calls before execution
- [agent identity](/concepts/agent-identity.md) — scoping tools per agent identity
- [least privilege](/concepts/least-privilege.md) — deny-by-default allowlisting
- [audit trail](/concepts/audit-trail.md) — human identity injected at admission
- [runtime governance](/concepts/runtime-governance.md) — governance at the moment of execution
