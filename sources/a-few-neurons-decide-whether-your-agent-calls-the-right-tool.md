---
title: "A Few Neurons Decide Whether Your Agent Calls the Right Tool"
type: "Source Summary"
description: "Tool-selection failures may live in a narrow neural circuit that evals and prompt tweaks cannot reach, pointing to fine-tuning and steering."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/a-few-neurons-decide-whether-your-agent-calls-the-right-tool/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md"
---

# A Few Neurons Decide Whether Your Agent Calls the Right Tool — Summary

**Original source**: `references/devlinliles.com/a-few-neurons-decide-whether-your-agent-calls-the-right-tool/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md`

## Summary

Faced with an agent that calls the wrong tool or fills in arguments with something almost right, teams reach for more scaffolding: a bigger eval harness, more test cases, a reworded prompt. An interpretability paper traced the decision of whether to call a tool, and which one, to a narrow, locatable set of neurons carrying most of that decision. The post argues this locates a real share of [tool calling](/concepts/tool-calling.md) failure inside the model, where evals and prompts cannot reach, and reframes that failure as a representational limitation rather than a coverage problem.

## Key Claims

- An eval reports a wrong tool call after the fact; a prompt tries to bias the decision before it happens; neither touches the circuit actually making the call.
- Prompt tweaks plateau because if the tool-selection circuit is thin or miscalibrated for a pattern, no phrasing reaches it.
- The lever for a meaningful share of failure sits inside the model: [targeted fine-tuning](/concepts/targeted-fine-tuning.md) on the specific circuit, activation steering at inference time, or choosing a base model partly on this property.
- Most teams building on someone else's model cannot use those levers yet, because circuit-level fine-tuning and activation steering remain research-lab capabilities.
- Eval harnesses still earn their keep by catching failures a clearer prompt can fix and identifying the leftover pile.

## Relevance

Informs [tool-calling](/concepts/tool-calling.md) reliability and [interpretability](/concepts/interpretability.md), and connects to [targeted fine-tuning](/concepts/targeted-fine-tuning.md) as an alternative to prompt iteration.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a sharp conceptual distinction between outside-the-model and inside-the-model fixes. Caveats: rests on a single unnamed paper's benchmark and offers no replication; explicitly conditional on the finding holding up.

## Entities Mentioned

- None.

## Concepts Covered

- [tool-calling](/concepts/tool-calling.md) — the decision located in a narrow neural circuit
- [interpretability](/concepts/interpretability.md) — tracing a decision back to specific neurons
- [targeted-fine-tuning](/concepts/targeted-fine-tuning.md) — a proposed lever on the identified circuit

## Related Sources

- [Classical Statistics vs. Machine Learning: A Practical Distinction](/sources/classical-statistics-vs-machine-learning-a-practical-distinction.md)
- [The Compression Cliff Nobody Budgeted For](/sources/the-compression-cliff-nobody-budgeted-for.md)
