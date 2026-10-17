---
title: "Databricks"
type: "Entity"
description: "Data and AI platform whose Unity Catalog embeds governance, lineage, and asset discovery directly in the compute layer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [platform, data-governance, unity-catalog]
sources:
  - "/sources/from-cop-to-coach-when-governance-stopped-being-about-control.md"
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/nobody-is-building-a-separate-silo-for-ai-assets-anymore.md"
  - "/sources/the-catalog-is-now-the-control-plane.md"
  - "/sources/the-fourth-principle-federated-governance-and-the-hardest-problem-in-data-mesh.md"
  - "/sources/the-policy-binder-didnt-change-anyones-behavior.md"
---

# Databricks

Databricks is a data and AI platform cited across this corpus as the leading example of governance embedded in the platform rather than bolted on beside it. Its Unity Catalog has widened from tables to models, functions, agents, and MCP services.

## Overview

Writers use Databricks to argue that runtime-captured lineage stays accurate where manual documentation drifts. Blue Cross Blue Shield of Minnesota encoded federated governance into a Databricks medallion platform with Unity Catalog and an onboarding framework, and California's DHCS rebuilt its platform with governance engineered into the pipeline.

## Key Claims

- Unity Catalog and Snowflake Horizon put governance inside the compute and storage layer.
- Runtime-captured lineage stays accurate where manual lineage documentation drifts.
- Databricks widened Unity Catalog to govern models, functions, agents, and MCP services.
- Multi-engine estates still lack cross-catalog policy synchronization.
- BCBSM used Unity Catalog plus an onboarding framework to make federated governance computational.

## Related

- [Unity Catalog](/entities/unity-catalog.md) — Databricks' governance layer
- [Embedded Governance](/concepts/embedded-governance.md) — the pattern Databricks exemplifies
- [Data Mesh](/concepts/data-mesh.md) — federated governance context
- [Governance Belongs in the Platform, Not Next to It](/sources/governance-belongs-in-the-platform-not-next-to-it.md) — primary source
