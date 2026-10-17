---
title: "The Four Layers of Runtime AI Governance"
type: "Source Summary"
description: "Lays out a four-layer AI governance stack and argues runtime policy enforcement is the hardest, most absent layer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-four-layers-of-runtime-ai-governance/the-four-layers-of-runtime-ai-governance.md"
---

# The Four Layers of Runtime AI Governance — Summary

**Original source**: `references/devlinliles.com/the-four-layers-of-runtime-ai-governance/the-four-layers-of-runtime-ai-governance.md`

## Summary

Written ahead of the EU AI Act's August 2 Annex III obligations, this post argues most organizations have invested in the wrong governance layer. A complete stack runs in sequence across four layers: policy and compliance management, AI inventory and shadow AI discovery, model monitoring and drift detection, and runtime policy enforcement. Runtime enforcement is the hardest and most absent layer, and agent identity is the overlooked control.

## Key Claims

- The four layers work in sequence and each depends on the one below; a runtime gateway enforces nothing if no policy pack exists, so the sequence cannot be shortcut.
- Coverage is uneven: most large enterprises have meaningful layer-one coverage, fewer than half have done a real AI inventory, monitoring is spotty, and runtime enforcement is almost entirely absent.
- Runtime enforcement is the only layer that intercepts a wrong action before it happens and where "audit-ready" means the record was generated at the moment of decision.
- Agent identity is the control nobody discusses: agents often run under over-provisioned, unaudited service accounts whose blast radius rivals privileged human identity.
- With five weeks left, start with a shadow AI audit and close the highest-risk layer gap in sequence rather than attempting all four at once.

## Relevance

Defines [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md), [AI Inventory](/concepts/ai-inventory.md), [Model Drift Detection](/concepts/model-drift-detection.md), and [agent identity](/concepts/agent-identity.md); touches the [audit trail](/concepts/audit-trail.md) and [least privilege](/concepts/least-privilege.md).

## Quality

Practitioner blog post by Devlin Liles. Strong on distinguishing the layers, but the coverage statistics are impressionistic and the vendor mentions are illustrative.

## Entities Mentioned

- [Microsoft Purview](/entities/microsoft-purview.md) — default layer-one tooling for Microsoft 365 and Azure environments
- [EU AI Act](/entities/eu-ai-act.md) — Annex III deadline that drives the post

## Concepts Covered

- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the gateway that intercepts wrong actions
- [AI Inventory](/concepts/ai-inventory.md) — discovering sanctioned and shadow AI usage
- [Model Drift Detection](/concepts/model-drift-detection.md) — continuous production monitoring
- [agent identity](/concepts/agent-identity.md) — the non-human identity control
- [audit trail](/concepts/audit-trail.md) — records generated at the moment of decision
- [least privilege](/concepts/least-privilege.md) — auditing agent service-account permissions
