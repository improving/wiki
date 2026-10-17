---
title: "POCO separation"
type: "Concept"
description: "Keeping persistence-ignorant plain objects separate from the framework plumbing that loads and saves them."
created: '2026-10-17'
updated: '2026-10-17'
tags: [entity-framework, architecture, dotnet]
sources:
  - "/sources/object-repository-extending-the-standard-repository-pattern.md"
  - "/sources/rewriting-a-talk-the-day-before-awesome.md"
---

# POCO separation

POCO separation keeps domain objects plain — no base class, no framework attributes — so persistence concerns live in repositories and mapping code rather than in the entities themselves. In this corpus it appears through Entity Framework Code-First, where a fresh CTP made the boundary practical to demonstrate.

## Key Claims

- A generic repository exposes IQueryable over an Entity Framework ObjectContext.
- Repeating the same LINQ in many places duplicates magic numbers; a product-specific repository centralizes queries like "long-running products".
- Wrapping queries in an object repository enables unit and integration tests, including performance validation.
- A new Entity Framework Code-First CTP let the author rewrite an upcoming POCO talk overnight in four to five hours.
- Being on the latest technology makes a talk more compelling.

## Related

- [Repository pattern](/concepts/repository-pattern.md) — where the persistence boundary lives
- [IQueryable](/concepts/iqueryable.md) — the leaky abstraction POCO separation guards against
- [Unit of work](/concepts/unit-of-work.md) — tracks the objects across a transaction
- [Entity Framework](/entities/entity-framework.md) — the ORM in these examples
- [Object Repository: Extending the Standard Repository Pattern](/sources/object-repository-extending-the-standard-repository-pattern.md) — primary source
