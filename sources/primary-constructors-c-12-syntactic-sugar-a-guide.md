---
title: "Primary Constructors (C# 12 Syntactic Sugar): A Guide"
type: "Source Summary"
description: "Explains C# 12 primary constructors and their pitfalls: parameters are not fields, not inherited, and not read-only."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, microsoft, improving.com]
sources:
  - "references/improving.com/primary-constructors-c-12-syntactic-sugar-a-guide/primary-constructors-c-12-syntactic-sugar-a-guide.md"
---

# Primary Constructors (C# 12 Syntactic Sugar): A Guide — Summary

**Original source**: `references/improving.com/primary-constructors-c-12-syntactic-sugar-a-guide/primary-constructors-c-12-syntactic-sugar-a-guide.md`

## Summary

Chris Powell introduces C# 12 primary constructors, which place constructor parameters on the class and make them available throughout the body, reducing boilerplate and improving readability. He cautions that the parameters are not fields, are not available to child classes, must be re-declared when overriding, and are not read-only — so dependency-injection parameters can cause runtime errors unless assigned to read-only fields.

## Key Claims

- C# 12 and .NET 8 (November 2023) introduced primary constructors.
- Class parameters are not fields and are not available on `this`.
- Primary constructors work on classes, structs, and records, easing DTO creation.
- Class parameters are not available to child classes; the code will not compile if used there.
- Overriding a constructor requires including the class parameters via `this()`.
- Parameters are not read-only, so DI parameters can produce NullReferenceExceptions if a method runs before assignment.
- Assigning parameters to read-only fields prevents such runtime errors.

## Relevance

Informs [code readability](/concepts/code-readability.md), [type safety](/concepts/type-safety.md), and [software craftsmanship](/concepts/software-craftsmanship.md) in .NET.

## Quality

Concise how-to by Chris Powell; practical caveats, but the examples live in code images not reproduced in text.

## Entities Mentioned

- [C#](/entities/c-sharp.md) — the language gaining primary constructors
- [Microsoft](/entities/microsoft.md) — vendor of .NET and C#

## Concepts Covered

- [code readability](/concepts/code-readability.md) — reducing constructor boilerplate
- [type safety](/concepts/type-safety.md) — read-only fields preventing runtime errors
- [software craftsmanship](/concepts/software-craftsmanship.md) — using a feature with care
