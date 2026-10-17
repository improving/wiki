---
title: "Specification pattern"
type: "Concept"
description: "Encapsulating a query or business rule as a composable, testable object that repositories can execute and reuse."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-engineering, querying, testing]
sources:
  - "/sources/highway-data-getting-started-video.md"
  - "/sources/i-disagree-with-the-pit-of-doom.md"
---

# Specification pattern

The Specification pattern encapsulates a query or business rule in a composable object so it can be reused, tested in memory, and executed against a real data store. In this corpus it is the constructive answer to the argument that repository abstractions are a "pit of doom": specifications earn the abstraction back by making queries first-class, testable artifacts rather than ad-hoc strings buried in callers.

## Key Claims

- A repository offers both an in-memory collection interface and a testable seam, so a specification can run against fakes as easily as against a live store.
- The pattern shines when paired with pre/post interception, projection, and paging extensions, letting one specification drive many shapes of result.
- Reusing already-tested queries across applications is genuinely valuable, not accidental duplication.
- Abstractions should still expose an escape hatch; the critique targets hiding the data store entirely, not composing queries.
- Highway.Data's getting-started material treats repository patterns, queries, scalars, and advanced queries as one connected topic.

## Related

- [Repository pattern](/concepts/repository-pattern.md) — the abstraction specifications are designed to serve
- [IQueryable](/concepts/iqueryable.md) — the composition mechanism that lets specifications stay deferred
- [expression trees](/concepts/expression-trees.md) — how a specification becomes executable against a provider
- [Highway.Data](/entities/highway-data.md) — framework whose introductory material covers repository patterns and advanced queries
- [Highway.Data Getting Started Video](/sources/highway-data-getting-started-video.md) — primary source
- [I Disagree with the Pit of Doom](/sources/i-disagree-with-the-pit-of-doom.md) — primary source
