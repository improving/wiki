---
title: "Ragas"
type: "Entity"
description: "RAG evaluation library cited here as a reference-free metrics library and a sibling to DeepEval."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, evaluation, rag]
sources:
  - "/sources/llm-evaluation-ai-native-applications.md"
  - "/sources/evaluating-rag-systems-with-deepeval.md"
---

# Ragas

Ragas is a RAG evaluation library that appears in this corpus as one of the standard tools for scoring retrieval-augmented generation. It is characterized as a reference-free metrics library, meaning it can grade RAG outputs without a hand-labeled expected answer for every case.

## Role in the Corpus

- The LLM evaluation survey names Ragas as a reference-free RAG metrics library, alongside lm-evaluation-harness, [DeepEval](/entities/deepeval.md), Promptfoo, Langfuse, Arize Phoenix, Evidently, Giskard, and [LangSmith](/entities/langsmith.md).
- The DeepEval RAG walkthrough references Ragas as a sibling RAG evaluation library, positioning the two as alternatives for the same job of grading faithfulness, recall, and relevance.
- Both tools sit inside the shift from deterministic assertions to continuous quality evaluation, where the question becomes "is this output good enough?" rather than "did I get exactly this output?".

## Related

- [RAG evaluation](/concepts/rag-evaluation.md) — the metrics Ragas provides
- [LLM evaluation](/concepts/llm-evaluation.md) — the wider discipline
- [DeepEval](/entities/deepeval.md) — the sibling framework
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — the pattern being graded
