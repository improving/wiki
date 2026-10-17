---
title: "Bolt-on Governance"
type: "Concept"
description: "Governance implemented as separate documents and manual catalogs beside the pipeline, which drifts stale and changes no behavior."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, data, platforms]
sources:
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/the-policy-binder-didnt-change-anyones-behavior.md"
---

# Bolt-on Governance

Bolt-on governance is the pattern of adding policy documents, catalogs, and review processes alongside a data or AI pipeline rather than inside it. Across this corpus it is named as the reason governance programs fail: it depends on manual curation, drifts out of date, and never touches the moment where a decision is actually made.

## Key Claims

- Only 8 percent of organizations rated their data governance programs highly successful in 2020.
- The top barriers were behavioral — policy adherence and usability — not budget.
- Bolt-on governance left catalogs stale and unused because curation was manual.
- The alternative is embedding governance in the compute and storage layer: Databricks Unity Catalog and Snowflake Horizon put governance inside the platform.
- Runtime-captured lineage stays accurate where manual lineage documentation drifts.
- dbt contracts and access controls bring embedded governance to the transformation layer.
- Multi-engine estates still lack cross-catalog policy synchronization.
- The California Department of Health Care Services (DHCS) rebuilt its platform with governance engineered into the pipeline.

## Related

- [Embedded Governance](/concepts/embedded-governance.md) — the in-platform alternative
- [Data Governance](/concepts/data-governance.md) — the discipline this pattern undermines
- [Data Catalog](/concepts/data-catalog.md) — the artifact that goes stale under manual curation
- [Runtime Lineage](/concepts/runtime-lineage.md) — lineage captured at runtime instead of documented
- [AI Inventory](/concepts/ai-inventory.md) — the governed asset registry this approach leaves incomplete
- [automated testing](/concepts/automated-testing.md) — the in-pipeline discipline that shows what embedded enforcement looks like
- [Governance Belongs in the Platform, Not Next to It](/sources/governance-belongs-in-the-platform-not-next-to-it.md) — primary source
- [The Policy Binder Didn't Change Anyone's Behavior](/sources/the-policy-binder-didnt-change-anyones-behavior.md) — primary source
