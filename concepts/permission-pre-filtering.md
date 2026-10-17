---
title: "Permission Pre-Filtering"
type: "Concept"
description: "Hard-excluding candidates the caller cannot access before scoring, keeping probabilistic tags out of the exclusion path."
created: '2026-10-17'
updated: '2026-10-17'
tags: [retrieval, governance, access-control]
sources:
  - "/sources/permissions-are-not-tags-the-pre-filter-problem-nobody-names.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
---

# Permission Pre-Filtering

Permission pre-filtering removes every candidate a caller is not authorized to see *before* relevance scoring runs, rather than filtering results afterward. It matters because permission checks and metadata tags fail in opposite directions: an authorization lookup has exactly one acceptable failure mode, while a tag classifier is wrong some fraction of the time.

## Key Claims

- Permission checks are deterministic lookups with one acceptable failure direction; tag filtering depends on an LLM classifier that is wrong some fraction of the time.
- A misclassified tag should soft-boost a candidate, never hard-exclude it — hard-excluding on tags silently drops correct answers.
- Permissions must hard-exclude before scoring; tags should soft-boost to cost precision, not recall.
- Naive RAG fails the same five ways: permissions, authority, oversaturation, time, and structure.
- Filtering systems fail when the underlying candidate pool is mostly empty.

## Related

- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — the pipeline this gate protects
- [Reranking](/concepts/reranking.md) — runs after the permission gate
- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — the failure mode a mostly-empty pool exposes
- [Least privilege](/concepts/least-privilege.md) — the access principle behind hard exclusion
- [The Architecture of Enterprise AI Retrieval](/sources/the-architecture-of-enterprise-ai-retrieval.md) — primary source
