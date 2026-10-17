---
title: "Time Is Not a Timestamp: Fixing Temporal and Graph Retrieval"
type: "Source Summary"
description: "Temporal and graph retrieval need fact-level validity and traced graph edges, with the temporal layer running first."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval.md"
---

# Time Is Not a Timestamp: Fixing Temporal and Graph Retrieval — Summary

**Original source**: `references/devlinliles.com/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval/time-is-not-a-timestamp-fixing-temporal-and-graph-retrieval.md`

## Summary

Devlin Liles argues that two of the six retrieval vectors in a hybrid knowledge system — temporal and graph — behave unlike the rest and are most often mishandled. Temporal retrieval must treat validity as a property of the fact, not the document, because a 2018 regulation can stay valid until a 2022 amendment and a 2023 report can describe a 2020 incident. Graph retrieval earns its cost only for multi-hop, cross-document questions, and it must run after fact-level validity, since traversing through an expired fact yields an answer that is structurally sound and factually wrong.

## Key Claims

- Scoring relevance off a document's publish date confidently retrieves superseded documents; capture fact-level valid-from and valid-until at ingestion instead.
- The practical fix is a reranking step that hard-removes expired facts, boosts explicitly time-bounded facts, and falls back to recency decay only when nothing specific applies — recency decay is the fallback, not the strategy.
- Graph retrieval pays off for multi-hop questions and cross-document synthesis, not single-fact lookups or narrow structured domains.
- Graph traversal gets less discriminative as corpora grow, with gains plateauing once a corpus crosses roughly five to fifteen million tokens.
- A lighter open knowledge graph plus personalized PageRank seeded from query entities lands roughly ten to thirty times cheaper than full community-detection GraphRAG on multi-hop QA.

## Relevance

Central to [temporal retrieval](/concepts/temporal-retrieval.md); it also informs [knowledge graph](/concepts/knowledge-graph.md) design and [reranking](/concepts/reranking.md) within [RAG](/concepts/retrieval-augmented-generation.md).

## Quality

Practitioner blog post by Devlin Liles. Grounded in concrete build experience and named cost ratios; the ten-to-thirty-times figure is his own estimate rather than a published benchmark.

## Entities Mentioned

- [PageRank](/entities/pagerank.md) — personalized PageRank used as a cheaper multi-hop traversal

## Concepts Covered

- [temporal retrieval](/concepts/temporal-retrieval.md) — fact-level validity over document dates
- [knowledge graph](/concepts/knowledge-graph.md) — reasoning substrate with references back to source clauses
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the six-vector system these two belong to
- [Reranking](/concepts/reranking.md) — where expired-fact removal and time-boosting run
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — the dominant read-only pattern being extended
