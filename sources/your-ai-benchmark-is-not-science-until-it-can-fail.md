---
title: "Your AI Benchmark Is Not Science Until It Can Fail"
type: "Source Summary"
description: "Benchmark scores are not evidence unless they can fail; saturation and contamination break falsifiability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/your-ai-benchmark-is-not-science-until-it-can-fail/your-ai-benchmark-is-not-science-until-it-can-fail.md"
---

# Your AI Benchmark Is Not Science Until It Can Fail — Summary

**Original source**: `references/devlinliles.com/your-ai-benchmark-is-not-science-until-it-can-fail/your-ai-benchmark-is-not-science-until-it-can-fail.md`

## Summary

The post applies Karl Popper's falsifiability criterion to AI benchmarks, arguing that most capability claims rest on tests that can no longer fail. Two failure modes — saturation and training-data contamination — undermine the benchmark as a falsifying test, and the field is entering an early replication crisis. The proposed fix is organization-specific internal eval suites drawn from real use cases and explicit failure modes, which can genuinely be passed or failed.

## Key Claims

- A claim is scientific only if falsifiable; astrology fails not for inaccuracy but because every failed prediction is reinterpreted rather than refuted.
- MMLU is saturated: frontier models cluster above 88–90%, making differences statistically meaningless, and a 2025 study found static QA/reasoning datasets plateau within two years of release.
- Contamination is measurable: a 57% exact match rate for ChatGPT predicting masked MMLU choices, with inference-time decontamination removing roughly 23% of MMLU score inflation.
- The ARC-AGI trajectory shows a treadmill: ARC-AGI-1 saturated above 96%; ARC-AGI-2 went from 0% at launch (March 2025) to 73–85% by April 2026; ARC-AGI-3 (March 2026) sits below 0.4% versus 100% for humans.
- The right question is whether a model performs adequately on the specific tasks and failure conditions of a given workflow — which requires building an internal eval suite, not reading vendor scores.

## Relevance

Informs [benchmark saturation](/concepts/benchmark-saturation.md), [benchmark validity](/concepts/benchmark-validity.md), and the [replication crisis](/concepts/replication-crisis.md) as they apply to AI evaluation and procurement.

## Quality

Practitioner blog post by Devlin Liles. Figures are traceable to cited papers but are given inline without links; the argument is conceptual rather than empirical, so the numbers are best treated as illustrative of a broader trend.

## Entities Mentioned

- [Karl Popper](/entities/karl-popper.md) — source of the falsifiability criterion the post applies
- [ChatGPT](/entities/chatgpt.md) — cited in the MMLU contamination findings

## Concepts Covered

- [Benchmark Saturation](/concepts/benchmark-saturation.md) — the first failure mode, when tests stop discriminating
- [Replication Crisis](/concepts/replication-crisis.md) — evaluation claims failing to reproduce across setups
- [Benchmark Validity](/concepts/benchmark-validity.md) — whether a benchmark measures the capability it claims
