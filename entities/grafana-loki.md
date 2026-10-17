---
title: "Grafana Loki"
type: "Entity"
description: "Grafana's log aggregation system that indexes only metadata and labels, making it lighter and cheaper than Elasticsearch."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, logging, open-source]
sources:
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
---

# Grafana Loki

Grafana's log aggregation system, the "L" of the LGTM stack, used in this corpus as the lighter, cheaper log backend in an open-source [observability](/concepts/observability.md) setup. Rather than indexing full log content like Elasticsearch, Loki indexes only metadata and labels, which is what makes it cheap and also what shapes how teams query it.

## How It Works Here

- Loki indexes only metadata/labels rather than full log content, making it lighter and cheaper than Elasticsearch.
- In a Spring Boot example, the app writes logs to a file and Grafana Agent scrapes it into Loki.
- A Loki derived-field regex links trace IDs in log lines to [Grafana Tempo](/entities/grafana-tempo.md), tying logs to traces.
- Loki helped Paytm Insider save 75% of logging and monitoring costs, per the corpus.
- Advantages over ELK include native metrics/logs/traces correlation, lower storage cost, cloud-native scalability, and vendor neutrality.

## Related

- [Grafana](/entities/grafana.md) — the visualization and query front end
- [Grafana Tempo](/entities/grafana-tempo.md) — the tracing backend paired with Loki
- [metrics-logs-traces](/concepts/metrics-logs-traces.md) — the three telemetry pillars
- [observability](/concepts/observability.md) — understanding system state from its outputs
