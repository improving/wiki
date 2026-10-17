---
title: "Policy Doc or Teams Message: Measuring Authority in a Knowledge Base"
type: "Source Summary"
description: "Authority is a source property that belongs in reranking; contradiction should be surfaced, not silently resolved by tier."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md"
---

# Policy Doc or Teams Message: Measuring Authority in a Knowledge Base — Summary

**Original source**: `references/devlinliles.com/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md`

## Summary

Retrieval finds the most relevant passages but not which to believe; an enterprise corpus states the same claim with wildly different authority. Authority is a property of the source and is mostly free to capture from existing metadata (system of origin, approval status, validity dates), the graph vector (a PageRank-like centrality score), and corroboration (independent agreement across sources). But static authority weighting can confidently suppress a correct, newer source, so contradictions should surface to a human rather than be auto-resolved.

## Key Claims

- Tag documents at ingestion with source system, governance/approval status, sign-off, and valid-from/valid-until dates, then bake that into the ranker.
- SharePoint approval workflows and Confluence "official versus working" spaces already carry this metadata.
- Centrality computed from the graph vector already built for multi-hop retrieval supplies a second authority signal; corroboration is distinct and should be tracked separately.
- The harder failure case is a stale policy doc outranking a correct Teams message, so authority alone can suppress the right answer with total confidence.
- Authority belongs in the cross-encoder reranker as a weight, not a hard filter; contradiction detection should put disagreements in front of a person.

## Relevance

Informs [corroboration](/concepts/corroboration.md), [reranking](/concepts/reranking.md), and enterprise retrieval authority design.

## Quality

Practitioner blog post by Devlin Liles. Grounded in two real project experiences (medical record timelines, healthcare documentation); reasoned design guidance rather than measured results.

## Entities Mentioned

- [SharePoint](/entities/sharepoint.md) — approval workflows as a source of authority metadata
- [Confluence](/entities/confluence.md) — official-versus-working spaces as authority metadata
- [PageRank](/entities/pagerank.md) — the analogy for graph-based centrality as authority

## Concepts Covered

- [Corroboration](/concepts/corroboration.md) — independent agreement as a distinct authority signal
- [Reranking](/concepts/reranking.md) — where authority belongs as a scoring weight
