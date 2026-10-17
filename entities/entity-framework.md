---
title: "Entity Framework"
type: "Entity"
description: "Microsoft's .NET ORM, the setting for the corpus's repository-pattern, IQueryable, and POCO-separation discussions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [product, orm, dotnet, architecture]
sources:
  - "/sources/i-disagree-with-the-pit-of-doom.md"
  - "/sources/object-repository-extending-the-standard-repository-pattern.md"
  - "/sources/rewriting-a-talk-the-day-before-awesome.md"
---

# Entity Framework

Entity Framework is Microsoft's object-relational mapper for .NET. It is the concrete setting for this corpus's classic architecture debates: whether a repository abstraction earns its keep, how to wrap repeated LINQ queries, and the appeal of POCO-based Code-First development.

## Overview

- A generic repository exposes [IQueryable](/concepts/iqueryable.md) over an Entity Framework ObjectContext.
- Repeating the same LINQ in many places duplicates magic numbers; a product-specific repository centralizes the long-running-products query.
- A repository provides both an in-memory collection interface and a testable abstraction, with the Specification pattern shining under pre/post interception, projection, and paging.
- A fresh Code-First CTP let the author rewrite an upcoming POCO talk overnight in four to five hours, keeping the material current.

## Related

- [Repository pattern](/concepts/repository-pattern.md) — the abstraction debated around EF
- [IQueryable](/concepts/iqueryable.md) — the query surface a generic repository exposes
- [LINQ](/entities/linq.md) — the query syntax whose repetition motivates wrapping
- [Specification pattern](/concepts/specification-pattern.md) — composes EF queries with interception and paging
- [POCO separation](/concepts/poco-separation.md) — the persistence-ignorant style EF Code-First enabled
- [Object Repository: Extending the Standard Repository Pattern](/sources/object-repository-extending-the-standard-repository-pattern.md) — primary source
