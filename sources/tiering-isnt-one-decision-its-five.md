---
title: "Tiering Isn't One Decision, It's Five"
type: "Source Summary"
description: "Five 2026 results show cost savings come from tiering model choice across five layers of the stack, not one frontier pick."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/tiering-isnt-one-decision-its-five/tiering-isnt-one-decision-its-five.md"
---

# Tiering Isn't One Decision, It's Five — Summary

**Original source**: `references/devlinliles.com/tiering-isnt-one-decision-its-five/tiering-isnt-one-decision-its-five.md`

## Summary

Devlin Liles argues that reflexively running the frontier model for every task is an expensive habit, and that most agent failures diagnosed as capability gaps are really routing gaps. Citing five 2026 research results, he shows tiering applies at five distinct layers of the stack — team design, message pruning, plan-versus-execution, the function call itself, and LoRA routing inside one model. No shared technique ties them together; what they share is refusing to treat "which model" as one decision made once. He cautions the headline savings are benchmark-specific, not guaranteed.

## Key Claims

- Cognition's Devin Fusion runs a frontier planner alongside a cheap "sidekick"; on FrontierCode it cut cost 35% versus the frontier model alone at equivalent performance, reaching 41% with a newer sidekick, with 88% of merged PRs routed automatically.
- Fusion's key design is caching each model's context separately so delegation doesn't reset the meter and erase savings.
- HyFunc (KDD 2026) tiers within a single tool call: compress intent to a soft token, retrieve a few candidate functions, then let a prefix-tuned model emit the call — 0.828s latency, 80.1% accuracy on BFCL.
- SafeSieve (AAAI 2026) prunes multi-agent chatter, cutting token consumption 12.4%–27.8% while holding or improving accuracy by up to 2.22 points; cost-based clustering cut spend a further 13.3%.
- ReMix fixes LoRA routers that collapse onto one adapter, using a leave-one-out policy gradient so every adapter contributes.

## Relevance

Central to [model routing](/concepts/model-routing.md) and [model selection](/concepts/model-selection.md), and it touches [token cost](/concepts/token-cost.md) and [multi-agent coordination](/concepts/multi-agent-coordination.md).

## Quality

Practitioner blog post by Devlin Liles. Well-cited to named 2026 papers and benchmarks; the figures are vendor and benchmark results that he explicitly warns may not transfer.

## Entities Mentioned

- [Cognition](/entities/cognition.md) — builder of Devin Fusion, the dual-model harness

## Concepts Covered

- [model routing](/concepts/model-routing.md) — the core thesis across five layers
- [Model selection](/concepts/model-selection.md) — rejecting the default frontier choice
- [token cost](/concepts/token-cost.md) — the cost lever tiering targets
- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — message pruning and team-graph generation
- [fine-tuning](/concepts/fine-tuning.md) — LoRA adapter routing inside a single model
