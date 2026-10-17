---
title: "Kafka Schema Evolution With Java Spring Boot and Protobuf"
type: "Source Summary"
description: "A hands-on tutorial evolving a Protobuf message schema across Kafka producers and consumers, demonstrating forward and backward compatibility."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, kafka, improving.com]
sources:
  - "references/improving.com/kafka-schema-evolution-with-java-spring-boot-and-protobuf/kafka-schema-evolution-with-java-spring-boot-and-protobuf.md"
---

# Kafka Schema Evolution With Java Spring Boot and Protobuf — Summary

**Original source**: `references/improving.com/kafka-schema-evolution-with-java-spring-boot-and-protobuf/kafka-schema-evolution-with-java-spring-boot-and-protobuf.md`

## Summary

A tutorial demonstrating Kafka schema evolution with Java, Spring Boot, and Protobuf: a v1 message schema is changed — a field removed, an enum added — and two consumers on the same topic safely deserialize both versions, showing forward and backward compatibility.

## Key Claims

- Protobuf uses an IDL; each field's index is serialized rather than its name and cannot change once messages are produced with it.
- Removing a field requires adding it to the `reserved` block so no one reuses the field number or name.
- Forward compatibility: a v2 consumer reads a v1 message — the removed `topic` field is absent and the new `Version` enum defaults to `UNKNOWN`.
- Backward compatibility: a v1 consumer reads a v2 message — it ignores `version` and shows an empty `topic`.
- The schema is registered in a Schema Registry much like Avro, with versions listed per subject and references to imported proto files.
- Spring Boot, Gradle, and the protoc build plugin generate the Java classes; a docker-compose file runs Zookeeper, Kafka, schema registry, and the app locally.

## Relevance

Informs [schema drift](/concepts/schema-drift.md) and [data contracts](/concepts/data-contract.md) for [real-time data streaming](/concepts/real-time-data-streaming.md) over Kafka.

## Quality

Detailed practitioner tutorial by Scott Strzynski; working code and a companion repo, but a deliberately simple example app.

## Entities Mentioned

- [Apache Kafka](/entities/apache-kafka.md) — the event streaming platform
- [Protobuf](/entities/protobuf.md) — the IDL and serialization format
- [Java](/entities/java.md) — implementation language
- [Spring Boot](/entities/spring-boot.md) — application framework
- [Confluent](/entities/confluent.md) — schema registry context
- [GitHub](/entities/github.md) — host of the sample code

## Concepts Covered

- [schema drift](/concepts/schema-drift.md) — evolving a schema without breaking consumers
- [data contract](/concepts/data-contract.md) — reserved fields and compatibility rules
- [real-time data streaming](/concepts/real-time-data-streaming.md) — producing and consuming events
