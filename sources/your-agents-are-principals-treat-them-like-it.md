---
title: "Your Agents Are Principals. Treat Them Like It."
type: "Source Summary"
description: "AI agents are a new class of identity principal; existing security tooling must be pointed at them before deployment."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, devlinliles.com]
sources:
  - "references/devlinliles.com/your-agents-are-principals-treat-them-like-it/your-agents-are-principals-treat-them-like-it.md"
---

# Your Agents Are Principals. Treat Them Like It. — Summary

**Original source**: `references/devlinliles.com/your-agents-are-principals-treat-them-like-it/your-agents-are-principals-treat-them-like-it.md`

## Summary

The post argues that AI agents are a new class of security principal and that the existing identity stack — built for humans — fails against them because agents authenticate without reasoning, act at machine speed, acquire permissions dynamically, and are injected rather than phished. It contends that the tools to govern them already exist and only need to be pointed at agents deliberately, shifting governance from human-reviewed provisioning to policy-as-code enforced at runtime. The recurring principle is that permissions, not the model, are the perimeter.

## Key Claims

- 91% of organizations have deployed AI agents; only 10% have a governance strategy for them.
- Machine identities already outnumber human ones roughly 80:1 (CyberArk), and 68% of organizations lack identity security controls for AI systems.
- OWASP ranks indirect prompt injection (XPIA) the top LLM risk; EchoLeak (CVE-2025-32711) scored CVSS 9.3 and CVE-2025-53773 achieved remote code execution via prompt injection in GitHub Copilot.
- MCP accumulated 99 published CVEs in 2025, prompting an OWASP MCP Top 10; Microsoft's agent failure-mode taxonomy grew from v1.0 (April 2025) to v2.0 (June 2026).
- Manual review cannot scale to an 80:1 ratio, so governance must move to runtime policy-as-code (e.g. Microsoft's Agent Governance Toolkit, April 2026); EU AI Act high-risk obligations, including 15-day incident reporting, activate August 2, 2026.

## Relevance

Informs [agent identity](/concepts/agent-identity.md), [Policy as Code](/concepts/policy-as-code.md), [Least privilege](/concepts/least-privilege.md), and the [prompt injection](/concepts/prompt-injection.md) threat model for agentic deployments.

## Quality

Practitioner blog post by Devlin Liles. Densely sourced with named CVEs, standards, and regulatory dates, but it leans on vendor material (Microsoft, CyberArk, Okta), so the framing should be read with that in mind.

## Entities Mentioned

- [Microsoft Entra Agent ID](/entities/microsoft-entra-agent-id.md) — extends the Entra ID identity fabric to autonomous and delegated agents
- [Model Context Protocol](/entities/model-context-protocol.md) — supply-chain surface with tool-poisoning risk
- [OWASP](/entities/owasp.md) — ranks prompt injection top risk and publishes the MCP Top 10
- [Okta](/entities/okta.md) — extends identity posture management to non-human identities
- [EU AI Act](/entities/eu-ai-act.md) — high-risk obligations activating August 2026

## Concepts Covered

- [agent identity](/concepts/agent-identity.md) — treating agents as first-class principals
- [Policy as Code](/concepts/policy-as-code.md) — runtime enforcement replacing manual review
- [Least privilege](/concepts/least-privilege.md) — scoping permissions to bound blast radius
- [Prompt injection](/concepts/prompt-injection.md) — the XPIA threat that replaces phishing
