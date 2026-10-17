---
title: "over-engineering"
type: "Concept"
description: "Adding unnecessary abstraction and complexity that raises cost and cognitive load without delivering user value."
created: '2026-10-17'
updated: '2026-10-17'
tags: [engineering, ux, architecture]
sources:
  - "/sources/hidden-cost-of-over-engineering-enterprise-applications.md"
  - "/sources/reinventing-the-wheel.md"
  - "/sources/internal-developer-portal-what-reduces-cognitive-load.md"
---

# over-engineering

Over-engineering is the habit of adding abstraction, layers, and cleverness that raise cost and complexity without delivering value to the user. Improving writers describe it as revving a bike engine in the driveway — noise and RPMs without movement — where technical output is mistaken for progress. Its root cause is a reversed sequence: teams start with the tool instead of the problem, and its clearest symptom is language and interfaces built for the builder rather than the person using them.

## Key Claims

- The tell is machine-facing language that imposes a "linguistic tax": users almost never want to "Delete" an order but to cancel, archive, or reverse, yet the button and the soft-delete misdescribe both intent and behavior.
- "Load more items" describes what the database is doing; "Show more" captures what the user wants — abstract product names like Azure and GraphQL signal the same builder-first mindset.
- The right order is need, then problem, then solution, with tools last; elaborate architecture for simple problems grows because building something impressive is easier to justify than admitting a simple solution would work.
- Reinventing the wheel: teams "spend a year reproducing baseline capabilities of a foundation model or a SaaS API that could be delivered today," driven by innovation bias, not-invented-here, poor time-to-value awareness, and no buy-build-blend framework.
- Start near the shelf — cloud services, foundation models, vector databases, orchestration frameworks — and earn the right to customize only where defensibility, domain grounding, or unique data requires it.
- Abstraction debt is the platform-scale version: layers that hide context instead of complexity create confident deployments and helpless incident responses when something breaks.
- Speed gets measured, direction does not: lines of code per hour and story points never tell you whether you are building the right thing.

## Related

- [abstraction debt](/concepts/abstraction-debt.md) — the accumulated cost of context-hiding layers
- [buy, build, or partner](/concepts/buy-build-partner.md) — the decision framework that counters reinvention
- [reducing cognitive load](/concepts/cognitive-load-design.md) — the user-facing cost of needless complexity
- [outcomes over outputs](/concepts/outcomes-over-outputs.md) — measuring direction, not just speed
- [user experience](/concepts/user-experience.md) — building for the person, not the developer
