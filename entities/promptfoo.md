---
title: "Promptfoo"
type: "Entity"
description: "Prompt testing and evaluation tool used here to automate quantitative prompt checks and model comparisons."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, evaluation, testing]
sources:
  - "/sources/building-prompt-evaluation-habit.md"
  - "/sources/llm-evaluation-ai-native-applications.md"
---

# Promptfoo

Promptfoo is a prompt testing and evaluation tool that appears in this corpus as the way to automate the quantitative half of [prompt evaluation](/concepts/prompt-evaluation.md) — the yes/no checks that can run at the same speed as the AI.

## Role in the Corpus

- In building a prompt-evaluation habit, the guidance is to automate quantitative checks first (word count, tests passing, schema conformance) using tools like Promptfoo, and reserve judgment-based checks for LLM-as-a-judge with a written rubric.
- Structured outputs let those checks be validated against a schema, making pass/fail mechanical rather than subjective.
- The LLM evaluation survey notes Promptfoo was acquired by [OpenAI](/entities/openai.md) in 2026 but remains MIT-licensed, and lists it in the evaluation tool map.
- The broader argument is that a prompt promoted from one-off to shared use should be re-tested on every change, with prompt regression testing catching problems before production.

## Related

- [prompt evaluation](/concepts/prompt-evaluation.md) — the discipline Promptfoo serves
- [LLM evaluation](/concepts/llm-evaluation.md) — the wider discipline
- [evals as code](/concepts/evals-as-code.md) — versioned graders wired into CI
- [OpenAI](/entities/openai.md) — the acquirer
