---
title: "distributed tracing"
type: "Concept"
description: "Following a request across services via propagated trace context, and the collector topology that keeps traces whole."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, platform, kubernetes]
sources:
  - "/sources/observability-driven-development-designing-observable-applications.md"
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/ensure-trace-integrity-with-opentelemetry.md"
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
---

# distributed tracing

Distributed tracing follows a single request as it crosses services by propagating trace context, letting a team locate where a call broke rather than guessing from per-service metrics. It is the telemetry pillar that answers "which hop," but it is also the one teams most often skip: most organizations have metrics and logs and stall when tracing comes up. In Kubernetes, keeping traces whole is itself an infrastructure problem, because spans for one trace must reach the same collector before they can be stitched together.

## Key Claims

- Each pillar does something the others cannot do cheaply: traces locate the break, metrics give affordable scale, logs preserve exact detail.
- Tail-based sampling evaluates a trace only after all its spans arrive, so every span for a traceID must reach the same collector pod.
- A stateless Collector Deployment behind a load balancer fragments spans: a test setup lost 35–40% of spans, showing up as incomplete traces in [Google Cloud](/entities/google-cloud.md) Trace or Jaeger.
- The tested fix is a two-tier collector: frontend load-balancing collectors route by `routing_key: traceID`, and backend collectors run as a StatefulSet behind a headless service — span loss dropped to near zero.
- Tail-sampling policies capture 100% of error and high-latency (>1s) traces and 10% of normal traces; backend StatefulSets scaled across 9–30 replicas.
- Wiring is concrete: a [Spring Boot](/entities/spring-boot.md) app adds micrometer-tracing with the [OpenTelemetry](/entities/opentelemetry.md) bridge and a Zipkin exporter, enables tracing at sampling probability 1.0, and injects trace/span IDs into log lines so a Loki derived-field regex links logs to traces.

## Related

- [observability](/concepts/observability.md) — the practice tracing serves
- [metrics logs traces](/concepts/metrics-logs-traces.md) — the three telemetry pillars
- [container orchestration](/concepts/container-orchestration.md) — StatefulSets and headless services
- [OpenTelemetry](/entities/opentelemetry.md) — the collection and routing layer
- [Grafana Tempo](/entities/grafana-tempo.md) — the tracing backend in the open-source stack
