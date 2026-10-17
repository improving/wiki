---
title: "context engineering"
type: "Concept"
description: "Deliberately assembling the durable, shared context that makes AI-assisted work reliable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, engineering, developer-experience]
sources:
  - "/sources/vibes-arent-a-strategy-engineering-context-in-the-age-of-ai.md"
  - "/sources/from-ai-tools-to-ai-workflows-building-systems-that-scale-knowledge.md"
  - "/sources/how-to-onboard-ai-coding-agent.md"
  - "/sources/embedding-ai-into-daily-development.md"
  - "/sources/the-engineers-evolution-stage-3-directing-the-work-instead-of-doing-it.md"
---

# context engineering

Context engineering is the discipline of giving AI systems deliberate, durable context rather than relying on a conversation. It treats project knowledge — standards, decisions, plans, and intent — as shared artifacts stored in the repository, so the AI reads, plans, implements, tests, and writes learnings back. It matters because the [context window](/concepts/context-window.md) is a hard limit: as sessions grow, earlier decisions are summarized, compressed, or dropped, and the model contradicts itself.

## Key Claims

- Vibe coding cracks in enterprise systems not because AI can't write code but because teams ignore how LLMs fail and let context evaporate; the fix is "living context" in files, not chat memory.
- Value created in a chat vanishes when the prompt window closes; teams should externalize understanding into skill files, documented standards, architectural decision records, and written plans.
- An AI coding agent needs onboarding like a new engineer: it never sat in the architecture discussions, so absent explicit context it defaults to the most common approach on the internet.
- Separate context (what you document) from guardrails (what you encode and run deterministically) — a rule in the prompt is only a suggestion.
- Front-load the most important information because input tokens are cheaper than output, and delete changed patterns rather than marking them deprecated, since an agent reads "deprecated" docs as still valid.
- Shared context scales for teams: one developer's update benefits every other developer and every AI assistant.
- A healthy Stage 3 engineer runs at roughly 92–94% acceptance on agent output; the skills are prompt and context engineering, writing evaluable skills, and critical review.

## Related

- [context management](/concepts/context-management.md) — keeping the right information in the working window
- [prompt engineering](/concepts/prompt-engineering.md) — shaping output within a single prompt
- [vibe coding](/concepts/vibe-coding.md) — the unstructured-prompting failure mode
- [encoded standards](/concepts/encoded-standards.md) — turning judgment into reusable rules
- [Tim Rayburn](/entities/tim-rayburn.md) — argues the case in "Vibes Aren't a Strategy"
