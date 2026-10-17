---
title: "cognitive load"
type: "Concept"
description: "The mental effort a tool or process imposes on developers, which platforms exist to reduce."
created: '2026-10-17'
updated: '2026-10-17'
tags: [platform, developer-experience, psychology]
sources:
  - "/sources/internal-developer-portal-what-reduces-cognitive-load.md"
  - "/sources/building-golden-paths.md"
  - "/sources/elevating-developer-experience-maersks-path-to-a-more-user-centric.md"
  - "/sources/how-to-fail-at-platform-engineering.md"
  - "/sources/what-nobody-tells-you-about-golden-paths-at-scale.md"
  - "/sources/gpu-platform-engineering-golden-path.md"
  - "/sources/platform-engineering-maturity-model.md"
---

# cognitive load

Cognitive load is the mental effort a tool or process imposes on the people using it — infrastructure complexity, undocumented steps, unclear rules — and it is the burden platforms exist to reduce. The corpus's sharpest point is that reducing cognitive load is the outcome platforms should be measured on, not adoption percentages.

## Key Claims

- Golden paths reduce cognitive load and speed onboarding, but they cover only the first ~1% of an application's lifetime ([golden paths at scale](/sources/what-nobody-tells-you-about-golden-paths-at-scale.md)).
- Activity metrics such as 90% golden path adoption say nothing about whether cognitive load went down, incidents fell, or lead times improved ([IDP cognitive load](/sources/internal-developer-portal-what-reduces-cognitive-load.md)).
- Insufficient or outdated documentation causes cognitive load and a flood of support tickets; docs should stay current, ideally with a dedicated team and search ([how to fail](/sources/how-to-fail-at-platform-engineering.md)).
- Maersk's IDP standardized security practices and commit formatting, reducing cognitive load so developers could focus on product work ([Maersk IDP](/sources/elevating-developer-experience-maersks-path-to-a-more-user-centric.md)).
- "Swiss knife" bloat — trying to solve every problem at once — and excessive customization options both raise cognitive load and the learning curve ([how to fail](/sources/how-to-fail-at-platform-engineering.md)).
- Prompt fatigue is a new class of cognitive load that arrives "wearing a productivity hat" when a platform has no opinionated AI integration layer ([IDP cognitive load](/sources/internal-developer-portal-what-reduces-cognitive-load.md)).
- The GPU case shows the platform absorbing scheduling and driver complexity so teams do not have to carry it in "tribal knowledge disguised as YAML" ([GPU golden path](/sources/gpu-platform-engineering-golden-path.md)).

## Related

- [developer experience](/concepts/developer-experience.md) — the friction this load produces
- [golden path](/concepts/golden-path.md) and [internal developer portal](/concepts/internal-developer-portal.md) — mechanisms that lower it
- [platform engineering](/concepts/platform-engineering.md) and [abstraction debt](/concepts/abstraction-debt.md)
- [platform as a product](/concepts/platform-as-a-product.md)
