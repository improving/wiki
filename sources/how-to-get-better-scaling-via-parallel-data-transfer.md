---
title: "How to Get Better Scaling via Parallel Data Transfer using Upgraded Spark Connector"
type: "Source Summary"
description: "Improving's Alex Le explains how the open-source Vertica Spark Connector moves large datasets in parallel, scaling better than JDBC/ODBC."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, engineering, improving.com]
sources:
  - "references/improving.com/how-to-get-better-scaling-via-parallel-data-transfer/how-to-get-better-scaling-via-parallel-data-transfer.md"
---

# How to Get Better Scaling via Parallel Data Transfer using Upgraded Spark Connector — Summary

**Original source**: `references/improving.com/how-to-get-better-scaling-via-parallel-data-transfer/how-to-get-better-scaling-via-parallel-data-transfer.md`

## Summary

Improving Vancouver's Alex Le wrote a companion article on the upgraded Vertica Spark Connector, which transfers data between Vertica and Apache Spark in parallel. Because it uses the Spark DataSource V2 API, the connector integrates into Spark SQL query planning and optimizations, and it scales better than JDBC/ODBC for large transfers. It replaces a now-deprecated older connector.

## Key Claims

- Apache Spark is a fast, scalable distributed compute engine supporting Python, SQL, Scala, Java, and R under the Apache 2.0 license.
- In a typical workflow Vertica acts as the data warehouse and Spark as the "user" of the data, enriching models or transforming data upstream.
- The Vertica Spark Connector is open source and actively maintained by Vertica for current Spark 3 releases.
- It uses the Spark DataSource V2 API to integrate directly into Spark SQL query planning and optimizations.
- It is preferred over JDBC/ODBC for moving large amounts of data between Spark and Vertica because it transfers in parallel.
- Common uses include massive parallel ingestion into Vertica, integrating Vertica into Spark ETL pipelines, and ML with VerticaPy.

## Relevance

Concerns [ETL](/concepts/etl.md) and [data integration](/concepts/data-integration.md) mechanics, part of broader [data platform modernization](/concepts/data-platform-modernization.md).

## Quality

Short practitioner note by Alex Le; concrete on capabilities but largely a pointer to an external Vertica-hosted article.

## Entities Mentioned

- [Improving](/entities/improving.md) — author's firm
- [Apache Spark](/entities/apache-spark.md) — distributed compute engine
- [Vertica](/entities/vertica.md) — analytical database

## Concepts Covered

- [ETL](/concepts/etl.md) — pipelines moving and reshaping data
- [data integration](/concepts/data-integration.md) — connecting and consolidating data
- [data platform modernization](/concepts/data-platform-modernization.md) — upgrading legacy data stacks
