---
title: "Unit of work"
type: "Concept"
description: "A repository abstraction that groups queries and commands into one testable, reusable unit of data access."
created: '2026-10-17'
updated: '2026-10-17'
tags: [software-engineering, data-access, testing]
sources:
  - "/sources/highway-data-getting-started-video.md"
  - "/sources/i-disagree-with-the-pit-of-doom.md"
---

# Unit of work

The unit of work is the [Repository pattern](/concepts/repository-pattern.md)'s boundary: one abstraction that presents data as an in-memory collection while grouping related queries and commands into a single, testable operation. It matters here because it is the design idea behind [Highway.Data](/entities/highway-data.md) and the subject of a running debate about whether repository abstractions earn their place.

## Key Claims

- A repository provides both an in-memory collection interface and a testable abstraction.
- The [Specification pattern](/concepts/specification-pattern.md) shines with pre/post interception, projection, and paging extensions.
- Reusing tested queries across applications is genuinely valuable.
- Abstractions should expose an escape hatch rather than be abandoned.
- The Highway.Data getting-started video covers patterns, queries, scalars, commands, advanced queries, eager loading, and the IDomain abstraction in one sitting.

## Related

- [Repository pattern](/concepts/repository-pattern.md) — the abstraction the unit of work defines
- [Specification pattern](/concepts/specification-pattern.md) — composable, reusable query criteria
- [IQueryable](/concepts/iqueryable.md) — the LINQ query surface these repositories wrap
- [I Disagree with the Pit of Doom](/sources/i-disagree-with-the-pit-of-doom.md) — primary source
