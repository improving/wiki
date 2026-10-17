---
title: "Azure Synapse Analytics"
type: "Entity"
description: "Microsoft's cloud analytics service, whose notebooks and querying capabilities are now folded into Microsoft Fabric."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, microsoft, cloud]
sources:
  - "/sources/azure-synapse-notebooks-and-spark-temporary-storage.md"
  - "/sources/microsoft-fabric-onelake-provides-a-unified-data-lake.md"
  - "/sources/business-transformation-through-microsoft-fabric-new-era-of-data.md"
  - "/sources/shutdown-app.md"
---

# Azure Synapse Analytics

Azure Synapse Analytics is Microsoft's cloud analytics service, combining notebook-based data engineering, querying, and ETL over [Apache Spark](/entities/apache-spark.md) and SQL. Improving's writing treats it both as a hands-on engineering environment and as a capability that has been absorbed into [Microsoft Fabric](/entities/microsoft-fabric.md).

## Key Claims

- Synapse notebooks support Python, C#, R, and SQL with Spark's distributed compute in one collaborative interface.
- Notebooks can call other notebooks with `%run /<path>/Notebook1` or `mssparkutils.notebook.run(...)`, and run several in parallel with `runMultiple`.
- Called notebooks share the caller's Spark session, but their variables are invisible to the caller and the exit command returns only strings.
- Writing data frames to Spark temporary storage with `createTempView` lets the caller read them via Spark SQL without saving to a data lake; `createGlobalTempView` shares across sessions in the same pool.
- Fabric absorbs Synapse (querying) and Azure Data Factory (ETL) into a single SaaS experience, reducing the need for specialized infrastructure skills.
- Synapse also appears as the Azure analytics context for an Improving-built mine "Shutdown App" delivered on [Microsoft Power Platform](/entities/power-platform.md).

## Related

- [Microsoft Fabric](/entities/microsoft-fabric.md) — the platform that absorbed Synapse
- [ETL](/concepts/etl.md) — structuring transformation notebooks
- [lakehouse](/concepts/lakehouse.md) — the data-lake-plus-warehouse setting
- [Microsoft Power Platform](/entities/power-platform.md) — the low-code suite in the Shutdown App case
