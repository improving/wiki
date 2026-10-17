---
title: "Callback Pattern to the Rescue"
type: "Source Summary"
description: "A C# walkthrough of the Callback / Chain of Responsibility pattern for composing handlers that pass along unhandled callbacks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/callback-pattern-to-the-rescue/callback-pattern-to-the-rescue.md"
---

# Callback Pattern to the Rescue — Summary

**Original source**: `references/devlinliles.com/callback-pattern-to-the-rescue/callback-pattern-to-the-rescue.md`

## Summary

Liles presents the Callback / Chain of Responsibility pattern as a fix for interfaces that have callbacks you don't want at your implementation layer. Using a login credential resolution scenario—already logged in, token from another system, domain authenticated, otherwise prompt the user—he shows how composing handlers lets the chain succeed and return at the deepest level actually needed.

## Key Claims

- Define two interfaces: `ICallbackHandler` with `Handle(params ICallBack[] callBacks)`, and `ICallBack` with a `Handled` flag.
- Callbacks carry data only; the example `WarningCallBack` holds a `WarningDescription` string and no behavior.
- The handler processes each callback and returns only the unhandled ones, so handlers can be composed into a handler or cache stack.
- Each handler either resolves a callback or passes it to the next, which is the Chain of Responsibility pattern.
- The author credits David O'Hara and Craig Neuwirt for the approach.

## Relevance

A legacy .NET / C# pattern note illustrating interface composition and a chain-of-responsibility approach to callback handling.

## Quality

Practitioner blog post by Devlin Liles. Short, code-heavy note built on a single illustrative login example; no discussion of tradeoffs or alternatives.

## Entities Mentioned

- [C#](/entities/c-sharp.md) — language of the examples

## Concepts Covered

- None.

## Related Sources

- [Composing Complex Queries with LINQ](/sources/composing-complex-queries-with-linq.md)
- [LINQ, Lambdas, and the Learning Curve](/sources/linq-lambdas-and-the-learning-curve.md)
- [RhinoMocks and Constrained Expectations](/sources/rhinomocks-and-constrained-expectations.md)
