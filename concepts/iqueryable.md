---
title: "IQueryable"
type: "Concept"
description: "The LINQ abstraction that lets queries compose in expression-tree form, enabling dynamic filtering and sorting."
created: '2026-10-17'
updated: '2026-10-17'
tags: [dotnet, linq, expression-trees]
sources:
  - "/sources/composing-complex-queries-with-linq.md"
  - "/sources/dynamic-sort-with-linq.md"
---

# IQueryable

The [LINQ](/entities/linq.md) abstraction over composable queries that keeps predicates and projections in [expression-tree](/concepts/expression-trees.md) form. It matters because that form is what lets complex WHERE chains and string-driven sorting be assembled at runtime rather than hand-written as switch statements.

## Key Claims

- Complex WHERE chains with several OR/AND operations make LINQ queries look complicated.
- A `ParameterRebinder` ExpressionVisitor maps parameters between two lambda expressions so predicates can be joined.
- `BuildAnd`, `BuildOr`, and `BuildOrElse` compose predicates from arrays of conditions, enabling dynamic query composition from a UI filter.
- LINQ lacks string-based property access, forcing switch statements or custom extensions for dynamic sorting.
- Expression trees convert property-name strings into sort lambdas via reflection; chained `ThenBy` supports multi-column sorts with per-column direction.
- [NUnit](/entities/nunit.md) tests verify ascending, descending, and multi-sort behavior.

## Related

- [expression trees](/concepts/expression-trees.md) — the mechanism IQueryable composes over
- [Specification pattern](/concepts/specification-pattern.md) — reusable predicates for filtering
- [LINQ](/entities/linq.md) — the language feature
- [C#](/entities/c-sharp.md) — host language
- [Composing Complex Queries with LINQ](/sources/composing-complex-queries-with-linq.md) — primary source
- [Dynamic Sort with LINQ](/sources/dynamic-sort-with-linq.md) — primary source
