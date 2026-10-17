---
title: "The Free Half of Speculative Decoding"
type: "Source Summary"
description: "Quantizing the draft model in speculative decoding is nearly free, while quantizing the target model costs real accuracy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, other, devlinliles.com]
sources:
  - "references/devlinliles.com/the-free-half-of-speculative-decoding/the-free-half-of-speculative-decoding.md"
---

# The Free Half of Speculative Decoding — Summary

**Original source**: `references/devlinliles.com/the-free-half-of-speculative-decoding/the-free-half-of-speculative-decoding.md`

## Summary

A technical report from Nota Inc., part of an efficiency competition built around Qwen3.5-4B on a single 24GB NVIDIA A10G, shows that speculative decoding has two halves that carry very different risk. Quantizing the target to INT4 with AWQ plus quantization-aware distillation produced 2.16x over the BF16 baseline; adding a quantized draft model with a sliding-window attention trim reached 3.57x in the authors' ablation, with 6.978x on the official leaderboard. The asymmetry: the draft model never gets the final word, so a worse drafter only produces more rejected guesses.

## Key Claims

- Target-only INT4 (AWQ) plus quantization-aware distillation: 2.16x over the BF16 baseline.
- Adding the quantized draft plus sliding-window attention trim: 3.57x in ablation; 6.978x on the competition leaderboard, measured on the A10G.
- The quantized draft model's mean acceptance length moved only 5.03 to 4.98 across three benchmarks — a rounding error, not a tradeoff.
- Raw INT4 on the target dropped IFEval below the competition's quality gate before correction, and the shipped system still trails BF16 on MMLU-Pro, IFEval, and GPQA-Diamond.
- The narrow setting — one 24GB card, a 4B model — matches the constrained environments most clients actually deploy into.

## Relevance

Informs [speculative decoding](/concepts/speculative-decoding.md) and inference efficiency for [open-weight models](/concepts/open-weight-models.md) on owned hardware.

## Quality

Practitioner blog post by Devlin Liles. Strengths: specific numbers tied to a named paper and competition; caveat: single-paper, leaderboard-based evidence, and the speedup figures come from illustrative charts.

## Entities Mentioned

- None.

## Concepts Covered

- [Speculative Decoding](/concepts/speculative-decoding.md) — quantizing the draft vs. target model
- [Open-Weight Models](/concepts/open-weight-models.md) — the constrained, self-hosted deployment context
