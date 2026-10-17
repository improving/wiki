---
title: "The Architecture of Enterprise AI Retrieval"
type: "Source Summary"
description: "Naive RAG fails five identical ways; retrieval should be a sequence of gates, each with its own failure mode and acceptable direction of error."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/the-architecture-of-enterprise-ai-retrieval/the-architecture-of-enterprise-ai-retrieval.md"
---

# The Architecture of Enterprise AI Retrieval — Summary

**Original source**: `references/devlinliles.com/the-architecture-of-enterprise-ai-retrieval/the-architecture-of-enterprise-ai-retrieval.md`

## Summary

The post argues that enterprise "semantic search" requests are really pipeline problems, and that naive RAG fails in five identical ways across domains: permissions as post-filter, unscored authority, oversaturation from added vectors, document dates used as fact validity, and flat knowledge graphs that cannot reason. It prescribes treating retrieval as a sequence of gates, each with its own failure mode and acceptable direction of error — a hard permission gate first, a soft tag boost, authority and corroboration as reranker features, fact-level validity, and a textbook-structured graph — with one catalog serving both the human and machine clocks.

## Key Claims

- Hybrid search plus a cross-encoder reranker is now the baseline; the differentiator is gating, not the presence of a reranker.
- Production recall@10: BM25 ~65%, dense vectors ~75–80%, combined 88–92%; Anthropic's contextual retrieval cuts top-20 failures 35% with chunking, 49% with BM25+RRF, 67% with a reranker.
- Permissions must be a hard pre-filter; tags should soft-boost, because a wrong hard-exclude costs the correct answer entirely.
- "Lost in the middle" degrades mid-context performance by more than 30%, so a fixed budget of three to ten passages should reach the model.
- Validity belongs to the fact, not the document; a flat knowledge graph should be sequenced like a textbook; one catalog should serve both the human and machine clocks.

## Relevance

Core to enterprise [hybrid retrieval](/concepts/hybrid-retrieval.md), [cross-encoder reranking](/concepts/cross-encoder-reranker.md), [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md), and [permission pre-filtering](/concepts/permission-pre-filtering.md), touching [semantic search](/concepts/semantic-search.md), [keyword search](/concepts/keyword-search.md), [temporal retrieval](/concepts/temporal-retrieval.md), [knowledge graphs](/concepts/knowledge-graph.md), [lost in the middle](/concepts/lost-in-the-middle.md), [retrieval oversaturation](/concepts/retrieval-oversaturation.md), [active metadata](/concepts/active-metadata.md), and [corroboration](/concepts/corroboration.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: drawn from three production builds across unrelated domains, with cited recall figures and a composed architecture diagram. Caveats: some numbers are vendor-published and the piece is a broad synthesis.

## Entities Mentioned

- [Unity Catalog](/entities/unity-catalog.md) — Databricks widened it to cover models, agents, and MCP services
- [Microsoft Entra Agent ID](/entities/microsoft-entra-agent-id.md) — gives agents an identity principal inside the identity system
- [Microsoft Purview](/entities/microsoft-purview.md) — extends audit trails to prompt chains and tool calls
- [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) — a cross-boundary catalog spec that feeds, but does not replace, the graph
- [SharePoint](/entities/sharepoint.md) — an example of existing approval metadata that can signal authority
- [Anthropic](/entities/anthropic.md) — source of the published contextual-retrieval failure-reduction figures

## Concepts Covered

- [hybrid retrieval](/concepts/hybrid-retrieval.md) — the baseline combination of vectors
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the highest-leverage single addition, and where authority is built in
- [reciprocal rank fusion](/concepts/reciprocal-rank-fusion.md) — fusing incompatible vector scores at k=60
- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — permissions as a hard gate before scoring
- [Semantic Search](/concepts/semantic-search.md) — strong on meaning, weak on proper nouns and citations
- [Keyword Search](/concepts/keyword-search.md) — BM25 covering semantic search's gaps
- [temporal retrieval](/concepts/temporal-retrieval.md) — validity as a property of the fact, not the document
- [knowledge graph](/concepts/knowledge-graph.md) — structured like a textbook, not a flat warehouse
- [Lost in the middle](/concepts/lost-in-the-middle.md) — why a fixed passage budget is the fix for saturation
- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — every vector must earn its place
- [Active Metadata](/concepts/active-metadata.md) — the catalog as a live control plane
- [Corroboration](/concepts/corroboration.md) — independent witnesses as a distinct authority signal

## Related Sources

- [Permissions Are Not Tags: The Pre-Filter Problem Nobody Names](/sources/permissions-are-not-tags-the-pre-filter-problem-nobody-names.md)
