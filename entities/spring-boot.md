---
title: "Spring Boot"
type: "Entity"
description: "Java framework for building services, used here with Kafka, observability stacks, and native-image deployments."
created: '2026-10-17'
updated: '2026-10-17'
tags: [java, backend, framework]
sources:
  - "/sources/adding-a-spring-boot-app-to-the-grafana-observability-platform.md"
  - "/sources/natively-compiled-java-on-google-app-engine.md"
  - "/sources/kafka-schema-evolution-with-java-spring-boot-and-protobuf.md"
  - "/sources/unleashing-feature-flags-onto-kafka-consumers.md"
  - "/sources/how-to-keep-a-secret.md"
---

# Spring Boot

Spring Boot is the Java application framework that recurs across this corpus as the default way to stand up services, from Kafka consumers to instrumented microservices. It is also the baseline against which lighter, compile-time-injection frameworks are compared.

## Where It Appears

- Observability: a Spring Boot app is wired into the Grafana LGTM stack — logs written to a file and scraped into Loki, metrics exposed via `spring-boot-starter-actuator` and `micrometer-registry-prometheus` into Mimir, and traces emitted via `micrometer-tracing` and the OTel bridge into Tempo.
- Performance: Micronaut performs dependency injection and AOP at compile time while Spring does it at runtime, contributing to slower startup that a GraalVM native image can eliminate.
- Streaming: Spring Boot is the application framework in the Kafka Protobuf schema-evolution tutorial and in the Kafka consumer feature-flag example.
- Security: Spring Boot Actuator can expose secrets held in environment variables, an argument for vault API access over env vars.

## Related

- [Java](/entities/java.md) — the language Spring Boot is built on
- [Apache Kafka](/entities/apache-kafka.md) — the streaming platform it consumes from
- [Protobuf](/entities/protobuf.md) — the serialization format used with it in the tutorial
- [observability](/concepts/observability.md) — the telemetry it emits
- [Grafana](/entities/grafana.md) — the stack it is instrumented into
