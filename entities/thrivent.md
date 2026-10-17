---
title: "Thrivent"
type: "Entity"
description: "Financial services firm with a Databricks and Confluent data platform."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, financial-services, streaming]
sources:
  - "/sources/empowering-thrivents-data-driven-future.md"
---

# Thrivent

Thrivent is a financial services firm that appears in this corpus as the framing for a Databricks-plus-Confluent data platform. The write-up uses Thrivent's data-driven future to argue that financial services need governed batch and real-time analytics for personalization, compliance, and fraud detection.

## Data Platform

- Databricks provides a lakehouse with Delta Lake, Unity Catalog governance, and collaborative notebooks.
- Confluent, built on Apache Kafka, provides enterprise streaming with Schema Registry, replication, and security protocols.
- Confluent TableFlow converts Kafka streams into Delta Lake tables, tightening integration between streaming and analytical data.
- Financial services use this combination for compliance, regulatory data, personalization, and fraud detection, with the platform lowering operational complexity while strengthening governance.

## Related

- [data platform modernization](/concepts/data-platform-modernization.md) — modern data ecosystem
- [lakehouse](/concepts/lakehouse.md) — Delta Lake and Unity Catalog
- [real-time data streaming](/concepts/real-time-data-streaming.md) — Kafka-based pipelines
- [data governance](/concepts/data-governance.md) — governed access and schemas
- [Databricks](/entities/databricks.md) — unified analytics platform
- [Confluent](/entities/confluent.md) — enterprise streaming platform
- [Apache Kafka](/entities/apache-kafka.md) — streaming substrate
