---
title: "Skill Registry"
type: "Concept"
description: "A governed, reviewed catalog of agent skills — not just a Git folder of markdown files."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, agents, skills]
sources:
  - "/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md"
  - "/sources/call-twenty-five-the-skill-that-never-checked-its-own-data.md"
---

# Skill Registry

A skill registry is a governed catalog of agent skills: it verifies, versions, and owns the assets it lists. The corpus draws a hard line between a registry and a shared folder — a folder of skills is a shared drive, and without review gates, scope, evaluation, and monitoring it provides no authority to the agents that consume it.

## Key Claims

- A folder of skills is a shared drive, not a registry.
- Authors must not approve their own skills; separation of duties is the key rule.
- New skills must be evaluated alone and alongside the existing library.
- Production must pin versions and ground skills in governed data sources.
- A registry-level freshness and lineage check flags ungrounded output — one skill kept emitting confident numbers from data frozen by a silent ETL failure across twenty-five calls.
- A last-known-good fallback degrades gracefully instead of refusing outright.

## Related

- [Review Gate](/concepts/review-gate.md) — the gate that turns a folder into a registry
- [Version Pinning](/concepts/version-pinning.md) — required for production skill use
- [Runtime Lineage](/concepts/runtime-lineage.md) — backs the freshness check that flags stale output
- [Data Governance](/concepts/data-governance.md) — the grounding sources skills must draw from
- [Quality Gates](/concepts/quality-gates.md) — evaluation checkpoints before promotion
- [A Skill Registry Needs a Review Gate, Not Just a Folder](/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md) — primary source
- [Call Twenty-Five - The Skill That Never Checked Its Own Data](/sources/call-twenty-five-the-skill-that-never-checked-its-own-data.md) — primary source
