---
title: "Repository pattern"
type: "Concept"
description: "An abstraction that presents persistent data as an in-memory collection while centralizing reusable, testable queries."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-design, data-access, testing]
sources:
  - "/sources/highway-data-getting-started-video.md"
  - "/sources/i-disagree-with-the-pit-of-doom.md"
  - "/sources/object-repository-extending-the-standard-repository-pattern.md"
---

# Repository pattern

The repository pattern presents a data store as an in-memory collection and wraps data access behind an abstraction that can be tested and reused. Across this corpus it is contested ground: one camp argues the abstraction is a needless "pit of doom," while the counterargument is that a repository earns its place through testability and query reuse.

## Key Claims

- A repository provides both an in-memory collection interface and a testable abstraction over the store.
- A generic repository exposes [IQueryable](/concepts/iqueryable.md) over an [Entity Framework](/entities/entity-framework.md) ObjectContext, but repeating the same LINQ in many places duplicates magic numbers.
- An object-specific repository (for example, a product repository) centralizes a long-running products query so logic and magic numbers live in one place.
- Wrapping queries enables unit and integration tests for performance validation.
- The [Specification pattern](/concepts/specification-pattern.md) shines with pre/post interception, projection, and paging extensions.
- Reusing tested queries across applications is genuinely valuable; abstractions should expose an escape hatch rather than be abandoned.

## Related

- [IQueryable](/concepts/iqueryable.md) — the query surface a generic repository exposes
- [Specification pattern](/concepts/specification-pattern.md) — composes reusable query criteria
- [Highway.Data](/entities/highway-data.md) — a framework built around these repository patterns
- [Object Repository: Extending the Standard Repository Pattern](/sources/object-repository-extending-the-standard-repository-pattern.md) — primary source
