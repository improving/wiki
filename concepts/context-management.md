---
title: "Context Management"
type: "Concept"
description: "Keeping exactly the right information in an agent's working window, treating context as a whiteboard rather than a filing cabinet."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, retrieval, memory]
sources:
  - "/sources/agentic-development-is-eleven-problems-not-one.md"
  - "/sources/the-context-window-is-not-a-filing-cabinet.md"
  - "/sources/you-are-not-talking-to-an-individual.md"
---

# Context Management

Context management is the discipline of keeping exactly the right information in an agent's working [context window](/concepts/context-window.md). Across this corpus it is one of the competencies that matter most in production: the window is a whiteboard, not a filing cabinet, and being explicit about what each step needs is what makes retrieval bounded and reliable.

## Key Claims

- Saturation, pollution, and retrieval latency are the three context window problems; [context pollution](/concepts/context-pollution.md) misleads agents even when there is technically enough room.
- [RAG](/concepts/retrieval-augmented-generation.md) shifts the failure from "window too full" to "window filled with the wrong things."
- Being explicit about what each step needs makes retrieval bounded and reliable, which is why context management is a distinct competency rather than a model capability.
- Agentic development spans eleven competency blocks across foundation, operational, governance, and intelligence layers; coordination and context management matter most in production, and most teams stall after building foundation plus minimal governance.
- Each inference is a token of a type, so continuity, consistency, and identity must be engineered externally — continuity is a state file read at session start, not a property of the model.
- Inference is stochastic: the same input yields outputs from the same distribution, not identical answers, so working memory must be managed explicitly.

## Related

- [Context Window](/concepts/context-window.md) — the resource being managed
- [Context Pollution](/concepts/context-pollution.md) — the failure mode that fills it
- [Working Memory](/concepts/working-memory.md) — the externalized continuity layer
- [The Context Window Is Not a Filing Cabinet](/sources/the-context-window-is-not-a-filing-cabinet.md) — primary source
