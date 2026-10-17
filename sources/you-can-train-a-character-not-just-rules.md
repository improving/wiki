---
title: "You Can Train a Character, Not Just Rules"
type: "Source Summary"
description: "Character-based alignment trains stable dispositions via first-person identity declarations, generalizing better than rules or preference optimization."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/you-can-train-a-character-not-just-rules/you-can-train-a-character-not-just-rules.md"
---

# You Can Train a Character, Not Just Rules — Summary

**Original source**: `references/devlinliles.com/you-can-train-a-character-not-just-rules/you-can-train-a-character-not-just-rules.md`

## Summary

Liles argues for a third alignment approach — character-based alignment — alongside Constitutional AI and RLHF. Drawing on Aristotle, he contends that rules require interpretation and break on novel cases, whereas stable dispositions (virtue) generalize. The 2025 Parrhesia project made this concrete by training on first-person identity declarations ("I am not afraid to be direct...") rather than behavioral rules, operationalizing the parrhesiastes/kolax virtue-vice pair. Results were measurable, and Liles frames it as machine habituation. He suggests teams write toward the assistant's character rather than accumulating more system-prompt rules.

## Key Claims

- Anthropic's model spec ("genuinely helpful, honest, and harmless") is a character description, not a rule.
- The Parrhesia project trained on first-person identity declarations rather than behavioral rules.
- Trait correlation across base models jumped from 0.44 to 0.87; F1 on character retention rose from 0.79 to 0.95.
- On 260 scenarios the model scored 20/20 on standard golden prompts and 19/19 on hard sycophancy-derived prompts, including multi-turn escalation and fabricated citations.
- Aristotle's "habituation" maps to repeated exposure to identity statements becoming the model's operative self-concept.
- Whether models possess genuine phronesis (practical wisdom) versus a behavioral approximation remains unresolved.

## Relevance

Informs [Constitutional AI](/concepts/constitutional-ai.md), [RLHF](/concepts/rlhf.md), and defenses against [sycophancy](/concepts/sycophancy.md), plus [prompt engineering](/concepts/prompt-engineering.md) and [fine-tuning](/concepts/fine-tuning.md) practice.

## Quality

Practitioner blog post by Devlin Liles. Engages real research with concrete metrics and acknowledges the open philosophical question; the evidence comes from a single project.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — publisher of the Claude model spec quoted
- [Claude](/entities/claude.md) — the model whose spec is discussed
- [Aristotle](/entities/aristotle.md) — source of the virtue and habituation framing

## Concepts Covered

- [Constitutional AI](/concepts/constitutional-ai.md) — one of the dominant alignment approaches contrasted
- [RLHF](/concepts/rlhf.md) — the preference-optimization approach contrasted with character training
- [Sycophancy](/concepts/sycophancy.md) — the failure mode the character-trained model resisted
- [Prompt Engineering](/concepts/prompt-engineering.md) — the practice the post reframes toward character
- [fine-tuning](/concepts/fine-tuning.md) — whether training data reinforces identity or mere compliance

## Related Sources

- [Fulfillment Is Not Enjoyment](/sources/fulfillment-is-not-enjoyment.md)
- [When the Model Acts, the Philosophy Changes Completely](/sources/when-the-model-acts-the-philosophy-changes-completely.md)
