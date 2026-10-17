---
title: "domain-driven design"
type: "Concept"
description: "Modeling software around the business domain and bounded contexts, the method behind service decomposition."
created: '2026-10-17'
updated: '2026-10-17'
tags: [architecture, engineering, delivery]
sources:
  - "/sources/microservices-architecture.md"
  - "/sources/how-to-modernize-your-application-a-catalyst-for-business.md"
  - "/sources/everything-you-need-to-know-about-reactive-systems.md"
  - "/sources/developer-of-the-future.md"
  - "/sources/legacy-modernization-cloud-replatforming-companies.md"
---

# domain-driven design

Domain-driven design (DDD) is the practice of modeling software around the business domain — its entities, language, and bounded contexts — so the architecture reflects how the business actually works rather than how the code happens to be structured. In this corpus it is the load-bearing method behind [microservices](/concepts/microservices.md): shifting to a service architecture without changing the design process just recreates the same problems in more places, so boundaries must be found in the domain first.

## Key Claims

- Decomposition follows DDD bounded contexts, so each microservice corresponds to a coherent part of the business rather than an arbitrary technical slice.
- Each bounded context should own its own database, split from the monolith along service boundaries, with event-driven communication between contexts.
- Shifting architecture without changing the design process recreates worse problems, which is why the corpus recommends DDD to decompose complexity into business domains.
- DDD is paired with delivery discipline — Scrum, Extreme Programming, CI/CD, and DevOps — and is applied to real modernizations, including NCLH's reservation-platform rebuild using DDD and reactive architecture with 40+ engineers on a multi-year engagement.
- The domain comes before the code: the developer-of-the-future argument is to model the domain first, then build message-driven services that keep domain consistency with real-time state.

## Related

- [microservices](/concepts/microservices.md) — the architecture DDD boundaries define
- [reactive systems](/concepts/reactive-systems.md) — message-driven services over the modeled domain
- [application modernization](/concepts/application-modernization.md) — where DDD guides decomposition
- [event-driven architecture](/concepts/event-driven-architecture.md) — decoupling bounded contexts
- [Eric Evans](/entities/eric-evans.md) — author of Domain-Driven Design
