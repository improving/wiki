---
title: "Architecture Drift at AI Speed: When Your Agents Don't Respect Boundaries"
type: "Source Summary"
description: "Parallel AI coding agents erode architectural boundaries at machine speed; isolation plus automated boundary enforcement is the structural defense."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/architecture-drift-at-ai-speed-when-your-agents-dont-respect-boundaries/architecture-drift-at-ai-speed-when-your-agents-dont-respect-boundaries.md"
---

# Architecture Drift at AI Speed: When Your Agents Don't Respect Boundaries — Summary

**Original source**: `references/devlinliles.com/architecture-drift-at-ai-speed-when-your-agents-dont-respect-boundaries/architecture-drift-at-ai-speed-when-your-agents-dont-respect-boundaries.md`

## Summary

AI coding agents do not respect architectural boundaries unless forced to, and parallel agents drift from coherent architecture to entanglement faster than human teams have experienced. A single agent takes the shortest path to working code, crossing domain boundaries invisibly; multiplied across parallel features, each locally rational decision is globally destructive. The defense is structural: isolation (separate worktrees, scoped workspaces) plus automated boundary enforcement on every PR. Unchecked, drift compounds into a maintenance treadmill that costs 30–50% of delivery velocity by quarters two and three.

## Key Claims

- Parnas (1972) established information hiding as the decomposition criterion; Perry and Wolf (1992) named architectural drift and erosion; Lehman's laws predicted the dynamic.
- Parallel agents without isolation produce 10x merge conflicts and coordination overhead that erases the throughput gain.
- By quarter two of uncontrolled AI generation, delivery velocity drops 30–40%; by quarter three, it is down 50%.
- Isolation prevents mechanical conflicts; automated boundary enforcement prevents architectural decay.
- ArchUnit and dependency linters existed for years, but AI changes the arithmetic, making them load-bearing at machine violation rates.

## Relevance

Informs [boundary enforcement](/concepts/boundary-enforcement.md) and [technical debt](/concepts/technical-debt.md), with [state isolation](/concepts/state-isolation.md) enabling safe [multi-agent coordination](/concepts/multi-agent-coordination.md).

## Quality

Practitioner blog post by Devlin Liles. Grounded in named software-engineering literature and clear mechanisms; the velocity-loss percentages read as illustrative estimates rather than measured data.

## Entities Mentioned

- [David Parnas](/entities/david-parnas.md) — 1972 information-hiding paper cited as the origin of module boundaries

## Concepts Covered

- [Boundary enforcement](/concepts/boundary-enforcement.md) — automated structural validation on every PR
- [Technical Debt](/concepts/technical-debt.md) — the debt that accumulates at AI speed
- [state isolation](/concepts/state-isolation.md) — separate worktrees and scoped workspaces for parallel agents
- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — parallel execution and its coordination overhead
