---
title: "Okta"
type: "Entity"
description: "Identity platform cited in the corpus as the place where agent and human identities get governed, scoped, and audited."
created: '2026-10-17'
updated: '2026-10-17'
tags: [identity, security, governance]
sources:
  - "/sources/coalition-first-regulator-second.md"
  - "/sources/your-agents-are-principals-treat-them-like-it.md"
  - "/sources/the-market-just-valued-the-agent-security-gap-at-1-1-billion.md"
---

# Okta

Okta is the identity platform that anchors this corpus's argument that agents are non-human identities and must be governed like any other principal. It appears as the concrete place where permissions, scoping, and audit records live — the layer where security policy is actually enforced rather than promised. Its own survey data also supplies the market's clearest measure of the gap: most organizations have suffered agent security incidents while most still do not enforce access policies for AI identities.

## Overview

One post frames agents as principals at massive scale: 91% of organizations have deployed agents, but only 10% have a governance strategy. Agents break human security assumptions through machine speed, dynamic permissions, and injectability, and indirect prompt injection is OWASP's top LLM risk with real CVEs. The conclusion is that permissions, not the model, are the perimeter.

The coalition post supplies the accountability backdrop: over a hundred companies signed a letter admitting internal safeguards are insufficient alone, and a state subpoena demanded pre-incident testing records. Enterprises must retain timestamped testing records, not just vendor assurances — which makes identity platforms and their logs part of the evidence chain.

## Key Claims

- 91% of organizations deployed agents; only 10% have a governance strategy.
- Agents break human security assumptions: machine speed, dynamic permissions, injectable.
- Permissions, not the model, are the perimeter; scope them to bound blast radius.
- Over a hundred companies signed a letter admitting safeguards are insufficient alone.
- Enterprises must retain timestamped testing records, not just vendor assurances.
- Okta reports 88% of organizations saw AI agent security incidents this year, while 86% do not enforce access policies for AI identities.
- Obsidian Security raised $85M at a $1.1B valuation, pricing the enterprise risk of agents operating without access controls.

## Related

- [agent identity](/concepts/agent-identity.md) — the framing Okta operationalizes
- [Least privilege](/concepts/least-privilege.md) — the scoping discipline
- [AI Governance](/concepts/ai-governance.md) — the program around it
- [Audit Trail](/concepts/audit-trail.md) — the recordkeeping it supports
- [Your Agents Are Principals](/sources/your-agents-are-principals-treat-them-like-it.md) — primary source
