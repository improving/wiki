---
type: Reference
title: "Ensure Trace Integrity with OpenTelemetry: StatefulSets, Helm, and Load Balancing"
resource: "https://www.improving.com/thoughts/ensure-trace-integrity-with-opentelemetry/"
author: "Kevin Gibson"
published: '2025-06-06'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Struggling with incomplete traces in your Kubernetes cluster? Distributed tracing is a game-changer for debugging microservices, but OpenTelemetry can falter without the right setup. Tail-based sampling, which prioritizes critical traces, demands precise span alignment—yet fragmented traces are a common headache.

This guide unveils a proven OpenTelemetry tail sampling Kubernetes solution using StatefulSets, Helm, and load-balancing collectors. Backed by real-world tests, we’ll show you how to eliminate dropped spans and achieve reliable observability. Ready to transform your Kubernetes observability? Let’s dive in!

### **Why TraceID Routing Fails in Kubernetes**

In Kubernetes, OpenTelemetry Collectors are typically deployed as a Deployment, with pods behind a load-balanced service. This scales well but creates chaos for tail sampling. Why? Tail sampling evaluates traces after collecting all spans, requiring every span for a TraceID to hit the same collector pod. Without consistent routing, spans scatter across pods, leading to incomplete traces in backends like Google Cloud Trace or Jaeger.

The culprit? The stateless nature of Deployments, where pods lack stable identities. To ensure trace integrity, spans must reliably reach the same backend collector, especially for error detection or high-latency analysis.

### **A Robust Solution: StatefulSets and Load-Balancing Collectors**

Our solution deploys OpenTelemetry Collectors in a two-tier architecture: load-balancing collectors (frontend) and backend collectors as a StatefulSet. Paired with a headless service and Helm, this setup guarantees consistent TraceID routing and supports tail sampling. Key components include:

- **OpenTelemetry Operator: **Automates collector deployment, workload instrumentation, and telemetry pipelines for seamless Kubernetes observability.
- **Load-Balancing Collectors:** Deployed as a `Deployment`, these collectors receive spans and use the `loadbalancing` exporter to route them by TraceID to a specific backend pod.
- Backend Collectors (StatefulSet): Configured as a StatefulSet, each pod has a stable DNS name (e.g., `dev-opentelemetry-backend-collector-0`), ensuring reliable routing.
- **Headless Service**: A `ClusterIP: None` service exposes backend pod DNS names, enabling precise targeting by the load-balancing exporter.
- **Service Name Matching**: The headless service name (e.g., `dev-opentelemetry-backend-collector-headless`) must match the `StatefulSet`’s `serviceName` for Kubernetes DNS resolution.
- **Tail Sampling**: Backend collectors apply policies (100% for errors/high-latency, 10% for normal traces) to prioritize critical data.
- **Helm Deployment**: The `opentelemetry-collector `Helm chart simplifies configuration for both collector tiers.

### **Bypassing OpenTelemetry Operator Limits**

The **OpenTelemetry Operator** streamlines management but lacks support for the `statefulset.serviceName` parameter needed for headless services. Our workaround? Pair the operator with the `opentelemetry-helm-charts` Helm chart, which offers full control over StatefulSet and service settings, ensuring proper DNS-based routing.

### **How It Works: Configuration Details**

We implement this using two configurations: the load-balancing collector (`operator-collector.yaml`) and backend collector (`backend-collector.yaml`). Below are key excerpts from a tested setup.

### **Load-Balancing Collector** (`operator-collector.yaml`):

```yaml
open_telemetry_collectors:
  main:
    name: "dev-opentelemetry-main"
    replicas: 9
    config:
      receivers:
        otlp:
          protocols:
            grpc:
              endpoint: 0.0.0.0:4317
      processors:
        batch:
          send_batch_size: 20000
          timeout: 5s
      exporters:
        loadbalancing:
          routing_key: "traceID"
          protocol:
            otlp:
              tls:
                insecure: true
          resolver:
            k8s:
              service: dev-opentelemetry-backend-collector-headless.otel-dev
      service:
        pipelines:
          traces:
            receivers: [otlp]
            processors: [batch]
            exporters: [loadbalancing]
```

### **Backend Collector** (`backend-collector.yaml`):

```yaml
opentelemetry-collector:
  nameOverride: "dev-opentelemetry-backend-collector"
  mode: statefulset
  replicaCount: 9
  serviceName: dev-opentelemetry-backend-collector-headless
  service:
    type: ClusterIP
    clusterIP: None
  config:
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
    processors:
      tail_sampling:
        num_traces: 10000
        decision_wait: 10s
        policies:
          - name: error-policy
            type: and
            and_sub_policy:
              - name: error-status
                type: status_code
                status_codes: [ERROR]
              - name: error-sampling
                type: probabilistic
                sampling_percentage: 100
          - name: latency-policy
            type: latency
            latency:
              threshold_ms: 1000
            probabilistic:
              sampling_percentage: 100
          - name: normal-policy
            type: probabilistic
            probabilistic:
              sampling_percentage: 10
      batch:
        send_batch_size: 20000
    exporters:
      googlecloud:
        project: gcp-dev-otel
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [tail_sampling, batch]
          exporters: [googlecloud]
```

### **Key Notes**:

- The load-balancing collector routes spans by TraceID to backend pods via the headless service.
- The backend StatefulSet matches its `serviceName` to the headless service for DNS resolution.
- Tail sampling ensures errors and high-latency traces are fully captured, with efficient normal trace sampling.
- Batch processing optimizes throughput for high-scale tracing.

### **Proof in Action: Test Results**

To validate this setup, we used **telemetrygen** jobs to generate 100 traces (15 spans each) across errors, high-latency (>1.5s), and normal categories, targeting 100% sampling for errors/latency and 10% for normal traces. Tests compared two environments: `dev` (with load-balancing and backend collectors) and `tst` (tail sampling without load-balancing collectors).

#### **Dev Environment**:

- **Errors**: 1500 spans (100% collected).
- **High-Latency**: 1500 spans (100% collected).
- **Normal**: 195 spans (13% collected, slightly above target, under review).
- **Takeaway**: Near-perfect trace alignment, with all spans for a TraceID reaching the same backend pod, ensuring complete traces.

#### **Tst Environment**:

- **Errors**: 988 spans (65% collected, 35% lost).
- **High-Latency**: 988 spans (65% collected, 35% lost).
- **Normal**: 90 spans (6% collected, 40% lost).
- **Takeaway**: Significant span loss due to missing load-balancing collectors, causing trace fragmentation as spans are scattered across pods.

**Key Insight**: Tail sampling in Kubernetes fails without load-balancing collectors, as shown by `tst`’s 35–40% span loss. The `dev` setup proves the architecture’s reliability for microservices tracing.

### **Why This Solution Wins**

This approach delivers:

- **Complete Traces**: Load-balancing collectors ensure trace integrity for accurate tail sampling.
- **Smart Sampling**: Prioritizes errors and high-latency traces while efficiently sampling normal ones.
- **Scalability**: **StatefulSets** and autoscaling (9–30 replicas) handle high-scale tracing effortlessly.
- **Ease of Use**: Helm and the OpenTelemetry Operator simplify deployment, bypassing operator limitations.
- **Proven Results**: Tests confirm `dev`’s success vs. `tst`’s failures, validating the setup for Kubernetes observability.

### **Use Cases**

Perfect for:

- **Microservices Monitoring**: Full visibility into distributed systems.
- **DevOps and SRE**: Faster debugging with reliable traces.
- **Large-Scale Clusters**: Managing heavy trace volumes in Kubernetes.
- **Tail Sampling**: Advanced error and latency analysis.

### **Get Started Today**

Don’t let **trace fragmentation** slow your team down. With **OpenTelemetry**, **StatefulSets**, and **load-balancing collectors**, you can master **Kubernetes observability**.

Our tested configurations (`operator-collector.yaml, backend-collector.yaml`) and **Helm**-based approach makes implementation a breeze.

Explore the[ **OpenTelemetry Helm Charts**](https://github.com/open-telemetry/opentelemetry-helm-charts) or[ **OpenTelemetry documentation**](https://opentelemetry.io/docs/) to dive deeper.

Want to supercharge your microservices tracing? [Contact our observability experts for hands-on support!](https://www.improving.com/contact)
