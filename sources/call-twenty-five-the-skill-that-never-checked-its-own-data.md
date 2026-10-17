---
title: "Call Twenty-Five - The Skill That Never Checked Its Own Data"
type: "Source Summary"
description: "A bug-free reporting skill still returned stale numbers; a source-freshness check in the skill registry fixes it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/call-twenty-five-the-skill-that-never-checked-its-own-data/call-twenty-five-the-skill-that-never-checked-its-own-data.md"
---

# Call Twenty-Five - The Skill That Never Checked Its Own Data — Summary

**Original source**: `references/devlinliles.com/call-twenty-five-the-skill-that-never-checked-its-own-data/call-twenty-five-the-skill-that-never-checked-its-own-data.md`

## Summary

A financial-reporting skill, generate-quarterly-variance-summary, was never buggy, yet across fifty sequential calls a silent ETL failure at call twenty-five froze its data mart. Every later report looked identical to a healthy one—100% silent staleness. Liles' fix leaves the skill's calculation logic untouched: its registry entry names the data source it depends on, and before returning output it checks that source's governance record for last-verified time and current lineage certification.

## Key Claims

- The skill inherited its trustworthiness from a source it never checked, so nothing in its own logic could notice the source had stopped updating.
- When the source misses its freshness SLA or loses lineage certification, the skill returns a flagged response ("ungrounded, source stale") and points to the last known-good governed output.
- Replayed against the same call-twenty-five failure, all twenty-five affected calls were correctly flagged at the moment the source went bad.
- The freshness SLA belongs to the data source's owner, not the skill's author; set too strict, it trains everyone to ignore the warning.
- The check covers declared external source freshness only—not drift in the skill's own procedural logic or business rules.

## Relevance

Extends [skill registry](/concepts/skill-registry.md) governance and speaks directly to [quiet drift](/concepts/quiet-drift.md) in agent data dependencies.

## Quality

Practitioner blog post by Devlin Liles. Clear scenario and mechanism with an explicit stated limitation; based on a constructed replay rather than production measurement.

## Entities Mentioned

- None.

## Concepts Covered

- [Skill Registry](/concepts/skill-registry.md) — carries the source dependency and freshness check
- [Quiet Drift](/concepts/quiet-drift.md) — the silent staleness the skill could not detect
