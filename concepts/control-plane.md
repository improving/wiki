---
title: "Control plane"
type: "Concept"
description: "The stateless signaling and policy layer that is separated from the stateful data plane so each can scale."
created: '2026-10-17'
updated: '2026-10-17'
tags: [architecture, governance, scalability]
sources:
  - "/sources/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md"
  - "/sources/the-catalog-is-now-the-control-plane.md"
---

# Control plane

The control plane is the layer that makes decisions, signals state changes, and enforces policy, kept distinct from the data plane that carries stateful work. It matters across this corpus in two settings: real-time media, where stateless signaling must scale separately from stateful relays, and data governance, where the catalog is becoming the control plane that executes policy at runtime.

## Key Claims

- Signaling is short-lived and stateless, while media relay is long-lived and stateful, so the two scale on different terms.
- The control plane scales horizontally behind a standard load balancer; stateful media sessions cannot.
- Entangling the planes forces a rebuild, not a config change, under load.
- In governance, Gartner replaced its metadata management quadrant with a governance platforms quadrant, signaling consolidation into unified AI-augmented catalogs.
- The catalog becomes the control plane so policy follows data across engines, rather than living in committees.
- Programs that keep governance as bolt-on compliance still face an 80% failure rate.

## Related

- [Media relay](/concepts/media-relay.md) — the stateful data plane counterpart
- [Data Catalog](/concepts/data-catalog.md) — the governance control plane
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — what a control plane executes
- [Gartner](/entities/gartner.md) — source of the quadrant consolidation signal
- [Split the Control Plane From the Data Plane](/sources/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md) — media architecture source
- [The Catalog Is Now the Control Plane](/sources/the-catalog-is-now-the-control-plane.md) — governance source
