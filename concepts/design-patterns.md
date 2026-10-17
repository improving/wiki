---
title: "design patterns"
type: "Concept"
description: "Reusable solutions to recurring design problems, and the shared vocabulary they create across a team."
created: '2026-10-17'
updated: '2026-10-17'
tags: [engineering, design, architecture]
sources:
  - "/sources/why-design-patterns-matter.md"
  - "/sources/books-every-developer-should-read.md"
  - "/sources/java-enums-for-better-code.md"
  - "/sources/developer-of-the-future.md"
  - "/sources/best-current-practices-part-i.md"
  - "/sources/slaying-the-dragon-tips-for-legacy-application-modernization.md"
---

# design patterns

Design patterns are tried-and-tested solutions to recurring design problems that give practitioners a common language. The corpus treats them as more than code templates: in UX they make interfaces predictable and reduce cognitive load, in software they name structural idioms a team can reason with, and because they are time-bound and context-dependent they are best applied as trade-offs rather than dictates.

## Key Claims

- A pattern is a shared vocabulary first: naming a solution lets a team discuss and reuse it, whether for registration forms, navigation menus, and product listings in UX, or for structural idioms in code.
- Patterns reduce cognitive load and ensure predictability — early UX designers solving each problem uniquely made it hard for users to move between interfaces, which is why standardized patterns emerged through user testing.
- Patterns are time-bound: the monolith was once a best practice, and microservices, the Actor model, and Chaos Monkey all carry hidden assumptions about reuse, maintenance capacity, and ops maturity.
- Foundational texts matter — Head First Design Patterns is recommended over the aging Gang of Four examples, and Refactoring to Patterns and Working Effectively with Legacy Code pair patterns with incremental change.
- Concrete idioms appear throughout the corpus: Java enums as objects that collapse a handler set and its lookup map into one source of truth, and newtype/tagged-type patterns for type safety.
- In legacy modernization, patterns help once tests are in place: as coupled code splits, teams look for patterns, remove duplication, unify similar classes behind abstract base classes, and introduce interfaces and dependency injection.

## Related

- [microservices](/concepts/microservices.md) — an architectural pattern with hidden assumptions
- [type-safety](/concepts/type-safety.md) — newtype and tagged-type patterns
- [code readability](/concepts/code-readability.md) — idioms that remove hardcoded lookup tables
- [user experience](/concepts/user-experience.md) — consistent, predictable interfaces
- [software craftsmanship](/concepts/software-craftsmanship.md) — patterns as shared craft vocabulary
