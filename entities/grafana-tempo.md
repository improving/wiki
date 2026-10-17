---
title: "Grafana Tempo"
type: "Entity"
description: "Grafana's distributed tracing backend, the trace store of the open-source LGTM observability stack."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, tracing, open-source]
sources:
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
---

# Grafana Tempo

Grafana's distributed tracing backend, the "T" of the LGTM stack, storing the traces that let teams follow a request across services. In this corpus it is the trace pillar of an open-source [observability](/concepts/observability.md) setup, wired to logs and metrics through Grafana and OpenTelemetry.

## How It Works Here

- Tempo provides the tracing backend in a stack that maps Prometheus to metrics, Loki to logs, and Grafana to visualization.
- In a Spring Boot example, the app adds micrometer-tracing with the OTel bridge and a Zipkin exporter, enables tracing with sampling probability 1.0, and injects trace/span IDs into log lines.
- A Loki derived-field regex links trace IDs in logs to Tempo, connecting [distributed-tracing](/concepts/distributed-tracing.md) to log context.
- The stack's advantages over ELK include native metrics/logs/traces correlation and vendor neutrality.

## Related

- [Grafana](/entities/grafana.md) — the visualization layer that queries Tempo
- [Grafana Loki](/entities/grafana-loki.md) — the log backend paired with Tempo
- [distributed-tracing](/concepts/distributed-tracing.md) — following a request across services
- [observability](/concepts/observability.md) — system insight from telemetry outputs
