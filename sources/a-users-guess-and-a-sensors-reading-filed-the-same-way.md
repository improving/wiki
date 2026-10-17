---
title: "A User's Guess and a Sensor's Reading, Filed the Same Way"
type: "Source Summary"
description: "Tagging facts with source and verification status at write time lets a remediation agent gate actions by how well-founded each fact is."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/a-users-guess-and-a-sensors-reading-filed-the-same-way/a-users-guess-and-a-sensors-reading-filed-the-same-way.md"
---

# A User's Guess and a Sensor's Reading, Filed the Same Way — Summary

**Original source**: `references/devlinliles.com/a-users-guess-and-a-sensors-reading-filed-the-same-way/a-users-guess-and-a-sensors-reading-filed-the-same-way.md`

## Summary

The author built an IT helpdesk remediation agent ingesting facts from three sources of wildly different reliability: end-user self-reports, device telemetry, and admin confirmations. The first version wrote all three to one fact table with no provenance or verification columns, so the remediation step treated a user's guess with the same authority as a verified sensor reading. Across a hundred-case sample, roughly a third of user self-reports were wrong about the actual cause, yet disk-cleanup remediations ran on guesses just as readily as on genuinely low-disk devices. The fix tags every fact with source and verification status at write time.

## Key Claims

- Source records origin (user-reported, telemetry, admin-verified); verification status records how much anyone has checked it (unverified, corroborated, verified), both set in the same transaction as the fact.
- The remediation step reads status before acting: an unverified self-report can trigger a diagnostic or a telemetry check but cannot directly authorize a remediation reserved for corroborated or verified facts.
- [Corroboration](/concepts/corroboration.md) is the mechanism letting an unverified fact earn its way up when an independent source confirms it.
- An over-caution rate must be tracked alongside remediation-appropriateness; a gate that blocks everything looks good on the first metric and bad on the second.
- Provenance tagging fails the moment an attacker can make a planted fact arrive through the legitimate channel, and corroboration fails when two "independent" sources read the same underlying feed.

## Relevance

Informs [corroboration](/concepts/corroboration.md) and [trusted signals](/concepts/trusted-signals.md) in agent pipelines, and connects to [data governance](/concepts/data-governance.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: a concrete before/after design with a measured one-third error rate and an explicit anti-over-caution metric. Caveats: single hundred-case sample; the trust-boundary and shared-feed weaknesses are acknowledged as unsolved.

## Entities Mentioned

- None.

## Concepts Covered

- [corroboration](/concepts/corroboration.md) — a second independent source letting an unverified fact earn action-worthiness
