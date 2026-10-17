---
title: "The Catalog Is Now the Control Plane"
type: "Source Summary"
description: "Gartner's governance-platform consolidation and vendor interoperability bets point to the catalog as the single control plane for data and AI."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-catalog-is-now-the-control-plane/the-catalog-is-now-the-control-plane.md"
---

# The Catalog Is Now the Control Plane — Summary

**Original source**: `references/devlinliles.com/the-catalog-is-now-the-control-plane/the-catalog-is-now-the-control-plane.md`

## Summary

Gartner's 2021 retirement of the Metadata Management Magic Quadrant and its 2025 launch of the Data and Analytics Governance Platforms Magic Quadrant mark governance's consolidation into a single [control plane](/concepts/control-plane.md) spanning data and AI. The post separates three AI-augmented catalog capabilities — automated metadata generation, semantic search and discovery, and agentic governance — and argues the catalog, not a committee, is becoming the authoritative governance layer. Both Databricks and Snowflake are betting on this via open standards.

## Key Claims

- The four-year Gartner arc, from a 2021 market guide to a 2025 Magic Quadrant, signals point tools converging into unified data-and-AI governance platforms.
- Three distinct capabilities hide under "AI-augmented catalog": automated metadata generation, semantic search, and agentic governance.
- Alation (Numbers Station AI, May 2025) and Collibra (Deasy Labs, July 2025) are building governance that acts — detecting violations and triggering remediation — not just observes.
- Databricks open-sourced Unity Catalog under the Linux Foundation in mid-2024 and added Apache Iceberg REST Catalog support; Snowflake's Horizon is built on Apache Polaris, the same standard.
- The series opened with 8% of governance programs highly successful; the 80% failure prediction still holds for programs that never move governance into the platform.

## Relevance

Central to [AI governance](/concepts/ai-governance.md) and [data governance](/concepts/data-governance.md), illustrating [embedded governance](/concepts/embedded-governance.md) and [runtime governance](/concepts/runtime-governance.md) where policies execute in the platform.

## Quality

Practitioner blog post by Devlin Liles. Strong on dated vendor, standards, and survey specifics; the 80% failure figure and the direction-of-travel claims are the author's framing rather than measured outcomes.

## Entities Mentioned

- [Gartner](/entities/gartner.md) — its Magic Quadrant shifts date the market consolidation
- [Unity Catalog](/entities/unity-catalog.md) — the governed-data layer behind the BCBSM examples and the open-sourced control plane
- [Databricks](/entities/databricks.md) — open-sourced Unity Catalog and backs the interoperability bet
- [Snowflake](/entities/snowflake.md) — Horizon/Polaris side of the same interoperability bet
- [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) — case study for governed-data AI (Genie, Mosaic AI, MLflow)

## Concepts Covered

- [control plane](/concepts/control-plane.md) — the catalog as the unified governance layer
- [AI governance](/concepts/ai-governance.md) — governance extended to models, RAG content, and unstructured data
- [data governance](/concepts/data-governance.md) — the discipline consolidating into that platform
- [embedded governance](/concepts/embedded-governance.md) — governance running in the platform rather than a committee
- [runtime governance](/concepts/runtime-governance.md) — policies executing at runtime
