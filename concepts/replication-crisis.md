---
title: "Replication Crisis"
type: "Concept"
description: "The unreliability of published AI benchmark results when prompts, parameters, and test selection go undocumented."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evals, benchmarks, science]
sources:
  - "/sources/ai-evals-have-a-replication-problem.md"
  - "/sources/your-ai-benchmark-is-not-science-until-it-can-fail.md"
---

# Replication Crisis

The replication crisis in AI evals is the gap between a published benchmark score and the evidence behind it. Scores hide the prompts, parameters, and test selection that produced them, model weights drift, and saturation has made headline gaps statistically meaningless — so a number that cannot fail is not science.

## Key Claims

- A claim is scientific only if it is falsifiable, per Popper.
- Published benchmark scores hide the exact prompts, parameters, and test selection that produced them; any variation from the original setup drops consistency sharply.
- Model drift means a score describes weights that may no longer exist.
- MMLU saturated above 88–90%, making score gaps statistically meaningless; decontamination removes about 23% of MMLU inflation.
- Build internal, falsifiable eval suites from real use cases against pinned model versions.

## Related

- [Benchmark Validity](/concepts/benchmark-validity.md) — whether a score measures what it claims
- [Benchmark Saturation](/concepts/benchmark-saturation.md) — the ceiling that makes gaps meaningless
- [Model Drift Detection](/concepts/model-drift-detection.md) — tracking weights that move under a score
- [evals-as-code](/concepts/evals-as-code.md) — persistent suites instead of ad hoc runs
- [Prompt Engineering](/concepts/prompt-engineering.md) — undocumented prompts as the root cause
- [Your AI Benchmark Is Not Science Until It Can Fail](/sources/your-ai-benchmark-is-not-science-until-it-can-fail.md) — primary source
