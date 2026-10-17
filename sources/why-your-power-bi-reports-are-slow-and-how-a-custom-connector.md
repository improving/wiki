---
title: "Why Your Power BI Reports Are Slow — And How a Custom Connector with Query Folding Can Fix It"
type: "Source Summary"
description: "Explains why Power BI reports slow down and how custom connectors with query folding push transformations to the source."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, microsoft, improving.com]
sources:
  - "references/improving.com/why-your-power-bi-reports-are-slow-and-how-a-custom-connector/why-your-power-bi-reports-are-slow-and-how-a-custom-connector.md"
---

# Why Your Power BI Reports Are Slow — And How a Custom Connector with Query Folding Can Fix It — Summary

**Original source**: `references/improving.com/why-your-power-bi-reports-are-slow-and-how-a-custom-connector/why-your-power-bi-reports-are-slow-and-how-a-custom-connector.md`

## Summary

Query folding means pushing transformations, aggregations, and joins down to the data source, where indexes and partitioning already exist, so Power BI fetches less data — improving speed and lowering cost. Standard connectors and drivers often cannot fold on large or complex sources, so Power BI pulls everything across and does the work itself, sometimes converting types incorrectly, and API sources may have no connector at all. A custom connector with a compatible driver gives control over fetching and native query support, avoiding paying twice for the same storage.

## Key Claims

- Query folding pushes transformations, aggregations, and joins to the data source to be executed more efficiently.
- Folding reduces the data Power BI receives and prepares, improving processing speed and lowering cost.
- Standard connectors and drivers may not support folding on large or complex sources, so Power BI pulls all rows across and aggregates in its own capacity.
- Power BI may apply type conversions the source could not, sometimes incorrectly.
- Data source interfaces that are APIs may have no connector, another case for custom connectors and drivers.
- Queries too complex to express in M language need native query support, which not all connectors provide.
- Pulling all data into a Power BI capacity means paying for the same storage twice — once in the source, once in Power BI.

## Relevance

Informs [query folding](/concepts/query-folding.md), [business intelligence](/concepts/business-intelligence.md), and [data integration](/concepts/data-integration.md) by explaining where report performance is actually lost.

## Quality

Practitioner explainer by Steve Lord; clear mechanics and a memorable analogy, with an Improving sales close.

## Entities Mentioned

- [Power BI](/entities/power-bi.md) — the reporting tool being optimized

## Concepts Covered

- [query folding](/concepts/query-folding.md) — main topic
- [business intelligence](/concepts/business-intelligence.md) — decision-ready reporting
- [data integration](/concepts/data-integration.md) — connectors and drivers moving data
