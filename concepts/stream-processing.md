---
title: "stream processing"
type: "Concept"
description: "Computing over unbounded event streams, often with engines such as Flink or Spark Structured Streaming."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, streaming, platform]
sources:
  - "/sources/simplify-stream-processing-with-serverless-apache-flink.md"
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/real-time-is-the-easy-part.md"
  - "/sources/unleash-real-time-agentic-ai-with-streaming-agents-on-confluent-cloud.md"
  - "/sources/designing-a-gcp-cloud-etl-pipeline.md"
---

# stream processing

Stream processing computes over unbounded event streams — filtering, joining, aggregating, and enriching data as it flows — rather than reprocessing it in batches. Engines such as Apache Flink and Spark Structured Streaming make this practical, and managed serverless offerings now remove most of the infrastructure burden.

## Key Claims

- Apache Flink is a unified stream *and* batch processing framework and a top-five Apache project, powering stream processing at Uber, Netflix, LinkedIn, ING, Goldman Sachs, and Comcast.
- Confluent's cloud-native, serverless Apache Flink service reached general availability across AWS, Azure, and Google Cloud alongside its managed Kafka, backed by a 99.99% uptime SLA.
- Spark Structured Streaming runs dynamic micro-batches capped at about one second of data with watermarked stateful aggregations, HDFS checkpointing for exactly-once, and Parquet output.
- Tuning matters more than raw compute: broadcast joins for reference data under 100MB, G1GC to avoid JVM stalls, salting and repartitioning for skew, and daily compaction of small files.
- A serverless GCP Dataflow (Apache Beam) job parses files, applies schema-aware transformations, deduplicates with windowing and watermarking, and writes to BigQuery, autoscaling 5–200 workers with dynamic work rebalancing.
- Streaming agents run on managed Flink and Kafka, using familiar Flink APIs with native support for model inference, tool calling with MCP, embeddings for RAG, and external tables.
- Agents can use input/output topics as a communication backbone, giving auditability, access control, integration, and fresh context.

## Related

- [real-time data streaming](/concepts/real-time-data-streaming.md) — the delivery layer beneath it
- [event-driven architecture](/concepts/event-driven-architecture.md) — the communication model
- [ETL](/concepts/etl.md) — the pipeline shape stream processing modernizes
- [latency budget](/concepts/latency-budget.md) — the end-to-end target it must meet
