---
title: "From \"Ship a Feature Faster\" to Building a Developer Platform for AI Agents"
type: "Source Summary"
description: "Agent code passed every quality gate yet drifted from architecture and intent, pushing Project X to a governed human-on-the-loop platform."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, platform, improving.com]
sources:
  - "references/improving.com/from-ship-a-feature-faster-to-building-a-developer-platform-for-ai-agents/from-ship-a-feature-faster-to-building-a-developer-platform-for-ai-agents.md"
---

# From "Ship a Feature Faster" to Building a Developer Platform for AI Agents — Summary

**Original source**: `references/improving.com/from-ship-a-feature-faster-to-building-a-developer-platform-for-ai-agents/from-ship-a-feature-faster-to-building-a-developer-platform-for-ai-agents.md`

## Summary

On Project X, agent-generated implementations passed every traditional quality gate — style, linting, type checking, automated tests — while still diverging from the architecture, the story's intent, or the business requirement. Closing that alignment gap pulled the team into a larger platform question: existing developer platforms and delivery practices were not designed to govern autonomous actors, so the operating model moved from human-in-the-loop toward human-on-the-loop.

## Key Claims

- The October webinar "Ship a Feature Faster" (with David O'Hara) built a real feature on Improving's Engage platform live across four weeks of UX, code/testing, platform/CI-CD, and data/analytics.
- Agent-generated code was well formed but not always the right code; the problem was alignment, not code quality.
- One case: an agent created frontend tests by mocking an entire shared data module instead of the project's request-mocking infrastructure; tests passed and the linter stayed silent, but the suite was brittle and could reach real APIs.
- The gap exposed a new platform responsibility: gates that evaluate a pull request against the linked issue, acceptance criteria, requirements, and architecture — testing whether the agent built the right thing, not just the thing correctly.
- Tooling progression on Project X: April shared context, May specification quality, June standardized skills and AI quality gates in CI, July project-state synchronization.
- Human-on-the-loop keeps human accountability: people define objectives, priorities, architectural and security boundaries, and decision rights; the agent operates within them and escalates exceptions and tradeoffs.
- Enterprise platforms weren't designed for autonomous actors; secrets management, branch protections, agent authentication, auditability, and secret scanning need explicit controls (GitHub Apps, fine-grained PATs, GitHub Actions environments, Azure Key Vault, HashiCorp Vault).
- Project X began around Stage 3 and moved toward Stages 5 and 6 of Improving's eight-stage AI Maturity Model; every increase in autonomy requires matching platform maturity and oversight.
- The next frontier is bounded planning loops: agents participate earlier in the lifecycle while remaining inside human-defined objectives and decision rights.

## Relevance

Informs [AI governance](/concepts/ai-governance.md), [human-in-the-loop](/concepts/human-in-the-loop.md), [platform engineering](/concepts/platform-engineering.md), and the [AI maturity model](/concepts/ai-maturity-model.md).

## Quality

Practitioner field report by Bill Curry; concrete case detail and honest about open questions, though vendor-adjacent (Improving services, Devin, GitHub Copilot).

## Entities Mentioned

- [Bill Curry](/entities/bill-curry.md) — author
- [Improving](/entities/improving.md) — ran Project X and the AI Maturity Model
- [David O'Hara](/entities/david-o-hara.md) — co-host of the original webinar
- [Devin](/entities/devin.md) — an execution agent used on Project X
- [GitHub Copilot](/entities/github-copilot.md) — another execution agent used on Project X

## Concepts Covered

- [AI governance](/concepts/ai-governance.md) — controls for autonomous actors
- [human-in-the-loop](/concepts/human-in-the-loop.md) — reframed as human-on-the-loop
- [platform engineering](/concepts/platform-engineering.md) — the platform must govern agents, not just help humans
- [AI maturity model](/concepts/ai-maturity-model.md) — the Stage 3 to 5/6 progression
- [quality gates](/concepts/quality-gates.md) — the traditional gates that missed alignment drift
