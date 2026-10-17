---
title: "Amir Rajan"
type: "Entity"
description: ".NET developer and author who defends the repository abstraction and records a deliberate apprenticeship in Ruby."
created: '2026-10-17'
updated: '2026-10-17'
tags: [developer, dotnet, ruby]
sources:
  - "/sources/i-disagree-with-the-pit-of-doom.md"
  - "/sources/starting-out-in-ruby.md"
---

# Amir Rajan

A .NET developer and author who appears in this corpus as a defender of well-chosen abstractions and as a deliberate learner of new languages.

## Overview

Rajan's contributions sit at the intersection of design patterns and craftsmanship: he argues for keeping the [repository pattern](/concepts/repository-pattern.md) rather than abandoning it, and he treats learning Ruby as an apprenticeship rather than a syntax transfer.

## Key Claims

- Against Ayende's "pit of doom" critique, Rajan argues the repository earns its place by providing both an in-memory collection interface and a testable abstraction.
- The [Specification pattern](/concepts/specification-pattern.md) shines with pre/post interception, projection, and paging extensions, and reusing tested queries across applications is genuinely valuable.
- His rule for abstractions: expose an escape hatch rather than abandon the abstraction — a stance relevant to [IQueryable](/concepts/iqueryable.md) and [Unit of work](/concepts/unit-of-work.md) debates.
- On Ruby, he notes that the language lets you extend a class to add a class-scoped method and override constructors to return other objects; his apprenticeship pairs Ruby Koans with a console game project.
- His stated goal is to learn Ruby properly, not to write [C#](/entities/c-sharp.md) in Ruby.

## Related

- [Repository pattern](/concepts/repository-pattern.md) — the abstraction he defends
- [Specification pattern](/concepts/specification-pattern.md) — pattern he argues pairs well with repositories
- [I Disagree with the Pit of Doom](/sources/i-disagree-with-the-pit-of-doom.md) — primary source
