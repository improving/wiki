---
title: "query folding"
type: "Concept"
description: "Pushing transformations back to the source database so reporting tools fetch less data."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, business-intelligence, performance]
sources:
  - "/sources/why-your-power-bi-reports-are-slow.md"
  - "/sources/why-your-power-bi-reports-are-slow-and-how-a-custom-connector.md"
---

# query folding

Query folding is the practice of pushing transformations, aggregations, and joins down to the source data system — where indexes and partitioning already exist — instead of pulling everything into the reporting tool. In Power BI it is the difference between a fast, cheap report and one that imports millions of rows into an oversized capacity.

## Key Claims

- Folding lets the data source do the heavy lifting where indexes and partitioning already exist, reducing the data the reporting tool must receive and prepare ([why reports are slow](/sources/why-your-power-bi-reports-are-slow.md)).
- Standard connectors and drivers may not support folding on large or complex sources, so Power BI pulls all rows across and aggregates in its own capacity ([why reports are slow](/sources/why-your-power-bi-reports-are-slow.md)).
- When Power BI cannot fold, it may also apply type conversions the source could not perform — sometimes incorrectly ([custom connector](/sources/why-your-power-bi-reports-are-slow-and-how-a-custom-connector.md)).
- Data sources exposed only through APIs may have no connector at all, another case where a custom connector is needed ([custom connector](/sources/why-your-power-bi-reports-are-slow-and-how-a-custom-connector.md)).
- Queries too complex to express in the M language need native query support, which not all connectors provide ([custom connector](/sources/why-your-power-bi-reports-are-slow-and-how-a-custom-connector.md)).
- A report needing monthly sales by region should push that aggregation to the source rather than importing millions of rows; pulling all data into a Power BI capacity means paying for the same storage twice ([why reports are slow](/sources/why-your-power-bi-reports-are-slow.md)).
- Custom connectors with native query support let teams reuse existing, proven SQL rather than re-writing it in M ([why reports are slow](/sources/why-your-power-bi-reports-are-slow.md)).

## Related

- [business intelligence](/concepts/business-intelligence.md) — report performance and cost
- [data integration](/concepts/data-integration.md) — the connectors and drivers that enable folding
- [Power BI](/entities/power-bi.md) — the tool where the pattern is most often applied
