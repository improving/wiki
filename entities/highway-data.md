---
title: "Highway.Data"
type: "Entity"
description: "A .NET repository and query library defended in this corpus as a testable abstraction worth keeping."
created: '2026-10-17'
updated: '2026-10-17'
tags: [dotnet, orm, repository, c-sharp]
sources:
  - "/sources/highway-data-getting-started-video.md"
  - "/sources/i-disagree-with-the-pit-of-doom.md"
---

# Highway.Data

Highway.Data is a .NET library that provides a repository abstraction over a data store, with query, scalar, and command support plus eager loading. In this corpus it is the concrete example in the argument that the repository pattern earns its place through testability and query reuse.

## Overview

- A getting-started video series covers patterns, queries, scalars, commands, advanced queries, eager loading, and the IDomain abstraction.
- The library exposes both an in-memory collection interface and a testable abstraction over the database.
- Its Specification-pattern support shines with pre/post interception, projection, and paging extensions.
- Reusing tested queries across applications is presented as genuinely valuable.
- The counterargument (Ayende's critique) is answered by keeping an escape hatch rather than abandoning the abstraction.

## Related

- [Repository pattern](/concepts/repository-pattern.md) — the abstraction Highway.Data implements
- [Specification pattern](/concepts/specification-pattern.md) — query composition built on top
- [Entity Framework](/entities/entity-framework.md) — the underlying ORM in the .NET stack
- [LINQ](/entities/linq.md) — the query syntax the library builds on
- [I Disagree with the Pit of Doom](/sources/i-disagree-with-the-pit-of-doom.md) — primary source
