---
title: "Apache Arrow"
type: "Entity"
description: "Columnar in-memory format whose Flight SQL protocol offers roughly 20x faster data access than JDBC/ODBC."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, engineering, open-source]
sources:
  - "/sources/how-we-achieved-faster-results-arrow-flightsql.md"
---

# Apache Arrow

Apache Arrow is a columnar in-memory data format that Improving's data engineering writing highlights mainly through **Arrow Flight SQL**, an interface for moving Arrow data over the network. The pitch is performance: FlightSQL is presented as roughly 20x faster than the JDBC and ODBC protocols most BI tools still use.

## Key Claims

- Arrow Flight SQL is presented as a roughly 20x faster alternative to JDBC and ODBC for querying data.
- FlightSQL is usable from Python, C++, Java, and other languages.
- A JDBC driver built on Arrow FlightSQL lets existing applications such as Tableau gain the speedup with no application changes.
- Apache Arrow Flight parallelizes loading and unloading Arrow data over the network, per the GrayBeardsOnStorage podcast.
- The material comes from talks by James Duong, an Apache Arrow contributor and [Bit Quill Technologies](/entities/bit-quill.md) co-founder, spanning the Cloud Data Lake Conference, the Data Thread Conference, and a podcast.

## Related

- [data integration](/concepts/data-integration.md) — the data-movement performance Arrow improves
- [business intelligence](/concepts/business-intelligence.md) — BI tools that benefit from faster access
- [Dremio](/entities/dremio.md) — query engine Duong contributes to
