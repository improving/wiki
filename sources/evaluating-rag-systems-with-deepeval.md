---
title: "Evaluating RAG Systems with DeepEval Metrics"
type: "Source Summary"
description: "Shows how to gate RAG systems with DeepEval's RAG Triad, walking a baseline-vs-candidate prompt comparison where a humorous prompt fails relevancy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, testing, improving.com]
sources:
  - "references/improving.com/evaluating-rag-systems-with-deepeval/evaluating-rag-systems-with-deepeval.md"
---

# Evaluating RAG Systems with DeepEval Metrics — Summary

**Original source**: `references/improving.com/evaluating-rag-systems-with-deepeval/evaluating-rag-systems-with-deepeval.md`

## Summary

RAG has two failure surfaces — the retriever can return the wrong chunks and the generator can ignore them — and manual spot-checking catches neither. The post shows how to grade RAG systems with DeepEval's three core metrics (the RAG Triad) as pass/fail quality gates, then runs a baseline-versus-candidate prompt comparison where a humorous candidate prompt fails answer relevancy.

## Key Claims

- Every DeepEval metric scores 0.0–1.0, uses per-metric pass/fail thresholds, extracts discrete claims and checks each against a reference, and reports a written reason plus verbose log.
- The RAG Triad is FaithfulnessMetric (grades the generator strictly), ContextualRecallMetric (grades the retriever), and AnswerRelevancyMetric (checks the generator stayed on topic); the demo uses thresholds of 0.80, 0.75, and 0.80.
- The gate is all-or-nothing: if any metric falls below its threshold, the test case and the pytest run fail.
- Rough score guide: 0.9–1.0 excellent, 0.8–0.9 good, 0.7–0.8 borderline, below 0.7 fail and block deployment.
- In the demo, baseline and candidate prompts retrieved the same three chunks and were graded against the same expected answer, so any difference came from the generator alone.
- The candidate prompt kept faithfulness and contextual recall at 1.00 but scored answer relevancy 0.75 (below 0.80), failing the run; one "no" verdict out of four extracted statements gave 3/4, while "idk" verdicts do not count against the score.
- Response options: revert to baseline, refine the candidate to keep humor but make every sentence progress the answer, or lower the answer-relevancy threshold to 0.70.
- Common issues: API key errors, LLM-as-judge variance near a threshold, and checking the verbose log when a score looks wrong.

## Relevance

Defines [RAG evaluation](/concepts/rag-evaluation.md) within [LLM evaluation](/concepts/llm-evaluation.md), using [model-as-judge](/concepts/model-as-judge.md) grading and [quality gates](/concepts/quality-gates.md) in CI.

## Quality

Hands-on practitioner walkthrough by Sarvani Yallapragada; concrete and reproducible via a public demo repo, though built on one worked example.

## Entities Mentioned

- [Sarvani Yallapragada](/entities/sarvani-yallapragada.md) — author
- [DeepEval](/entities/deepeval.md) — the evaluation framework used
- [Ragas](/entities/ragas.md) — sibling RAG evaluation library referenced
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [RAG evaluation](/concepts/rag-evaluation.md) — faithfulness, recall, relevancy scoring
- [LLM evaluation](/concepts/llm-evaluation.md) — continuous output-quality measurement
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — grounding answers in retrieved context
- [model-as-judge](/concepts/model-as-judge.md) — LLM scoring against a rubric
- [quality gates](/concepts/quality-gates.md) — thresholds that block a merge
- [evals as code](/concepts/evals-as-code.md) — versioned graders in the pipeline
- [golden dataset](/concepts/golden-dataset.md) — fixed fixture questions with expected answers
