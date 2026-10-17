---
title: "The Categorization Skill That Never Changed"
type: "Source Summary"
description: "Bolting unrelated features into one prompt file degraded categorization accuracy until the skill was split behind a thin dispatcher."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-categorization-skill-that-never-changed/the-categorization-skill-that-never-changed.md"
---

# The Categorization Skill That Never Changed — Summary

**Original source**: `references/devlinliles.com/the-categorization-skill-that-never-changed/the-categorization-skill-that-never-changed.md`

## Summary

An expense-report assistant started as a single categorization skill, then over four releases accreted unrelated features — travel-policy Q&A, currency conversion, receipt-OCR troubleshooting — into the same prompt file. Categorization logic never changed, yet accuracy measurably declined. The cause was cross-talk: unrelated instructions sharing one file competed for the model's attention on every request. Splitting the four capabilities into separate single-responsibility skill files behind a thin [dispatcher pattern](/concepts/dispatcher-pattern.md) kept the categorization prompt byte-identical and accuracy flat.

## Key Claims

- Against a fixed thirty-item seeded expense test set, categorization accuracy trended downward from release one to release four even though the categorization task itself never changed.
- The regression came from cross-talk: instructions for newer, unrelated functions sat in the same prompt file and competed for attention on every categorization request.
- The fix separated the four capabilities into four narrowly scoped prompt files dispatched by a thin router that only decides which skill handles a request.
- The categorization file stayed checksum-verified byte-identical across all four releases, so accuracy stayed flat as a mechanical consequence — no prompt improvement was needed.
- The pattern earns its keep only when a genuinely unrelated second capability is about to be added; a router spanning forty skills just relocates the problem one layer up.

## Relevance

Informs the [dispatcher pattern](/concepts/dispatcher-pattern.md) and [coordination overhead](/concepts/coordination-overhead.md) within the agentic-delivery theme; the isolation test — does one capability's instructions ever change because of another — is the practical contribution.

## Quality

Practitioner blog post by Devlin Liles. Concrete and honest about limits, but grounded in a single internal case and a 30-item test set; the "fortieth skill" scaling concern is raised but left unsolved.

## Entities Mentioned

- None.

## Concepts Covered

- [dispatcher pattern](/concepts/dispatcher-pattern.md) — the thin router that dispatches to single-responsibility skills
- [coordination overhead](/concepts/coordination-overhead.md) — the cost of splitting capabilities too finely or maintaining a growing skill collection
