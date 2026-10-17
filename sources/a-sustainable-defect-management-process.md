---
title: "A Sustainable Defect Management Process"
type: "Source Summary"
description: "A six-step process that separates raw incidents from investigated problems and actionable bugs, ending repeated bug bankruptcy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, quality, improving.com]
sources:
  - "references/improving.com/a-sustainable-defect-management-process/a-sustainable-defect-management-process.md"
---

# A Sustainable Defect Management Process — Summary

**Original source**: `references/improving.com/a-sustainable-defect-management-process/a-sustainable-defect-management-process.md`

## Summary

Olivier Aubin argues that most organizations' defect processes collapse because "bug" is used as a catch-all for questions, feature requests, and real defects alike. He proposes a sustainable workflow that separates raw observations from investigated problems and only then creates actionable bugs, so backlogs stay prioritized and teams avoid repeated "bug bankruptcy."

## Key Claims

- Organizations reach "bug bankruptcy" — deleting all bugs for a fresh start — only to see the pile return a year later.
- Definitions: an incident or observation is one occurrence with no implied action; a problem is a collection of similar incidents to investigate; a bug is an actionable, developer-focused work item.
- Step 1: log all incidents in a separate database, never de-duplicating, categorized by product area.
- Step 2: review new incidents daily and attach them to existing problems.
- Step 3: review patterns weekly, using analytics to group incidents into new problems.
- Step 4: assess severity, likelihood, and impact to decide whether a problem is a defect worth remediating.
- Step 5: create bugs or feature requests only for problems to be resolved soon, with priority, completion criteria, and success metrics; step 6: treat bugs as first-class work items.
- The incident stream can later be treated like any event stream for analytics, monitoring, and alerting.

## Relevance

Directly addresses [defect management](/concepts/defect-management.md), with implications for [quality assurance](/concepts/quality-assurance.md) and [technical debt](/concepts/technical-debt.md).

## Quality

Experienced practitioner proposal by Olivier Aubin; specific and process-oriented, though a single-authored framework without case metrics.

## Entities Mentioned

- [Improving](/entities/improving.md) — the consultancy offering the process

## Concepts Covered

- [defect management](/concepts/defect-management.md) — triaging defects so backlogs stay actionable
- [quality assurance](/concepts/quality-assurance.md) — engineering confidence in fitness for purpose
- [technical debt](/concepts/technical-debt.md) — poorly defined bugs accumulating as debt
