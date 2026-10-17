---
title: "code readability"
type: "Concept"
description: "Making names, constants, and signatures carry meaning so code explains itself without comments."
created: '2026-10-17'
updated: '2026-10-17'
tags: [craftsmanship, maintainability, dotnet]
sources:
  - "/sources/comments-vs-well-written-code.md"
  - "/sources/linq-lambdas-and-the-learning-curve.md"
---

# code readability

Code readability is the property that lets a reader understand code from its names, constants, and signatures rather than from comments. This corpus treats it as the core of craftsmanship: readable identifiers are easier to search, refactor, and trust than prose annotations, and the same instinct applies to how language features are used.

## Key Claims

- The author's first act in unfamiliar code is to collapse comments, and never re-expand them.
- Well-named identifiers are easier to find with Edit then Find than comments.
- The comment-free MultiStateSalesTaxCalculator example beats the commented class1 version.
- Good code documents itself through names, constants, and method signatures.
- Lambda syntax, not verbose query syntax, is where LINQ's real power and reusability live.
- Intuitively named lambda variables preserve readability while replacing loops.

## Related

- [Software Craftsmanship](/concepts/software-craftsmanship.md) — the discipline that prizes readable code
- [Technical Debt](/concepts/technical-debt.md) — what unreadable code accumulates
- [LINQ](/entities/linq.md) — the feature whose readability depends on lambdas
- [expression trees](/concepts/expression-trees.md) — the mechanism behind lambda-based queries
- [Comments vs. Well-Written Code](/sources/comments-vs-well-written-code.md) — primary source
- [LINQ, Lambdas, and the Learning Curve](/sources/linq-lambdas-and-the-learning-curve.md) — primary source
