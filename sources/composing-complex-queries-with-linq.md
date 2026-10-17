---
title: "Composing Complex Queries with LINQ"
type: "Source Summary"
description: "Shows how to compose reusable AND/OR LINQ predicates using expression trees and a parameter rebinder."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/composing-complex-queries-with-linq/composing-complex-queries-with-linq.md"
---

# Composing Complex Queries with LINQ — Summary

**Original source**: `references/devlinliles.com/composing-complex-queries-with-linq/composing-complex-queries-with-linq.md`

## Summary

Devlin Liles addresses the common need to build chains of complex WHERE clauses with several AND/OR operations — queries that look unwieldy and usually need reuse across several places, such as from a UI filter. His solution composes small `Expression<Func<T, bool>>` predicates on the fly. A `ParameterRebinder` (an `ExpressionVisitor`) rewrites the second lambda's parameters to match the first, and a static `Utility` class exposes `And`, `Or`, `OrElse`, and `BuildAnd`/`BuildOr`/`BuildOrElse` helpers that aggregate arrays of conditions into a single composable predicate applied via `IQueryable.Where`.

## Key Claims

- Small, named [expression trees](/concepts/expression-trees.md) like `isRed`, `isCheap`, and `isClothing` can be combined at runtime into one predicate.
- `Compose<T>` maps the second expression's parameters onto the first's, then merges the two bodies via a supplied combinator.
- `BuildOrElse`/`BuildAnd` aggregate a `params` array of conditions into one predicate, enabling dynamic composition from a UI filter.
- The composed result is applied to an [IQueryable](/concepts/iqueryable.md) with `.Where(isAcceptable)`, preserving deferred execution.
- The technique is adapted and extended from a Microsoft "LINQ to Entities: Combining Predicates" article.

## Relevance

Informs [expression trees](/concepts/expression-trees.md) and [IQueryable](/concepts/iqueryable.md) usage in [LINQ](/entities/linq.md) and C# query composition.

## Quality

Practitioner blog post by Devlin Liles. Concise, working code with a clear usage example; light on caveats (e.g. `BuildOrElse`'s implementation reuses `Expression.Or`, and the snippet's sample tax rates differ from the other example).

## Entities Mentioned

- [LINQ](/entities/linq.md) — the query technology being composed
- [C#](/entities/c-sharp.md) — the language of the examples

## Concepts Covered

- [expression trees](/concepts/expression-trees.md) — predicates composed and parameter-rebound as trees
- [IQueryable](/concepts/iqueryable.md) — the queryable target the composed predicate filters

## Related Sources

- [Callback Pattern to the Rescue](/sources/callback-pattern-to-the-rescue.md)
- [RhinoMocks and Constrained Expectations](/sources/rhinomocks-and-constrained-expectations.md)
