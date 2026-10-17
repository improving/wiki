---
title: "microservices"
type: "Concept"
description: "Decomposing systems into independently deployable services with clear domain boundaries."
created: '2026-10-17'
updated: '2026-10-17'
tags: [architecture, platform, delivery]
sources:
  - "/sources/microservices-architecture.md"
  - "/sources/everything-you-need-to-know-about-reactive-systems.md"
  - "/sources/how-to-modernize-your-application-a-catalyst-for-business.md"
  - "/sources/best-current-practices-part-i.md"
  - "/sources/modern-software-solutions.md"
  - "/sources/developer-of-the-future.md"
---

# microservices

Microservices decompose a system into independently deployable services organized around business domains, so each can be scaled, deployed, and evolved on its own. The corpus is deliberately balanced about them: clients ask for microservices as the known path to scalability, but the disadvantages — structural complexity, data sharing across services, and spread-out cross-cutting concerns — are often intentional consequences of the choice, and a half-hearted migration can leave a "microservice-monolith" with the worst of both.

## Key Claims

- Advantages are structural separation of concerns, targeted scaling, and dispersing complexity across many teams; disadvantages are fast-growing structural complexity, integration patterns and duplicate storage to share data, and logging and security spread across services.
- Success depends less on the architecture than on discipline: Domain-Driven Design to find boundaries, plus automation, DevOps, disciplined development, extensive testing, and clear messaging/integration patterns.
- Decomposition follows bounded contexts, each service owns its database split along service boundaries, and event-driven communication reduces direct dependencies between services.
- Best practices are context-dependent, not universal: microservices assume reuse, maintenance capacity, and a mature ops organization, so they should be adopted as a trade-off rather than a dictate.
- Microservices dissolved the binary buy-versus-build decision, letting teams integrate cloud capabilities and focus custom code on true differentiators while buying commodity capability.
- Message-driven design via the Actor model avoids retrieving from a database on every call, giving domain consistency, elasticity, resilience, and real-time retrieval.

## Related

- [domain-driven design](/concepts/domain-driven-design.md) — the method for finding service boundaries
- [reactive systems](/concepts/reactive-systems.md) — message-driven, elastic, resilient systems
- [event-driven architecture](/concepts/event-driven-architecture.md) — decoupling producers from consumers
- [application modernization](/concepts/application-modernization.md) — decomposing the monolith incrementally
- [DevOps](/concepts/devops.md) — the delivery culture microservices require
