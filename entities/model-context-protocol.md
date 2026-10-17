---
title: "Model Context Protocol"
type: "Entity"
description: "Open protocol standardizing how agents connect to tools and data, made stateless in 2026 while remaining an under-specified contract."
created: '2026-10-17'
updated: '2026-10-17'
tags: [protocol, agents, interoperability]
sources:
  - "/sources/mcp-went-stateless-the-state-didnt-go-anywhere.md"
  - "/sources/name-resolution-was-never-enough.md"
  - "/sources/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md"
  - "/sources/the-approval-that-expires-building-a-vendor-gate-on-evidence.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
  - "/sources/your-agents-are-principals-treat-them-like-it.md"
  - "/sources/your-multi-agent-system-has-a-coordination-problem.md"
  - "/sources/nist-is-wiring-the-agent-standards-layer.md"
  - "/sources/your-agents-have-keys-nobody-changed-the-locks.md"
---

# Model Context Protocol

The Model Context Protocol (MCP) is an open standard for connecting AI agents to tools and data sources. Across this corpus it is treated as the de facto agent-to-tool interface, and also as an under-specified contract whose security and state-management gaps carry real consequences.

## Overview

MCP's 2026-07-28 specification dropped the session handshake, moving state into explicit application-level handles while every request carries its own protocol version and capabilities. Commentators stress that a stateless protocol does not mean the application is stateless, and that capability-first discovery — not name resolution — is where agent tooling is heading.

## Key Claims

- Every MCP request now carries its own protocol version and capabilities; state lives in application-level handles.
- The spec adds RFC 9207 issuer validation and deprecates Dynamic Client Registration.
- Roots, Sampling, Logging, and HTTP+SSE carry a twelve-month support window.
- MCP is an under-specified tool contract, with 99 CVEs reported in 2025.
- MCP standardizes agent-to-tool communication while A2A targets agent-to-agent.
- NIST's AI Agent Standards Initiative names MCP and A2A as baseline interoperability protocols, so building agent infrastructure without them accrues compounding integration debt.
- Agent identity frameworks built around MCP anchor to OAuth 2.0 and OIDC, making a standards-compliant architecture by definition more governable.
- MCP also widens the attack surface: ServiceNow opening its system to agents via MCP exposes non-human identities that 92% of security leaders cannot see and 86% enforce no policies on.

## Related

- [Tool Calling](/concepts/tool-calling.md) — the interaction MCP standardizes
- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — where MCP and A2A divide responsibility
- [agent identity](/concepts/agent-identity.md) — the governance layer MCP's widening surface demands
- [Service Discovery](/concepts/service-discovery.md) — the capability-first successor to name resolution
- [MCP Went Stateless](/sources/mcp-went-stateless-the-state-didnt-go-anywhere.md) — primary source
