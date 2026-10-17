---
title: "Scala"
type: "Entity"
description: "Statically typed JVM language fusing object-oriented and functional programming, and Improving's language for distributed services."
created: '2026-10-17'
updated: '2026-10-17'
tags: [language, functional-programming, jvm]
sources:
  - "/sources/why-improving-uses-scala.md"
  - "/sources/make-invalid-states-unrepresentable.md"
  - "/sources/designing-an-on-prem-etl-pipeline-for-10tb-day-with-sub-second-latency.md"
  - "/sources/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
---

# Scala

Scala is a statically typed JVM language that combines object-oriented and functional programming, created by Martin Odersky in 2004 to show the two paradigms could be fused practically. It recurs in this corpus as Improving's language for distributed, cloud-native services and as the preferred language for Apache Spark.

## Use and Strengths

- Benefits cited include scalability, static type safety, Java interoperability, immutable data and pure functions, concise syntax, and a large community.
- The type system supports generics, variance annotations, type bounds, implicits, and polymorphic methods, with errors surfacing at compile time.
- Preferred for Apache Spark because its concise syntax and functional features simplify parallel, distributed code.
- Improving uses Scala with Akka to modernize monoliths into distributed, resilient microservices on a Reactive architecture for public-sector, tourism, finance, and logistics clients.
- Appears as the language of Andrew Watson's type-safety examples, moving from `String` to `Int` to refined, newtype, and tagged types so invalid states cannot be constructed.
- Used alongside Python in the on-prem ETL pipeline, and is the prior primary language of the author of the Rust IoT retrospective.

## Related

- [Apache Spark](/entities/apache-spark.md) — distributed engine where Scala is preferred
- [Java](/entities/java.md) — JVM language Scala interoperates with
- [functional programming](/concepts/functional-programming.md) — immutable data and pure functions
- [type safety](/concepts/type-safety.md) — compile-time error catching
- [reactive systems](/concepts/reactive-systems.md) — resilient, message-driven architecture
