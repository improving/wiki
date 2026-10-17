---
title: "expression trees"
type: "Concept"
description: "Code-as-data representations in .NET that let LINQ predicates and sort lambdas be composed dynamically at runtime."
created: '2026-10-17'
updated: '2026-10-17'
tags: [dotnet, linq, query-composition]
sources:
  - "/sources/composing-complex-queries-with-linq.md"
  - "/sources/dynamic-sort-with-linq.md"
---

# expression trees

Expression trees represent code as a data structure rather than compiled instructions, which is what allows [LINQ](/entities/linq.md) queries to be inspected, rewritten, and assembled at runtime. In this corpus they are the enabling mechanism behind two common problems: composing dynamic filter chains and building sort orders from string property names.

## Key Claims

- Complex WHERE chains with several OR/AND operations make LINQ queries hard to read, motivating programmatic composition.
- A `ParameterRebinder` ExpressionVisitor maps parameters between two lambda expressions so separate predicates can be combined.
- `BuildAnd`, `BuildOr`, and `BuildOrElse` compose predicates from arrays of conditions, enabling dynamic queries driven by a UI filter.
- LINQ lacks string-based property access, forcing switch statements or custom extensions for dynamic sorting.
- Expression trees convert property-name strings into sort lambdas via reflection, producing dynamic `OrderBy`/`ThenBy` chains.
- Chained `ThenBy` supports multi-column sorts with per-column direction, verified by unit tests for ascending, descending, and multi-sort cases.

## Related

- [LINQ](/entities/linq.md) — the query technology these trees power
- [IQueryable](/concepts/iqueryable.md) — the interface whose providers consume expression trees
- [Specification pattern](/concepts/specification-pattern.md) — a related approach to composable predicates
- [NUnit](/entities/nunit.md) — the framework used to test the sort behavior
- [Composing Complex Queries with LINQ](/sources/composing-complex-queries-with-linq.md) — primary source
