---
title: "SharePoint"
type: "Entity"
description: "Microsoft's enterprise content platform, used in this corpus as a testbed for authority-aware, permission-filtered retrieval."
created: '2026-10-17'
updated: '2026-10-17'
tags: [microsoft, enterprise, retrieval, knowledge-base]
sources:
  - "/sources/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md"
  - "/sources/the-architecture-of-enterprise-ai-retrieval.md"
  - "/sources/the-six-vectors-and-the-reranker-that-actually-matters.md"
---

# SharePoint

SharePoint is Microsoft's enterprise content and collaboration platform, and this corpus treats it as the canonical messy knowledge base against which enterprise retrieval must be measured.

## Overview

The core problem: relevance does not measure believability, so a Teams message can outrank a policy doc. Authority is a property of the source, largely available from existing metadata, and graph centrality propagates trust much like PageRank propagates web importance — though corroboration across independent witnesses differs from structural authority. Retrieval should therefore be a sequence of distinct gates: permissions hard-exclude before scoring, hybrid search plus a cross-encoder reranker is baseline rather than a differentiator, and validity belongs on the fact, not the document.

## Key Claims

- Relevance does not measure believability; authority must be captured separately
- Permissions must hard-exclude before scoring; tags should soft-boost to cost precision
- Hybrid search plus a cross-encoder reranker is baseline, not a differentiator
- A static trust score can confidently suppress a stale-but-correct source
- Contradictions should be surfaced rather than auto-resolved

## Related

- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — hard-exclude before scoring
- [hybrid retrieval](/concepts/hybrid-retrieval.md) — keyword plus dense baseline
- [cross-encoder reranker](/concepts/cross-encoder-reranker.md) — the addition that matters most
- [Corroboration](/concepts/corroboration.md) — independent-witness agreement
- [Microsoft](/entities/microsoft.md) — the platform's owner
- [The Architecture of Enterprise AI Retrieval](/sources/the-architecture-of-enterprise-ai-retrieval.md) — primary source
