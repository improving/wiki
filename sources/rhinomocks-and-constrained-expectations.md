---
title: "RhinoMocks and Constrained Expectations"
type: "Source Summary"
description: "A short C# post demonstrating RhinoMocks Matches() constraints, strict mocks versus stubs, and manual verification."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/rhinomocks-and-constrained-expectations/rhinomocks-and-constrained-expectations.md"
---

# RhinoMocks and Constrained Expectations — Summary

**Original source**: `references/devlinliles.com/rhinomocks-and-constrained-expectations/rhinomocks-and-constrained-expectations.md`

## Summary

A brief code-snippet post showing how to use RhinoMocks constraints in tests. Through three illustrative test methods it contrasts strict mocks, which enforce the constraint and fail when the wrong input arrives, with stubs, which are more permissive and make it easier to get a passing test against failing code. It also notes a compile-time gotcha with the `Matches()` predicate.

## Key Claims

- The `Matches()` method accepts any predicate or method call that returns a boolean.
- A lambda with a method body (for example `() => {}`) will not compile inside an expectation.
- A strict mock enforces the constraint; a stub does not, making it easier to get a passing test on failing code.
- With a stub, the constraint must be verified manually using `AssertWasCalled`.

## Relevance

Informs [automated testing](/concepts/automated-testing.md) practice in C#, specifically the behavior difference between mocks and stubs when writing expectations.

## Quality

Practitioner blog post by Devlin Liles. Purely illustrative code with minimal prose; no benchmarks or broader testing guidance.

## Entities Mentioned

- [C#](/entities/c-sharp.md) — the language of the sample tests

## Concepts Covered

- [automated testing](/concepts/automated-testing.md) — the post's domain, via mocking constraints

## Related Sources

- [Callback Pattern to the Rescue](/sources/callback-pattern-to-the-rescue.md)
- [Composing Complex Queries with LINQ](/sources/composing-complex-queries-with-linq.md)
