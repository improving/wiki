---
title: "Embedded Governance"
type: "Concept"
description: "Governance enforced inside platforms and engineering workflows rather than documented alongside them, so policy and lineage stay accurate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, platform, data]
sources:
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/why-80-of-governance-programs-fail-and-what-the-other-20-do-differently.md"
---

# Embedded Governance

Embedded governance puts policy, access control, and lineage inside the compute and storage layers that engineers already use, rather than in a separate catalog or review committee. Across this corpus it is the durable alternative to [bolt-on governance](/concepts/bolt-on-governance.md): enforcement happens at runtime, so the recorded policy matches reality instead of drifting.

## Key Claims

- Databricks Unity Catalog and Snowflake Horizon put governance inside the platform.
- Runtime-captured lineage stays accurate where manual lineage documentation drifts.
- dbt contracts and access controls bring embedded governance to the transformation layer.
- Multi-engine estates still lack cross-catalog policy synchronization.
- Gartner predicts 80% of data and analytics governance initiatives will fail by 2027.
- Successful programs pick a specific outcome, embed governance in engineering workflows, and establish real ownership; only 42.3% of organizations have well-established data and AI ethics policies.

## Related

- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the pattern embedded governance replaces
- [Data Governance](/concepts/data-governance.md) — the broader discipline
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — how embedded policy is applied
- [Runtime Lineage](/concepts/runtime-lineage.md) — lineage captured at execution rather than by hand
- [Governance Belongs in the Platform, Not Next to It](/sources/governance-belongs-in-the-platform-not-next-to-it.md) — primary source
- [Why 80% of Governance Programs Fail (And What the Other 20% Do Differently)](/sources/why-80-of-governance-programs-fail-and-what-the-other-20-do-differently.md) — primary source
