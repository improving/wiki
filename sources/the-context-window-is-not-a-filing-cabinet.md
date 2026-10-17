---
title: "The Context Window Is Not a Filing Cabinet"
type: "Source Summary"
description: "Filling the context window is the default mistake; context management keeps the working window to exactly what the current step needs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-context-window-is-not-a-filing-cabinet/the-context-window-is-not-a-filing-cabinet.md"
---

# The Context Window Is Not a Filing Cabinet — Summary

**Original source**: `references/devlinliles.com/the-context-window-is-not-a-filing-cabinet/the-context-window-is-not-a-filing-cabinet.md`

## Summary

Most teams fill the context window and assume more context is better context. [Context management](/concepts/context-management.md) is the discipline of keeping the working window to exactly what the current step needs — no more, no less. The post names three failure modes: saturation (irrelevant prior steps crowding out new information), pollution (contradicted or stale information misleading the agent), and retrieval latency (multi-hop lookups). It surveys patterns and argues most context problems are really retrieval problems, so specificity about what each step needs is the core practice.

## Key Claims

- Saturation looks like capacity but is a selection problem: LLMs lose coherence in the latter portions of long contexts before the nominal token ceiling, as [lost in the middle](/concepts/lost-in-the-middle.md) describes.
- [Context pollution](/concepts/context-pollution.md) is subtler and more damaging — old or contradicted information misleads the agent even when there is room, and looks like model error rather than a hygiene problem.
- The worst retrieval latency is multi-hop: the agent needs fact A to retrieve B to retrieve C, three dependent round trips that are slow and fragile at every hop.
- Sliding windows break on long dependency chains; [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) shifts failure from "window too full" to "window filled with the wrong things."
- Reranking retrieved chunks — scoring the top 20 and injecting only the top 5 — produces meaningfully better context quality.

## Relevance

Core to [context management](/concepts/context-management.md) and [context pollution](/concepts/context-pollution.md), with retrieval patterns spanning [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md), [reranking](/concepts/reranking.md), and [lost in the middle](/concepts/lost-in-the-middle.md).

## Quality

Practitioner blog post by Devlin Liles. Good taxonomy and a memorable whiteboard-versus-filing-cabinet framing; tool recommendations are vendor-friendly and evidence is anecdotal.

## Entities Mentioned

- [LangChain](/entities/langchain.md) — cited for memory and retrieval primitives

## Concepts Covered

- [context management](/concepts/context-management.md) — the operational discipline of the working window
- [context pollution](/concepts/context-pollution.md) — stale or contradicted context misleading the agent
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — external retrieval as the common context pattern
- [reranking](/concepts/reranking.md) — scoring retrieved chunks before injection
- [lost in the middle](/concepts/lost-in-the-middle.md) — coherence loss in long contexts

## Related Sources

- [When Your Agent Books 'Paris,' Is It Thinking About a City?](/sources/when-your-agent-books-paris-is-it-thinking-about-a-city.md)
