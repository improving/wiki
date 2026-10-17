---
title: "Vibes Aren't a Strategy: Engineering Context in the Age of AI"
type: "Source Summary"
description: "Argues vibe coding breaks down at scale and teams must engineer durable 'living context' rather than rely on prompts."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, engineering, improving.com]
sources:
  - "references/improving.com/vibes-arent-a-strategy-engineering-context-in-the-age-of-ai/vibes-arent-a-strategy-engineering-context-in-the-age-of-ai.md"
---

# Vibes Aren't a Strategy: Engineering Context in the Age of AI — Summary

**Original source**: `references/improving.com/vibes-arent-a-strategy-engineering-context-in-the-age-of-ai/vibes-arent-a-strategy-engineering-context-in-the-age-of-ai.md`

## Summary

Vibe coding — describing what you want and letting AI generate code — is seductive for simple projects but cracks in enterprise systems. Tim Rayburn argues the failure is not that AI can't write code but that teams ignore the context window and how LLMs fail. The fix is context engineering: durable, shared artifacts ("living context") that AI reads, updates, and reuses instead of relying on conversation memory.

## Key Claims

- The context window is the core limit: as conversations grow, earlier details are summarized, compressed, or dropped, so the AI forgets decisions and contradicts itself.
- Developers then spend more time correcting the AI than benefiting from it.
- Code that doesn't match team preferences is often self-inflicted: without explicit guidance, AI defaults to its own interpretation of best practices.
- Context engineering requires deliberate, durable artifacts describing not just what to build but how.
- "Living context" treats project knowledge as a shared source of truth stored in files; the AI reads it, plans, implements, tests, and writes learnings back.
- Shared context scales for teams: one developer's update benefits every other developer and every AI assistant.
- Structured agile AI-development methods add roles, workflows, and artifacts; the discipline matters more than the specific framework.
- Acceleration without direction just gets you lost faster.

## Relevance

A direct treatment of [vibe coding](/concepts/vibe-coding.md) versus [context engineering](/concepts/context-engineering.md), grounded in the [context window](/concepts/context-window.md) and [context management](/concepts/context-management.md), and echoing [prompt engineering](/concepts/prompt-engineering.md).

## Quality

Practitioner essay by Tim Rayburn, companion to an Improving talk; clear and well-argued, though conceptual rather than measured.

## Entities Mentioned

- [Improving](/entities/improving.md) — author's employer
- [Tim Rayburn](/entities/tim-rayburn.md) — author

## Concepts Covered

- [vibe coding](/concepts/vibe-coding.md) — prompting without structured context
- [context engineering](/concepts/context-engineering.md) — durable, deliberate context
- [context window](/concepts/context-window.md) — the bounded attention limit
- [context management](/concepts/context-management.md) — keeping the right information in scope
- [prompt engineering](/concepts/prompt-engineering.md) — shaping model output
