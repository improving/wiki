---
title: "Review Gate"
type: "Concept"
description: "A governed registry requires a review gate with separation of duties, evaluation, version pinning, and grounding — not just a folder of skills."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, skills, registry]
sources:
  - "/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md"
  - "/sources/one-catalog-every-consumer.md"
---

# Review Gate

A review gate is the enforced checkpoint that turns a folder of artifacts into a governed registry. In this corpus it appears most sharply for agent skills: a Git repository of skills is a shared drive, not a registry, because nothing stops an author from merging their own unreviewed, possibly insecure work. A real gate imposes separation of duties, independent evaluation, version pinning, and grounding in governed data before anything reaches production.

## Key Claims

- A folder of skills is a shared drive, not a registry; the gate is what makes it a registry.
- Authors must not approve their own skills — separation of duties is the key rule.
- New skills must be evaluated alone *and* alongside the existing library, to catch oversaturation and interference.
- Production use requires pinned versions and skills grounded in governed data sources.
- No 2026 agent platform ships all five governance capabilities; review gates remain preview-stage at best.
- Every vendor's governance weakens at its own boundary, so teams must build the gaps themselves.

## Related

- [Skill Registry](/concepts/skill-registry.md) — the artifact a review gate governs
- [Quality Gates](/concepts/quality-gates.md) — the general gate pattern this specializes
- [Version Pinning](/concepts/version-pinning.md) — a required property of gated artifacts
- [federation](/concepts/federation.md) — the cross-catalog layer review gates still lack
- [Review Bottleneck](/concepts/review-bottleneck.md) — the throughput cost a gate imposes
- [A Skill Registry Needs a Review Gate, Not Just a Folder](/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md) — primary source
