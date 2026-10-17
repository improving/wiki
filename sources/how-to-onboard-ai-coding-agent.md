---
title: "Right Way to Onboard an AI Coding Agent"
type: "Source Summary"
description: "Onboarding an AI coding agent means making implicit knowledge explicit through coding standards, ADRs, and structured context."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, engineering, improving.com]
sources:
  - "references/improving.com/how-to-onboard-ai-coding-agent/how-to-onboard-ai-coding-agent.md"
---

# Right Way to Onboard an AI Coding Agent — Summary

**Original source**: `references/improving.com/how-to-onboard-ai-coding-agent/how-to-onboard-ai-coding-agent.md`

## Summary

Daniel Scheufler argues that an AI coding agent needs onboarding much like a new engineer: it wasn't in the meetings where the architecture was decided, so unless you make your standards explicit it will reproduce the most common approach on the internet. The work is to capture what "the right way" actually means — coding standards, ADRs, a business glossary — while distinguishing documented context from encoded guardrails.

## Key Claims

- The agent will default to the most popular internet approach unless you tell it your context; it never sat in the architecture discussions.
- Production code should be succinct while test code should be descriptive, and standards must capture the "whys," not just the "hows."
- Architecture Decision Records make implicit decisions explicit so the agent continues your pattern instead of reverting to internet-default.
- Separate context (what you document) from guardrails (what you encode and run deterministically); a rule in the prompt is only a suggestion.
- Structure context so the most important information comes first — input tokens are cheaper than output, so front-loading cuts cost and token hunting.
- Delete changed patterns rather than marking them deprecated: an agent reads "deprecated" docs as still valid, and may even read the trash.
- Start with one area and iterate: each time the agent errs, ask whether you documented it, and if so make the documentation clearer.

## Relevance

Core to [context engineering](/concepts/context-engineering.md) and to avoiding [vibe coding](/concepts/vibe-coding.md), this depends on deliberate [context management](/concepts/context-management.md) and on turning judgment into [encoded standards](/concepts/encoded-standards.md).

## Quality

Practitioner how-to by Improving's Daniel Scheufler; specific and practical, though it defers guardrail mechanics to a later post.

## Entities Mentioned

- [Daniel Scheufler](/entities/daniel-scheufler.md) — author
- [Improving](/entities/improving.md) — the consultancy behind the guidance

## Concepts Covered

- [context engineering](/concepts/context-engineering.md) — the main topic
- [vibe coding](/concepts/vibe-coding.md) — the failure mode avoided
- [context management](/concepts/context-management.md) — structuring what the agent sees
- [encoded standards](/concepts/encoded-standards.md) — turning craft into reusable rules
