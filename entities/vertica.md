---
title: "Vertica"
type: "Entity"
description: "Analytical database with a Spark connector for parallel transfer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, engineering, analytics]
sources:
  - "/sources/how-to-get-better-scaling-via-parallel-data-transfer.md"
---

# Vertica

Vertica is an analytical database that appears in this corpus through its open-source Spark Connector, which Improving Vancouver highlighted for moving large datasets in parallel. The write-up positions Vertica as the data warehouse in a Spark-centric data platform, where fast bulk transfer between the two matters.

## Spark Connector

- In a typical workflow, Vertica acts as the data warehouse and Apache Spark as the consumer that enriches models or transforms data upstream.
- The Vertica Spark Connector is open source and actively maintained by Vertica for current Spark 3 releases.
- It uses the Spark DataSource V2 API to integrate directly into Spark SQL query planning and optimizations, transferring in parallel rather than through JDBC/ODBC.
- It is preferred over JDBC/ODBC for large transfers, and common uses include massive parallel ingestion into Vertica, embedding Vertica in Spark ETL pipelines, and ML with VerticaPy.

## Related

- [ETL](/concepts/etl.md) — pipelines moving and reshaping data
- [data integration](/concepts/data-integration.md) — connecting and consolidating data
- [data platform modernization](/concepts/data-platform-modernization.md) — upgrading legacy data stacks
- [Apache Spark](/entities/apache-spark.md) — the distributed compute engine Vertica connects to
- [Improving](/entities/improving.md) — author firm behind the write-up
