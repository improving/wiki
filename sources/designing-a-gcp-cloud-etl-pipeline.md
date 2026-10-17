---
title: "Designing a GCP Cloud ETL Pipeline for 10TB/Day with Sub-Second Latency"
type: "Source Summary"
description: "Architecture of a serverless GCP ETL pipeline handling 10TB/day at roughly 600ms latency via GCS, Pub/Sub, Dataflow, and BigQuery."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, cloud, improving.com]
sources:
  - "references/improving.com/designing-a-gcp-cloud-etl-pipeline/designing-a-gcp-cloud-etl-pipeline.md"
---

# Designing a GCP Cloud ETL Pipeline for 10TB/Day with Sub-Second Latency — Summary

**Original source**: `references/improving.com/designing-a-gcp-cloud-etl-pipeline/designing-a-gcp-cloud-etl-pipeline.md`

## Summary

An architecture walkthrough of a serverless, event-driven ETL pipeline Improving built on Google Cloud that ingests 10TB/day and lands data in BigQuery with roughly 600ms end-to-end latency. Files uploaded to GCS trigger a Cloud Function, which publishes to Pub/Sub; a Dataflow streaming job transforms and writes to BigQuery.

## Key Claims

- Targets: 10TB/day (~115MB/sec sustained) and under one second from upload to BigQuery visibility, fully serverless and autoscaling with minimal ops.
- GCS "object finalized" events trigger a Cloud Function that parses metadata, adds schema and version tags, and publishes to a Pub/Sub topic.
- Pub/Sub buffers and decouples, enabling horizontal scaling, replay on downstream failure, and backpressure via flow control.
- Dataflow (Apache Beam, Java SDK) in streaming mode parses files, applies schema-aware transformations, deduplicates with windowing and watermarking, and writes to BigQuery.
- Optimizations: 512MB Cloud Function memory to cut cold starts, reused network clients, 1000 concurrent executions; Dataflow Streaming Engine plus Runner v2, autoscaling 5–200 workers, dynamic work rebalancing, chunked files.
- BigQuery tables are partitioned by ingestion date and clustered by source_id and event_type, with daily compaction and streaming-buffer lag monitoring.
- Results: ~600ms average end-to-end latency; lessons are to design for retries and idempotency, pre-scale, tune batches, and decouple stages.

## Relevance

A concrete [ETL](/concepts/etl.md) design for [real-time data streaming](/concepts/real-time-data-streaming.md), built on [event-driven architecture](/concepts/event-driven-architecture.md) and measured with [observability](/concepts/observability.md).

## Quality

Hands-on architecture write-up by Manik Hossain; specific on configuration and results, though light on the bottleneck detail.

## Entities Mentioned

- [Google Cloud](/entities/google-cloud.md) — platform for the pipeline
- [BigQuery](/entities/bigquery.md) — analytics layer
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [ETL](/concepts/etl.md) — extract, transform, load pipeline
- [real-time data streaming](/concepts/real-time-data-streaming.md) — continuous event processing
- [event-driven architecture](/concepts/event-driven-architecture.md) — GCS triggers and Pub/Sub
- [observability](/concepts/observability.md) — monitoring latency and lag
- [stream processing](/concepts/stream-processing.md) — Dataflow over unbounded data
- [data integration](/concepts/data-integration.md) — connecting sources to analytics
- [latency budget](/concepts/latency-budget.md) — sub-second end-to-end target
