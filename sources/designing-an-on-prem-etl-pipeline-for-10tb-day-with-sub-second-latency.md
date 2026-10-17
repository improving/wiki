---
title: "Designing an On-Prem ETL Pipeline for 10TB/day with Sub-Second Latency Using Spark, Kafka, and Hive"
type: "Source Summary"
description: "Shows a sub-second, 10TB/day on-prem ETL pipeline built on Kafka, Spark Structured Streaming, and Hive."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, platform, improving.com]
sources:
  - "references/improving.com/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
---

# Designing an On-Prem ETL Pipeline for 10TB/day with Sub-Second Latency Using Spark, Kafka, and Hive — Summary

**Original source**: `references/improving.com/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md`

## Summary

Shows that sub-second, 10TB/day ETL isn't cloud-only by describing an on-premise pipeline built on Kafka, Spark Structured Streaming, and Hive. The post details tuning choices — Kafka partitioning and low-latency producer settings, dynamic micro-batches, broadcast joins, G1GC, salting for skew, and small-file compaction — and argues partitioning strategy matters more than raw compute.

## Key Claims

- Requirements: sub-second ingestion-to-query latency, 100K+ events/sec, high availability, up to 10TB/day, and schema flexibility for evolving IoT data.
- Kafka: 100+ partitions, LZ4 compression, replication factor 3, Avro with Schema Registry, linger.ms=1ms and acks=1 to prioritize speed.
- Spark Structured Streaming: dynamic micro-batches capped at ~1 second of data, watermarked stateful aggregations, HDFS checkpointing for exactly-once, fastavro parsing, and Parquet output.
- Hive: external partitioned tables, Snappy Parquet with predicate pushdown, and the Tez engine with Bloom filters and vectorized execution; Spark writes to HDFS and Hive picks up partitions via MSCK REPAIR TABLE or ALTER TABLE ADD PARTITION.
- Optimizations: micro-batches under 50ms, broadcast joins for reference data under 100MB to avoid shuffles, parallel Kafka reads, G1GC to avoid JVM stalls, salting and repartitioning for skew, and daily compaction of small Parquet files.
- Monitoring used Prometheus for Kafka lag, Grafana for Spark metrics, and an end-to-end latency dashboard from Kafka write to Hive write.
- Testing simulated 10TB/day ingestion, benchmarked three years of history, and stress-tested at 3x load; lessons include testing end-to-end latency, not per-layer performance.

## Relevance

An [ETL](/concepts/etl.md) and [stream processing](/concepts/stream-processing.md) design for [real-time data streaming](/concepts/real-time-data-streaming.md), with a [latency budget](/concepts/latency-budget.md) measured end to end.

## Quality

Detailed performance-engineering write-up by Manik Hossain; strong on tuning specifics, though it stops short of production cost comparisons.

## Entities Mentioned

- [Apache Kafka](/entities/apache-kafka.md) — the real-time backbone
- [Apache Spark](/entities/apache-spark.md) — structured streaming engine
- [Apache Hive](/entities/apache-hive.md) — storage and query layer
- [Scala](/entities/scala.md) — language used alongside Python
- [Python](/entities/python.md) — PySpark jobs
- [Prometheus](/entities/prometheus.md) — Kafka lag monitoring
- [Grafana](/entities/grafana.md) — Spark metrics dashboards
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [ETL](/concepts/etl.md) — high-throughput data pipeline
- [stream processing](/concepts/stream-processing.md) — Spark over unbounded events
- [real-time data streaming](/concepts/real-time-data-streaming.md) — sub-second delivery
- [latency budget](/concepts/latency-budget.md) — end-to-end latency target
- [observability](/concepts/observability.md) — lag and metrics dashboards
- [hybrid cloud](/concepts/hybrid-cloud.md) — on-prem as a viable alternative
