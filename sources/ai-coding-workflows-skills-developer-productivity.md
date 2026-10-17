---
title: "Breaking the Stage 2 Ceiling: A Live Walkthrough of Workflows and Skills"
type: "Source Summary"
description: "Junior devs gain ~30% from AI coding assistants and seniors 3-5%; the gap is workflow, not model, closed by plans, workflows, and skills."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, developer-experience, improving.com]
sources:
  - "references/improving.com/ai-coding-workflows-skills-developer-productivity/ai-coding-workflows-skills-developer-productivity.md"
---

# Breaking the Stage 2 Ceiling: A Live Walkthrough of Workflows and Skills — Summary

**Original source**: `references/improving.com/ai-coding-workflows-skills-developer-productivity/ai-coding-workflows-skills-developer-productivity.md`

## Summary

Most developers using AI coding assistants are stuck at the "Stage 2" ceiling, where the tool helps with a single task but nothing connects across sessions. The post walks through moving past it by persisting plans into the repo, writing the development process down as reusable workflows, and promoting workflows into AI-triggered skills, shifting the developer from doer to director to system designer.

## Key Claims

- Junior developers see roughly a 30 percent productivity gain from AI coding assistants; senior developers see closer to 3 to 5 percent, and the gap is about how the tool is used, not the model.
- Stage 2 is the default configuration: Windsurf and Code Explorer with no MCPs, rules, workflows, or skills, turbo and auto-continue off, producing call-and-response work whose context never travels between sessions.
- The first move is small on purpose: save the plan to a `plan.md` file in the project so it survives the chat window.
- The second move is writing the process down in plain English — BDD-style specs, TDD follow-on, SOLID principles, match the existing architecture — as a reusable workflow file.
- Improving's instrumentation puts a healthy Stage 3 acceptance rate at 92 to 94 percent; below that trust or definitions are weak, above it the team is over-trusting the agent.
- A workflow is something a developer triggers on purpose; a skill is something the AI triggers on its own when it semantically matches the skill's description.
- Running the full chain against the pause/resume plan produced eleven features and sixty-one detailed tasks, plus docs and spec files.
- Three things make it hold: persistent planning artifacts, living documentation (which cheapens the Agile Manifesto's documentation tradeoff), and quality gates that set where the AI stops and a human reviews.
- Roles evolve: doer at Stage 2, director/reviewer at Stage 3, system designer and governor at Stage 4.

## Relevance

Informs [AI maturity model](/concepts/ai-maturity-model.md), [context engineering](/concepts/context-engineering.md), the [woodshop-to-factory transition](/concepts/woodshop-to-factory-transition.md), and [encoded standards](/concepts/encoded-standards.md).

## Quality

Practitioner walkthrough by Devlin Liles; concrete and honest about what is still hard, though vendor-adjacent (Windsurf, Improving's own tools and metrics).

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author; Improving's Chief AI Officer
- [Improving](/entities/improving.md) — publishes the AI maturity curve and acceptance-rate instrumentation
- [Windsurf](/entities/windsurf.md) — the agentic IDE used in the demo

## Concepts Covered

- [AI maturity model](/concepts/ai-maturity-model.md) — the Stage 2 to Stage 4 progression
- [context engineering](/concepts/context-engineering.md) — persisting the shared context AI needs
- [woodshop-to-factory transition](/concepts/woodshop-to-factory-transition.md) — the post's central metaphor
- [encoded standards](/concepts/encoded-standards.md) — workflows and skills as shareable process
- [quality gates](/concepts/quality-gates.md) — the boundary where humans review
