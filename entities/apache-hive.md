---
title: "Apache Hive"
type: "Entity"
description: "SQL-on-Hadoop data warehouse layer used as the storage and query tier of a high-throughput on-prem ETL pipeline."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, warehouse, apache]
sources:
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
---

# Apache Hive

Apache Hive is the SQL-on-Hadoop data warehouse layer that appears in this corpus as the storage and query tier at the end of a sub-second, 10TB/day on-prem ETL pipeline. It shows that Hadoop-era components still earn a place when partitioned and tuned carefully.

## Role in the Pipeline

- Configured with external partitioned tables and Snappy Parquet with predicate pushdown, plus the Tez engine with Bloom filters and vectorized execution.
- Spark writes Parquet to HDFS and Hive picks up the new partitions via `MSCK REPAIR TABLE` or `ALTER TABLE ADD PARTITION`.
- Serves as the query endpoint whose write completes the pipeline, with an end-to-end latency dashboard measured from Kafka write to Hive write.
- The wider argument is that partitioning strategy matters more than raw compute for sub-second latency, and that sub-second ETL is not cloud-only.

## Related

- [Apache Spark](/entities/apache-spark.md) — the streaming engine that writes into Hive
- [Apache Kafka](/entities/apache-kafka.md) — the real-time backbone feeding the pipeline
- [ETL](/concepts/etl.md) — the pipeline pattern it terminates
- [data platform modernization](/concepts/data-platform-modernization.md) — the broader shift it participates in
