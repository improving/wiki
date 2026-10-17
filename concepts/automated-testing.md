---
title: "automated testing"
type: "Concept"
description: "Encoding expected behavior as repeatable, fast checks that validate requirements and serve as scaffolding for reliable delivery."
created: '2026-10-17'
updated: '2026-10-17'
tags: [testing, quality, delivery]
sources:
  - "/sources/debugging-mark-of-failure-or-mark-of-caution.md"
  - "/sources/your-ci-cd-pipeline-is-already-cognitive-scaffolding.md"
---

# automated testing

Automated testing is the practice of expressing expected behavior as code that runs quickly and repeatably, rather than relying on manual inspection or interactive debugging. Across this corpus it is treated as both a quality mechanism and a form of preserved organizational knowledge.

## Key Claims

- Properly written automated tests validate all known requirements quickly and repeatably, where debugging is repetitive, human-error prone, uncodified, and time-consuming.
- The counter-position, attributed to David Corbin, is that debugging finds what tests never covered — so the two are complements, not substitutes.
- One author challenges readers to break a tested system without modifying its tests, framing tests as the codification of intent.
- Delivery tooling such as version control, tests, and CI/CD externalizes and preserves team knowledge beyond any individual.
- Good scaffolding produces compounding organizational capability, not just efficiency.
- Deploying agents without governance scaffolding repeats the CI-without-quality-gates mistake, tying testing discipline to AI governance.

## Related

- [cognitive scaffolding](/concepts/cognitive-scaffolding.md) — the framing that links tests to preserved knowledge
- [test-driven development](/concepts/test-driven-development.md) — the discipline of writing tests first
- [Quality Gates](/concepts/quality-gates.md) — the enforcement point tests feed into
- [Bolt-on Governance](/concepts/bolt-on-governance.md) — embedding controls in the pipeline rather than beside it
- [Debugging: Mark of Failure or Mark of Caution?](/sources/debugging-mark-of-failure-or-mark-of-caution.md) — primary source
- [Your CI/CD Pipeline Is Already Cognitive Scaffolding](/sources/your-ci-cd-pipeline-is-already-cognitive-scaffolding.md) — primary source
