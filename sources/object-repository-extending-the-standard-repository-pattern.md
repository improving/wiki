---
title: "Object Repository: Extending the Standard Repository Pattern"
type: "Source Summary"
description: "An object-specific repository wraps repeated LINQ queries so a magic number lives in one place, illustrated over Entity Framework 4.1."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/object-repository-extending-the-standard-repository-pattern/object-repository-extending-the-standard-repository-pattern.md"
---

# Object Repository: Extending the Standard Repository Pattern — Summary

**Original source**: `references/devlinliles.com/object-repository-extending-the-standard-repository-pattern/object-repository-extending-the-standard-repository-pattern.md`

## Summary

The post addresses the repeated [LINQ](/entities/linq.md) queries developers write against an object set and shows a small fix: an object-specific repository layered over a generic one. It builds a generic [Entity Framework](/entities/entity-framework.md) repository exposing [IQueryable](/concepts/iqueryable.md), then wraps a "long running products" query in a product-specific repository so the query and its magic number live in one place. The result is a single definition reused everywhere and a natural seam for tests.

## Key Claims

- The generic repository returns an `IQueryable<T>` from the object context and handles save, add, delete, attach, and detach.
- Repeating the same query (for example `DaysToManufacture > 3`) across a codebase is tedious and hides an uncontrolled magic number.
- An object-specific repository such as `ProductRepository` wraps that query behind an interface, so callers no longer remember the `3`.
- If the threshold changes, it changes in exactly one place.
- The wrapper also gives a natural seam for unit, integration, and performance tests.

## Relevance

A concrete implementation of the [Repository pattern](/concepts/repository-pattern.md) and [POCO separation](/concepts/poco-separation.md) in a legacy .NET stack, showing how [IQueryable](/concepts/iqueryable.md) supports composable, centralized queries.

## Quality

Practitioner blog post by Devlin Liles. Clear, compilable example, but it targets Entity Framework 4.1 and is illustrative rather than benchmarked.

## Entities Mentioned

- [Entity Framework](/entities/entity-framework.md) — the ORM the repository wraps
- [LINQ](/entities/linq.md) — the query syntax being centralized

## Concepts Covered

- [Repository pattern](/concepts/repository-pattern.md) — extended with an object-specific layer
- [POCO separation](/concepts/poco-separation.md) — the persistence-ignorant model the repository works over
- [IQueryable](/concepts/iqueryable.md) — the composable query surface the repository returns
