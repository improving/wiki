---
title: "Your Model Doesn't Know What 'Hot' Feels Like"
type: "Source Summary"
description: "Language models manipulate ungrounded symbols, so physical-world and sensory tasks need human-grounded validation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/your-model-doesnt-know-what-hot-feels-like/your-model-doesnt-know-what-hot-feels-like.md"
---

# Your Model Doesn't Know What 'Hot' Feels Like — Summary

**Original source**: `references/devlinliles.com/your-model-doesnt-know-what-hot-feels-like/your-model-doesnt-know-what-hot-feels-like.md`

## Summary

The post explains the symbol grounding problem — Stevan Harnad's 1990 argument that symbols need anchoring outside themselves to carry meaning — and its language-model form, sometimes called the vector grounding problem. A model's token for "hot" sits in a statistical neighborhood of other tokens, not in physical sensation; meaning is relational rather than perceptual. It argues that multimodal training narrows but does not close the gap, and that the response is structural: staff the validation layer with humans who have the sensorimotor grounding the model lacks.

## Key Claims

- For a language model, "hot" connects to co-occurrence patterns, not to heat; the system is a dictionary defining words with other words all the way down.
- Grounded concepts generalize by analogy to physical reality, while statistically approximated ones generalize by pattern similarity — identical most of the time, divergent at the edges.
- A Frontiers in Systems Neuroscience perspective found vision-language models diverge from human grounding on how objects can be physically manipulated or used.
- The gap is sharpest in physical-world reasoning (structural engineering, logistics, materials, safety), sensory/experiential domains (UX research, ergonomics), and novel domain transfer.
- This is a structural feature, not a model bug awaiting an update, so reliability depends on correctly staffing human domain experts into validation.

## Relevance

Informs how teams reason about grounding failures and the limits of text-trained models in physical and sensory domains.

## Quality

Practitioner blog post by Devlin Liles. It accurately restates Harnad's problem, but the supporting research is cited without links and the argument is conceptual rather than empirically demonstrated.

## Entities Mentioned

- None.

## Concepts Covered

- None.

## Related Sources

- [The Model Knows More Than It's Telling You](/sources/the-model-knows-more-than-its-telling-you.md)
- [When Your Agent Books 'Paris,' Is It Thinking About a City?](/sources/when-your-agent-books-paris-is-it-thinking-about-a-city.md)
