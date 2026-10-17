---
title: "Designing for Testing"
type: "Source Summary"
description: "Four concise principles for treating tests as first-class production code owned by the whole team."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agile-post, devlinliles.com]
sources:
  - "references/devlinliles.com/designing-for-testing/designing-for-testing.md"
---

# Designing for Testing — Summary

**Original source**: `references/devlinliles.com/designing-for-testing/designing-for-testing.md`

## Summary

Distilled from years of discussions about TDD, BDD, and manual test case management, the post offers four principles for making testing a first-class part of development: everyone owns UI automation, shared test code is production code, every developer can read/write/run tests, and the toolchain must be stupid easy to use.

## Key Claims

- Tests are the practice squad: if they aren't strong enough to challenge the team, mistakes surface in production.
- Shared test code — data factories, simulators, and toolkit code — should meet production standards, because a craftsman takes pride in his tools.
- Every "Developer" in the Scrum.org sense (testers, coders, and others) should be able to read, write, and run the tests; out of sight means it doesn't matter.
- Building, deploying, and testing should be trivially easy so it becomes part of the workflow (e.g., a psake-driven loop: pull, build, change, build, merge, build, push).

## Relevance

Informs [automated testing](/concepts/automated-testing.md), [test-driven development](/concepts/test-driven-development.md), and [software craftsmanship](/concepts/software-craftsmanship.md) as cultural prerequisites for maintainable code.

## Quality

Practitioner blog post by Devlin Liles. Strength: a terse, memorable checklist that ties testing to team ownership and craft. Caveat: an opinion list with no evidence or case detail, and tooling examples are Windows-specific.

## Entities Mentioned

- [Scrum.org](/entities/scrum-org.md) — source of the inclusive "Developer" definition

## Concepts Covered

- [automated testing](/concepts/automated-testing.md) — the practice the principles support
- [test-driven development](/concepts/test-driven-development.md) — the surrounding discipline discussed
- [software craftsmanship](/concepts/software-craftsmanship.md) — the craftsman ethos applied to test tooling
