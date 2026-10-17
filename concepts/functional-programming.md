---
title: "functional programming"
type: "Concept"
description: "Building software from pure functions and immutable data, with algebraic types and compile-time checking."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-craft, type-safety, languages]
sources:
  - "/sources/why-improving-uses-scala.md"
  - "/sources/leaning-into-types.md"
  - "/sources/make-invalid-states-unrepresentable.md"
  - "/sources/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
---

# functional programming

A style of building software from pure functions and immutable data, so behavior is easier to reason about and the compiler can enforce more of it. In this corpus it appears mainly through Scala, the JVM language Improving uses for distributed microservices, and through the type-driven practices — algebraic data types, pattern matching, refined and tagged types — that functional languages make practical.

## Key Claims

- Scala, created by Martin Odersky in 2004, fuses object-oriented and functional programming on the JVM; Improving uses it with Akka to modernize monoliths into distributed, cloud-native microservices.
- Core benefits cited are immutable data and pure functions alongside static type safety, Java interoperability, concise syntax, and a large community.
- Scala is the preferred language for Apache Spark because its concise syntax and functional features simplify parallel, distributed code.
- Algebraic data types, as in F#, let the compiler catch missing cases — a `Safe | Malicious` union produced an "Incomplete pattern matches" error until the malicious branch was handled.
- Union modeling replaces flags and runtime checks: representing a job applicant as `SubmittedResume | ScheduledInterview | Rejected | MadeOffer`, each carrying only its legal data, prevents illegal states.
- Functional type constructs — refined types, newtypes, and tagged types — stop values of the same underlying type from being swapped, such as age and weight.
- The recurring recommendation is to think harder about types up front and recoup the effort through less logic and build-time error reporting across all code paths.

## Related

- [type safety](/concepts/type-safety.md) — the compile-time checking functional types lean on
- [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md) — the practice of encoding constraints in types
- [design patterns](/concepts/design-patterns.md) — newtype and tagged-type patterns used in these examples
- [Scala](/entities/scala.md) — the language Improving uses to apply these ideas
- [Rust](/entities/rust.md) — a systems language where the same type-safety concerns show up
