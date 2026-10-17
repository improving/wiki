---
title: "Adding a Spring Boot App to the Grafana Observability Platform"
type: "Source Summary"
description: "A walkthrough of wiring a Spring Boot app into the Grafana LGTM stack for logs, metrics, and traces via Docker Compose."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, observability, improving.com]
sources:
  - "references/improving.com/adding-a-spring-boot-app-to-the-grafana-observability-platform/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
---

# Adding a Spring Boot App to the Grafana Observability Platform — Summary

**Original source**: `references/improving.com/adding-a-spring-boot-app-to-the-grafana-observability-platform/adding-a-spring-boot-app-to-the-grafana-observability-platform.md`

## Summary

Scott Bock shows how to connect a Spring Boot application to the open-source Grafana observability stack. Using Docker Compose he stands up Grafana, Loki (logs), Mimir (metrics), and Tempo (traces), then configures the app and Grafana Agent to ship each telemetry type.

## Key Claims

- Grafana provides data sources for logs (Loki), metrics (Mimir), and traces (Tempo) alongside its visualization layer.
- A single docker-compose.yaml brings up Grafana, InfluxDB, Loki, Tempo, and Mimir; grafana-datasources.yaml links them to Grafana.
- Logs: Spring Boot writes to a file and Grafana Agent scrapes it into Loki.
- Metrics: add spring-boot-starter-actuator and micrometer-registry-prometheus, expose the prometheus endpoint, and let the agent scrape it.
- Traces: add micrometer-tracing with the OTel bridge and a Zipkin exporter, enable tracing with sampling probability 1.0, and inject trace/span IDs into log lines.
- A Loki derived-field regex links trace IDs in logs to Tempo.
- The complete example lives at github.com/scottbock/observability-example.

## Relevance

A concrete walkthrough of [observability](/concepts/observability.md) and the [metrics/logs/traces](/concepts/metrics-logs-traces.md) split, including [distributed tracing](/concepts/distributed-tracing.md).

## Quality

Practical how-to by Scott Bock with full config and a public repo; assumes comfort with Docker and Spring Boot.

## Entities Mentioned

- [Grafana](/entities/grafana.md) — visualization layer of the stack
- [Grafana Loki](/entities/grafana-loki.md) — log aggregation backend
- [Grafana Tempo](/entities/grafana-tempo.md) — distributed tracing backend
- [Spring Boot](/entities/spring-boot.md) — the application being instrumented
- [OpenTelemetry](/entities/opentelemetry.md) — tracing bridge used via micrometer

## Concepts Covered

- [observability](/concepts/observability.md) — understanding system state from its outputs
- [metrics logs traces](/concepts/metrics-logs-traces.md) — the three telemetry pillars wired together
- [distributed tracing](/concepts/distributed-tracing.md) — trace context propagated through the app
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the metrics/logs/traces split
