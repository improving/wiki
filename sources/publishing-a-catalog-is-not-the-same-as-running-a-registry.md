---
title: "Publishing a Catalog Is Not the Same as Running a Registry"
type: "Source Summary"
description: "Agentic Resource Discovery solves cross-boundary federation, but a crawled catalog is not a governed, health-checked registry."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/publishing-a-catalog-is-not-the-same-as-running-a-registry/publishing-a-catalog-is-not-the-same-as-running-a-registry.md"
---

# Publishing a Catalog Is Not the Same as Running a Registry — Summary

**Original source**: `references/devlinliles.com/publishing-a-catalog-is-not-the-same-as-running-a-registry/publishing-a-catalog-is-not-the-same-as-running-a-registry.md`

## Summary

The post evaluates the Agentic Resource Discovery (ARD) specification as a shortcut to cross-organization capability discovery. ARD lets an organization publish an `ai-catalog.json` that a registry crawls and indexes, with domain ownership as the trust anchor and a hand-off to each tool's native protocol. The author argues this genuinely solves federation — discovery across a boundary neither party controls — but is not a registry: health checks, version pinning, authorization, and active-metadata enrichment still have to happen somewhere on the receiving end.

## Key Claims

- ARD was published June 17, 2026 by a coalition of eleven companies including Google, Microsoft, GitHub, Hugging Face, Cisco, and Databricks, with working implementations shipping the same day.
- The spec is "request-only": an agent asks, a registry answers from the last crawl, and nothing more is guaranteed.
- Google's own Agent Registry inside Gemini Enterprise adds namespaced identity, enforced egress policy, and version pinning — precisely what the open spec leaves out.
- A catalog entry is self-reported, batch-published metadata of the kind active metadata replaced in enterprise data catalogs.
- The data-mesh precedent applies: pure domain autonomy without a small, non-negotiable set of shared standards yields fragmentation dressed up as federation.

## Relevance

Informs [federation](/concepts/federation.md), [active metadata](/concepts/active-metadata.md), [data mesh](/concepts/data-mesh.md), [data catalogs](/concepts/data-catalog.md), [knowledge graphs](/concepts/knowledge-graph.md), [version pinning](/concepts/version-pinning.md), and [service discovery](/concepts/service-discovery.md).

## Quality

Practitioner blog post by Devlin Liles. A well-sourced analytical argument (vendor blogs, spec docs) with a clear thesis; it is opinionated and part of a series rather than an independent evaluation.

## Entities Mentioned

- [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) — the specification under discussion
- [Google](/entities/google.md) — coalition member; ships a proprietary governed registry layer
- [Hugging Face](/entities/hugging-face.md) — coalition member that published a launch post

## Concepts Covered

- [federation](/concepts/federation.md) — what ARD solves
- [Active Metadata](/concepts/active-metadata.md) — the enrichment a crawl-and-index model lacks
- [Data Mesh](/concepts/data-mesh.md) — precedent for federated governance tradeoffs
- [Data Catalog](/concepts/data-catalog.md) — the static catalog pattern being compared
- [knowledge graph](/concepts/knowledge-graph.md) — what a federation feed must feed into
- [Version Pinning](/concepts/version-pinning.md) — omitted by the open spec, added by Google's product
- [Service Discovery](/concepts/service-discovery.md) — DNS-era analogy for the unresolved gap

## Related Sources

- [One Catalog, Every Consumer](/sources/one-catalog-every-consumer.md)
