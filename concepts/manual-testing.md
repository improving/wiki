---
title: "manual testing"
type: "Concept"
description: "Human-driven exploratory and usability testing that automation cannot fully replace, best paired with automated checks."
created: '2026-10-17'
updated: '2026-10-17'
tags: [testing, quality, software-craft]
sources:
  - "/sources/software-testing-manual-and-automation.md"
  - "/sources/multi-layered-testing-overview.md"
  - "/sources/is-qa-engineer-really-worth-the-investment.md"
  - "/sources/process-focused-quality-assurance.md"
---

# manual testing

Testing driven by human observation, intuition, and experience rather than pre-written scripts. The corpus treats it as the part of quality work that automation frees up rather than replaces: automated layers handle fast regression and business-rule checks, leaving people to explore, judge usability, and probe edge cases a script will not imagine.

## Key Claims

- Manual testing relies on human observation, intuition, and experience; automation runs pre-written scripts faster and across multiple environments.
- Automation is strongest at regression testing — faster, more consistent, wider coverage, earlier feedback — but carries high setup and maintenance cost and covers UX and usability poorly.
- Manual testing surfaces usability problems and edge cases automation misses, and can validate automated results.
- A layered automated suite — unit, integration, and system/GUI — runs before QA deployment so that it "frees manual QA for edge-case and exploratory testing."
- QA that over-relies on repetitive manual work becomes a budget sinkhole; the fix is to automate the repetitive checks and test what matters to users.
- The human contribution starts before testing: QA reviewing requirements, surfacing ambiguities, and challenging assumptions at kickoff catches bugs that originate in conversations, not code.
- The likely future is more automation, but exploratory and usability testing will still need people.

## Related

- [quality assurance](/concepts/quality-assurance.md) — the broader discipline manual testing sits inside
- [automated testing](/concepts/automated-testing.md) — the encoded checks that complement it
- [test automation](/concepts/test-automation.md) — scripts that run without a human
- [test pyramid](/concepts/test-pyramid.md) — how unit, integration, and GUI layers are balanced
- [Selenium](/entities/selenium.md) — browser automation used to move repetitive checks off people
