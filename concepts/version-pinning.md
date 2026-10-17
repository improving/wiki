---
title: "Version Pinning"
type: "Concept"
description: "Locking exact versions of skills, models, and tools so production behavior stays reproducible and governed."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, reproducibility, skills]
sources:
  - "/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md"
  - "/sources/off-the-shelf-gets-you-partway-there.md"
---

# Version Pinning

Version pinning fixes the exact revision of a skill, model, or dependency that production runs. This corpus treats it as a governance primitive rather than a packaging detail: without it, a governed [Skill Registry](/concepts/skill-registry.md) degrades into an unversioned shared folder, and silent upstream changes break reproducibility and trust.

## Key Claims

- Production must pin versions and ground skills in governed data sources.
- Over 2,500 Claude Code plugin marketplaces exist with no trust authority, so unpinned discovery is unsafe.
- Agentic Resource Discovery federates self-reported metadata but verifies no health or ownership.
- Documents and skills fail discovery for the same structural reason, so pinning must pair with a governed catalog answering "current, owned, safe-to-use."
- New skills must be evaluated alone and alongside the existing library before they are pinned into production.

## Related

- [Skill Registry](/concepts/skill-registry.md) — the catalog pinning makes trustworthy
- [Skill Discovery](/concepts/skill-discovery.md) — the problem versioning partially answers
- [Model Drift Detection](/concepts/model-drift-detection.md) — detecting change where pinning is absent
- [A Skill Registry Needs a Review Gate, Not Just a Folder](/sources/a-skill-registry-needs-a-review-gate-not-just-a-folder.md) — primary source
