---
title: "Make Invalid States Unrepresentable"
type: "Source Summary"
description: "Walks from String to Int to constrained and tagged types, showing how type choices eliminate invalid values."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, engineering, improving.com]
sources:
  - "references/improving.com/make-invalid-states-unrepresentable/make-invalid-states-unrepresentable.md"
---

# Make Invalid States Unrepresentable — Summary

**Original source**: `references/improving.com/make-invalid-states-unrepresentable/make-invalid-states-unrepresentable.md`

## Summary

Andrew Watson argues that modeling data with precise types lets the compiler do validation. Using an age field in Scala, he moves from `String` (stringly-typed, validated everywhere) to `Int` (fails fast, unrepresentable strings) to runtime assertions, refined types, and finally newtypes and tagged types that keep an `Age` from being confused with a `Weight`.

## Key Claims

- A `String` age requires parsing and validation at every use and can throw at runtime.
- An `Int` age fails fast and makes the string case unrepresentable.
- Runtime assertions (e.g. `0 <= age < 150`) catch invalid numbers but halt execution at runtime.
- Compile-time refined types work only for literal values, so user input still needs runtime constraints.
- Newtypes and tagged types prevent swapping values of the same underlying type, such as age and weight.
- Prefer low-cardinality types like enums to high-cardinality types to limit invalid states.
- Move toward specificity only as requirements demand; going from specific to general types is easier than the reverse.

## Relevance

Informs [type safety](/concepts/type-safety.md), [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md), and [functional programming](/concepts/functional-programming.md).

## Quality

Technical explainer by Andrew Watson with Scala examples; rigorous and practical, though language-specific.

## Entities Mentioned

- [Scala](/entities/scala.md) — the language used for the examples

## Concepts Covered

- [type safety](/concepts/type-safety.md) — main topic
- [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md) — the central technique
- [functional programming](/concepts/functional-programming.md) — refined and tagged types
- [design patterns](/concepts/design-patterns.md) — newtype and tagged-type patterns
