---
title: "RAG evaluation"
type: "Concept"
description: "Scoring retrieval-augmented generation on faithfulness, context recall, and answer relevance against thresholds."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, testing, retrieval]
sources:
  - "/sources/evaluating-rag-systems-with-deepeval.md"
  - "/sources/llm-evaluation-ai-native-applications.md"
  - "/sources/building-prompt-evaluation-habit.md"
---

# RAG evaluation

RAG evaluation scores [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) on faithfulness, context recall, and answer relevance against pass/fail thresholds, because RAG has two failure surfaces — the retriever can return the wrong chunks and the generator can ignore them — and manual spot-checking catches neither. The RAG Triad turns each metric into a CI quality gate: if any metric falls below its threshold, the run fails.

## Key Claims

- The RAG Triad is FaithfulnessMetric (grades the generator strictly), ContextualRecallMetric (grades the retriever), and AnswerRelevancyMetric (checks the generator stayed on topic).
- Every metric scores 0.0–1.0 with per-metric thresholds; a worked example uses 0.80, 0.75, and 0.80, and the gate is all-or-nothing.
- A rough score guide: 0.9–1.0 excellent, 0.8–0.9 good, 0.7–0.8 borderline, and below 0.7 fails and blocks deployment.
- Metrics extract discrete claims and check each against a reference, reporting a written reason plus a verbose log.
- In the demo, a humorous candidate prompt kept faithfulness and recall at 1.00 but scored answer relevancy 0.75 (below 0.80), failing the run.
- Response options when a gate fails: revert to baseline, refine the prompt so every sentence progresses the answer, or lower the threshold deliberately.
- Watch LLM-as-judge variance near a threshold, and check the verbose log when a score looks wrong.

## Related

- [LLM evaluation](/concepts/llm-evaluation.md) — the broader measurement discipline
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — the system being scored
- [Model-as-judge](/concepts/model-as-judge.md) — the grading mechanism
- [Quality Gates](/concepts/quality-gates.md) — thresholds that block a merge
- [evals-as-code](/concepts/evals-as-code.md) — versioned graders in the pipeline
- [Reranking](/concepts/reranking.md) — a lever on context recall
- [Golden Dataset](/concepts/golden-dataset.md) — fixed fixture questions with expected answers
