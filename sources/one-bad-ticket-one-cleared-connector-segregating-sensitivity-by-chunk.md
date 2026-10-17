---
title: "One Bad Ticket, One Cleared Connector - Segregating Sensitivity by Chunk"
type: "Source Summary"
description: "Connector-level sensitivity flags leak embedded PII; classifying and gating permission per chunk drops the PII-in-citation rate to zero."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, devlinliles.com]
sources:
  - "references/devlinliles.com/one-bad-ticket-one-cleared-connector-segregating-sensitivity-by-chunk/one-bad-ticket-one-cleared-connector-segregating-sensitivity-by-chunk.md"
---

# One Bad Ticket, One Cleared Connector - Segregating Sensitivity by Chunk — Summary

**Original source**: `references/devlinliles.com/one-bad-ticket-one-cleared-connector-segregating-sensitivity-by-chunk/one-bad-ticket-one-cleared-connector-segregating-sensitivity-by-chunk.md`

## Summary

A HelpDesk Copilot RAG assistant assigned one permissioning decision per connector, so a tickets connector marked "cleared" indexed all 40 seeded tickets — including a handful with pasted fake SSNs and card fragments. Running 20 queries, the PII-in-citation rate came back above zero because nothing inspected individual ticket content. The fix moves the unit of decision from the connector to the chunk: each retrieved chunk is classified for embedded PII at ingestion, and a per-chunk [permission pre-filter](/concepts/permission-pre-filtering.md) runs after retrieval and before generation.

## Key Claims

- Connector-level flags can correctly mark a wholly sensitive source off-limits yet fail the moment a mostly-clean source hides one sensitive document.
- Per-chunk classification plus a per-chunk filter after retrieval dropped the PII-in-citation rate to 0% across all three connectors.
- The fix is granular, not wholesale: the other 39 non-sensitive tickets still retrieved and answered correctly.
- This matches broader [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) security guidance (Elastic Labs, Protecto.ai, 2026) that sensitivity resolves per-record or per-chunk.
- The mechanism solves the granularity half only; a 2026 clinical benchmark found F1 for the same detector dropping from ~0.81 on general text to 0.41 on clinical text.

## Relevance

Informs [permission pre-filtering](/concepts/permission-pre-filtering.md) and [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) security, and the wiki's least-privilege and data-governance themes.

## Quality

Practitioner blog post by Devlin Liles. Concrete before/after measurement on a synthetic dataset; the regex classifier is explicitly a stand-in and the F1 shift shows detection accuracy, not the gating pattern, is the real limitation.

## Entities Mentioned

- None.

## Concepts Covered

- [Permission Pre-Filtering](/concepts/permission-pre-filtering.md) — per-chunk gating after retrieval, before generation
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — the retrieval pipeline where the leak occurs
