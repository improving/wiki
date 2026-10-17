---
title: "Your Stakeholders Are Your Data Quality System"
type: "Source Summary"
description: "Argues manual data testing did not scale, so governance must run in the pipeline via contracts, ownership, and observability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/your-stakeholders-are-your-data-quality-system/your-stakeholders-are-your-data-quality-system.md"
---

# Your Stakeholders Are Your Data Quality System — Summary

**Original source**: `references/devlinliles.com/your-stakeholders-are-your-data-quality-system/your-stakeholders-are-your-data-quality-system.md`

## Summary

The post argues that because manual data testing scales with engineering time while the data estate scales with business complexity, the end user has become the de facto data quality monitor at most organizations. It traces the response: statistical observability to catch unforeseen breakage, [data ownership](/concepts/data-ownership.md) established before tooling, and [data contracts](/concepts/data-contract.md) enforced at build time by dbt Core v1.5's access, contracts, and versions primitives. Its core claim is that governance running inside the system — [policy as code](/concepts/policy-as-code.md) — is the only kind that covers the whole estate.

## Key Claims

- In 2023, 74% of data professionals said stakeholders find data quality issues "all or most of the time" before the data team does, up from 47% the year before (a 57% increase).
- Mean time to resolution for data incidents rose from roughly six hours in 2022 to fifteen hours in 2023.
- The average data team had 290 tests covering 24 dbt models (~12 tests per model), and untested tables are usually the legacy ones that have been quietly wrong for months.
- dbt Core v1.5 (April 2023) shipped access, contracts, and versions — governance enforced by the build tool rather than documented in a catalog.
- Deploying observability without first establishing ownership is the most common mistake; it produces alerts no team owns, stretching resolution from hours to a week.

## Relevance

Informs [data contracts](/concepts/data-contract.md), [data ownership](/concepts/data-ownership.md), and [policy as code](/concepts/policy-as-code.md), with ties to [data governance](/concepts/data-governance.md) and observability practice.

## Quality

Practitioner blog post by Devlin Liles. Well-sourced with named surveys and release notes, and grounded in a real engagement; the dbt/dagster stack specifics are case-specific.

## Entities Mentioned

- [Snowflake](/entities/snowflake.md) — platform for the Ascend data platform
- [Ascend](/entities/ascend.md) — charter school system and case study partner
- [dbt](/entities/dbt.md) — tool whose v1.5 contracts provide build-time governance
- [Improving](/entities/improving.md) — consultancy that built the platform

## Concepts Covered

- [Data Contract](/concepts/data-contract.md) — declared schema enforced at compile time
- [Policy as Code](/concepts/policy-as-code.md) — governance executing as a side effect of engineering
- [Data Ownership](/concepts/data-ownership.md) — the prerequisite governance move
- [Data Governance](/concepts/data-governance.md) — the broader discipline the post reframes
