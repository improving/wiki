---
title: "Least privilege"
type: "Concept"
description: "Granting agents and services only the access each action needs, enforced at runtime rather than assumed from policy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, security, access-control]
sources:
  - "/sources/governance-is-not-overhead-it-is-the-engine-of-trust.md"
  - "/sources/your-ai-governance-policy-is-not-governance.md"
  - "/sources/your-agents-have-keys-nobody-changed-the-locks.md"
---

# Least privilege

Least privilege is the principle that any actor — human, service, or agent — should hold only the access required for the action it is performing, and no more. Across this corpus it appears as a core component of AI governance: because agents execute at machine speed and cannot exercise judgment, access must be constrained architecturally rather than trusted. The same lens treats agents as non-human identities that deserve the provisioning, auditing, and revocation lifecycle granted to human employees — and finds that most organizations extend them none of it.

## Key Claims

- Access control is one of five governance components named alongside audit trails, boundary enforcement, quality gates, and human approval.
- A written policy cannot stop a bad access attempt; only runtime enforcement can, at the moment each action executes.
- Governance must be code executing at machine speed, not committee review that happens after the fact.
- Agents frequently run under over-provisioned, unaudited service accounts, so access is broader than intended.
- The practical test: ask what would happen if an agent tried to access restricted data right now.
- Agents are non-human identities, but they rarely get an onboarding checklist, role-based access, or an offboarding step, so privileges accumulate and are never revoked ([your agents have keys](/sources/your-agents-have-keys-nobody-changed-the-locks.md)).
- The gap is measurable: 92% of security leaders lack visibility into what agent access exists, and 86% enforce no policy over it.
- The recommended discipline mirrors human lifecycle management — apply least privilege, audit access regularly, and revoke on role or mission change — especially as platforms like ServiceNow open their systems to agents through MCP and widen the attack surface.

## Related

- [Boundary enforcement](/concepts/boundary-enforcement.md) — enforces where an agent may act
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the layer that applies least privilege live
- [agent identity](/concepts/agent-identity.md) — scoping access requires knowing which agent is acting
- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — narrowing reachable data before retrieval
- [Governance Is Not Overhead. It Is the Engine of Trust.](/sources/governance-is-not-overhead-it-is-the-engine-of-trust.md) — primary source
- [Your AI Governance Policy Is Not Governance](/sources/your-ai-governance-policy-is-not-governance.md) — primary source
