---
title: "Claude Opus 4.8"
type: "Entity"
description: "Anthropic frontier model used here to show tiered routing economics and the gap between coding benchmarks and merge-ready work."
created: '2026-10-17'
updated: '2026-10-17'
tags: [model, coding-agents, benchmarks]
sources:
  - "/sources/not-every-ticket-needs-the-250000-engineer.md"
  - "/sources/the-gap-between-coding-benchmarks-and-client-ready-software.md"
---

# Claude Opus 4.8

Claude Opus 4.8 is an Anthropic frontier model that this corpus uses to illustrate two related arguments: that flagship defaults waste money, and that coding benchmarks overstate production readiness.

## Overview

On cost, roughly 80 percent of issue resolution is nearly free and premium tiers buy the last 15 points, so teams that default to a flagship can spend nearly double their loaded engineer. Cost per solved task is the metric that prices retries and the whole agent harness, not the headline token rate.

On capability, FrontierCode graded merge-readiness with maintainers and Claude Opus 4.8 scored 13.4 percent on the hardest tasks. RoadmapBench tasks touch a median of 3,700 lines across 51 files, and SaaSBench found over 95 percent of agent failures happen before the agent reaches business logic.

## Key Claims

- Premium tiers buy the last 15 points; most resolution is nearly free
- Flagship-default teams can spend nearly double their loaded engineer
- Claude Opus 4.8 scored 13.4% on the hardest FrontlineCode tasks
- METR time horizon doubles about every 4.3 months
- Coding demos measure a different job than production modernization work

## Related

- [model routing](/concepts/model-routing.md) — routing work by task seniority
- [Model selection](/concepts/model-selection.md) — choosing tiers deliberately
- [Benchmark Validity](/concepts/benchmark-validity.md) — why benchmark scores overstate readiness
- [time horizon](/concepts/time-horizon.md) — METR's doubling measure
- [METR](/entities/metr.md) — source of the doubling estimate
- [The Gap Between Coding Benchmarks and Client-Ready Software](/sources/the-gap-between-coding-benchmarks-and-client-ready-software.md) — primary source
