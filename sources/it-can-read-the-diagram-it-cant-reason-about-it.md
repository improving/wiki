---
title: "It Can Read the Diagram. It Can't Reason About It."
type: "Source Summary"
description: "FeynmanBench shows vision-language models read diagram symbols well but collapse on relational reasoning, exposing benchmark validity limits."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/it-can-read-the-diagram-it-cant-reason-about-it/it-can-read-the-diagram-it-cant-reason-about-it.md"
---

# It Can Read the Diagram. It Can't Reason About It. — Summary

**Original source**: `references/devlinliles.com/it-can-read-the-diagram-it-cant-reason-about-it/it-can-read-the-diagram-it-cant-reason-about-it.md`

## Summary

Vision-language models can identify the components in a diagram but fail to reason about how they connect. Using FeynmanBench, which tests five progressively harder checkpoints of Feynman-diagram reasoning across nineteen models from five providers and over 2,000 diagrams, Liles shows a consistent "CP3 cliff": models excel at recognizing symbols but collapse when asked to hold a whole graph in mind. He maps this to his client advice that AI helps "in the boxes, not the arrows," and warns against treating any benchmark score as measuring your diagrams.

## Key Claims

- GPT-5.5 scores 84% on checkpoint 1 (identifying particles/vertices) but falls to 46% on checkpoint 3 (graph reconstruction) and 16% on checkpoint 5 (deriving physics).
- Every model shows the same shape; Claude Sonnet 4.6 drops from 65% to 3%, Doubao Seed 2.0 Pro from 79% to under 1%.
- Rarer-but-simpler diagram topologies score worse than common-but-complex ones, indicating pattern-matching against training data.
- A single static image encoding loses relational information permanently; letting a model re-look mid-reasoning (DeepEyes) improved grounding.
- Models default to the camera's viewpoint even when told to reason from another frame of reference (OrientSAM).

## Relevance

Central to [benchmark validity](/concepts/benchmark-validity.md) and [benchmark saturation](/concepts/benchmark-saturation.md); informs discussions of [hallucination](/concepts/hallucination.md) and generalization limits.

## Quality

Practitioner blog post by Devlin Liles. Richly sourced (FeynmanBench, ICML 2026 work, DeepEyes, OrientSAM) and concrete with figures; relies on secondary reporting of those studies and is careful to scope its clinical claims.

## Entities Mentioned

- [GPT-5.5](/entities/gpt-5-5.md) — top overall model, illustrates the CP3 cliff
- [Claude Sonnet 4.6](/entities/claude-sonnet-4-6.md) — shows steep checkpoint drop and the rarity inversion

## Concepts Covered

- [Benchmark validity](/concepts/benchmark-validity.md) — a benchmark measures its own diagrams, not yours
- [Benchmark saturation](/concepts/benchmark-saturation.md) — general scores say little about structured reasoning
- [Hallucination](/concepts/hallucination.md) — ungrounded conclusions via shortcut correlation

## Related Sources

- [No Model Is Consistently Good at Reading Minds](/sources/no-model-is-consistently-good-at-reading-minds.md)
