---
title: "C#"
type: "Entity"
description: "Microsoft's .NET language whose LINQ, lambdas, and tooling shaped a generation of productivity and testing practices."
created: '2026-10-17'
updated: '2026-10-17'
tags: [language, dotnet, software-craftsmanship]
sources:
  - "/sources/callback-pattern-to-the-rescue.md"
  - "/sources/composing-complex-queries-with-linq.md"
  - "/sources/linq-lambdas-and-the-learning-curve.md"
  - "/sources/productivity-tips-write-it-once.md"
  - "/sources/rhinomocks-and-constrained-expectations.md"
---

# C#

C# is Microsoft's primary .NET language. This corpus's C# posts are older craft material: LINQ composition, lambda syntax, code templates, mocking, and the callback pattern — the groundwork beneath the AI-era delivery writing.

## Overview

The recurring theme is reducing friction between intent and implementation. Lambdas are presented as LINQ's real power, with intuitively named variables replacing loops; expression-tree rebinding composes dynamic filters; templates scaffold classes and tests in seconds.

## Key Claims

- Verbose SQL-like LINQ syntax forces developers to relearn LINQ later; lambdas are the durable skill.
- A ParameterRebinder ExpressionVisitor maps parameters so predicates can be composed into AND/OR chains.
- BuildAnd, BuildOr, and BuildOrElse enable dynamic query composition from a UI filter.
- Code templates generated a Person class in 19 seconds and scaffold TDD tests with assertions pre-filled.
- RhinoMocks' Matches() accepts any boolean predicate, but not a lambda with a body; stubs do not fail automatically.

## Related

- [LINQ](/entities/linq.md) — the query language these posts center on
- [expression trees](/concepts/expression-trees.md) — the mechanism behind composable predicates
- [test-driven development](/concepts/test-driven-development.md) — the practice the templates scaffold
- [Productivity Tips: Write It Once](/sources/productivity-tips-write-it-once.md) — primary source
