---
title: "Unlock Your Data"
type: "Source Summary"
description: "Store incoming data raw and uninterpreted in a data lake, then curate it only when a concrete business need justifies the processing investment."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, improving.com]
sources:
  - "references/improving.com/unlock-your-data/unlock-your-data.md"
---

# Unlock Your Data — Summary

**Original source**: `references/improving.com/unlock-your-data/unlock-your-data.md`

## Summary

Olivier Aubin contrasts traditional upfront schema design with a data-lake approach that stores incoming data raw and uninterpreted. Using an online merchant's shopping data as a running example, he argues that flexibility and scalability matter more than a well-defined schema, and that curation should happen only when a concrete business use case justifies the processing cost.

## Key Claims

- Traditional structured storage parses and stores each datum relationally, discarding metadata like time, clerk, and store location — losing potentially valuable context.
- "Unstructured data" is better called "uninterpreted data": each datum has structure, but no destination schema is imposed on it.
- A data warehouse is structured and curated for a specific business case but carries high upfront cost and doesn't flexibly support future needs.
- Data lakes scale nearly without limit and store data in small nuggets, so new data carries little overhead; processing uses parallel algorithms across the distributed array.
- Storing metadata — timestamps, source identifiers, incoming schema — is essential for correct interpretation later.
- Streamed server logs can be cracked open into explicit data (page views, cart adds, transactions) and implicit data (shopping patterns, churn, correlated purchases).
- Follow an agile approach: defer decisions, store data as close to its original format as possible, and curate when value is known.

## Relevance

Speaks to [data platform modernization](/concepts/data-platform-modernization.md), [data integration](/concepts/data-integration.md), and [ETL](/concepts/etl.md), with the deferred-curation stance relevant to [data quality](/concepts/data-quality.md).

## Quality

Practitioner essay by Olivier Aubin; clear conceptual framing with a concrete example, though it predates the lakehouse pattern it anticipates.

## Entities Mentioned

- [Improving](/entities/improving.md) — the consultancy offering strategic data advice

## Concepts Covered

- [data platform modernization](/concepts/data-platform-modernization.md) — replacing brittle stacks with scalable storage
- [data integration](/concepts/data-integration.md) — consolidating data across sources
- [ETL](/concepts/etl.md) — moving and reshaping data between systems
- [data quality](/concepts/data-quality.md) — curated subsets for reporting and analytics
