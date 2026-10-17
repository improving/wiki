---
title: "agent identity"
type: "Concept"
description: "Treating agents as non-human identities subject to scoping, least privilege, and runtime policy like any principal."
created: '2026-10-17'
updated: '2026-10-17'
tags: [security, governance, identity]
sources:
  - "/sources/nobody-owns-the-agent.md"
  - "/sources/the-day-your-agent-got-its-own-email-address.md"
  - "/sources/the-four-layers-of-runtime-ai-governance.md"
  - "/sources/the-incident-rate-is-in.md"
  - "/sources/your-agents-are-principals-treat-them-like-it.md"
---

# agent identity

Agent identity is the practice of treating autonomous agents as first-class non-human principals — scoped, credentialed, and audited like any other identity. Across this corpus the argument is that agents break human security assumptions, so permissions rather than the model are the perimeter, and identity governance must bound their blast radius. Newer sources reframe it as an accountability problem as much as a tooling one: breaches are widespread, but named ownership and visibility are not.

## Key Claims

- 91% of organizations deployed agents, but only 10% have a governance strategy.
- Agents break human security assumptions: machine speed, dynamic permissions, and injectability.
- Indirect [prompt injection](/concepts/prompt-injection.md) is [OWASP](/entities/owasp.md)'s top LLM risk, with real CVEs; permissions, not the model, are the perimeter.
- Agents often run under over-provisioned, unaudited service accounts, so [Least privilege](/concepts/least-privilege.md) scoping bounds blast radius.
- A complete governance stack needs four sequential layers, with [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) the hardest and most commonly missing; [EU AI Act](/entities/eu-ai-act.md) Annex III high-risk obligations take effect on August 2.
- 88% of organizations deploying AI agents suffered a security breach within twelve months, yet only 7.2% name an individual formally accountable for agent behavior — an accountability gap, not a tooling gap.
- 92% of organizations lack full visibility into their AI identities, and teams share human credentials with agents precisely because dedicated agent identity does not exist.
- Google giving enterprise agents persistent, org-issued identities (their own email address) turns agent governance into an identity-architecture problem: you cannot audit what you cannot attribute, nor revoke access you never granted.
- The remediation prescription is concrete: registered OAuth clients, scoped short-lived tokens, and provenance-separated audit logs.
- Shared credentials leave agents functioning as ungoverned [shadow IT](/concepts/shadow-it.md) at ten times the speed.

## Related

- [Least privilege](/concepts/least-privilege.md) — scoping the agent perimeter
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — intercepting wrong actions before execution
- [prompt injection](/concepts/prompt-injection.md) — the top risk agents are exposed to
- [shadow IT](/concepts/shadow-it.md) — the failure mode shared agent credentials recreate at scale
- [AI Governance](/concepts/ai-governance.md) — the strategy most organizations lack
- [Your Agents Are Principals. Treat Them Like It.](/sources/your-agents-are-principals-treat-them-like-it.md) — primary source
