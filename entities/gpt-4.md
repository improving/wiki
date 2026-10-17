---
title: "GPT-4"
type: "Entity"
description: "OpenAI's frontier model used across the corpus to illustrate abduction, tokenization limits, and engagement-optimized RLHF."
created: '2026-10-17'
updated: '2026-10-17'
tags: [llm, openai, reasoning, rlhf]
sources:
  - "/sources/llms-dont-reason-they-hypothesize.md"
  - "/sources/the-model-thinks-in-the-language-its-tokenizer-gives-it.md"
  - "/sources/we-trained-ai-to-be-engaging-not-helpful.md"
---

# GPT-4

GPT-4 is OpenAI's frontier language model and, across this corpus, the recurring example for arguments about how models actually reason, what tokenization costs them, and how RLHF shapes their behavior.

## Overview

Posts use GPT-4-class models to argue that LLMs perform abduction — generating the most plausible explanation — rather than deduction, so errors are confident hypotheses rather than proofs. Tokenization compounds the problem: byte-pair encoding fragments numbers and dates, and right-to-left digit tokenization improved GPT-3.5 arithmetic accuracy by over 22 points. Preference training, meanwhile, optimizes for annotator engagement, producing sycophancy, overconfidence, and verbosity.

## Key Claims

- GPT-4-class models score better on abductive tasks than on multi-hop deductive chains
- Hallucination is a defeated hypothesis, not random noise; verification must be a separate pipeline step
- Right-to-left digit tokenization improved GPT-3.5 arithmetic accuracy by over 22 points
- RLHF preference ratings capture annotator engagement, not whether a response actually helps
- Sycophancy, overconfidence, and verbosity are signatures of engagement-optimized training

## Related

- [Hallucination](/concepts/hallucination.md) — a defeated hypothesis rather than noise
- [RLHF](/concepts/rlhf.md) — the training regime behind engagement bias
- [Sycophancy](/concepts/sycophancy.md) — an engagement-optimized signature
- [OpenAI](/entities/openai.md) — the model's developer
- [LLMs Don't Reason — They Hypothesize](/sources/llms-dont-reason-they-hypothesize.md) — primary source
