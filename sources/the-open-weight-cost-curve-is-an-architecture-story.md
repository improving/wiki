---
title: "The Open-Weight Cost Curve Is an Architecture Story"
type: "Source Summary"
description: "Argues open-weight economics rest on four durable architecture techniques — intelligence per watt, sparsity, linear attention, targeted fine-tuning — not leaderboard standings."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/the-open-weight-cost-curve-is-an-architecture-story/the-open-weight-cost-curve-is-an-architecture-story.md"
---

# The Open-Weight Cost Curve Is an Architecture Story — Summary

**Original source**: `references/devlinliles.com/the-open-weight-cost-curve-is-an-architecture-story/the-open-weight-cost-curve-is-an-architecture-story.md`

## Summary

Devlin Liles argues that the churn of open-weight coding leaders — Kimi, GLM, DeepSeek trading the top spot — distracts from the efficiency research that actually determines self-hosting economics. He isolates four durable techniques that do not reset when the next model ships: intelligence per watt as a metric, sparse activation and attention, linear attention, and targeted fine-tuning at small scale. The number attached to each keeps moving; the technique is what a client is really buying.

## Key Claims

- A Stanford/Together AI paper proposes capability per watt (task accuracy divided by power); local models already handle 88.7% of single-turn chat and reasoning queries, and local intelligence-per-watt improved 5.3x over two years — roughly 3.2x from models and 1.7x from accelerators.
- GLM-5 is a mixture-of-experts model with ~745B total parameters but only 8 of 256 experts active per token (~5.9%), letting it process 200,000 tokens of context without full dense-attention compute.
- MiniMax M2.5's Lightning Attention puts it at roughly 80% on SWE-bench Verified — within a point of Claude Opus 4.6 — at about $0.30/$2.40 per million input/output tokens against Opus's list near $75 per million output tokens; the exact multiple (20x–60x) should be treated as directional.
- SWE-Dev took a 32B open model to 36.6% on SWE-bench Verified via targeted training and inference-time scaling rather than more pretraining, in range of GPT-4o.

## Relevance

Informs [Targeted Fine-Tuning](/concepts/targeted-fine-tuning.md), [Open-Weight Models](/concepts/open-weight-models.md), and [token cost](/concepts/token-cost.md) trade-offs in self-hosting decisions.

## Quality

Practitioner blog post by Devlin Liles. Well-sourced with named papers and figures; explicitly cautions that vendor multiples are directional until independently rerun.

## Entities Mentioned

- [SWE-bench](/entities/swe-bench.md) — benchmark behind the M2.5 and SWE-Dev figures
- [Together AI](/entities/together-ai.md) — co-author of the intelligence-per-watt paper

## Concepts Covered

- [Targeted Fine-Tuning](/concepts/targeted-fine-tuning.md) — small-model gains without matching parameter budgets
- [Open-Weight Models](/concepts/open-weight-models.md) — the self-hosting economics under discussion
- [token cost](/concepts/token-cost.md) — pricing gap between open and frontier APIs
