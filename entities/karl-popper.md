---
title: "Karl Popper"
type: "Entity"
description: "Philosopher of science whose falsifiability criterion anchors this corpus's critique of unfalsifiable AI benchmarks and evals."
created: '2026-10-17'
updated: '2026-10-17'
tags: [philosophy, science, evaluation]
sources:
  - "/sources/ai-evals-have-a-replication-problem.md"
  - "/sources/your-ai-benchmark-is-not-science-until-it-can-fail.md"
---

# Karl Popper

Karl Popper is the philosopher of science who argued that a claim is scientific only if it is falsifiable. This corpus applies that criterion directly to AI evaluation, arguing most benchmark-based capability claims have become unfalsifiable through saturation and contamination.

## Key Claims

- A claim is scientific only if it is falsifiable, per Popper.
- MMLU saturated above 88-90 percent, making score gaps statistically meaningless.
- Contamination inflates scores; decontamination removes about 23 percent of MMLU inflation.
- Published benchmark scores hide the exact prompts, parameters, and test selection that produced them.
- Model drift means a score describes weights that may no longer exist.

## Work

Popper's falsifiability standard drives two prescriptions: build internal, falsifiable eval suites from real use cases, and maintain persistent eval suites against pinned model versions rather than ad hoc runs. Organizations should treat a benchmark that cannot fail as marketing, not evidence.

## Related

- [John Searle](/entities/john-searle.md) — another philosophical critique of behavioral AI evidence
- [Benchmark Saturation](/concepts/benchmark-saturation.md) — the mechanism that makes scores unfalsifiable
- [Replication Crisis](/concepts/replication-crisis.md) — the evidential failure Popper's standard predicts
- [Version Pinning](/concepts/version-pinning.md) — the remedy for drift in eval results
- [Your AI Benchmark Is Not Science Until It Can Fail](/sources/your-ai-benchmark-is-not-science-until-it-can-fail.md) — primary source
