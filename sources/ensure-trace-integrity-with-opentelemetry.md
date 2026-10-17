---
title: "Ensure Trace Integrity with OpenTelemetry: StatefulSets, Helm, and Load Balancing"
type: "Source Summary"
description: "Shows how load-balancing collectors plus a StatefulSet backend fix the fragmented traces that break tail sampling in Kubernetes."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, improving.com]
sources:
  - "references/improving.com/ensure-trace-integrity-with-opentelemetry/ensure-trace-integrity-with-opentelemetry.md"
---

# Ensure Trace Integrity with OpenTelemetry — Summary

**Original source**: `references/improving.com/ensure-trace-integrity-with-opentelemetry/ensure-trace-integrity-with-opentelemetry.md`

## Summary

Tail-based sampling in Kubernetes fails when OpenTelemetry Collector pods are a stateless Deployment behind a load balancer, because spans for one traceID scatter across pods and traces arrive incomplete. The author's tested fix is a two-tier collector architecture: load-balancing collectors that route spans by traceID, plus backend collectors deployed as a StatefulSet behind a headless service so each pod has a stable DNS name. Tests cut span loss from 35–40% to near zero.

## Key Claims

- Tail sampling evaluates a trace only after all its spans arrive, so every span for a traceID must reach the same collector pod.
- Stateless Deployments lack stable pod identities, so spans fragment across pods and backends like Google Cloud Trace or Jaeger show incomplete traces.
- The fix: frontend load-balancing collectors use the `loadbalancing` exporter with `routing_key: traceID`; backend collectors run as a StatefulSet behind a headless (`ClusterIP: None`) service.
- The headless service name must match the StatefulSet's `serviceName` for Kubernetes DNS resolution.
- Tail-sampling policies capture 100% of error and high-latency (>1s) traces and 10% of normal traces.
- The OpenTelemetry Operator lacks `statefulset.serviceName` support, so the author pairs it with the `opentelemetry-helm-charts` Helm chart.
- telemetrygen tests: the dev setup collected 100% of error and latency spans and ~13% of normal; the tst setup without load balancing lost 35–40% of spans.
- Backend StatefulSets scaled across 9–30 replicas.

## Relevance

Informs [distributed tracing](/concepts/distributed-tracing.md), [observability](/concepts/observability.md), and [container orchestration](/concepts/container-orchestration.md).

## Quality

Practitioner deep-dive by Kevin Gibson with real test numbers; narrow to one collector-topology problem.

## Entities Mentioned

- [OpenTelemetry](/entities/opentelemetry.md) — the collector pipeline being scaled
- [Kubernetes](/entities/kubernetes.md) — the cluster it runs on
- [Google Cloud](/entities/google-cloud.md) — Google Cloud Trace export target

## Concepts Covered

- [distributed tracing](/concepts/distributed-tracing.md) — trace integrity across services
- [observability](/concepts/observability.md) — reliable telemetry pipelines
- [container orchestration](/concepts/container-orchestration.md) — StatefulSets and headless services
