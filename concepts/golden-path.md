---
title: "golden path"
type: "Concept"
description: "A supported, opinionated route for common tasks that makes the right way the easy way."
created: '2026-10-17'
updated: '2026-10-17'
tags: [platform, developer-experience, standards]
sources:
  - "/sources/building-golden-paths.md"
  - "/sources/platform-engineering-maturity-model.md"
  - "/sources/know-your-developer.md"
  - "/sources/what-nobody-tells-you-about-golden-paths-at-scale.md"
  - "/sources/gpu-platform-engineering-golden-path.md"
  - "/sources/platform-engineering-companies.md"
---

# golden path

A golden path is an opinionated, self-service, safe-by-default route through a common task — deploying a service, provisioning an environment — that makes the secure and compliant way the fastest one. The corpus is emphatic that a golden path is only "done" when it is opinionated, self-service, safe by default, and progressive, and that it must be treated as a product rather than a mandate.

## Key Claims

- A golden path earns adoption because it saves time, not because it is mandated; the secure, compliant route should be the fastest one ([platform engineering companies](/sources/platform-engineering-companies.md)).
- Building one does not require a full IDP: the four-phase sequence is standardize (one template enforcing resource limits, health checks, labels, namespaces), validate (declarative config rejected early with clear errors), GitOps (a git push watched by a CD tool like Argo CD), then self-service ([building golden paths](/sources/building-golden-paths.md)).
- Most teams start in Phase 0 chaos — ten scripts with ten different outcomes, images pinned to latest, missing resource limits and health checks ([building golden paths](/sources/building-golden-paths.md)).
- At scale golden paths fail by Day 50: creating projects is only ~1% of an application's lifetime, and a 6-person platform team cannot serve 200 engineers across 20 teams; four failure modes appear — the queue problem, the expertise problem, the maintenance trap, and rigidity/abstraction debt ([golden paths at scale](/sources/what-nobody-tells-you-about-golden-paths-at-scale.md)).
- The evolution is a marketplace where domain teams contribute capabilities under clear interfaces and automated validation; mature adopters see 3–4× faster capability development, with golden capabilities retained for 70–80% of teams ([golden paths at scale](/sources/what-nobody-tells-you-about-golden-paths-at-scale.md)).
- A durable golden path abstracts what is solved (container packaging, CI, observability, access controls) and keeps visible what is still a live decision (workload class, GPU sharing strategy, driver/firmware lifecycle) — otherwise it hides decisions teams never consciously made ([GPU golden path](/sources/gpu-platform-engineering-golden-path.md)).
- Portals are Level 3 infrastructure; teams should name what already exists and build one genuinely better golden path before building a portal ([maturity model](/sources/platform-engineering-maturity-model.md)).

## Related

- [platform engineering](/concepts/platform-engineering.md) and [internal developer platform](/concepts/internal-developer-platform.md)
- [internal developer portal](/concepts/internal-developer-portal.md) — the self-service interface over golden paths
- [cognitive load](/concepts/cognitive-load.md) and [abstraction debt](/concepts/abstraction-debt.md) — what good and bad paths do
- [developer experience](/concepts/developer-experience.md), [platform as a product](/concepts/platform-as-a-product.md)
