---
title: "Your Most Privileged User Isn't Human - And Your Platform Doesn't Know That Yet"
type: "Source Summary"
description: "Argues platforms must extend identity, policy, and decision attribution to AI agents as a new class of privileged operator."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, security, improving.com]
sources:
  - "references/improving.com/platform-security-governance-ai-agents/platform-security-governance-ai-agents.md"
---

# Your Most Privileged User Isn't Human - And Your Platform Doesn't Know That Yet — Summary

**Original source**: `references/improving.com/platform-security-governance-ai-agents/platform-security-governance-ai-agents.md`

## Summary

Cloud-native adoption fragmented security enforcement, leaving organizations secure on paper but cracked in practice. The post argues the internal platform should be the single security enforcement layer, then extends that argument to AI agents: agents are a new class of operator with broad permissions, dependencies like MCP servers, and audit trails that answer nothing. It offers three patterns — user context propagation, dynamic policy enforcement, and decision attribution — to answer WHO, WHAT, and WHY.

## Key Claims

- In the first half of 2025 there were more than 166 million data compromises, and 1 in 6 breaches now involve AI-driven attacks.
- Five platform governance capabilities: policy as code, guardrails by default, identity and access governance, audit and accountability, and compliance automation.
- AI agents added to platforms (ChatOps bots, SRE agents, cost agents) become operators that act faster than humans with broader permissions and useless audit trails.
- Agent dependencies — skills, tools, and MCP servers — are rarely scanned; a malicious MCP server needs no CVE to steal credentials or inject prompts.
- OWASP's Top 10 for Agentic Applications (December 2025) names privilege escalation, tool misuse, and identity abuse as top risks.
- Three extension patterns: user context propagation (WHO), dynamic policy enforcement via Kyverno/OPA (WHAT), and decision attribution via OpenTelemetry traces linked to audit logs (WHY).
- Recommendations: audit the platform, give agents dedicated identities, trace one high-privilege action end to end, and require accountability before read-write access.

## Relevance

Core to [platform engineering](/concepts/platform-engineering.md) and [agent identity](/concepts/agent-identity.md), applying [policy as code](/concepts/policy-as-code.md), [runtime policy enforcement](/concepts/runtime-policy-enforcement.md), and [audit trail](/concepts/audit-trail.md).

## Quality

Technical essay by Atulpriya Sharma; specific and architectural with code samples, but vendor-adjacent and conference-promotional.

## Entities Mentioned

- [Kyverno](/entities/kyverno.md) — policy engine used
- [OpenTelemetry](/entities/opentelemetry.md) — decision-trace capture
- [KubeCon](/entities/kubecon.md) — venue for the related talk
- [Improving](/entities/improving.md) — author's employer
- [Atulpriya Sharma](/entities/atulpriya-sharma.md) — author

## Concepts Covered

- [platform engineering](/concepts/platform-engineering.md) — platform as enforcement layer
- [agent identity](/concepts/agent-identity.md) — agents as non-human principals
- [policy as code](/concepts/policy-as-code.md) — executable, versioned rules
- [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) — blocking disallowed actions
- [zero trust security](/concepts/zero-trust-security.md) — verify every operator
- [audit trail](/concepts/audit-trail.md) — traceable accountability
