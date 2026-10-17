---
title: "The Model Inherited an Unequal World"
type: "Source Summary"
description: "Bias is structural, not a content problem: models inherit the epistemic hierarchy of their training data and need exposure assessment."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-model-inherited-an-unequal-world/the-model-inherited-an-unequal-world.md"
---

# The Model Inherited an Unequal World — Summary

**Original Source**: `references/devlinliles.com/the-model-inherited-an-unequal-world/the-model-inherited-an-unequal-world.md`

## Summary

Framing AI bias as a content problem — biased outputs fixed with filters or fine-tuning — misses where it lives. By the time a model generates output, the bias is already encoded in its probability distributions, so post-processing patches symptoms. The post uses Miranda Fricker's 2007 concept of epistemic injustice to argue the cause is structural: models inherit the epistemic hierarchy of their training corpus, and the responsible response is honest exposure assessment and proportionate controls rather than zero tolerance.

## Key Claims

- Fricker's testimonial injustice describes a speaker's credibility being systematically deflated because of identity; internet-scale training data encodes exactly this hierarchy.
- Common Crawl's language composition is roughly 44% English with the rest spread thinly across hundreds of languages; Llama 2's training mix was reported as 89.7% English after preprocessing.
- 2024 ACM FAccT research found LLMs reproduce testimonial injustice at scale — downranking, mistranslating, or failing to recognize non-dominant linguistic contributions — and exhibit hermeneutical injustice.
- Kotek et al. (ACM FAccT 2023) found LLMs 3 to 6 times more likely to pick gender-stereotypically aligned occupations in pronoun resolution, more extreme than actual Bureau of Labor Statistics figures.
- High-stakes contexts — hiring, lending, medical triage, legal analysis, performance evaluation — are most dangerous; mitigation is characterizing which populations are affected, then applying stronger human review, representative [targeted fine-tuning](/concepts/targeted-fine-tuning.md), or both.

## Relevance

Central to [AI governance](/concepts/ai-governance.md) and [data governance](/concepts/data-governance.md), with mitigation touching [fine-tuning](/concepts/fine-tuning.md) and [targeted fine-tuning](/concepts/targeted-fine-tuning.md).

## Quality

Practitioner blog post by Devlin Liles. Strongly sourced with named studies and specific figures; the philosophical framing is applied cleanly, though the mitigation advice remains high-level.

## Entities Mentioned

- None.

## Concepts Covered

- [AI governance](/concepts/ai-governance.md) — exposure assessment and proportionate controls before high-stakes deployment
- [data governance](/concepts/data-governance.md) — the demographic and linguistic composition of training data as a governance question
- [fine-tuning](/concepts/fine-tuning.md) — invoked as the content-framing fix the post argues is insufficient
- [targeted fine-tuning](/concepts/targeted-fine-tuning.md) — representative-data fine-tuning as one mitigation
