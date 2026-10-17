---
title: "One Exemplar Is Enough, and a Second One Leaks"
type: "Source Summary"
description: "Few-shot prompts need one exemplar for structure; repeating examples adds token cost and lets the model echo exemplar values."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/one-exemplar-is-enough-and-a-second-one-leaks/one-exemplar-is-enough-and-a-second-one-leaks.md"
---

# One Exemplar Is Enough, and a Second One Leaks — Summary

**Original source**: `references/devlinliles.com/one-exemplar-is-enough-and-a-second-one-leaks/one-exemplar-is-enough-and-a-second-one-leaks.md`

## Summary

A receipt-digitization prompt started with five few-shot examples, and on noisy OCR receipts the model sometimes echoed an exemplar's item name or price instead of reading the actual receipt. Stripping the prompt to a single exemplar with a generic placeholder ("Item Name") held extraction accuracy while eliminating the leakage. The lesson: showing structure and showing content are different jobs, and repeating an example reinforces its specific values without teaching anything new about shape.

## Key Claims

- The five identical exemplars conveyed the same structure; four contributed nothing measurable to producing the correct shape.
- On the same 20 seeded receipts, accuracy held after dropping to one placeholder exemplar, while leakage on menu-adjacent names dropped to zero.
- Token cost fell by roughly the cost of the four removed examples.
- One exemplar suffices when structure is simple and flat; genuinely variable or nested schemas may need a second exemplar chosen to demonstrate the variation the first missed.
- Placeholders must be obviously structural ("Item Name", "0.00"), since plausible-sounding values can still be echoed.

## Relevance

Informs [few-shot prompting](/concepts/few-shot-prompting.md) design and [token cost](/concepts/token-cost.md) trade-offs in evaluation-driven prompt work.

## Quality

Practitioner blog post by Devlin Liles. Single-case evidence (20 seeded receipts) with concrete figures; the author states his generalizability caveats explicitly.

## Entities Mentioned

- None.

## Concepts Covered

- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — main topic; the number of exemplars and their content
- [token cost](/concepts/token-cost.md) — reduced by dropping redundant examples
