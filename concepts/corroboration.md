---
title: "Corroboration"
type: "Concept"
description: "Independent confirmation that lets an unverified fact earn its way up to action-worthy status."
created: '2026-10-17'
updated: '2026-10-17'
tags: [trust, knowledge-base, verification]
sources:
  - "/sources/a-users-guess-and-a-sensors-reading-filed-the-same-way.md"
  - "/sources/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md"
---

# Corroboration

Corroboration is confirmation of a fact by independent witnesses, distinct from the structural authority a source carries by virtue of who published it or where it sits in a graph. It matters because knowledge systems need a way to let an unverified claim earn its way up to action-worthy status without a guess being treated like a sensor reading.

## Key Claims

- A fact table with no provenance lets a user's guess act like a sensor reading.
- Every fact should be tagged with its source and verification status at write time, not later.
- Corroboration lets an unverified fact earn its way up to action-worthy.
- Corroboration across independent witnesses differs from structural authority.
- Authority is largely a property of the source and can be derived mostly free from existing metadata; graph centrality propagates trust like PageRank propagates web importance.
- A static trust score can confidently suppress a stale-but-correct source, so contradictions should be surfaced rather than auto-resolved.

## Related

- [trusted signals](/concepts/trusted-signals.md) — facts reliable enough to act on
- [trust infrastructure](/concepts/trust-infrastructure.md) — the system that records provenance
- [PageRank](/entities/pagerank.md) — the analogy for propagating authority
- [A User's Guess and a Sensor's Reading](/sources/a-users-guess-and-a-sensors-reading-filed-the-same-way.md) — provenance-at-write-time source
- [Policy Doc or Teams Message](/sources/policy-doc-or-teams-message-measuring-authority-in-a-knowledge-base.md) — authority measurement source
