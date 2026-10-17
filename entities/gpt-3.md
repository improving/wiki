---
title: "GPT-3"
type: "Entity"
description: "OpenAI's landmark language model, used in this corpus as a baseline for prompting effects and as a foil in the neuron-count debate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [model, openai, llm]
sources:
  - "/sources/the-model-knows-more-than-its-telling-you.md"
  - "/sources/the-neuron-count-tell.md"
---

# GPT-3

GPT-3 is OpenAI's large language model that defined the modern scaling era. In this corpus it anchors two arguments: that measured capability depends on how a model is prompted, and that comparing parameter counts to biological neurons proves nothing.

## Overview

On evaluation, one post argues benchmark scores underestimate capability because prompting structure, not model knowledge alone, determines what performance can be elicited. Chain-of-thought lifted PaLM 540B on GSM8K from 18% to 57%, and few-shot examples activate capabilities zero-shot prompts leave dormant. Capability assessments therefore have a shelf life as prompting skill improves.

On analogy, the other post targets the habit of comparing artificial parameter counts to biological neuron counts. The 86 billion neuron figure is Herculano-Houzel's count of the human brain; an artificial neuron is a weighted sum, nothing like a biological cell, and consciousness has no agreed definition or unit. A precise-sounding number can substitute for an absent argument.

## Key Claims

- Model capability measured by simple prompts is a function of how it was asked.
- Chain-of-thought lifted PaLM 540B on GSM8K from 18% to 57%.
- Few-shot examples activate capabilities zero-shot prompts leave dormant.
- An artificial neuron is a weighted sum, nothing like a biological cell.
- The 86 billion neuron figure is a count of the human brain, not a benchmark.

## Related

- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — the technique that lifts elicited scores
- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — the prompting effect described
- [Benchmark Validity](/concepts/benchmark-validity.md) — the measurement critique
- [GPT-4](/entities/gpt-4.md) — its successor
- [GSM8K](/entities/gsm8k.md) — the benchmark cited
- [The Model Knows More Than It's Telling You](/sources/the-model-knows-more-than-its-telling-you.md) — primary source
