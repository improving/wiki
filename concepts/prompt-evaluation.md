---
title: "prompt evaluation"
type: "Concept"
description: "Treating prompts like code: defining done, then regression-testing them with quantitative and qualitative checks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, testing, engineering]
sources:
  - "/sources/building-prompt-evaluation-habit.md"
  - "/sources/no-ownership-or-maintenance.md"
  - "/sources/llm-evaluation-ai-native-applications.md"
---

# prompt evaluation

Prompt evaluation treats prompts like code: define what "done" looks like, then regression-test the prompt with quantitative and qualitative checks run at the same speed as the AI. The sources argue that a 100% acceptance rate is often proof that nobody is fact-checking, and that any prompt promoted from one-off to shared use needs a [Definition of Done](/concepts/definition-of-done.md) and automated checks before problems cascade downstream.

## Key Claims

- "It worked" (one input) and "it works" (repeatable) are different claims; only the second is something a team can build on.
- A reported 100% acceptance rate on AI-generated work should be alarm, not celebration — the pattern yields about three months of productivity then pain.
- Quantitative checks are yes/no and automatable (word count, tests passing), run first with tools like promptfoo and structured outputs checked against a schema.
- Qualitative checks need judgment: an LLM-as-a-judge with a written rubric and passing examples, then turned into a quantitative pass/fail.
- Checks should run in the same session and at the same speed as the AI, so problems are caught before they cascade.
- Evaluation compounds: test against a cheaper model and re-run evals when a provider updates a model, since prompt regression testing beats finding out in production.
- Models are living systems: one client's policy Q&A bot used monthly prompt-pack refreshes and quarterly drift evaluations against gold questions to prevent confidence erosion.

## Related

- [LLM evaluation](/concepts/llm-evaluation.md) — the broader measurement discipline
- [Definition of Done](/concepts/definition-of-done.md) — the bar a prompt must clear
- [test-driven development](/concepts/test-driven-development.md) — the borrowed discipline
- [Model-as-judge](/concepts/model-as-judge.md) — rubric-based LLM grading
- [evals-as-code](/concepts/evals-as-code.md) — versioned graders in the workflow
- [AI monitoring](/concepts/ai-monitoring.md) — where prompt refresh becomes ongoing
- [Golden Dataset](/concepts/golden-dataset.md) — fixed cases for regression
