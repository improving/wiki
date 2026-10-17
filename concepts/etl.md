---
title: "ETL"
type: "Concept"
description: "Extract-transform-load pipelines that move and reshape data between systems."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, integration, platform]
sources:
  - "/sources/etl-modernization-informatica-to-confluent-databricks.md"
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/designing-a-gcp-cloud-etl-pipeline.md"
  - "/sources/unlock-your-data.md"
---

# ETL

ETL (extract-transform-load) pipelines move and reshape data between systems. Legacy ETL was designed for manageable volumes and overnight batches, but real-time analytics has become a competitive necessity, so the workload is shifting from batch platforms toward streaming and lakehouse architectures that can deliver data in sub-second time.

## Key Claims

- Legacy batch ETL platforms such as Informatica have become bottlenecks through tightly coupled integrations, costly scaling, high on-premises operational overhead, batch delays, and weak built-in governance.
- A sub-second, 10TB/day on-prem pipeline is achievable with Kafka (100+ partitions, LZ4, Avro with Schema Registry, `linger.ms=1ms`), Spark Structured Streaming (dynamic micro-batches, watermarked aggregations, HDFS checkpointing), and Hive (partitioned Snappy Parquet, predicate pushdown, Tez with Bloom filters).
- A serverless GCP pipeline reaches roughly 600ms end-to-end for 10TB/day by chaining GCS object-finalized events, a Cloud Function, Pub/Sub, and a Dataflow streaming job into BigQuery.
- Partitioning strategy matters more than raw compute, and end-to-end latency must be tested rather than per-layer performance.
- An alternative to upfront schema design is to store incoming data raw and uninterpreted in a data lake, curating only when a concrete business use case justifies the processing cost.
- Data lakes store each datum in small nuggets and preserve metadata (timestamps, source identifiers, incoming schema) that structured storage discards, so interpretation stays possible later.
- Migration frameworks run assessment and planning, code and process modernization, real-time enablement via streaming, seamless integration with connectors, and security and governance from day one.

## Related

- [data platform modernization](/concepts/data-platform-modernization.md) — replacing brittle legacy pipelines
- [stream processing](/concepts/stream-processing.md) — the engine that makes continuous ETL possible
- [real-time data streaming](/concepts/real-time-data-streaming.md) — the low-latency target
- [data integration](/concepts/data-integration.md) — connecting and consolidating sources
