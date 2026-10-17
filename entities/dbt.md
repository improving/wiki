---
title: "dbt"
type: "Entity"
description: "Data transformation tool whose contracts and access controls bring embedded governance to the analytics transformation layer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data-tooling, transformation, governance]
sources:
  - "/sources/governance-belongs-in-the-platform-not-next-to-it.md"
  - "/sources/the-data-contract-is-an-api-for-trust.md"
---

# dbt

A SQL-first data transformation framework that the corpus treats as the place where governance reaches the transformation layer. Its contracts and access controls are cited as the practical mechanism for making [data contracts](/concepts/data-contract.md) enforceable rather than documentary.

## Overview

dbt sits alongside platform-native catalogs like [Unity Catalog](/entities/unity-catalog.md) and Snowflake Horizon in the [embedded governance](/concepts/embedded-governance.md) story: policy lives in the tool that builds the data, not in a bolt-on catalog. Contracts declare schema and expectations that the build validates, shifting accountability to producers.

## Key Claims

- dbt contracts and access controls bring embedded governance to the transformation layer.
- Enforcement at build time makes a contract a specification the system checks, not documentation.
- This complements runtime-captured [lineage](/concepts/runtime-lineage.md), which stays accurate where manual lineage documentation drifts.
- Multi-engine estates still lack cross-catalog policy synchronization, a gap dbt alone does not close.

## Related

- [Data Contract](/concepts/data-contract.md) — enforced through dbt
- [Embedded Governance](/concepts/embedded-governance.md) — the pattern dbt implements
- [Databricks](/entities/databricks.md) — platform whose Unity Catalog pairs with dbt
- [Governance Belongs in the Platform, Not Next to It](/sources/governance-belongs-in-the-platform-not-next-to-it.md) — source
