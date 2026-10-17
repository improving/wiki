---
title: "Runtime Lineage"
type: "Concept"
description: "Lineage captured automatically as a byproduct of execution, staying accurate where manually documented catalogs drift."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, metadata, data]
sources:
  - "/sources/from-cop-to-coach-when-governance-stopped-being-about-control.md"
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
---

# Runtime Lineage

Runtime lineage is the record of where data came from and how it changed, captured automatically as a byproduct of the system doing its work rather than documented by hand after the fact. This corpus traces the idea to Gartner's 2021 retirement of its Metadata Management Magic Quadrant in favor of *active metadata*: passive catalogs go stale because curation is underfunded manual labor, while runtime-captured lineage stays accurate because it is produced by execution itself. The practical consequence is that governance moves inside the platform — into the compute and storage layer — instead of living in a bolt-on catalog beside it.

## Key Claims

- Gartner retired its Metadata Management Magic Quadrant for Active Metadata Management in 2021.
- Active metadata is captured automatically as a byproduct of system operation.
- Passive catalogs go stale because curation is underfunded manual work.
- Runtime-captured lineage stays accurate where manual lineage documentation drifts.
- Databricks Unity Catalog and Snowflake Horizon put governance inside the platform; dbt contracts and access controls bring it to the transformation layer.
- Governance framed as enablement wins data-team support that compliance framing cannot.
- Multi-engine estates still lack cross-catalog policy synchronization.

## Related

- [Active Metadata](/concepts/active-metadata.md) — the automatic-capture principle behind runtime lineage
- [Data Catalog](/concepts/data-catalog.md) — the passive artifact runtime lineage improves on
- [Embedded Governance](/concepts/embedded-governance.md) — placing governance in the platform layer
- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the stale catalog pattern this replaces
- [metadata knowledge graph](/concepts/metadata-knowledge-graph.md) — a structure runtime lineage can populate
- [Unity Catalog](/entities/unity-catalog.md) — a platform that embeds runtime governance
- [Governance Belongs in the Platform, Not Next to It](/sources/governance-belongs-in-the-platform-not-next-to-it.md) — primary source
