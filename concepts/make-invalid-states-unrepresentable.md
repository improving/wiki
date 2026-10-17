---
title: "make invalid states unrepresentable"
type: "Concept"
description: "Encoding constraints in types so illegal values cannot be constructed, making validation a compile-time concern."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-craft, type-safety, design]
sources:
  - "/sources/make-invalid-states-unrepresentable.md"
  - "/sources/leaning-into-types.md"
  - "/sources/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
---

# make invalid states unrepresentable

A modeling discipline: choose types so that illegal values cannot be constructed at all, rather than validating them away at runtime. The corpus presents it as the practical payoff of a strong type system — the compiler does the checking, and whole classes of bug become impossible rather than merely detected.

## Key Claims

- A `String` age must be parsed and validated at every use and can throw at runtime; an `Int` age fails fast and makes the string case unrepresentable.
- Runtime assertions (for example `0 <= age < 150`) catch invalid numbers but halt execution at runtime, whereas type-level constraints move the check to build time.
- Compile-time refined types work only for literal values, so user input still needs runtime constraints — the technique shifts where validation lives, it does not eliminate it.
- Newtypes and tagged types prevent swapping values of the same underlying type, such as age and weight.
- Prefer low-cardinality types like enums over high-cardinality ones to limit how many invalid states exist.
- Replacing a boolean `isSanitized` flag with a distinct `SanitizedString` type makes `sanitize` the only way to construct the value, so forgetting sanitization becomes a compile error.
- Move toward specificity only as requirements demand; going from specific to general types is easier than the reverse.
- The Rust retrospective shows the cost of ignoring this: over 100 `.unwrap()` calls in ~5,000 lines, and `String` error types, are exactly what proper error enums would replace.

## Related

- [type safety](/concepts/type-safety.md) — the property that makes this possible
- [functional programming](/concepts/functional-programming.md) — algebraic data types and pattern matching
- [design patterns](/concepts/design-patterns.md) — newtype and tagged-type patterns
- [Scala](/entities/scala.md) — the language used for the worked examples
