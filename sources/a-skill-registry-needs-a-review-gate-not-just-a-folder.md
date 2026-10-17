---
title: "A Skill Registry Needs a Review Gate, Not Just a Folder"
type: "Source Summary"
description: "A folder of skills is not a registry; a governed skill library needs a fixed-order lifecycle with review, evaluation, and version pinning."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/a-skill-registry-needs-a-review-gate-not-just-a-folder/a-skill-registry-needs-a-review-gate-not-just-a-folder.md"
---

# A Skill Registry Needs a Review Gate, Not Just a Folder — Summary

**Original source**: `references/devlinliles.com/a-skill-registry-needs-a-review-gate-not-just-a-folder/a-skill-registry-needs-a-review-gate-not-just-a-folder.md`

## Summary

A Git repository with a folder per skill is a shared drive with better version history, not a registry, the post argues. The difference is a small number of gates running between someone writing a skill and an agent being allowed to invoke it in production, following [Anthropic](/entities/anthropic.md)'s lifecycle of plan, create, review, test, deploy, monitor, iterate. Each gate assumes the previous one happened, and the organizations getting this right treat governance as the first thing they build rather than retrofitting it after an incident.

## Key Claims

- Workflow-specific, narrowly scoped skills outperform broad ones because a narrow scope makes the agent's trigger decision cleaner.
- The author of a skill cannot approve it for deployment; a script embedding a credential or subtly overriding a safety boundary is what the author is least likely to catch.
- A representative evaluation set covers cases where the skill should trigger, clearly should not, and the ambiguous middle, and must run the skill both alone and alongside the existing library.
- Production should reference a specific tested version, keep the prior version for rollback, and treat every update as a new deployment requiring the full review cycle.
- A skill that queries ungoverned data can pass every code-level review and still return a confident, wrong number.

## Relevance

Core to [skill registry](/concepts/skill-registry.md) governance and the [review gate](/concepts/review-gate.md) concept; connects to [version pinning](/concepts/version-pinning.md) and [data governance](/concepts/data-governance.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: turns a vendor lifecycle into a concrete, ordered set of gates with a sharp separation-of-duties argument. Caveats: draws on [Atlan](/entities/atlan.md) and Anthropic documentation rather than original measurement; prescriptive rather than evidenced.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — source of the recommended skill lifecycle and security checklist
- [Atlan](/entities/atlan.md) — publisher of the enterprise skills governance guide

## Concepts Covered

- [skill-registry](/concepts/skill-registry.md) — the governed library beyond a folder of files
- [review-gate](/concepts/review-gate.md) — separation-of-duties approval before deployment
- [version-pinning](/concepts/version-pinning.md) — production referencing a specific tested version

## Related Sources

- [One Catalog, Every Consumer](/sources/one-catalog-every-consumer.md)
- [Somebody Has to Own the Skill Library](/sources/somebody-has-to-own-the-skill-library.md)
- [The Sandbox Held Until the Model Decided It Didn't Need To](/sources/the-sandbox-held-until-the-model-decided-it-didnt-need-to.md)
