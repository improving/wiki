---
title: "Prometheus"
type: "Entity"
description: "Open-source metrics monitoring system and time-series database, the default metrics layer of the cloud-native stack."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, metrics, cloud-native]
sources:
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
  - "/sources/introducing-the-amazon-timestream-for-liveanalytics-prometheus.md"
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/platform-engineering-maturity-model.md"
---

# Prometheus

The open-source metrics monitoring system and time-series database at the center of the cloud-native observability stack. It is the metrics pillar in this corpus's [observability](/concepts/observability.md) writing, and also the system whose local storage limits and cardinality ceiling drive the cost and architecture debates.

## In the Stack

- Prometheus provides metrics, with Kube-State-Metrics and Node Exporter supplying object and node metrics; Grafana visualizes them.
- It is the standardized metrics component in platform-engineering reference stacks.
- A Spring Boot app exposes a Prometheus endpoint via spring-boot-starter-actuator and micrometer-registry-prometheus, which an agent scrapes.

## Storage and Cost

- Prometheus local storage is size-limited; remote storage extends retention.
- The Amazon Timestream for LiveAnalytics Prometheus Connector translates between Prometheus and Timestream via remote_write and remote_read, deployable as a Lambda behind API Gateway in about five minutes.
- Benefits include serverless scalability, SQL-based querying, and lower storage costs; Prometheus requires an IAM access key rather than a role because of a Prometheus limitation.
- Prometheus' cardinality ceiling makes high-cardinality labels a footgun, which wide-event columnar stores avoid.

## Related

- [Grafana](/entities/grafana.md) — visualization layer for Prometheus metrics
- [Amazon Timestream](/entities/amazon-timestream.md) — remote storage target for Prometheus
- [observability](/concepts/observability.md) — system insight from telemetry
- [metrics-logs-traces](/concepts/metrics-logs-traces.md) — the three telemetry pillars
- [cloud-cost-management](/concepts/cloud-cost-management.md) — offloading metric storage to cut cost
