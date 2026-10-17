---
title: "vibe coding"
type: "Concept"
description: "Building software by prompting an AI without structured context, which trades short-term speed for drift."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, engineering, craft]
sources:
  - "/sources/vibes-arent-a-strategy-engineering-context-in-the-age-of-ai.md"
  - "/sources/embedding-ai-into-daily-development.md"
  - "/sources/how-to-onboard-ai-coding-agent.md"
  - "/sources/define-done-before-you-build-a-task-agent.md"
---

# vibe coding

Vibe coding is building software by prompting an AI without structured context, and the sources argue it trades short-term speed for drift: as conversations grow, the AI forgets decisions, contradicts itself, and reverts to internet-default patterns. The fix is not better prompts but [context management](/concepts/context-management.md) — durable, shared "living context" artifacts that the AI reads, updates, and reuses.

## Key Claims

- The [context window](/concepts/context-window.md) is the core limit: earlier details are summarized, compressed, or dropped, so developers spend more time correcting the AI than benefiting from it.
- Without explicit guidance, AI defaults to its own interpretation of best practices, so code that doesn't match team preferences is often self-inflicted.
- "Living context" treats project knowledge as a shared source of truth stored in files; the AI reads it, plans, implements, tests, and writes learnings back.
- Onboarding an AI agent means making implicit knowledge explicit — coding standards, ADRs, a business glossary — and deleting changed patterns rather than marking them deprecated, since an agent reads "deprecated" as still valid.
- Consistency starts with consistent prompting: define "done" as binary exit criteria, build prompts from Role/Task/Context/Constraints, and validate against an independent checklist.
- The reframe is from "Vibe Coding" to "Vibe Solving": outcome-first, with a plan before touching files, an adversarial second opinion from a separate model, and an Investigation Markdown ledger.
- Maintenance is where AI returns its highest ROI because it is pattern-heavy and boring for humans; a 3,000-test migration took two days instead of weeks.

## Related

- [Context Management](/concepts/context-management.md) — durable context over conversation memory
- [Context Window](/concepts/context-window.md) — the bounded attention limit
- [Prompt Engineering](/concepts/prompt-engineering.md) — shaping model output
- [encoded standards](/concepts/encoded-standards.md) — turning craft into reusable rules
- [Definition of Done](/concepts/definition-of-done.md) — measurable exit criteria
- [AI code review](/concepts/ai-code-review.md) — verification of AI-assisted work
- [AI augmentation](/concepts/ai-augmentation.md) — expanding the engineer, not replacing them
