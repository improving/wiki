---
title: "DeepEval"
type: "Entity"
description: "LLM evaluation framework whose RAG Triad metrics gate RAG systems in CI as pass/fail quality checks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, evaluation, testing]
sources:
  - "/sources/evaluating-rag-systems-with-deepeval.md"
  - "/sources/llm-evaluation-ai-native-applications.md"
---

# DeepEval

DeepEval is a pytest-style LLM evaluation framework whose RAG Triad metrics turn retrieval-augmented generation quality into pass/fail gates. It appears in this corpus as the concrete tool for enforcing [RAG evaluation](/concepts/rag-evaluation.md) inside CI.

## Role in the Corpus

- Every DeepEval metric scores 0.0–1.0, uses per-metric pass/fail thresholds, extracts discrete claims and checks each against a reference, and reports a written reason plus verbose log.
- The RAG Triad is FaithfulnessMetric (grades the generator strictly), ContextualRecallMetric (grades the retriever), and AnswerRelevancyMetric (checks the generator stayed on topic); a worked demo uses thresholds of 0.80, 0.75, and 0.80.
- The gate is all-or-nothing: if any metric falls below its threshold, the test case and the pytest run fail. A rough score guide runs 0.9–1.0 excellent, 0.8–0.9 good, 0.7–0.8 borderline, below 0.7 fail and block deployment.
- In the demo, baseline and candidate prompts retrieved the same three chunks, so any difference came from the generator alone; a humorous candidate kept faithfulness and contextual recall at 1.00 but scored answer relevancy 0.75, failing the run.
- The broader LLM-evaluation survey lists DeepEval among the evaluation frameworks, noting most production setups combine at least three tools.

## Related

- [RAG evaluation](/concepts/rag-evaluation.md) — the metrics DeepEval implements
- [LLM evaluation](/concepts/llm-evaluation.md) — the wider discipline
- [model-as-judge](/concepts/model-as-judge.md) — the LLM grading it relies on
- [quality gates](/concepts/quality-gates.md) — thresholds that block a merge
- [Ragas](/entities/ragas.md) — the sibling RAG evaluation library
