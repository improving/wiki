---
title: "Hidden Cost of Over-Engineering Enterprise Applications"
type: "Source Summary"
description: "Over-engineering is revving the engine in the driveway; its tell is machine-facing language, and its fix starts from user intent."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ux, engineering, improving.com]
sources:
  - "references/improving.com/hidden-cost-of-over-engineering-enterprise-applications/hidden-cost-of-over-engineering-enterprise-applications.md"
---

# Hidden Cost of Over-Engineering Enterprise Applications — Summary

**Original source**: `references/improving.com/hidden-cost-of-over-engineering-enterprise-applications/hidden-cost-of-over-engineering-enterprise-applications.md`

## Summary

Over-engineering feels productive — elaborate architecture, layers of abstraction, patterns on top of patterns — but it is like revving a bike engine in the driveway: noise and RPMs without movement. The clearest tell is machine-facing language that imposes a "linguistic tax" on users, and the root cause is a reversed sequence where teams start with the tool instead of the problem.

## Key Claims

- The bike metaphor: you can sit in the driveway, twist the throttle, and feel power through your whole body, but the bike does not move — technical output mistaken for progress.
- Linguistic tax: labels, buttons, and error messages reveal whether the system was built for the developer or the user.
- The "Delete" lie: users almost never want to delete an order — they want to cancel, archive, or reverse — and the system only soft-deletes, so the label misdescribes both intent and behavior.
- "Load more items" describes what the database is doing; "Show more" captures what the user wants.
- Abstract product names such as Azure (a sky color) and GraphQL signal the product was named by its builders, creating an entry barrier.
- Over-engineering starts when the sequence is reversed: teams start with the tool instead of the problem. The right order is need, then problem, then solution, with tools last.
- Elaborate architecture for simple problems grows because building something impressive is easier to justify than admitting a simple solution would work.
- Speed gets measured, direction does not: lines of code per hour and story points never tell you whether you are building the right thing.
- Kathy Sierra's principle — make the user feel like a "badass" — is flipped by over-engineering, which makes the developer the hero and leaves the user with a button that says "Delete" when they mean "Cancel."

## Relevance

Informs [over-engineering](/concepts/over-engineering.md), [user experience](/concepts/user-experience.md), and [outcomes over outputs](/concepts/outcomes-over-outputs.md).

## Quality

Opinion essay by Claudio Lassala; vivid, memorable examples, but lightly evidenced and ends with a service pointer.

## Entities Mentioned

- [Claudio Lassala](/entities/claudio-lassala.md) — author
- [Kathy Sierra](/entities/kathy-sierra.md) — cited on making the user feel like a "badass"
- [Improving](/entities/improving.md) — the product delivery and UX team behind the closing pitch

## Concepts Covered

- [over-engineering](/concepts/over-engineering.md) — the main topic
- [user experience](/concepts/user-experience.md) — building for the person, not the developer
- [outcomes over outputs](/concepts/outcomes-over-outputs.md) — measuring direction, not just speed
- [reducing cognitive load](/concepts/cognitive-load-design.md) — the linguistic tax as avoidable friction
