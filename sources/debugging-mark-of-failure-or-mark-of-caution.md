---
title: "Debugging: Mark of Failure or Mark of Caution?"
type: "Source Summary"
description: "A debate post arguing automated tests beat line-by-line debugging for validating new logic, with an open challenge."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agile-post, devlinliles.com]
sources:
  - "references/devlinliles.com/debugging-mark-of-failure-or-mark-of-caution/debugging-mark-of-failure-or-mark-of-caution.md"
---

# Debugging: Mark of Failure or Mark of Caution? — Summary

**Original source**: `references/devlinliles.com/debugging-mark-of-failure-or-mark-of-caution/debugging-mark-of-failure-or-mark-of-caution.md`

## Summary

A recap of a conference debate in which the author argues that having to debug new logic is a developer failure, because properly written automated tests validate known requirements faster, more reliably, and more explicitly than stepping through code. His interlocutor counters that debugging is the only way to catch behavior you didn't test for. The author invites the community to break his example.

## Key Claims

- Automated tests validate all known requirements quickly, repeatably, and as an explicit codification of system intent; debugging is repetitive, uncodified, and error-prone.
- The cost-to-benefit favors tests: cumulative testing plus debugging time exceeds the time to write good tests.
- Strict mocking and tests that constrain behavior still can't catch every unintended side effect (e.g., a setter firing an unrelated event).
- The author excludes systems without tests, where debugging is unambiguously the first choice.
- He offers a manufacturing-interface example (a mistimed vacuum port invalidates a $10,000,000 production run) and a public repo as a falsification challenge.

## Relevance

Informs [automated testing](/concepts/automated-testing.md) and [test-driven development](/concepts/test-driven-development.md) as the discipline for validating logic.

## Quality

Practitioner blog post by Devlin Liles. Strength: a concrete, falsifiable challenge with a real code example. Caveat: a personal debate framed as opinion, with an illustrative (not measured) cost figure.

## Entities Mentioned

- None.

## Concepts Covered

- [automated testing](/concepts/automated-testing.md) — the preferred validation method
- [test-driven development](/concepts/test-driven-development.md) — the surrounding practice under debate
