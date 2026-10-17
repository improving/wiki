---
title: "How A Global Healthcare Manufacturer Transformed Production Lines with Real-Time IoT Insights"
type: "Source Summary"
description: "Medtronic used Kafka, Confluent Cloud, and IoT data to replace paper-based production tracking with real-time pipelines and predictive maintenance."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, healthcare, improving.com]
sources:
  - "references/improving.com/how-a-global-healthcare-manufacturer-transformed-production-lines/how-a-global-healthcare-manufacturer-transformed-production-lines.md"
---

# How A Global Healthcare Manufacturer Transformed Production Lines with Real-Time IoT Insights — Summary

**Original source**: `references/improving.com/how-a-global-healthcare-manufacturer-transformed-production-lines/how-a-global-healthcare-manufacturer-transformed-production-lines.md`

## Summary

Medtronic, with 95,000 employees across 350 sites, replaced manual, paper-based production data collection with real-time IoT pipelines built with Improving and Confluent. Data from sensors, MES systems, and MQTT brokers streams into Kafka, where Kafka Streams embed business logic and Confluent Cloud scales across new sites. The result was improved visibility, reduced scrap and downtime, and predictive maintenance, with lessons about patience, designing for scale, and standardization.

## Key Claims

- Challenges: manual paper-based collection, data silos, high scrap rates, reactive maintenance, and unnoticed bottlenecks.
- Three pillars: capture real-time data from IoT devices, sensors, MES, and MQTT brokers; stream it into Kafka for reporting and real-time apps; scale and standardize on Confluent Cloud.
- Kafka Connect and MQTT connectors ingest production-line data; Power BI and data warehouses serve downstream analytics.
- Kafka Streams applications act on insights directly in the stream.
- Medtronic serves over 78 million people and treats more than 70 health conditions across 350 sites.
- Benefits: better visibility, automated collection, cost savings, optimized throughput, predictive maintenance, and scaling without rework.
- Lessons: introduce digital practices gradually, design for scale from the start, standardize data models and naming, and use partners like Confluent.

## Relevance

Informs [real-time data streaming](/concepts/real-time-data-streaming.md), [Internet of Things](/concepts/iot.md), and [event-driven architecture](/concepts/event-driven-architecture.md); touches [data platform modernization](/concepts/data-platform-modernization.md).

## Quality

Vendor-adjacent case study by Mark Soule; concrete on architecture and benefits but framed as a success story.

## Entities Mentioned

- [Medtronic](/entities/medtronic.md) — the healthcare manufacturer
- [Confluent](/entities/confluent.md) — streaming platform partner
- [Apache Kafka](/entities/apache-kafka.md) — the event backbone
- [MQTT](/entities/mqtt.md) — factory-floor messaging protocol
- [Power BI](/entities/power-bi.md) — downstream reporting
- [Improving](/entities/improving.md) — delivery partner

## Concepts Covered

- [real-time data streaming](/concepts/real-time-data-streaming.md) — streaming factory data
- [Internet of Things](/concepts/iot.md) — sensors and MES on the floor
- [event-driven architecture](/concepts/event-driven-architecture.md) — Kafka-based pipelines
- [data platform modernization](/concepts/data-platform-modernization.md) — off paper and batch
