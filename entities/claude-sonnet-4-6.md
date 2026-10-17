---
title: "Claude Sonnet 4.6"
type: "Entity"
description: "Anthropic mid-tier model cited for cost-efficient routing and for the gap between diagram recognition and relational reasoning."
created: '2026-10-17'
updated: '2026-10-17'
tags: [model, routing, vision]
sources:
  - "/sources/it-can-read-the-diagram-it-cant-reason-about-it.md"
  - "/sources/not-every-ticket-needs-the-250000-engineer.md"
---

# Claude Sonnet 4.6

Claude Sonnet 4.6 is an Anthropic mid-tier model that this corpus uses to argue for routing work by task seniority and to illustrate the distance between recognizing visual elements and reasoning about them.

## Overview

On cost, the model represents the tier that handles the bulk of issue resolution for little marginal spend, leaving premium tiers to buy the last 15 points. Cost per solved task — not token price — is the measure that prices retries and the full agent harness.

On capability, vision-language evaluation via FeynmanBench exposes a "CP3 cliff": models identify diagram elements but cannot reconstruct the underlying graphs. GPT-5.5 scored 84 percent at identification yet only 16 percent at deriving physics, suggesting pattern-matching of textbook-common topologies rather than genuine reasoning. Single-pass image encoding loses spatial relations; mid-reasoning re-inspection helps.

## Key Claims

- Mid-tier models cover most resolution work at low marginal cost
- Premium tiers buy the last 15 points; cost per solved task is the true metric
- FeynmanBench reveals a CP3 cliff between element identification and graph reconstruction
- GPT-5.5 scored 84% at identification but only 16% at deriving physics
- Mid-reasoning re-inspection recovers some lost spatial relations

## Related

- [model routing](/concepts/model-routing.md) — sending work to the right tier
- [Model selection](/concepts/model-selection.md) — deliberate tier choice
- [Benchmark Validity](/concepts/benchmark-validity.md) — scores overstating diagram-analysis ability
- [Claude Opus 4.8](/entities/claude-opus-4-8.md) — the flagship tier above it
- [GPT-5.5](/entities/gpt-5-5.md) — model measured on FeynmanBench
- [It Can Read the Diagram. It Can't Reason About It.](/sources/it-can-read-the-diagram-it-cant-reason-about-it.md) — primary source
