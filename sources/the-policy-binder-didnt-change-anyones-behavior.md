---
title: "The Policy Binder Didn't Change Anyone's Behavior"
type: "Source Summary"
description: "Governance frameworks of 2019–2021 failed because policy lived apart from engineering; the fix was embedding governance in the pipeline."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-policy-binder-didnt-change-anyones-behavior/the-policy-binder-didnt-change-anyones-behavior.md"
---

# The Policy Binder Didn't Change Anyone's Behavior — Summary

**Original source**: `references/devlinliles.com/the-policy-binder-didnt-change-anyones-behavior/the-policy-binder-didnt-change-anyones-behavior.md`

## Summary

Argues the 2019–2021 data governance gap was behavioral, not documentary. Only 8% of organizations rated their governance programs highly successful, and the top barriers were adherence and usability rather than budget or technology. The structural cause was bolt-on architecture: governance as a separate catalog maintained by hand, with no feedback loop to reinforce the behavior. The DHCS engagement serves as the counter-example, where governance was engineered into the Databricks pipeline and cataloging workflow rather than documented alongside it, so metadata traveled with the data.

## Key Claims

- In 2020 only 8% of organizations that had formal governance programs rated them highly successful.
- TDWI's top two barriers were "convincing employees to adhere to governance policies" (46%) and "creating policies that are clear and usable" (43%).
- Gartner pegged poor data quality at an average of $12.9 million per year, drawn from a 2020 survey of 154 data quality tool customers.
- DHCS's behavioral health data was fragmented across Excel spreadsheets, Microsoft Access databases, and a legacy Teradata warehouse with a decade of undocumented assumptions.
- The industry's response was architectural — active metadata, data contracts, platform-native governance, and observability — all attempts to answer the behavioral problem with a mechanical solution.

## Relevance

Informs [bolt-on governance](/concepts/bolt-on-governance.md), [policy as code](/concepts/policy-as-code.md), and [embedded governance](/concepts/embedded-governance.md) within the ai-governance cluster.

## Quality

Practitioner blog post by Devlin Liles. Mixes cited third-party survey figures with a first-hand client case study; the DHCS narrative is single-case evidence and the monetary figures are survey data.

## Entities Mentioned

- [Collibra](/entities/collibra.md) — catalog integrated into the DHCS data workflow
- [Databricks](/entities/databricks.md) — platform the DHCS data platform was rebuilt on
- [Snowflake](/entities/snowflake.md) — named as a store in the bolt-on pattern
- [California Department of Health Care Services](/entities/california-department-of-health-care-services.md) — the modernization case study
- [Gartner](/entities/gartner.md) — source of the $12.9M data-quality figure

## Concepts Covered

- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the structural root of the problem
- [Policy as Code](/concepts/policy-as-code.md) — the architectural response it sets up
- [Active Metadata](/concepts/active-metadata.md) — metadata that travels with the data
- [Data Contract](/concepts/data-contract.md) — one of the mechanical fixes named
- [Embedded Governance](/concepts/embedded-governance.md) — governance engineered into the pipeline
- [Data Catalog](/concepts/data-catalog.md) — the hand-maintained catalog it criticizes
