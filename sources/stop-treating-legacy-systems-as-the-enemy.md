---
title: "Stop Treating Legacy Systems as the Enemy"
type: "Source Summary"
description: "Legacy systems are accumulated answers to real problems; modernize them as archaeology with automated tests, not as a total rewrite."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, engineering, modernization, improving.com]
sources:
  - "references/improving.com/stop-treating-legacy-systems-as-the-enemy/stop-treating-legacy-systems-as-the-enemy.md"
---

# Stop Treating Legacy Systems as the Enemy — Summary

**Original source**: `references/improving.com/stop-treating-legacy-systems-as-the-enemy/stop-treating-legacy-systems-as-the-enemy.md`

## Summary

Calling a system "legacy" and meaning it as an insult is a mistake: a system that ran for fifteen years survived because it solved a real problem through market and technology shifts. The post argues for evolutionary maintenance — systematic, incremental, and protected by automated tests — treating the codebase as archaeology rather than demolition, because buried in it are undocumented business logic and edge cases worth carrying forward.

## Key Claims

- FoxPro and Microsoft Access applications built with "rapid application development" were dismissed as cheating by mainframe-era engineers, yet some ran businesses for decades.
- The pattern repeats each generation: Visual Basic was too simple for C++ developers, .NET was too abstracted for VB developers, and now AI-assisted development gets the same skepticism.
- A system that survived fifteen years is evidence of success, not failure; the problem is approaching it with contempt instead of curiosity.
- Total rewrites are dangerous; the author compares modernization to refueling a plane in mid-flight, where the business cannot stop generating revenue.
- Example: migrating from Fluent Assertions to Shouldly across a .NET codebase with over 3,000 tests; Context7 fed the AI current library documentation so it reasoned about real API changes instead of stale training knowledge.
- The AI's dependency scan surfaced that Lamar and Marten shared a dependency, so updating one without the other would have broken the build in ways that wouldn't show up immediately.
- Rather than rewriting test code, the AI generated custom extension methods to preserve the developer experience, compressing a multi-week manual effort into two days.
- The safety net is non-negotiable: without automated tests, evolutionary maintenance is "changing things and hoping nothing breaks."
- Legacy code holds "little gems" — edge case handlers, encoded regulatory validations, exception-routing workflows — that contempt-driven rewrites demolish and teams then rediscover through a production incident six months after launch.
- The right starting question is not "how do we get rid of this old system?" but "what has this system been holding together, and how do we keep that intact?"

## Relevance

Informs [legacy modernization](/concepts/legacy-modernization.md), [application modernization](/concepts/application-modernization.md), [test automation](/concepts/test-automation.md), and [incremental delivery](/concepts/incremental-delivery.md).

## Quality

Practitioner essay by Claudio Lassala; concrete migration example with real tools, opinionated but well-grounded.

## Entities Mentioned

- [Claudio Lassala](/entities/claudio-lassala.md) — author
- [Improving](/entities/improving.md) — the legacy modernization practice behind the post
- [FoxPro](/entities/foxpro.md) — the RAD tool dismissed in the opening example
- [Microsoft Access](/entities/microsoft-access.md) — the other RAD tool cited

## Concepts Covered

- [legacy modernization](/concepts/legacy-modernization.md) — the main topic
- [application modernization](/concepts/application-modernization.md) — evolving rather than rewriting
- [test automation](/concepts/test-automation.md) — the non-negotiable safety net
- [incremental delivery](/concepts/incremental-delivery.md) — systematic, incremental evolution
- [application modernization strategy](/concepts/application-modernization-strategy.md) — choosing rehost-to-retire options
