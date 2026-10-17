---
title: "Grafana"
type: "Entity"
description: "Observability visualization platform, the query and dashboard layer of the open-source LGTM stack."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, open-source, visualization]
sources:
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/introducing-the-amazon-timestream-for-liveanalytics-prometheus.md"
---

# Grafana

The visualization layer of the open-source observability stack, used in this corpus to bring metrics, logs, and traces into one interface and as the front end for the "LGTM" combination (Loki, Grafana, Tempo/Mimir). It recurs as the credible lower-cost alternative to commercial APM platforms, and as the dashboarding tool teams keep even when they swap backends.

## Role in the Stack

- Grafana is the visualization layer; Prometheus provides metrics, Loki logs, and Tempo traces, with OpenTelemetry for collection.
- The stack maps roles explicitly: Kube-State-Metrics and Node Exporter for object and node metrics, Grafana for visualization.
- Advantages over ELK include native metrics/logs/traces correlation, lower storage cost, cloud-native scalability, and vendor neutrality.
- In a Spring Boot example, a single docker-compose.yaml brings up Grafana, Loki, Tempo, and Mimir, linked by a grafana-datasources.yaml.
- Grafana can query Amazon Timestream for LiveAnalytics as a Prometheus remote store, extending metric retention.

## Context

- The canonical 2019 stack already included Prometheus, Grafana, and Alertmanager alongside ELK and Nagios/Zabbix, overwhelmingly infrastructure- and cause-focused.
- The observability cost crisis makes the Grafana stack attractive: multi-dimensional commercial pricing meets Kubernetes elasticity badly, and the CNCF-native LGTM stack usually costs less above roughly 200 nodes.
- Grafana Labs' 2023 survey found 52% of organizations use six or more observability tools and 11% use sixteen or more.

## Related

- [Grafana Loki](/entities/grafana-loki.md) — log aggregation backend
- [Grafana Tempo](/entities/grafana-tempo.md) — distributed tracing backend
- [Prometheus](/entities/prometheus.md) — the metrics system Grafana visualizes
- [observability](/concepts/observability.md) — understanding system state from its outputs
