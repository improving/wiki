---
title: "Entra ID"
type: "Entity"
description: "Microsoft's cloud identity platform, cited as the issuer and identity substrate behind agent authentication and least-privilege controls."
created: '2026-10-17'
updated: '2026-10-17'
tags: [identity, microsoft, security]
sources:
  - "/sources/mcp-went-stateless-the-state-didnt-go-anywhere.md"
  - "/sources/the-box-that-already-shipped-rollback-by-reversibility-type.md"
  - "/sources/the-day-your-agent-got-its-own-email-address.md"
---

# Entra ID

Entra ID is Microsoft's cloud identity and access management platform. In this corpus it appears as the identity substrate that agent-facing authentication builds on, both when protocols tighten issuer validation and when systems must prove what a principal actually did.

## Overview

The 2026-07-28 Model Context Protocol specification added RFC 9207 issuer validation and deprecated Dynamic Client Registration, shifting identity trust onto the authorization server rather than the client. That change makes platforms like Entra ID the place where agent identity is anchored, and it raises the bar for proving which principal performed an action.

The same concern runs through rollback design. When actions are tagged by reversibility type, "stateful-external" operations require polling real state before claiming success — which in practice means asking the identity or external system of record whether the change actually took effect, not trusting the caller's report.

## Key Claims

- Issuer validation (RFC 9207) moves identity trust to the authorization server, a role Entra ID fills.
- Dynamic Client Registration is deprecated, tightening how clients obtain credentials.
- Verifying stateful-external rollback requires checking the authoritative external system, not the agent's self-report.
- Reversibility tagging cut false rollback success from over 40% to under 5%.
- Google giving enterprise agents their own Workspace identities pushes agent governance onto the directory, making identity architecture the battleground.
- You cannot audit what you cannot attribute, nor revoke access you never granted; shared credentials turn agents into ungoverned shadow IT at ten times speed.

## Related

- [agent identity](/concepts/agent-identity.md) — the concept Entra ID anchors
- [Least privilege](/concepts/least-privilege.md) — the access discipline it enforces
- [Model Context Protocol](/entities/model-context-protocol.md) — the spec that added issuer validation
- [Microsoft Entra Agent ID](/entities/microsoft-entra-agent-id.md) — the agent-specific extension
- [AI Governance](/concepts/ai-governance.md) — the program agent identities must plug into
- [MCP Went Stateless](/sources/mcp-went-stateless-the-state-didnt-go-anywhere.md) — primary source
