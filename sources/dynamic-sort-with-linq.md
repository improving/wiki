---
title: "Dynamic Sort with LINQ"
type: "Source Summary"
description: "A reusable LINQ extension builds expression trees to sort IQueryable by column-name strings, verified with NUnit tests."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/dynamic-sort-with-linq/dynamic-sort-with-linq.md"
---

# Dynamic Sort with LINQ — Summary

**Original source**: `references/devlinliles.com/dynamic-sort-with-linq/dynamic-sort-with-linq.md`

## Summary

User requests to sort by column name are common, but LINQ does not support string-based property access, leaving a switch statement per column or a reflection-driven extension. The post presents a `LinqSortExtensions` class that splits a dotted property path, builds an `Expression` for the property, constructs a generic lambda, and reflects over `Queryable` to invoke the matching `OrderBy`/`ThenBy` overload. It supports chained, mixed-direction sorts and ships with NUnit tests proving ascending, descending, and multi-key behavior.

## Key Claims

- LINQ has no string-based property access; without a helper, dynamic sorting means a switch statement per column.
- `ApplyOrder` splits the property string on '.', walks nested properties, and builds a strongly typed expression tree via `Expression.Property` and `Expression.Lambda`.
- The extension reflects over `Queryable` methods to find the correct generic two-argument `OrderBy`/`OrderByDescending`/`ThenBy`/`ThenByDescending` overload and invokes it.
- `ThenBy`/`ThenByDescending` overloads allow multiple chained sorts with independently chosen directions.
- Four NUnit tests — `CanSortWithOnlyStrings`, `CanSortDescendingWithOnlyString`, `CanSortMultipleTimesAscending`, and `CanSortMultipleTimesWithMultipleDirections` — verify the behavior.

## Relevance

Informs [expression trees](/concepts/expression-trees.md) and [IQueryable](/concepts/iqueryable.md) as a legacy .NET technique for dynamic query building.

## Quality

Practitioner blog post by Devlin Liles, reposted from an older blog. Code-heavy with runnable NUnit tests; it omits performance, reflection-safety, and null-property caveats.

## Entities Mentioned

- [LINQ](/entities/linq.md) — the query technology being extended
- [Scott Guthrie](/entities/scott-guthrie.md) — cited for his Dynamic LINQ Part 1 article
- [NUnit](/entities/nunit.md) — the test framework used for the verification tests

## Concepts Covered

- [expression trees](/concepts/expression-trees.md) — used to build a typed property-accessor lambda
- [IQueryable](/concepts/iqueryable.md) — the interface the extension methods target
