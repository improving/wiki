---
title: "Azure Synapse Notebooks and Spark Temporary Storage"
type: "Source Summary"
description: "Shows how Synapse notebooks can pass data between called notebooks via Spark temporary views, avoiding round trips to the data lake."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, microsoft, improving.com]
sources:
  - "references/improving.com/azure-synapse-notebooks-and-spark-temporary-storage/azure-synapse-notebooks-and-spark-temporary-storage.md"
---

# Azure Synapse Notebooks and Spark Temporary Storage — Summary

**Original source**: `references/improving.com/azure-synapse-notebooks-and-spark-temporary-storage/azure-synapse-notebooks-and-spark-temporary-storage.md`

## Summary

The author explains how Azure Synapse notebooks, backed by Spark, let data engineers organize ETL logic by calling other notebooks with `%run` or `mssparkutils.notebook.run`. Because called notebooks share the caller's Spark session, data frames written to Spark temporary storage via `createTempView` remain accessible — solving the problem that called-notebook variables and string-only return values cannot carry data back. Global temp views extend that sharing across sessions in the same Spark pool.

## Key Claims

- Synapse notebooks support Python, C#, R, and SQL with Spark's distributed compute in a single collaborative interface.
- Notebooks can call other notebooks with `%run /<path>/Notebook1` or `mssparkutils.notebook.run(...)`, and run several in parallel with `runMultiple`.
- Called notebooks share the caller's Spark session, which matters for resource use.
- Variables in a called notebook are not visible to the caller, and the exit command returns only strings.
- Writing data frames to Spark temporary storage with `createTempView` lets the caller read them via Spark SQL without saving to a data lake.
- Standard temp views are scoped to one Spark session; `createGlobalTempView` shares data across sessions in the pool.
- Benefits include faster testing, a more compact ETL flow, and fewer cells per notebook.

## Relevance

Informs [ETL](/concepts/etl.md) and [data platform modernization](/concepts/data-platform-modernization.md); touches [lakehouse](/concepts/lakehouse.md).

## Quality

Practitioner how-to by Max Miller; narrow and technical, best suited to engineers already on Synapse.

## Entities Mentioned

- [Azure Synapse Analytics](/entities/azure-synapse.md) — the notebook platform
- [Apache Spark](/entities/apache-spark.md) — the compute engine
- [Microsoft](/entities/microsoft.md) — vendor of Synapse

## Concepts Covered

- [ETL](/concepts/etl.md) — structuring transformation notebooks
- [data platform modernization](/concepts/data-platform-modernization.md) — cloud data engineering
- [lakehouse](/concepts/lakehouse.md) — data-lake-plus-warehouse setting
