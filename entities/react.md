---
title: "ReAct"
type: "Entity"
description: "Reasoning-and-acting agent pattern in which a model interleaves thought steps with tool calls, referenced in agent-reliability discussions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, architecture, tooling]
sources:
  - "/sources/escalation-to-a-human-is-not-a-confidence-score.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
---

# ReAct

ReAct is a widely used agent pattern in which a model alternates reasoning steps with actions (typically tool calls), feeding each observation back into the next thought. It is the reference loop behind many tool-calling agents discussed in this corpus.

## Overview

The pattern matters here because its autonomy creates the reliability problems the corpus studies: when to escalate, how much confidence to place in an action, and which architectural layer owns each failure. One post argues that confidence cannot be a single scalar and that agents must separate evidence sufficiency, action difficulty, and request ambiguity; another frames agentic delivery as twelve compounding problems across four layers.

## Key Claims

- Confidence thresholds conflate decision difficulty, missing evidence, and unclear requests, so abstention machinery cuts risk more than swapping in a more accurate model
- Decomposing action confidence from request uncertainty improved clarification detection by 73%
- Failure in one agentic layer surfaces as a symptom in a different layer, so reliability is a property of the connecting architecture
- Most agent systems implement only working memory and therefore reset every session
- Planning answers *how* and Definition answers *what*; order matters

## Related

- [Tool Calling](/concepts/tool-calling.md) — the action half of the loop
- [Chain-of-Thought Prompting](/concepts/chain-of-thought-prompting.md) — the reasoning half
- [Working Memory](/concepts/working-memory.md) — the layer most systems under-implement
- [The Twelve Problems of Agentic Software Delivery](/sources/the-twelve-problems-of-agentic-software-delivery.md) — primary source
