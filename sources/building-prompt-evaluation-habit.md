---
title: "Building a Prompt Evaluation Habit Your Team Can Trust"
type: "Source Summary"
description: "Argues prompts reused across a team must be tested like code, with quantitative and qualitative checks run at the same speed as the AI."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, testing, improving.com]
sources:
  - "references/improving.com/building-prompt-evaluation-habit/building-prompt-evaluation-habit.md"
---

# Building a Prompt Evaluation Habit Your Team Can Trust — Summary

**Original source**: `references/improving.com/building-prompt-evaluation-habit/building-prompt-evaluation-habit.md`

## Summary

"It worked" and "it works" are different claims, and only the second is something a team can build on. The post argues that any prompt promoted from one-off to shared use should be evaluated like code — run against several real inputs, checked against a Definition of Done, and re-tested on every change — because a 100% acceptance rate is often proof that nobody is fact-checking.

## Key Claims

- The gap between "this looks good" and "this works" is the gap between a feeling and evidence; Stephen Covey calls the disciplined version Smart Trust.
- A reported 100% acceptance rate on AI-generated work should be alarm, not celebration, because it often means nobody is checking; the pattern yields about three months of productivity then pain.
- Define what "done" looks like first; a one-off manual check only proves the prompt worked on that one input.
- Quantitative checks are yes/no and automatable (word count, tests passing); automate them first, using tools like promptfoo, and use structured outputs to check against a schema.
- Qualitative checks need judgment; use LLM-as-a-judge with a written rubric and passing examples, then turn the grade into a quantitative pass/fail.
- Checks should run at the same speed as the AI, in the same session, so problems are caught before they cascade downstream.
- Evaluation compounds: test the prompt against a cheaper model, re-run evals when a provider updates a model — prompt regression testing beats finding out in production.

## Relevance

Defines [prompt evaluation](/concepts/prompt-evaluation.md) as part of [LLM evaluation](/concepts/llm-evaluation.md), borrowing [test-driven development](/concepts/test-driven-development.md) discipline and the [Definition of Done](/concepts/definition-of-done.md).

## Quality

Practitioner how-to by Daniel Scheufler; concrete and tool-aware, though the guidance is high-level on implementation.

## Entities Mentioned

- [Daniel Scheufler](/entities/daniel-scheufler.md) — author
- [Promptfoo](/entities/promptfoo.md) — prompt testing tool recommended
- [Stephen M.R. Covey](/entities/stephen-mr-covey.md) — source of Smart Trust
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [prompt evaluation](/concepts/prompt-evaluation.md) — testing prompts like code
- [LLM evaluation](/concepts/llm-evaluation.md) — continuous output-quality measurement
- [test-driven development](/concepts/test-driven-development.md) — defining checks before the artifact
- [Definition of Done](/concepts/definition-of-done.md) — the agreed bar a prompt must clear
- [model-as-judge](/concepts/model-as-judge.md) — rubric-based LLM grading
- [evals as code](/concepts/evals-as-code.md) — versioned graders in the workflow
