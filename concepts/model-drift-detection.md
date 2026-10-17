---
title: "Model Drift Detection"
type: "Concept"
description: "Continuously monitoring deployed models for behavior change, a monitoring layer in a runtime AI governance control plane."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, monitoring, runtime]
sources:
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/the-four-layers-of-runtime-ai-governance.md"
---

# Model Drift Detection

Model drift detection is the practice of continuously watching deployed models for changes in behavior, quality, or distribution so that degradation is caught while it is happening rather than in a post-mortem. In this corpus it is one layer of a runtime AI governance stack, and its value depends on the layers beneath it: you cannot monitor an inventory you have not built.

## Key Claims

- AI governance is data governance with the safety margin removed, so it must be a runtime control plane, not a policy document.
- A policy document cannot see, stop, or detect violations; a control plane can.
- Four layers — policy, inventory, monitoring, enforcement — form a dependency chain, and most organizations invest in the wrong one.
- Runtime enforcement is the only layer that intercepts wrong actions before they execute.
- Only 8 percent of organizations rated their governance program highly successful.
- EU AI Act Annex III high-risk obligations take effect on August 2.

## Related

- [AI Governance](/concepts/ai-governance.md) — the program drift detection serves
- [Control plane](/concepts/control-plane.md) — the architecture that makes monitoring live
- [AI Inventory](/concepts/ai-inventory.md) — the layer monitoring depends on
- [Quiet Drift](/concepts/quiet-drift.md) — undetected drift in agent behavior
- [runtime governance](/concepts/runtime-governance.md) — the broader runtime discipline
- [Governance as the Control Plane for AI](/sources/governance-as-the-control-plane-for-ai.md) — primary source
- [The Four Layers of Runtime AI Governance](/sources/the-four-layers-of-runtime-ai-governance.md) — primary source
