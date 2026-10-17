---
title: "Your Agents Have Keys. Nobody Changed the Locks."
type: "Source Summary"
description: "Argues AI agents are non-human identities needing the same least-privilege lifecycle as employees, which most enterprises never extended."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, driventodevelop.com]
sources:
  - "references/driventodevelop.com/your-agents-have-keys-nobody-changed-the-locks/your-agents-have-keys-nobody-changed-the-locks.md"
---

# Your Agents Have Keys. Nobody Changed the Locks. — Summary

**Original source**: `references/driventodevelop.com/your-agents-have-keys-nobody-changed-the-locks/your-agents-have-keys-nobody-changed-the-locks.md`

## Summary

David O'Hara argues that enterprises govern human identities rigorously—accounts, role-based access, approval chains, offboarding—but apply none of it to AI agents. With most security leaders lacking visibility into what agents can access and rarely enforcing policies on them, he calls the situation an open door rather than a governance gap. ServiceNow opening its system of action to any agent via MCP widens the attack surface, making agent identity governance urgent.

## Key Claims

- 92% of enterprise security leaders lack full visibility into what their AI agents can access
- 86% do not enforce access policies on agents at all
- Every agent is a non-human identity with credentials, permissions, and a blast radius if compromised
- The human identity lifecycle applies: provision with least privilege, audit regularly, revoke on change
- ServiceNow's MCP-based opening of its full system of action makes the attack surface programmable from outside
- The gap is not tooling but the assumption that agents need no governance because they are not people

## Relevance

Extends [least privilege](/concepts/least-privilege.md) and [agent identity](/concepts/agent-identity.md) into [AI governance](/concepts/ai-governance.md); the identity-layer companion to [you cant govern an inventory](/sources/you-cant-govern-an-inventory-you-dont-know-you-have.md).

## Quality

Practitioner blog post by David O'Hara. Punchy and specific, citing two survey statistics and a vendor announcement; argument is reasoned opinion with field anecdotes, not original research.

## Entities Mentioned

- [ServiceNow](/entities/servicenow.md) — opened its system of action to agents via MCP
- [Model Context Protocol](/entities/model-context-protocol.md) — the interface exposing ServiceNow to outside agents

## Concepts Covered

- [Least privilege](/concepts/least-privilege.md) — the provisioning principle agents should inherit
- [agent identity](/concepts/agent-identity.md) — agents treated as credentialed non-human identities
- [AI Governance](/concepts/ai-governance.md) — extending identity programs to machines and agents
