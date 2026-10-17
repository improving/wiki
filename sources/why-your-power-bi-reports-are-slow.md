---
title: "Why Your Power BI Reports Are Slow — And How a Custom Connector with Query Folding Can Fix It"
type: "Source Summary"
description: "Explains query folding in Power BI and why a custom connector with a compatible driver speeds reports and cuts storage cost."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, microsoft, improving.com]
sources:
  - "references/improving.com/why-your-power-bi-reports-are-slow/why-your-power-bi-reports-are-slow.md"
---

# Why Your Power BI Reports Are Slow — And How a Custom Connector with Query Folding Can Fix It — Summary

**Original source**: `references/improving.com/why-your-power-bi-reports-are-slow/why-your-power-bi-reports-are-slow.md`

## Summary

The author uses a packing-for-vacation analogy to explain query folding: push transformations, aggregations, and joins down to the data source instead of pulling everything into Power BI. Standard connectors and drivers often cannot fold, so Power BI pulls all rows and does the work itself, inflating memory, processing, and storage costs. A custom connector with a compatible driver gives full control, native query support, and better performance.

## Key Claims

- Query folding makes the data source do the heavy lifting where indexes and partitioning already exist, reducing the data Power BI must receive and prepare.
- Standard connectors and drivers may not support folding, causing Power BI to pull all data across and consume more memory and processing.
- Power BI may apply type conversions it does not know the source supports, potentially incorrectly.
- APIs without a connector are another case where custom connectors help.
- A report needing monthly sales by region should push that aggregation to the source rather than importing millions of rows.
- Storing the same data in both the source and Power BI pays for it twice.
- Custom connectors with native query support let teams reuse existing, proven SQL rather than re-writing it in M.

## Relevance

Informs [query folding](/concepts/query-folding.md) and [business intelligence](/concepts/business-intelligence.md); touches [data integration](/concepts/data-integration.md).

## Quality

Practitioner how-to by Steve Lord; clear analogy and practical guidance, with an Improving sales pitch attached.

## Entities Mentioned

- [Power BI](/entities/power-bi.md) — the reporting tool
- [Microsoft](/entities/microsoft.md) — vendor of Power BI

## Concepts Covered

- [query folding](/concepts/query-folding.md) — pushing work to the source
- [business intelligence](/concepts/business-intelligence.md) — report performance
- [data integration](/concepts/data-integration.md) — connector and driver plumbing
