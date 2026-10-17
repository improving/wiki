---
title: "AI Inventory"
type: "Concept"
description: "A live registry of the models, agents, and integrations an organization runs, and the layer runtime governance depends on."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, ai, inventory, control-plane]
sources:
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/nobody-owns-the-agent.md"
  - "/sources/the-agent-governance-stack-is-finally-here.md"
  - "/sources/the-four-layers-of-runtime-ai-governance.md"
  - "/sources/you-cant-govern-an-inventory-you-dont-know-you-have.md"
---

# AI Inventory

An AI inventory is the authoritative, continuously maintained record of which models, agents, service accounts, and integrations an organization is actually running. Across this corpus it is treated not as paperwork but as a load-bearing layer: without a current inventory, no policy can be scoped and no enforcement can be targeted. Newer sources show the market converging on the same sequence — inventory first, then control — and treat the missing inventory as a policy failure rather than a missing product.

## Key Claims

- Governance is described as a four-layer dependency chain — policy, inventory, monitoring, enforcement — where each layer needs the one beneath it; the inventory is what makes the others concrete.
- A policy document cannot see, stop, or detect a violation; a runtime control plane can, but only for assets it knows about.
- Agents frequently run under over-provisioned, unaudited service accounts, so an inventory must track identity and entitlements, not just model names.
- Only 8 percent of organizations rated their governance program highly successful, which one post attributes to investing in the wrong layer.
- EU AI Act Annex III high-risk obligations taking effect on August 2 make a defensible inventory a compliance prerequisite, not a nice-to-have.
- Five enterprise agent-governance products shipped within a thirteen-day window, and every one follows the same pattern — inventory first, then control — which the corpus reads as the market answering a tooling gap rather than a philosophy debate.
- One OutSystems survey found 96% of enterprises run agents but only 12% have central management, because agents were deployed at team level with no central registration.
- The named failure mode is "agent sprawl": unchecked employee agent creation, which Dataiku flags and Broadcom addresses by verifying agent identity and mission before authorizing action.
- The prescribed fix is a policy, not a platform purchase: register, name, and assign an owner before production — an "Agentic Landing Zone" is a decision, not a product.
- Only 7.2% of organizations name an individual formally accountable for agent behavior, so an inventory that does not record ownership is incomplete.

## Related

- [AI Governance](/concepts/ai-governance.md) — the broader program the inventory serves
- [agent identity](/concepts/agent-identity.md) — the identity and entitlement detail an inventory must carry
- [Control plane](/concepts/control-plane.md) — the runtime machinery the inventory feeds
- [runtime governance](/concepts/runtime-governance.md) — enforcement that depends on an accurate inventory
- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the manual, drifting alternative this layer replaces
- [Governance as the Control Plane for AI](/sources/governance-as-the-control-plane-for-ai.md) — primary source
- [The Four Layers of Runtime AI Governance](/sources/the-four-layers-of-runtime-ai-governance.md) — primary source
