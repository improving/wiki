---
title: "test-driven development"
type: "Concept"
description: "Writing tests that codify intent before or alongside code, extended in this corpus to evals for AI agents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [testing, engineering-practice, ai]
sources:
  - "/sources/debugging-mark-of-failure-or-mark-of-caution.md"
  - "/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md"
  - "/sources/productivity-tips-write-it-once.md"
  - "/sources/the-scaffolding-is-the-product-why-ai-in-software-development-is-a-systems.md"
---

# test-driven development

Test-driven development (TDD) writes tests that codify intent before or alongside the code. Across this corpus the discipline generalizes beyond hand-written code: automated tests validate known requirements quickly and repeatably, and the same logic extends to evals that specify AI agent behavior.

## Key Claims

- Properly written [automated tests](/concepts/automated-testing.md) validate all known requirements quickly and repeatably; debugging is repetitive, human-error prone, uncodified, and time-consuming.
- David Corbin's counterargument is that debugging finds what tests never covered — the author's challenge is to break a tested system without modifying its tests.
- [Eval-driven development](/concepts/evals-as-code.md) applies the pattern to agents: an eval is an automated test suite that serves as the specification for AI behavior, run in three tiers — [deterministic validation](/concepts/deterministic-validation.md), model-graded, then human review.
- 57% of organizations run agents in production and quality is the top barrier; eval-first development lets teams swap models in days with automated proof of safety.
- Templates can scaffold TDD tests with assertions pre-filled; a Person class was generated in 19 seconds, reducing the friction between intent and implementation.
- TDD is part of the scaffolding around a commodity model: the model alone yields 70% solutions, while context, testing, review, and CI/CD convert that to 95%.

## Related

- [automated testing](/concepts/automated-testing.md) — the mechanism TDD relies on
- [evals-as-code](/concepts/evals-as-code.md) — TDD's AI-era extension
- [deterministic validation](/concepts/deterministic-validation.md) — the first eval tier
- [Eval-Driven Development](/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md) — primary source
