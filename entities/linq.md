---
title: "LINQ"
type: "Entity"
description: "Microsoft's .NET query language and library whose lambda syntax and expression trees enable dynamic, composable data access."
created: '2026-10-17'
updated: '2026-10-17'
tags: [dotnet, language, data-access]
sources:
  - "/sources/composing-complex-queries-with-linq.md"
  - "/sources/dynamic-sort-with-linq.md"
  - "/sources/linq-lambdas-and-the-learning-curve.md"
  - "/sources/object-repository-extending-the-standard-repository-pattern.md"
---

# LINQ

Language Integrated Query is the .NET facility for querying in-memory collections, [Entity Framework](/entities/entity-framework.md) contexts, and other sources with one syntax. Across this corpus it appears less as a feature to admire than as a tool whose real power — and real learning curve — lives in its lambda and expression-tree machinery.

## Key Claims

- Lambda syntax, not SQL-like query syntax, is where LINQ's reusability lives; developers who learn the verbose form must relearn LINQ later ([linq, lambdas, and the learning curve](/sources/linq-lambdas-and-the-learning-curve.md))
- [Expression trees](/concepts/expression-trees.md) let string property names become sort lambdas, enabling dynamic `OrderBy`/`ThenBy` chains with per-column direction ([dynamic sort with linq](/sources/dynamic-sort-with-linq.md))
- A `ParameterRebinder` visitor maps parameters between lambdas so `BuildAnd`/`BuildOr` compose complex WHERE chains from arrays of conditions ([composing complex queries with linq](/sources/composing-complex-queries-with-linq.md))
- Repeating the same query in many places duplicates magic numbers; a product-specific [repository pattern](/concepts/repository-pattern.md) wrapper centralizes the logic ([object repository](/sources/object-repository-extending-the-standard-repository-pattern.md))
- NUnit tests verify ascending, descending, and multi-column sort behavior.

## Related

- [expression trees](/concepts/expression-trees.md) — the mechanism behind dynamic LINQ
- [IQueryable](/concepts/iqueryable.md) — the interface LINQ queries compose over
- [Repository pattern](/concepts/repository-pattern.md) — how repeated LINQ is wrapped
- [C#](/entities/c-sharp.md) — the language LINQ ships with
- [Devlin Liles](/entities/devlin-liles.md) — author of these posts
