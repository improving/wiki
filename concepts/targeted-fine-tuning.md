---
title: "Targeted Fine-Tuning"
type: "Concept"
description: "Fine-tuning a narrow, identified part of a model or a small model for one task, rather than broad retraining."
created: '2026-10-17'
updated: '2026-10-17'
tags: [fine-tuning, architecture, tool-calling]
sources:
  - "/sources/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md"
  - "/sources/the-open-weight-cost-curve-is-an-architecture-story.md"
---

# Targeted Fine-Tuning

Targeted fine-tuning means changing a narrow, identified part of a model — or training a smaller model for one specific task — instead of retraining broadly. This corpus presents it as the real lever behind both reliable tool calling and the open-weight cost curve: when a capability lives in a small, locatable circuit, adjusting that circuit beats prompting around it.

## Key Claims

- A narrow, locatable set of neurons carries the tool-selection decision.
- Evals diagnose tool-call errors after the fact, and prompts only bias probabilities; if the tool-selection circuit is thin, no phrasing reaches it.
- The real levers are targeted fine-tuning, activation steering, or base-model choice.
- Targeted training scaled a 32B open model to 36.6% on SWE-bench Verified.
- Architecture, not leaderboard position, drives open-weight cost: GLM-5 activates only 8 of 256 experts per token (about 5.9%), and MiniMax M2.5's linear attention decouples cost from context length.
- Local intelligence-per-watt improved 5.3x over two years.

## Related

- [fine-tuning](/concepts/fine-tuning.md) — the broader practice targeted fine-tuning narrows
- [Tool Calling](/concepts/tool-calling.md) — the capability this technique is used to repair
- [Interpretability](/concepts/interpretability.md) — locates the circuit that targeted work acts on
- [Open-Weight Models](/concepts/open-weight-models.md) — the models whose cost curve targeted training shapes
- [Speculative Decoding](/concepts/speculative-decoding.md) — a complementary architecture-level efficiency bet
- [SWE-bench](/entities/swe-bench.md) — the benchmark cited for targeted-training gains
- [A Few Neurons Decide Whether Your Agent Calls the Right Tool](/sources/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md) — primary source
- [The Open-Weight Cost Curve Is an Architecture Story](/sources/the-open-weight-cost-curve-is-an-architecture-story.md) — primary source
