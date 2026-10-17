---
title: "Protobuf"
type: "Entity"
description: "Interface definition language and serialization format enabling schema-evolved messages across Kafka producers and consumers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data, serialization, streaming]
sources:
  - "/sources/kafka-schema-evolution-with-java-spring-boot-and-protobuf.md"
  - "/sources/the-data-contract-is-an-api-for-trust.md"
---

# Protobuf

Protobuf is an interface definition language and serialization format that this corpus uses to demonstrate schema evolution on event streams. Its field-indexed wire format and compatibility rules make it a practical substrate for data contracts between producers and consumers.

## Schema Evolution

- Protobuf uses an IDL; each field's index is serialized rather than its name and cannot change once messages have been produced with it.
- Removing a field requires adding it to the `reserved` block so no one reuses the field number or name.
- Forward compatibility: a v2 consumer reads a v1 message, the removed field is absent, and the new enum defaults to `UNKNOWN`; backward compatibility: a v1 consumer reads a v2 message, ignoring the new field.
- The schema is registered in a Schema Registry much like Avro, with versions listed per subject and references to imported proto files.
- Chad Sanderson at Convoy built a parallel Protobuf/Kafka implementation as part of the data-contract pattern, showing serialization formats underpin enforceable interfaces.

## Related

- [Apache Kafka](/entities/apache-kafka.md) — the event streaming platform where Protobuf schemas evolve
- [schema drift](/concepts/schema-drift.md) — the failure the compatibility rules prevent
- [data contract](/concepts/data-contract.md) — the enforceable interface Protobuf helps define
- [Spring Boot](/entities/spring-boot.md) — the app framework in the tutorial
- [Confluent](/entities/confluent.md) — schema registry context
