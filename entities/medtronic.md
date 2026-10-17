---
title: "Medtronic"
type: "Entity"
description: "Medical device manufacturer using real-time streaming for production lines."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, healthcare, iot]
sources:
  - "/sources/how-a-global-healthcare-manufacturer-transformed-production-lines.md"
  - "/sources/data-streaming-world-tour-in-review-an-improving-perspective.md"
---

# Medtronic

Medtronic is a global medical device manufacturer that appears in this corpus as a flagship case for real-time IoT streaming on the factory floor. With 95,000 employees across 350 sites, it replaced manual, paper-based production tracking with Kafka-based pipelines built with Improving and Confluent.

## Real-Time Production Lines

- Challenges: manual paper-based collection, data silos, high scrap rates, reactive maintenance, and unnoticed bottlenecks.
- Three pillars: capture real-time data from IoT devices, sensors, MES systems, and MQTT brokers; stream it into Kafka for reporting and real-time apps; scale and standardize on Confluent Cloud.
- Kafka Connect and MQTT connectors ingest production-line data, Kafka Streams embed business logic, and Power BI and data warehouses serve downstream analytics.
- Reported benefits: better visibility, automated collection, cost savings, optimized throughput, predictive maintenance, and scaling without rework.
- Lessons: introduce digital practices gradually, design for scale from the start, standardize data models and naming, and use partners like Confluent.

## Presence in the Corpus

- Medtronic serves over 78 million people and treats more than 70 health conditions.
- Its story was a featured case on Confluent's 2025 Data Streaming World Tour, which Improving sponsored; attendees responded strongly to the IoT pipeline narrative.

## Related

- [real-time data streaming](/concepts/real-time-data-streaming.md) — streaming factory data
- [Internet of Things](/concepts/iot.md) — sensors and MES on the production line
- [event-driven architecture](/concepts/event-driven-architecture.md) — Kafka-based pipelines
- [data platform modernization](/concepts/data-platform-modernization.md) — moving off paper and batch
- [Confluent](/entities/confluent.md) — streaming platform partner
- [Apache Kafka](/entities/apache-kafka.md) — the event backbone
- [MQTT](/entities/mqtt.md) — factory-floor messaging protocol
- [Power BI](/entities/power-bi.md) — downstream reporting
