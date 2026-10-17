---
title: "A Skill Is Just Another Thing to Find"
type: "Source Summary"
description: "Agent skills are procedurally the same discovery problem as documents, with the same failure modes repeated at the skill layer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/a-skill-is-just-another-thing-to-find/a-skill-is-just-another-thing-to-find.md"
---

# A Skill Is Just Another Thing to Find — Summary

**Original source**: `references/devlinliles.com/a-skill-is-just-another-thing-to-find/a-skill-is-just-another-thing-to-find.md`

## Summary

[Anthropic](/entities/anthropic.md)'s Agent Skills format is deliberately plain: a folder with a markdown file, frontmatter, and supporting scripts. The post argues a SKILL.md describing how a finance team closes the books is structurally the same object as a policy document describing the same process, a piece of written knowledge someone must find at the moment of need. A person searching a wiki and an agent resolving which skill to invoke are asking the identical question on different clocks, and every document failure mode recurs at the skill layer.

## Key Claims

- Progressive disclosure loads a skill in three stages: name and description first, full instruction body only on a match, bundled scripts and references last on demand.
- That is metadata-first retrieval rebuilt for a different object, letting a system narrow the field before paying the cost of reading everything in full.
- [SkillsBench](/entities/skillsbench.md), the first peer-reviewed benchmark of agent skills, analyzed 47,150 public skills and found an average quality score of 6.2 out of 12, forcing researchers to test only the top quartile.
- Curated, reviewed skills raised agent pass rates by an average of 16.2 points across 84 tasks, and by 51.9 points in healthcare, the largest gain of any domain.
- Most organizations building skill libraries are relearning the tagging, folder-tree, and [vocabulary mismatch](/concepts/vocabulary-mismatch.md) problems from scratch.

## Relevance

Central to [skill discovery](/concepts/skill-discovery.md) and enterprise AI retrieval; connects to [semantic search](/concepts/semantic-search.md) and [vocabulary mismatch](/concepts/vocabulary-mismatch.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: grounds a conceptual claim in SkillsBench's concrete quality and pass-rate figures and names its sources. Caveats: leans on a vendor governance guide ([Atlan](/entities/atlan.md)) and the author's own prior series for framing.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — published and open-sourced the Agent Skills format
- [SkillsBench](/entities/skillsbench.md) — the peer-reviewed skill benchmark cited for quality and pass-rate figures
- [Atlan](/entities/atlan.md) — publisher of the enterprise skills governance guide cited

## Concepts Covered

- [skill-discovery](/concepts/skill-discovery.md) — finding the right skill at the moment of need

## Related Sources

- [Skill Sprawl Is the Shared Drive Again](/sources/skill-sprawl-is-the-shared-drive-again.md)
