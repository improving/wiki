---
title: "The Incident Rate Is In"
type: "Source Summary"
description: "Strata research showing 88% of enterprises had an agent security incident ends the forward-looking framing; agent identity is now a remediation architecture decision."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, driventodevelop.com]
sources:
  - "references/driventodevelop.com/the-incident-rate-is-in/the-incident-rate-is-in.md"
---

# The Incident Rate Is In — Summary

**Original source**: `references/driventodevelop.com/the-incident-rate-is-in/the-incident-rate-is-in.md`

## Summary

O'Hara says his two-year framing of agent security as a risk to manage before something goes wrong has been overtaken by data: Strata's 2026 research on enterprise AI identity found 88% of organizations reported a confirmed or suspected AI agent security incident in the past year, and 92% lack full visibility into their AI identities. The root cause is specific — teams share human credentials and access tokens with agents because no dedicated agent identity infrastructure exists, so agents inherit the access of whoever set them up, reaching ERP, CRM, and financial data with no scope limit and no audit trail separating agent actions from human ones. He describes the fix as an architecture decision, and notes the client conversation must be reframed from prevention to detection and response.

## Key Claims

- 88% of organizations reported a confirmed or suspected AI agent security incident in the last year; 92% lack full visibility into their AI identities.
- Teams share human credentials and access tokens with agents because no dedicated agent identity infrastructure exists.
- Agents run with the same access as the person who set them up, reaching ERP systems, CRMs, and financial data with no scope limitation.
- No audit trail distinguishes agent actions from human actions, so incidents cannot be attributed.
- The technical fix: registered OAuth clients per agent, short-lived scoped tokens, per-task authorization, and audit logs tracking agent provenance separately from human provenance — architecture that follows the governance you want.

## Relevance

Central to [agent identity](/concepts/agent-identity.md), [AI Governance](/concepts/ai-governance.md), and [Audit Trail](/concepts/audit-trail.md), and connects to [Least privilege](/concepts/least-privilege.md) and [Independent Verification](/concepts/independent-verification.md).

## Quality

Practitioner blog post by David O'Hara. Cites specific survey percentages and a concrete remediation pattern, but is also a soft pitch for Improving's Agentic Landing Zone offering.

## Entities Mentioned

- [Improving](/entities/improving.md) — offers the Agentic Landing Zone approach described

## Concepts Covered

- [agent identity](/concepts/agent-identity.md) — dedicated identity infrastructure as the root fix
- [AI Governance](/concepts/ai-governance.md) — reframing from prevention to incident response
- [Audit Trail](/concepts/audit-trail.md) — separating agent provenance from human provenance
- [Least privilege](/concepts/least-privilege.md) — short-lived scoped tokens and per-task authorization
- [Independent Verification](/concepts/independent-verification.md) — visibility into what agents did and where
