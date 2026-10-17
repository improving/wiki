---
title: "LLM evaluation"
type: "Concept"
description: "Continuously measuring AI output quality with datasets, metrics, and CI gates, because AI failures are silent."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, testing, engineering]
sources:
  - "/sources/llm-evaluation-ai-native-applications.md"
  - "/sources/building-prompt-evaluation-habit.md"
  - "/sources/evaluating-rag-systems-with-deepeval.md"
  - "/sources/designing-ai-systems-for-change.md"
  - "/sources/openai-ai-monitoring-budgets.md"
---

# LLM evaluation

LLM evaluation is the continuous measurement of AI output quality with datasets, metrics, and CI gates, because AI failures are usually silent — the pipeline succeeds while the output is subtly wrong. The sources frame the shift from deterministic assertions ("did I get exactly this output?") to continuous quality evaluation ("is this output good enough?"), and stress that the real problem is measurement discipline, not tooling.

## Key Claims

- Five differences from traditional testing: the same input can produce different outputs, quality is multidimensional, small changes cause large behavioral shifts, systems degrade without code changes, and failures are usually silent.
- Validate beyond correctness: hallucination/factual accuracy, RAG retrieval quality, response quality (correctness, relevance, tone, format, safety), consistency, agent tool-path behavior, and prompt/model regression.
- Start with twenty real production failures rather than a thousand synthetic tasks, and convert every incident into a task before its fix merges.
- Approaches combine traditional tests, rule-based structural checks, LLM-as-a-judge (pin the judge prompt and model; watch position, verbosity, and self-preference bias), human evaluation as calibration anchor, and versioned automated evals.
- Most production setups use at least three tools; the landscape includes Ragas, DeepEval, Promptfoo, Langfuse, LangSmith, Arize Phoenix, Evidently, and Giskard.
- Models age faster than software: version and evaluate models, prompts, embeddings, and datasets, and upgrade only after testing and approval.
- Monitoring costs roughly 20% of monitored compute (OpenAI's disclosure) — a floor most enterprises budget nothing for.

## Related

- [RAG evaluation](/concepts/rag-evaluation.md) — the retrieval-specific slice
- [prompt evaluation](/concepts/prompt-evaluation.md) — treating prompts as testable code
- [evaluation harness](/concepts/evaluation-harness.md) — dataset, runner, and regression gate
- [Golden Dataset](/concepts/golden-dataset.md) — fixed labeled cases
- [evals-as-code](/concepts/evals-as-code.md) — versioned graders in CI
- [Model-as-judge](/concepts/model-as-judge.md) — LLM scoring against a rubric
- [AI monitoring](/concepts/ai-monitoring.md) — evaluation extended into production
