---
title: "Every AI Value System Bottoms Out Somewhere"
type: "Source Summary"
description: "AI alignment's grounding problem is the Münchhausen Trilemma: RLHF and Constitutional AI both halt at an arbitrary axiom, merely relocated."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/every-ai-value-system-bottoms-out-somewhere/every-ai-value-system-bottoms-out-somewhere.md"
---

# Every AI Value System Bottoms Out Somewhere — Summary

**Original source**: `references/devlinliles.com/every-ai-value-system-bottoms-out-somewhere/every-ai-value-system-bottoms-out-somewhere.md`

## Summary

Alignment asks what a model should optimize for, and the field's answer — human preferences — rests on an unjustified axiom. The Münchhausen Trilemma says any justification chain ends in infinite regress, circular reasoning, or an axiomatic halt. RLHF bottoms out in human preferences; Constitutional AI relocates the axiom to a chosen constitution. Neither escapes the trilemma, but both make the grounding choice more explicit, auditable, and revisable. The governance implication is that adopting a provider's model means adopting a value structure.

## Key Claims

- The Münchhausen Trilemma (formalized by Hans Albert, 1968) leaves only regress, circularity, or an unjustified axiomatic stop — no fourth option.
- RLHF terminates at the axiomatic horn: human preferences are the stopping point, defensible but technically arbitrary.
- Constitutional AI moves the arbitrary axiom up one level; the constitution is chosen, not derived from first principles.
- RLHF, Constitutional AI, RLAIF, and DPO cluster closely in human preference evaluations despite substantially different grounding structures.
- Human preferences are not a fixed target; social choice work argues diverse values cannot aggregate to one signal without explicit choices about whose values take priority.
- Deploying a provider's model means deploying its value structure; system prompts modify it and fine-tuning edits the weights that encode it.

## Relevance

Informs [RLHF](/concepts/rlhf.md), [Constitutional AI](/concepts/constitutional-ai.md), [fine-tuning](/concepts/fine-tuning.md), and [AI governance](/concepts/ai-governance.md).

## Quality

Practitioner blog post by Devlin Liles. Lucid philosophical framing with named sources; the argument is conceptual rather than empirical, and it cites 2024-2025 work loosely.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — provider behind Constitutional AI

## Concepts Covered

- [RLHF](/concepts/rlhf.md) — the dominant alignment approach that bottoms out in human preferences
- [Constitutional AI](/concepts/constitutional-ai.md) — the approach that relocates the axiom to a written constitution
- [fine-tuning](/concepts/fine-tuning.md) — directly editing the weights that encode values
- [AI governance](/concepts/ai-governance.md) — knowing where your justification chain runs out

## Related Sources

- [When the Model Acts, the Philosophy Changes Completely](/sources/when-the-model-acts-the-philosophy-changes-completely.md)
