---
title: "Governance Belongs in the Platform, Not Next to It"
type: "Source Summary"
description: "Between 2021 and 2024 governance moved inside the compute and storage layer, replacing bolt-on catalogs with embedded, runtime enforcement."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/governance-belongs-in-the-platform-not-next-to-it/governance-belongs-in-the-platform-not-next-to-it.md"
---

# Governance Belongs in the Platform, Not Next to It — Summary

**Original source**: `references/devlinliles.com/governance-belongs-in-the-platform-not-next-to-it/governance-belongs-in-the-platform-not-next-to-it.md`

## Summary

Devlin Liles describes the 2021–2024 architectural shift in which governance moved from a separate catalog bolted onto the platform to a layer embedded inside the compute and storage tier. Databricks' Unity Catalog and Snowflake's Horizon both bet that governance should live where data actually moves, governing access control, [runtime lineage](/concepts/runtime-lineage.md), and audit logs below the engines that touch the data. He illustrates the shift with the BCBSM lakehouse implementation and the Snowflake-plus-dbt approach used for Ascend.

## Key Claims

- In a bolt-on model, lineage is human-documented and drifts immediately; in an [embedded](/concepts/embedded-governance.md) catalog it is observed at runtime from actual execution.
- At BCBSM, every asset across eleven domains, 133 subdomains, and 88-plus suppliers was governed through Unity Catalog, with column-level PHI/PII control and HIPAA-satisfying audit logs, across six SCAN security approvals.
- For Ascend, dbt contracts, access declarations, and versioning enforce [governance at the transformation layer](/concepts/data-contract.md): a schema violation or unauthorized reference fails the build before the table materializes.
- The honest caveat is multi-engine estates: Unity Catalog and Snowflake Horizon do not synchronize policies, and fine-grained policy does not yet carry cleanly across catalog boundaries, even as vendors converge on the Iceberg REST Catalog standard.
- The fix is deliberate architecture — decide which catalog is authoritative — not a retreat to bolt-on tooling.

## Relevance

Central to the [embedded governance](/concepts/embedded-governance.md) versus [bolt-on governance](/concepts/bolt-on-governance.md) distinction, and a foundation for [Data Governance](/concepts/data-governance.md) and [AI Governance](/concepts/ai-governance.md).

## Quality

Practitioner blog post by Devlin Liles. Concrete and technically specific with two named client cases; vendor-sourced framing and no independent measurement.

## Entities Mentioned

- [Unity Catalog](/entities/unity-catalog.md) — the embedded governance layer in the BCBSM case
- [Databricks](/entities/databricks.md) — platform whose 2021 announcement started the shift
- [dbt](/entities/dbt.md) — transformation-layer governance for the Ascend build
- [Blue Cross Blue Shield of Minnesota](/entities/blue-cross-blue-shield-of-minnesota.md) — large-scale lakehouse governance case
- [Snowflake](/entities/snowflake.md) — Horizon as the competing embedded catalog
- [Ascend](/entities/ascend.md) — charter school system built on Snowflake and dbt

## Concepts Covered

- [Embedded Governance](/concepts/embedded-governance.md) — governance inside the platform
- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the separate-catalog model it replaced
- [Runtime Lineage](/concepts/runtime-lineage.md) — lineage captured at execution, not documented
- [Data Contract](/concepts/data-contract.md) — schema and compatibility enforced at build time
- [Data Governance](/concepts/data-governance.md) — the discipline being relocated
- [AI Governance](/concepts/ai-governance.md) — the downstream payoff of governed training data
- [Control plane](/concepts/control-plane.md) — the catalog as the enforcement point
