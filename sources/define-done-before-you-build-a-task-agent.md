---
title: "Define Done Before you Build a Task Agent"
type: "Source Summary"
description: "Define measurable exit criteria before building a task agent, then prompt and validate against an independent checklist."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, engineering, improving.com]
sources:
  - "references/improving.com/define-done-before-you-build-a-task-agent/define-done-before-you-build-a-task-agent.md"
---

# Define Done Before you Build a Task Agent — Summary

**Original source**: `references/improving.com/define-done-before-you-build-a-task-agent/define-done-before-you-build-a-task-agent.md`

## Summary

Daniel Scheufler argues that before building a task agent you must define what "done" means as measurable exit criteria, then prompt with role, task, context, and constraints, and validate the output against an independent checklist. That discipline turns inconsistent, one-off vibe coding into reusable, trustworthy agents.

## Key Claims

- Consistency starts with consistent prompting: AI must be consistent before it can be trusted.
- Define the task narrowly ("write unit tests for a function"), and if you can't articulate "done," you don't know it either — done should be binary, as in Scrum's Definition of Done.
- Build prompts from four components — Role, Task, Context, Constraints — and phrase constraints as "DO X" because AI, like toddlers, doesn't understand NOT well.
- Build an independent validation checklist separate from the prompt; on failure, identify the missed criterion and refine the constraints or context.
- Expect prompts to lengthen initially then stabilize, allowing a shift from heavy to lighter models and declining cost per task.
- Signal of progress: fewer one-off chat prompts, more workflow invocations, and criteria appearing in team repositories; most common development tasks can be covered in about twelve weeks.

## Relevance

Defines [task agents](/concepts/task-agents.md) around a binary [Definition of Done](/concepts/definition-of-done.md), sitting at Stage 2 of the [AI maturity model](/concepts/ai-maturity-model.md). It applies [prompt engineering](/concepts/prompt-engineering.md) and [acceptance criteria](/concepts/acceptance-criteria.md) to agent work.

## Quality

Practitioner how-to by Improving's Daniel Scheufler; concrete and reproducible, though the twelve-week estimate is anecdotal.

## Entities Mentioned

- [Daniel Scheufler](/entities/daniel-scheufler.md) — author
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [task agents](/concepts/task-agents.md) — the main topic
- [Definition of Done](/concepts/definition-of-done.md) — measurable exit criteria
- [AI maturity model](/concepts/ai-maturity-model.md) — where this practice sits
- [prompt engineering](/concepts/prompt-engineering.md) — structuring the prompt
- [acceptance criteria](/concepts/acceptance-criteria.md) — the validation checklist
