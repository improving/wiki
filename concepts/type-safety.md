---
title: "type safety"
type: "Concept"
description: "Using the type system to make invalid states unrepresentable and catch errors at compile time."
created: '2026-10-17'
updated: '2026-10-17'
tags: [engineering, software-craft, architecture]
sources:
  - "/sources/make-invalid-states-unrepresentable.md"
  - "/sources/leaning-into-types.md"
  - "/sources/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
  - "/sources/why-improving-uses-scala.md"
  - "/sources/java-enums-for-better-code.md"
  - "/sources/primary-constructors-c-12-syntactic-sugar-a-guide.md"
---

# type safety

Type safety is the practice of choosing types precisely enough that the compiler enforces the rules a developer would otherwise check by hand, making invalid states unrepresentable. The corpus's recurring point is that a strong type system is necessary but not sufficient: developers must choose to lean into it, replacing flags and stringly-typed values with dedicated types, discriminated unions, and constrained primitives so that forgetting a check becomes a compile error rather than a runtime surprise.

## Key Claims

- Model data with the most specific type that works: a `String` age requires parsing and validation at every use, an `Int` fails fast, and refined/newtype/tagged types keep an `Age` from being confused with a `Weight`.
- A boolean `isSanitized` flag still lets unsanitized data reach code that assumes it is safe, but a distinct `SanitizedString` type makes `sanitize` the only way to construct the value the rest of the code accepts.
- Algebraic data types catch missing cases: an F# `Safe | Malicious` union produced an "Incomplete pattern matches" compiler error until the `Malicious` branch was handled, and modeling a job applicant as a union of states prevents illegal states with no runtime logic.
- Prefer low-cardinality types such as enums over high-cardinality ones to limit invalid states, and move toward specificity only as requirements demand — going from specific to general is easier than the reverse.
- Language support matters: Scala's type system offers generics, variance annotations, type bounds, implicits, and polymorphic methods with compile-time error catching; Rust's proper error enums and traits replace `String` error types and over 100 `.unwrap()` calls in a real project.
- Type choices pay off elsewhere too: Java enums as objects collapse a handler set and its lookup map into one source of truth, while C# 12 primary constructors cut boilerplate but carry pitfalls — parameters are not fields, not inherited, and not read-only, so DI parameters can cause runtime errors unless assigned to read-only fields.

## Related

- [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md) — the central technique
- [functional programming](/concepts/functional-programming.md) — algebraic data types and pattern matching
- [design patterns](/concepts/design-patterns.md) — newtype and tagged-type patterns
- [code readability](/concepts/code-readability.md) — types that make code explain itself
- [Scala](/entities/scala.md) — a statically typed JVM language used at Improving
- [Rust](/entities/rust.md) — memory-safe systems language with strong error types
