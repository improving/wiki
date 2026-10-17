---
title: "Interpretability"
type: "Concept"
description: "Understanding why a model produces an output, as distinct from observing that its behavior looks correct."
created: '2026-10-17'
updated: '2026-10-17'
tags: [models, explainability, governance]
sources:
  - "/sources/a-few-neurons-decide-whether-your-agent-calls-the-right-tool.md"
  - "/sources/black-box-ai-fails-webers-test.md"
  - "/sources/classical-statistics-vs-machine-learning-a-practical-distinction.md"
  - "/sources/read-the-paper-not-the-panel.md"
  - "/sources/the-chinese-room-is-running-in-production.md"
  - "/sources/the-interpretability-audit-you-cant-run-yet.md"
---

# Interpretability

Interpretability is the ability to explain *why* a model produced an output, as opposed to observing that its behavior looks correct. Across this corpus it is treated as an architecture requirement rather than a compliance checkbox: black-box neural networks cannot supply the articulable justifications that regulated domains demand, and behavioral scores can diverge from causal reliability on novel inputs.

## Key Claims

- Tool-calling failures trace to a narrow, locatable set of neurons; evals diagnose errors after the fact and prompts only bias probabilities, so the real levers are targeted fine-tuning, activation steering, or base-model choice.
- Weber's rational-legal authority requires decisions justifiable by articulable rules, and post-hoc XAI explanations can be plausible yet unfaithful to the model's actual process.
- Interpretability findings do not transfer across models: a refusal-residue probe hit AUROC 0.87 on Llama but collapsed to 0.43 on Qwen, so it cannot yet serve as an auditor-grade control.
- Behavioral benchmark scores and causal reliability on novel inputs are diverging; GPT-5.6 Sol scored 7.8% on ARC-AGI-3, still failing over 92% of tasks.
- Optimizing behavioral correctness at the expense of interpretability compounds the problem, so evaluation should target distribution shift, calibration, and graceful incompetence.
- The classical-statistics versus machine-learning choice is deliberate: classical statistics needs hypothesized relationships and mathematical guarantees, while ML learns rules from labeled data and can fail at scale on biased or unrepresentative data.

## Related

- [Calibration](/concepts/calibration.md) — stated confidence versus accuracy
- [Distribution shift](/concepts/distribution-shift.md) — where behavioral scores break down
- [Benchmark Validity](/concepts/benchmark-validity.md) — separating a finding from its framing
- [Symbolic AI](/concepts/symbolic-ai.md) — rule-based systems with articulable logic
- [Hallucination](/concepts/hallucination.md) — competence without understanding
- [The Interpretability Audit You Can't Run Yet](/sources/the-interpretability-audit-you-cant-run-yet.md) — primary source
