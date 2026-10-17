---
title: "How We Achieved 20x Faster Results than ODBC/JDBC using Arrow FlightSQL"
type: "Source Summary"
description: "A roundup of Bit Quill co-founder James Duong's talks on Apache Arrow FlightSQL as a roughly 20x faster alternative to JDBC/ODBC."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, engineering, improving.com]
sources:
  - "references/improving.com/how-we-achieved-faster-results-arrow-flightsql/how-we-achieved-faster-results-arrow-flightsql.md"
---

# How We Achieved 20x Faster Results than ODBC/JDBC using Arrow FlightSQL — Summary

**Original source**: `references/improving.com/how-we-achieved-faster-results-arrow-flightsql/how-we-achieved-faster-results-arrow-flightsql.md`

## Summary

This post points to presentations and a podcast featuring James Duong, an Apache Arrow contributor, Bit Quill co-founder, and Dremio contributor, on Apache Arrow FlightSQL. Duong pitches FlightSQL as a roughly 20x faster alternative to JDBC and ODBC, usable from Python, C++, Java, and other languages. A JDBC driver built on FlightSQL lets existing clients like Tableau benefit with zero application changes.

## Key Claims

- James Duong has worked with databases for over 15 years, from query engines to drivers and protocols, and is an industry specialist on Arrow FlightSQL.
- Arrow FlightSQL is presented as a ~20x faster alternative to JDBC and ODBC.
- FlightSQL can be used from Python, C++, Java, and other languages.
- A JDBC driver built on Arrow FlightSQL lets existing applications such as Tableau gain the performance with no application changes.
- The GrayBeardsOnStorage podcast describes Apache Arrow Flight as interfaces and services that parallelize loading and unloading Arrow data over the network very fast.
- Sources span Subsurface's Cloud Data Lake Conference, Voltron Data's Data Thread Conference, and the GrayBeardsOnStorage podcast.

## Relevance

Touches [data integration](/concepts/data-integration.md) performance and the tooling behind [business intelligence](/concepts/business-intelligence.md), within [data platform modernization](/concepts/data-platform-modernization.md).

## Quality

Short link roundup by Nitin Cunha; a pointer to external talks rather than a substantive technical write-up.

## Entities Mentioned

- [Apache Arrow](/entities/apache-arrow.md) — columnar format and FlightSQL
- [Dremio](/entities/dremio.md) — query engine Duong contributes to
- [James Duong](/entities/james-duong.md) — Arrow contributor and speaker
- [Bit Quill Technologies](/entities/bit-quill.md) — firm Duong co-founded
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [data integration](/concepts/data-integration.md) — fast data movement between systems
- [business intelligence](/concepts/business-intelligence.md) — BI tools benefiting from faster access
- [data platform modernization](/concepts/data-platform-modernization.md) — upgrading data access paths
