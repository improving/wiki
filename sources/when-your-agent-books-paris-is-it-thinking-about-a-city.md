---
title: "When Your Agent Books 'Paris,' Is It Thinking About a City?"
type: "Source Summary"
description: "Agents act on token representations that may lack genuine intentionality, so consequential actions need grounding against current world state."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/when-your-agent-books-paris-is-it-thinking-about-a-city/when-your-agent-books-paris-is-it-thinking-about-a-city.md"
---

# When Your Agent Books 'Paris,' Is It Thinking About a City? — Summary

**Original source**: `references/devlinliles.com/when-your-agent-books-paris-is-it-thinking-about-a-city/when-your-agent-books-paris-is-it-thinking-about-a-city.md`

## Summary

The post asks whether, when an agent emits the token "Paris," its representation refers to the actual city or merely to the token's statistical neighborhood in training data. Invoking Franz Brentano's 1874 concept of intentionality (the "aboutness" of mental states), the author argues that shallow representation is fine for retrieval and summarization but insufficient for agents that act in real systems. The fix is architectural: verify representations against current world state before acting, and treat unverified facts as unverified.

## Key Claims

- Brentano identified intentionality — directedness toward an object — as the defining feature of mental states.
- AI systems have genuine intentionality only sometimes, in narrow domains, under controlled conditions; not reliably enough for booking flights.
- Research distinguishes genuine intentionality from "quasi-intentionality," a functional mimicry of aboutness that suffices for coherent text but not reliable action.
- Grounding is an architectural problem: [RAG](/concepts/retrieval-augmented-generation.md) connects generation to a current knowledge base, and tool verification confirms a representation against live system state before acting.
- Best practice: treat representations as time-stamped; if the agent doesn't know when it last verified a fact, treat it as unverified.

## Relevance

Connects philosophical grounding to agent design, informing [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md), [tool calling](/concepts/tool-calling.md), and stale-representation failure modes.

## Quality

Practitioner blog post by Devlin Liles. Clear conceptual framing with a practical design checklist; it leans on philosophy and cited research rather than empirical measurement.

## Entities Mentioned

- None.

## Concepts Covered

- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — a grounding mechanism
- [Tool Calling](/concepts/tool-calling.md) — verification of representations against live system state

## Related Sources

- [The Catalog Already Learned to Talk to Machines](/sources/the-catalog-already-learned-to-talk-to-machines.md)
- [The Context Window Is Not a Filing Cabinet](/sources/the-context-window-is-not-a-filing-cabinet.md)

## Related Sources

- [Your Model Doesn't Know What 'Hot' Feels Like](/sources/your-model-doesnt-know-what-hot-feels-like.md)
