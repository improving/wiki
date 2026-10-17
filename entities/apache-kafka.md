---
title: "Apache Kafka"
type: "Entity"
description: "The distributed event streaming platform at the center of the corpus's real-time data and event-driven architectures."
created: '2026-10-17'
updated: '2026-10-17'
tags: [streaming, data, apache]
sources:
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/real-time-data-done-right.md"
  - "/sources/how-a-global-healthcare-manufacturer-transformed-production-lines.md"
  - "/sources/keda-the-gold-standard-for-kubernetes-autoscaling.md"
  - "/sources/kafka-schema-evolution-with-java-spring-boot-and-protobuf.md"
  - "/sources/unlocking-the-power-of-confluent-cloud-with-code-explorer.md"
---

# Apache Kafka

Apache Kafka is the distributed event streaming platform that anchors this corpus's real-time data architecture. It appears as the event backbone behind IoT pipelines, the substrate for stream processing and AI agents, and the technology whose managed services vendors compete to run.

## Uses in the Corpus

- A sub-second, 10TB/day on-prem ETL pipeline tuned Kafka with 100+ partitions, LZ4 compression, replication factor 3, Avro with Schema Registry, `linger.ms=1ms`, and `acks=1` to prioritize speed.
- Medtronic streamed IoT sensor, MES, and MQTT data into Kafka, embedded business logic with Kafka Streams, and scaled across sites on Confluent Cloud.
- KEDA scales Kafka consumers on consumer lag and can scale workloads to zero, because the native HPA scales only on CPU and memory.
- Protobuf schemas evolve across Kafka producers and consumers via a Schema Registry, demonstrating forward and backward compatibility.
- Confluent Cloud is pitched against AWS MSK with a 99.99% SLA, 200+ connectors, RBAC, and stream governance; Confluent is credited with over 60% of Apache Kafka commits.
- Serves as the messaging backbone in a legacy Java Swing modernization onto Azure, and as the event stream that Confluent's Streaming Agents run on.

## Related

- [Apache Flink](/entities/apache-flink.md) — the paired stream-processing engine
- [Confluent](/entities/confluent.md) — the commercial steward and managed offering
- [KEDA](/entities/keda.md) — event-driven autoscaling on Kafka lag
- [event-driven architecture](/concepts/event-driven-architecture.md) — the pattern it enables
- [real-time data streaming](/concepts/real-time-data-streaming.md) — the discipline it serves
