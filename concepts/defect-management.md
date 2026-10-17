---
title: "defect management"
type: "Concept"
description: "Triaging and tracking defects through incident, problem, and bug stages so backlogs stay actionable rather than accumulating."
created: '2026-10-17'
updated: '2026-10-17'
tags: [quality, testing, process]
sources:
  - "/sources/a-sustainable-defect-management-process.md"
  - "/sources/process-focused-quality-assurance.md"
  - "/sources/the-defect-is-in-the-definition.md"
  - "/sources/context-based-testing.md"
---

# defect management

The process by which observations about software become tracked, prioritized work — and the discipline of keeping that process from collapsing under its own backlog. The corpus argues the failure is definitional: when "bug" is a catch-all for questions, feature requests, and real defects alike, backlogs become unmanageable and teams periodically delete everything to start over.

## Key Claims

- Organizations reach "bug bankruptcy" — deleting all bugs for a fresh start — only to see the pile return within a year.
- The proposed vocabulary separates three things: an incident is one occurrence with no implied action, a problem is a collection of similar incidents to investigate, and a bug is an actionable, developer-focused work item.
- A six-step workflow logs all incidents without de-duplicating, reviews them daily against existing problems, groups patterns weekly, then assesses severity, likelihood, and impact before creating bugs.
- Bugs should be created only for problems to be resolved soon, with priority, completion criteria, and success metrics, and treated as first-class work items.
- The incident stream can itself be treated as an event stream for analytics, monitoring, and alerting.
- A related root-cause view asks why the process allowed a defect — an unclear requirement, easy-to-misuse architecture, missing communication, or overlooked assumption — rather than only fixing the symptom.
- In agentic delivery, under-specified task definitions are a defect source: if you can't write a test that fails when the requirement is violated, the requirement isn't defined well enough.
- Test organization matters too: bloated fixtures drive teams to abandon testing, so grouping specs by scenario context keeps defects findable.

## Related

- [quality assurance](/concepts/quality-assurance.md) — the discipline defects are a signal about
- [technical debt](/concepts/technical-debt.md) — poorly defined bugs accumulating as debt
- [acceptance criteria](/concepts/acceptance-criteria.md) — encoding definition of done so defects are caught at definition time
- [manual testing](/concepts/manual-testing.md) — where exploratory defects are found
