---
title: "APIs and the Walls They Build: Do Good Fences Make Good Neighbors?"
type: "Source Summary"
description: "Uses Frost's Mending Wall to argue APIs are fences that shape organizational behavior, so design them for the neighbors you want."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, software, architecture, improving.com]
sources:
  - "references/improving.com/apis-and-the-walls-they-build-do-good-fences-make-good-neighbors/apis-and-the-walls-they-build-do-good-fences-make-good-neighbors.md"
---

# APIs and the Walls They Build: Do Good Fences Make Good Neighbors? — Summary

**Original source**: `references/improving.com/apis-and-the-walls-they-build-do-good-fences-make-good-neighbors/apis-and-the-walls-they-build-do-good-fences-make-good-neighbors.md`

## Summary

The post uses Robert Frost's "Mending Wall" to argue that an API is a fence with a few approved entry points, separating "mine" from "theirs" — and that such a boundary shapes human behavior, not just code. Because a clean API boundary can discourage fixing a bug just beyond it, the author says architecture should be judged by whether it encourages the behaviors the company needs.

## Key Claims

- An API — a class interface, a library facade, or a vendor's REST service — is a fence with approved entry points that clearly marks what is mine and what is not.
- That boundary is useful but limiting: discovering a bug just past the entry point tempts developers to leave it for the owning team.
- This is Conway's Law at work: organizations tend to build systems that mirror their own communication structure.
- Amazon's "Team APIs" memo turned an API question into a "how we do business" question and, apocryphally, laid the groundwork for AWS.
- Counter-example: banks still run late-1970s/1980s COBOL systems touching about $3 trillion in daily transactions — successful but now constraining how the business can operate.
- The design question becomes: does this architecture encourage the behaviors the company needs — mutual support (InnerSource-style) or strong fences and separation of duties?

## Relevance

Frames APIs as [design patterns](/concepts/design-patterns.md) that create [abstraction debt](/concepts/abstraction-debt.md), and reads them through [systems thinking](/concepts/systems-thinking.md), with [Robert Frost](/entities/robert-frost.md) as the framing device.

## Quality

Thoughtful essay by Daniel Scheufler; a memorable argument connecting architecture to organizational behavior, but light on concrete design guidance.

## Entities Mentioned

- [Robert Frost](/entities/robert-frost.md) — poet whose "Mending Wall" frames the essay
- [Daniel Scheufler](/entities/daniel-scheufler.md) — author
- [Amazon](/entities/amazon.md) — cited for its "Team APIs" memo

## Concepts Covered

- [design patterns](/concepts/design-patterns.md) — reusable solutions and shared vocabulary
- [abstraction debt](/concepts/abstraction-debt.md) — hidden cost of leaky abstractions
- [systems thinking](/concepts/systems-thinking.md) — systems as interconnected wholes
- [technical debt](/concepts/technical-debt.md) — constraints architecture imposes over time
