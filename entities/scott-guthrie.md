---
title: "Scott Guthrie"
type: "Entity"
description: "Microsoft executive associated with .NET and Entity Framework; cited in a talk rewritten around a Code-First CTP release."
created: '2026-10-17'
updated: '2026-10-17'
tags: [microsoft, dotnet, speaker]
sources:
  - "/sources/dynamic-sort-with-linq.md"
  - "/sources/rewriting-a-talk-the-day-before-awesome.md"
---

# Scott Guthrie

Scott Guthrie is a Microsoft executive long associated with the .NET platform, ASP.NET, and Entity Framework. In this corpus he appears as the context for .NET-era tooling and for a talk rebuilt around a fresh Entity Framework release.

## Overview

One post describes rewriting an upcoming POCO talk overnight — four to five hours of work — after discovering an Entity Framework Code-First CTP released the day before, so the material would be current. Guthrie is the figurehead of that .NET lineage. The other post works the same stack from the other direction: a LINQ extension that builds dynamic `OrderBy`/`ThenBy` sorting from string property names using expression trees.

## Key Claims

- A new Entity Framework Code-First CTP the day before a talk made the material timely
- Rewriting the talk to use the latest features took four to five hours
- Being on the latest technology makes a talk more compelling
- LINQ lacks string-based property access, forcing switch statements or custom extensions
- Expression trees convert property-name strings into sort lambdas via reflection, and NUnit tests verify ascending, descending, and multi-column sorts

## Related

- [LINQ](/entities/linq.md) — the query technology from the same .NET lineage
- [Entity Framework](/entities/entity-framework.md) — the CTP driving the talk rewrite
- [Expression Trees](/concepts/expression-trees.md) — the mechanism behind dynamic sorting
- [POCO Separation](/concepts/poco-separation.md) — the talk's subject
- [Dynamic Sort with LINQ](/sources/dynamic-sort-with-linq.md) — primary source
