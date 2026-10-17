---
title: "Context Pollution"
type: "Concept"
description: "Filling an agent's context window with irrelevant or wrong information that misleads it despite ample room."
created: '2026-10-17'
updated: '2026-10-17'
tags: [context, retrieval, agents]
sources:
  - "/sources/the-context-window-is-not-a-filing-cabinet.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
---

# Context Pollution

Context pollution is the presence of irrelevant, stale, or misleading material in an agent's working context — a failure that occurs even when there is technically enough room. It matters because retrieval does not remove the problem, it relocates it: RAG shifts failure from a window that is too full to a window filled with the wrong things.

## Key Claims

- Saturation, pollution, and retrieval latency are the three context window problems.
- Pollution misleads agents even when the window has plenty of free space.
- RAG shifts failure from "window too full" to "window filled with wrong things."
- Being explicit about what each step needs makes retrieval bounded and reliable.
- Context handling is part of a larger stack of twelve compounding problems across four layers, where a failure in one layer surfaces as a symptom in another.
- Most systems implement only working memory, so they reset every session, worsening pollution from re-fetched stale context.

## Related

- [Context Window](/concepts/context-window.md) — the resource being polluted
- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — the sibling failure of too much context
- [Context Management](/concepts/context-management.md) — the discipline that prevents pollution
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — mechanism that can introduce it
- [The Context Window Is Not a Filing Cabinet](/sources/the-context-window-is-not-a-filing-cabinet.md) — primary source
- [The Twelve Problems of Agentic Software Delivery](/sources/the-twelve-problems-of-agentic-software-delivery.md) — broader problem stack
