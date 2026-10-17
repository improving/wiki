---
title: "data quality"
type: "Concept"
description: "The accuracy, completeness, and consistency of data, treated as an engineered property with owners and gates."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, governance, quality]
sources:
  - "/sources/empowering-your-data-estate-modern-practices-for-data-quality.md"
  - "/sources/your-stakeholders-are-your-data-quality-system.md"
  - "/sources/garbage-in-garbage-out.md"
  - "/sources/data-debt-ai-predictions.md"
  - "/sources/real-time-is-the-easy-part.md"
---

# data quality

Data quality is the accuracy, completeness, and consistency of data, treated as an engineered property with named owners and enforced gates rather than a byproduct. Because AI systems amplify whatever data they learn from, poor quality produces confident wrong answers at scale, so quality must be measured, monitored, and enforced with the same rigor as code quality — long before modeling begins.

## Key Claims

- Seven foundations of quality: accessibility, accuracy, completeness, consistency, precision/relevance, timeliness, and observability.
- Poor data quality costs millions annually through error correction, missed opportunities, compliance penalties, and lost trust — cited consequences include incorrect credit scores affecting loan approvals and data errors leading to homes mistakenly demolished.
- A four-level data-maturity model runs Data Neutral (reactive, manual), Data Aware (basic validation, Excel/SQL), Data Critical (proactive governance, KPIs, audits), and Data Driven (AI-ready, embedded).
- In 2023, 74% of data professionals said stakeholders find data quality issues "all or most of the time" before the data team does, up from 47% the year before; mean time to resolution rose from roughly six hours in 2022 to fifteen hours in 2023.
- The average data team had 290 tests covering 24 dbt models (~12 tests per model), and untested tables are usually the legacy ones quietly wrong for months.
- Enforce quality with data contracts defining schemas, acceptable ranges, and update cadences, plus automated quality gates in CI/CD so missing, stale, or out-of-range data fails fast.
- Standard metrics can look green while data is silently missing, so quality needs black-box and white-box signals such as dead-letter-queue buildup, unreconciled events, and entity staleness.

## Related

- [data readiness](/concepts/data-readiness.md) — whether data is fit for AI at all
- [data debt](/concepts/data-debt.md) — the accumulated cost of letting quality slide
- [data contract](/concepts/data-contract.md) — the enforceable specification that gates it
- [data ownership](/concepts/data-ownership.md) — named accountability for outcomes
