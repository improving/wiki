---
title: "Skill Sprawl Is the Shared Drive Again"
type: "Source Summary"
description: "Unreviewed skill catalogs grow into near-duplicates that degrade retrieval and ship prompt-injection risk; curation, not speed, is the fix."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/skill-sprawl-is-the-shared-drive-again/skill-sprawl-is-the-shared-drive-again.md"
---

# Skill Sprawl Is the Shared Drive Again — Summary

**Original source**: `references/devlinliles.com/skill-sprawl-is-the-shared-drive-again/skill-sprawl-is-the-shared-drive-again.md`

## Summary

Skill libraries are accumulating the way shared drives do: nobody decides to create three overlapping skills for one job, but each gets written by whoever hits the gap first, and nothing owns deduplication. The post documents the scale — SkillsMP indexes roughly 1.9 million public skills, and a [SkillsBench](/entities/skillsbench.md) analysis of 47,150 of them scored the average at 6.2 of 12 — and argues catalog size and quality are close to inversely related. It then argues skill sprawl is worse than document sprawl because a skill can execute code, and the same missing review gate that lets duplicates in also lets vulnerabilities in.

## Key Claims

- Catalog size and quality are nearly inversely related; the openness that grew the catalog to ~1.9M entries is what let most ship without a duplicate check.
- Recall degrades as the pile grows — the [retrieval oversaturation](/concepts/retrieval-oversaturation.md) problem one layer up, where more candidates add noise, not coverage.
- A Snyk audit of 22,511 skills found 140,963 distinct issues (~6.3 per skill); the ToxicSkills work found [prompt injection](/concepts/prompt-injection.md) in 36% of skills examined.
- Sprawl and security share one root cause: no gate between "someone wrote this" and "an agent can invoke this."
- Curated, reviewed skills lifted agent pass rates by 16.2 points on average; two or three narrow skills gained 18.6 points, while one monolithic skill reduced performance by 2.9 points.

## Relevance

Informs [retrieval oversaturation](/concepts/retrieval-oversaturation.md), [prompt injection](/concepts/prompt-injection.md), and the ownership question taken up in the next post in the series.

## Quality

Practitioner blog post by Devlin Liles. Cites named 2026 research with specific figures (SkillsBench, Snyk ToxicSkills), though all evidence is secondhand and the Elvis Sun anecdote is a single case.

## Entities Mentioned

- [SkillsBench](/entities/skillsbench.md) — the benchmark scoring public skill quality and measuring curation gains.

## Concepts Covered

- [Retrieval oversaturation](/concepts/retrieval-oversaturation.md) — overlapping skills make selection less reliable as the corpus grows.
- [Prompt injection](/concepts/prompt-injection.md) — present in 36% of skills examined and a live exposure in an agent's toolset.

## Related Sources

- [A Skill Is Just Another Thing to Find](/sources/a-skill-is-just-another-thing-to-find.md)
- [The Handbook Is in the Context. The Compliance Isn't.](/sources/the-handbook-is-in-the-context-the-compliance-isnt.md)
