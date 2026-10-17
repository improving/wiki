---
title: "Tool Calling"
type: "Concept"
description: "A model's ability to select and invoke the right tool; bounded by a thin neural circuit and fragile under compression."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, reliability, interpretability]
sources:
  - "/sources/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md"
  - "/sources/the-compression-cliff-nobody-budgeted-for.md"
---

# Tool Calling

Tool calling is the step where an agent selects and invokes an external function or tool. It is the point where a model stops describing an action and performs one, so failures here break the whole [orchestration layer](/concepts/orchestration-layer.md). This corpus argues tool-calling reliability is a representational property of the model, not a prompt-writing problem.

## Key Claims

- A narrow, locatable set of neurons carries the tool-selection decision.
- Evals diagnose tool-call errors after the fact; prompts only bias probabilities.
- If the tool-selection circuit is thin, no amount of rephrasing reaches it.
- Under [prompt compression](/concepts/context-management.md), tool-calling reliability stays flat until a sharp threshold, then falls off a cliff.
- Redundant restated schemas look safest to cut but are the most load-bearing.
- End-to-end task completion and readability benchmarks mask malformed tool calls.

## Related

- [Targeted Fine-Tuning](/concepts/targeted-fine-tuning.md) — a real lever on the selection circuit
- [Interpretability](/concepts/interpretability.md) — locating the neurons that decide tool choice
- [evaluation harness](/concepts/evaluation-harness.md) — catches malformed calls that benchmarks hide
- [A Few Neurons Decide Whether Your Agent Calls the Right Tool](/sources/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md) — primary source
