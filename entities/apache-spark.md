---
title: "Apache Spark"
type: "Entity"
description: "Distributed data-processing engine for batch and streaming, used across ETL, analytics, and machine learning."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, processing, apache]
sources:
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/how-to-get-better-scaling-via-parallel-data-transfer.md"
  - "/sources/why-improving-uses-scala.md"
  - "/sources/azure-synapse-notebooks-and-spark-temporary-storage.md"
  - "/sources/engineering-scalable-ai-platforms-strategies-for-sustain-and-reuse.md"
  - "/sources/data-management-for-ai-in-the-cloud.md"
---

# Apache Spark

Apache Spark is a fast, scalable distributed compute engine for batch and streaming data, appearing across this corpus's ETL, analytics, and machine-learning work. It runs under the Apache 2.0 license and supports Python, SQL, Scala, Java, and R.

## Where It Appears

- Runs Spark Structured Streaming in a sub-second, 10TB/day ETL pipeline using dynamic micro-batches capped at ~1 second of data, watermarked stateful aggregations, HDFS checkpointing for exactly-once, and Parquet output.
- Scala is the preferred language for Spark because its concise syntax and functional features simplify parallel, distributed code.
- The Vertica Spark Connector uses the Spark DataSource V2 API to transfer data in parallel, integrating into Spark SQL query planning and scaling better than JDBC/ODBC for large moves.
- Azure Synapse notebooks share the caller's Spark session, so data frames written to Spark temporary views carry between notebooks without round-tripping to a data lake.
- Named as the distributed framework in MLOps and as an open-source processing/ETL option in cloud data management.

## Related

- [Apache Hive](/entities/apache-hive.md) — the query and storage layer at the end of the pipeline
- [Apache Kafka](/entities/apache-kafka.md) — the streaming source Spark consumes
- [Scala](/entities/scala.md) — the preferred Spark language
- [Python](/entities/python.md) — PySpark jobs
- [ETL](/concepts/etl.md) — the pipeline pattern Spark implements
- [Azure Synapse Analytics](/entities/azure-synapse.md) — a platform whose notebooks run Spark
