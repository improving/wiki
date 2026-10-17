---
title: "Bill Curry"
type: "Entity"
description: "Improving writer on developer platforms and AI agents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [author, platform, ai, architecture]
sources:
  - "/sources/from-ship-a-feature-faster-to-building-a-developer-platform-for-ai-agents.md"
  - "/sources/modern-software-solutions.md"
  - "/sources/engineering-behind-the-color-software-for-a-global-paint-brand.md"
  - "/sources/ship-faster-with-ai-series.md"
---

# Bill Curry

An Improving technologist and writer on the shift from helping human developers to governing autonomous AI agents, and on the architecture decisions behind modern software. His Project X field report is one of the corpus's most concrete accounts of agent-driven delivery hitting its limits.

## Topics and Work

- Reports that on Project X, agent-generated code passed every traditional gate — style, linting, type checking, tests — yet still drifted from architecture and intent, exposing a need for gates that test whether the agent built the *right* thing.
- Describes moving from [human-in-the-loop](/concepts/human-in-the-loop.md) to human-on-the-loop, where people define objectives, boundaries, and decision rights and the agent escalates exceptions, tied to Improving's eight-stage [AI maturity model](/concepts/ai-maturity-model.md).
- Argues enterprise platforms were not designed for autonomous actors, so secrets management, branch protections, agent authentication, and auditability need explicit controls.
- Reframes the buy-versus-build debate as "buy and build": integrate third-party capabilities and reserve custom code for true differentiators.
- Documents a global paint brand's internal RAG assistant on Azure, where the real work was curating two decades of messy legacy content and sharpening vague sales questions before retrieval.

## Related

- [platform engineering](/concepts/platform-engineering.md) — the platform must govern agents, not just help humans
- [AI governance](/concepts/ai-governance.md) — controls for autonomous actors
- [quality gates](/concepts/quality-gates.md) — the traditional gates that missed alignment drift
- [buy, build, or partner](/concepts/buy-build-partner.md) — choosing among purchasing, building, and partnering
