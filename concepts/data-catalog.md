---
title: "Data Catalog"
type: "Concept"
description: "A searchable inventory of data and AI assets whose value depends on active, continuously current metadata."
created: '2026-10-17'
updated: '2026-10-17'
tags: [metadata, governance, discovery]
sources:
  - "/sources/from-cop-to-coach-when-governance-stopped-being-about-control.md"
  - "/sources/the-audit-trail-is-the-product-not-the-camera.md"
  - "/sources/the-catalog-already-learned-to-talk-to-machines.md"
---

# Data Catalog

A data catalog is an inventory of an organization's data and AI assets — datasets, prompts, agents — with the metadata needed to find and trust them. Across this corpus the catalog's value depends less on the software than on whether its metadata stays current, which favors active metadata captured from systems over passive manual curation.

## Key Claims

- Passive catalogs go stale because curation is underfunded manual work; they are only as current as the last human update.
- Gartner retired its Metadata Management Magic Quadrant for Active Metadata Management in 2021, reframing governance from control to enablement.
- Active metadata is captured automatically as a byproduct of system operation and wired into source systems, keeping descriptions continuously current.
- A metadata knowledge graph models prompt–model–data relationships that flat keyword entries cannot.
- Audit trails are passive governance checked after the fact; data governance fixed this by enforcing policy before a disallowed query executes.
- Retrieval over catalog metadata differs from retrieval over prompt content.

## Related

- [Active Metadata](/concepts/active-metadata.md) — what keeps a catalog from going stale
- [metadata knowledge graph](/concepts/metadata-knowledge-graph.md) — the graph shape catalogs need for machine retrieval
- [Data Governance](/concepts/data-governance.md) — enforcement that makes cataloged assets trustworthy
- [Audit Trail](/concepts/audit-trail.md) — the passive counterpart to runtime enforcement
- [Data Mesh](/concepts/data-mesh.md) — federated discovery across domain-owned catalogs
- [The Catalog Already Learned to Talk to Machines](/sources/the-catalog-already-learned-to-talk-to-machines.md) — primary source
