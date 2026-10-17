---
title: "GSM8K"
type: "Entity"
description: "A grade-school math word-problem benchmark whose scores swing widely with prompting strategy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [benchmark, evaluation, llm, prompting]
sources:
  - "/sources/the-model-knows-more-than-its-telling-you.md"
  - "/sources/the-stopping-rule-your-agent-doesnt-have.md"
---

# GSM8K

GSM8K is a benchmark of grade-school math word problems used to measure language-model reasoning. It appears in this corpus as evidence that a single benchmark score is a function of the prompt and stopping policy around the model, not a fixed property of the model itself.

## Key Claims

- Chain-of-thought prompting lifted PaLM 540B on GSM8K from 18% to 57%, showing how much of the score is elicited rather than stored.
- Few-shot examples activate capabilities that zero-shot prompts leave dormant, so headline numbers depend on evaluation format.
- Capability assessments have a shelf life: as prompting skill improves, the same model measures higher without changing.
- The stopping-rule work generalizes the lesson — reported acceptance can rise while true validity falls, so benchmark numbers need a validity check.

## Related

- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — the technique that moved GSM8K scores most
- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — example count changes elicited performance
- [Benchmark Validity](/concepts/benchmark-validity.md) — why a score may not measure the capability it names
- [The Model Knows More Than It's Telling You](/sources/the-model-knows-more-than-its-telling-you.md) — primary source
