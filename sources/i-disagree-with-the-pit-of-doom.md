---
title: "I Disagree with the Pit of Doom"
type: "Source Summary"
description: "Rebuts Ayende's critique of the repository abstraction, defending repositories and the specification pattern for testability and query reuse."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/i-disagree-with-the-pit-of-doom/i-disagree-with-the-pit-of-doom.md"
---

# I Disagree with the Pit of Doom — Summary

**Original source**: `references/devlinliles.com/i-disagree-with-the-pit-of-doom/i-disagree-with-the-pit-of-doom.md`

## Summary

Liles responds point by point to Ayende's "Architecting in the Pit of Doom: The Evils of the Repository Abstraction Layer." He agrees that abstractions eventually fall down but disputes that the repository abstraction is therefore a mistake, arguing a well-formed repository plus specification pattern buys testability, query reuse, and the ability to change data access without rewriting queries.

## Key Claims

- A repository's purpose is both an in-memory collection interface and a testable abstraction over data; NHibernate and Entity Framework are opinionated about unit of work and data access, and those opinions cannot always be taken.
- Applications may legitimately mix data stores (a non-relational cache plus a relational transactional store), which favors a standard querying architecture.
- He returns `IEnumerable<T>` rather than `IQueryable<T>` to prevent an explosion of joins onto returned queries.
- The specification pattern shines for testable, reusable queries on a single type, with paging, ordering, sorting, projection, interception, and SQL logging as extensions.
- All abstractions fall down; the answer is to know where the abstraction stops—Highway.Data exposes advanced query support to reach the underlying implementation when needed.

## Relevance

A direct argument about the [repository pattern](/concepts/repository-pattern.md), [specification pattern](/concepts/specification-pattern.md), and [unit of work](/concepts/unit-of-work.md) in the [Highway.Data](/entities/highway-data.md) lineage, contrasting [Entity Framework](/entities/entity-framework.md) and engaging [Amir Rajan](/entities/amir-rajan.md).

## Quality

Practitioner blog post by Devlin Liles. A reasoned rebuttal that concedes points where it agrees; it is an opinion exchange between practitioners and offers no benchmarks, relying on design arguments and experience.

## Entities Mentioned

- [Amir Rajan](/entities/amir-rajan.md) — named as a participant in the conversation
- [Entity Framework](/entities/entity-framework.md) — an opinionated data-access implementation the post contrasts with
- [Highway.Data](/entities/highway-data.md) — the author's framework, whose advanced query support answers Ayende's objection

## Concepts Covered

- [Repository pattern](/concepts/repository-pattern.md) — the abstraction under debate
- [Specification pattern](/concepts/specification-pattern.md) — defended as enabling testable, reusable queries
- [Unit of work](/concepts/unit-of-work.md) — the opinionated structure the post resists
- [IQueryable](/concepts/iqueryable.md) — deliberately avoided in favor of `IEnumerable<T>`
