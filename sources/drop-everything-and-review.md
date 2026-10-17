---
title: "Drop Everything and Review"
type: "Source Summary"
description: "Code review is a 'middle loop' between inner and outer dev loops; treat reviewing as top priority (DEAR)."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, culture, agile, improving.com]
sources:
  - "references/improving.com/drop-everything-and-review/drop-everything-and-review.md"
---

# Drop Everything and Review — Summary

**Original source**: `references/improving.com/drop-everything-and-review/drop-everything-and-review.md`

## Summary

Andrew Watson proposes a "middle loop" of software development — the code review loop — distinct from the fast single-developer inner loop and the slow multi-environment outer loop. He argues async code review unnecessarily inflates this middle loop, because reviewers delay, hide in crowds, and treat review as thankless, blocking the author. His remedy is a norm he calls Drop Everything and Review (DEAR): after production incidents, reviewing code should be the first task on a developer's list. Where possible, synchronous review or pair/mob programming shrinks or eliminates the middle loop.

## Key Claims

- The inner loop is a single developer's fast code-build-test cycle, as short as static analysis takes.
- The outer loop covers deployment, acceptance and performance tests, and can take minutes to days.
- The middle loop is code review — the first time multiple stakeholders see the same new code.
- Async review inflates the middle loop; developers may glob fixes into one PR or ping reviewers, disrupting flow.
- Review is thankless, and reviewers added in crowds assume others will cover the work.
- DEAR: after production incidents, reviewing code should always be first on a developer's TODO list.

## Relevance

Concerns [code review](/concepts/code-review.md), [developer experience](/concepts/developer-experience.md), and [release frequency](/concepts/release-frequency.md).

## Quality

Practitioner opinion by Andrew Watson; a clear loop model and concrete norm, but no data.

## Entities Mentioned

- (none)

## Concepts Covered

- [code review](/concepts/code-review.md) — the middle loop
- [developer experience](/concepts/developer-experience.md) — flow and blocking
- [release frequency](/concepts/release-frequency.md) — review as a delivery constraint
