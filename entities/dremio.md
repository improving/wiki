---
title: "Dremio"
type: "Entity"
description: "Data lakehouse query engine behind the Arrow Flight SQL speedups."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, analytics, engineering]
sources:
  - "/sources/how-we-achieved-faster-results-arrow-flightsql.md"
---

# Dremio

Dremio is a data lakehouse query engine that appears in this corpus as one of the projects Apache Arrow contributor James Duong works on. The write-up frames it through Apache Arrow Flight SQL, pitched as a roughly 20x faster alternative to JDBC and ODBC for querying data platforms like Dremio.

## Arrow Flight SQL

- James Duong — an Apache Arrow contributor, Bit Quill co-founder, and Dremio contributor — pitches Arrow Flight SQL as a ~20x faster alternative to JDBC and ODBC.
- Flight SQL can be used from Python, C++, Java, and other languages, and a JDBC driver built on it lets existing clients such as Tableau gain the performance with no application changes.
- The GrayBeardsOnStorage podcast describes Apache Arrow Flight as interfaces and services that parallelize loading and unloading Arrow data over the network very fast.

## Related

- [Apache Arrow](/entities/apache-arrow.md) — the columnar format and Flight SQL layer
- [data integration](/concepts/data-integration.md) — fast data movement between systems
- [business intelligence](/concepts/business-intelligence.md) — BI tools such as Tableau benefit from faster access
- [data platform modernization](/concepts/data-platform-modernization.md) — upgrading data access paths
- [James Duong](/entities/james-duong.md) — Arrow contributor and speaker behind the work
- [Bit Quill Technologies](/entities/bit-quill.md) — firm Duong co-founded
