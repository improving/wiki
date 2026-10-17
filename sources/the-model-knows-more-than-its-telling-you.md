---
title: "The Model Knows More Than It's Telling You"
type: "Source Summary"
description: "Argues LLM capability is elicited by prompting, not fixed, so benchmarks and one-off evals systematically understate what models can do."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-model-knows-more-than-its-telling-you/the-model-knows-more-than-its-telling-you.md"
---

# The Model Knows More Than It's Telling You — Summary

**Original source**: `references/devlinliles.com/the-model-knows-more-than-its-telling-you/the-model-knows-more-than-its-telling-you.md`

## Summary

Devlin Liles argues that enterprise AI's costliest misconception is treating model capability as fixed. Drawing on Michael Polanyi's 1966 idea of tacit knowledge — "we can know more than we can tell" — he contends that much of what a language model knows sits inert in its weights until the right prompt structure elicits it. Measured capability is therefore a function of how the model was asked, not just what it knows, which makes prompting a first-class engineering concern rather than documentation.

## Key Claims

- In the original Wei et al. 2022 chain-of-thought paper, CoT prompting lifted PaLM 540B on GSM8K from 18% (standard prompting) to 57%, surpassing a fine-tuned GPT-3 with a verifier — with no change to the model itself.
- Standard benchmark evaluations use standard prompting, so they measure only the "explicit layer" and systematically underestimate capability.
- Few-shot examples and step-by-step reasoning give tacit knowledge a scaffold to organize around and externalize.
- Because elicitation is a skill, capability assessments have a shelf life; locking architecture to early assessments boxes teams into artifacts of underdeveloped prompting.

## Relevance

Informs [tacit knowledge](/concepts/tacit-knowledge.md), [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md), [few-shot prompting](/concepts/few-shot-prompting.md), and [prompt engineering](/concepts/prompt-engineering.md) as levers on measured capability.

## Quality

Practitioner blog post by Devlin Liles. Strong conceptual framing anchored in one well-known figure (Wei et al.); the capability-shelf-life governance claim is argument rather than evidence.

## Entities Mentioned

- [GPT-3](/entities/gpt-3.md) — fine-tuned baseline with a verifier that CoT prompting surpassed
- [GSM8K](/entities/gsm8k.md) — math word-problem benchmark where the 18%→57% jump was measured

## Concepts Covered

- [Tacit Knowledge](/concepts/tacit-knowledge.md) — the post's central analogy
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — an elicitation technique
- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — worked examples as elicitation
- [Prompt Engineering](/concepts/prompt-engineering.md) — recast as first-class engineering

## Related Sources

- [The Neuron Count Tell](/sources/the-neuron-count-tell.md)
- [The Stopping Rule Your Agent Doesn't Have](/sources/the-stopping-rule-your-agent-doesnt-have.md)

## Related Sources

- [Your Model Doesn't Know What 'Hot' Feels Like](/sources/your-model-doesnt-know-what-hot-feels-like.md)
