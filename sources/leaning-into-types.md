---
title: "Leaning Into Types"
type: "Source Summary"
description: "Argues that replacing boolean flags with dedicated types lets the compiler enforce sanitization and legal state."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, software-craft, improving.com]
sources:
  - "references/improving.com/leaning-into-types/leaning-into-types.md"
---

# Leaning Into Types — Summary

**Original source**: `references/improving.com/leaning-into-types/leaning-into-types.md`

## Summary

A strong type system is not enough; developers must choose to use it, and one practical way is to replace flags with types. A boolean `isSanitized` flag still lets unsanitized data reach code that assumes it is safe, but a distinct `SanitizedString` type makes sanitization the only way to construct the value the rest of the code accepts. Languages with algebraic data types go further, letting the compiler flag incomplete pattern matches and illegal state combinations.

## Key Claims

- Wrapping a string with an `isSanitized` flag still requires logic in every consumer to check the flag — work that can be forgotten.
- Making sanitized strings a distinct type means the only way to obtain that type is by calling `sanitize`, so forgetting sanitization becomes a compile error.
- Algebraic data types (as in F#) catch missing cases: a `Safe | Malicious` union produced an "Incomplete pattern matches" compiler error until the `Malicious` branch was handled.
- Modeling a job applicant as a union of states (`SubmittedResume`, `ScheduledInterview`, `Rejected`, `MadeOffer`), each carrying only its legal data, prevents illegal states without any runtime logic.
- The author notes Idris can even generate the skeleton covering all cases, using algebraic data types to enumerate possibilities.
- The recommendation is to think harder about types up front and recoup the effort through less logic and build-time error reporting on all code paths.

## Relevance

Informs [type safety](/concepts/type-safety.md), [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md), and the wider use of [functional programming](/concepts/functional-programming.md) constructs such as discriminated unions.

## Quality

Practitioner how-to by Ahmed Hammad, using F#-inspired pseudocode; concrete and clear, with the caveat that its algebraic-data-type benefits depend on language support.

## Entities Mentioned

- (none)

## Concepts Covered

- [type safety](/concepts/type-safety.md) — using types to catch errors at compile time
- [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md) — encoding constraints so illegal values cannot exist
- [functional programming](/concepts/functional-programming.md) — algebraic data types and pattern matching
