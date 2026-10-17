---
title: "This Golang Behavior is Unexpected... Or is it?"
type: "Source Summary"
description: "Uses a surprising Go slice/append example to show how capacity aliasing causes bugs Rust would catch at compile time."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, software, improving.com]
sources:
  - "references/improving.com/this-golang-behavior-is-unexpected-or-is-it/this-golang-behavior-is-unexpected-or-is-it.md"
---

# This Golang Behavior is Unexpected... Or is it? — Summary

**Original source**: `references/improving.com/this-golang-behavior-is-unexpected-or-is-it/this-golang-behavior-is-unexpected-or-is-it.md`

## Summary

Xander Apponi dissects a Go example in which appendAndChange modifies the caller's slice only sometimes. The cause is Go slices' separate length and capacity: append allocates a new backing array when capacity is insufficient, so mutations are lost, but reuses the array when capacity allows, so mutations leak back to the caller. He contrasts this with Rust, where move semantics and a push method taking &mut self prevent the ambiguity at compile time.

## Key Claims

- Go slices carry both a length and a capacity; cap(s) counts the underlying array from the slice's first element.
- append allocates a bigger array only when the backing array is too small, so whether a mutation is visible depends on spare capacity.
- In the example, appending to [1 2 3] leaves the original intact, but appending to [1 2 3 5] modifies it, because the second slice has spare capacity.
- The documented fix is to store append's return value, but the author argues developers should not have to read base-library docs to find such edge cases.
- Rust's Vec::push takes &mut self and returns (), and its move semantics reject the aliasing pattern with a compile error suggesting a borrow instead.
- The root problem in Go is two pointers with different attributes (length, capacity) to the same underlying array.

## Relevance

A concrete illustration of [type safety](/concepts/type-safety.md) and [code readability](/concepts/code-readability.md) trade-offs between [Go](/entities/go.md) and [Rust](/entities/rust.md).

## Quality

Careful technical explainer by Xander Apponi; well-diagrammed and concrete, with a clear bias toward Rust.

## Entities Mentioned

- [Go](/entities/go.md) — the language with the surprising behavior
- [Rust](/entities/rust.md) — the comparison language with stronger compile checks

## Concepts Covered

- [type safety](/concepts/type-safety.md) — compile-time prevention of aliasing bugs
- [code readability](/concepts/code-readability.md) — how standard-library design shapes confusion
