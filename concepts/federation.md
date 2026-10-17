---
title: "federation"
type: "Concept"
description: "Cross-organization discovery via published, self-reported catalogs — a partial answer that still needs registry and governance layers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [discovery, governance, catalogs]
sources:
  - "/sources/off-the-shelf-gets-you-partway-there.md"
  - "/sources/publishing-a-catalog-is-not-the-same-as-running-a-registry.md"
---

# federation

Federation is an approach to discovery in which each domain publishes its own catalog and consumers crawl across boundaries to find assets. Across this corpus it is framed as necessary but insufficient: it answers cross-org discovery while leaving verification, enrichment, and governance unsolved.

## Key Claims

- [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) federates self-reported metadata via `ai-catalog.json` crawled from domain-owned files.
- Federation answers cross-boundary discovery but is not a registry; crawled catalogs are static and need enrichment.
- Over 2,500 Claude Code plugin marketplaces exist with no trust authority, illustrating the discovery-without-authority failure.
- Documents and skills fail discovery for the same structural reason, so the gap is not unique to any asset type.
- Google ships a proprietary governance layer that the open specification omits, leaving the hard part unstandardized.
- The goal is one governed catalog answering three questions: is it current, is it owned, is it safe to use.

## Related

- [Skill Discovery](/concepts/skill-discovery.md) — the discovery problem federation addresses for skills
- [Skill Registry](/concepts/skill-registry.md) — the governed layer beyond federated catalogs
- [trust infrastructure](/concepts/trust-infrastructure.md) — the authority federation alone does not provide
- [Agentic Resource Discovery](/entities/agentic-resource-discovery.md) — the specification implementing federated discovery
- [Publishing a Catalog Is Not the Same as Running a Registry](/sources/publishing-a-catalog-is-not-the-same-as-running-a-registry.md) — primary source
