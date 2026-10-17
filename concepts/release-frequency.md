---
title: "release frequency"
type: "Concept"
description: "How often a team ships, constrained by automation and definition of done."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agile, delivery, devops]
sources:
  - "/sources/when-should-we-release-in-scrum.md"
  - "/sources/drop-everything-and-review.md"
---

# release frequency

Release frequency is how often a team puts working software in front of users, and in this corpus the default answer is "as often as possible." Because a product backlog is a set of hypotheses, every delay postpones both learning and value — but frequency is bounded in practice by deployment automation, the definition of done, and the transaction cost of shipping.

## Key Claims

- Release as often as possible to shorten the feedback loop on backlog hypotheses and stop investing in unvalidated ideas.
- Common reasons to delay: product complexity, dependencies with other groups, large ideas, and expensive transaction costs.
- One client moved from annual to quarterly releases, showing progress toward continuous delivery without achieving it fully.
- The "it depends" factors are how automated deployment, validation, and rollback are; whether policies and processes are conducive to change; and how fast customers adopt changes.
- If adoption lags capability, the work shifts to making the change easy and intuitive for customers.
- Three recurring questions frame the trade-off: how long do you want to delay learning, delay value, and invest in unvalidated ideas?
- Code review is a "middle loop" that inflates lead time when done asynchronously; the DEAR norm (drop everything and review) and synchronous or pair/mob review shrink it.

## Related

- [incremental delivery](/concepts/incremental-delivery.md) — shipping in small, complete slices
- [Definition of Done](/concepts/definition-of-done.md) — the bar for releasable work
- [CI/CD](/concepts/ci-cd.md) — automation of deploy, validate, and back out
- [code review](/concepts/code-review.md) — the middle loop that gates releases
- [product backlog](/concepts/product-backlog.md) — ideas and hypotheses of value
