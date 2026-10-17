---
title: "Can't Leak What Never Leaves - Air-Gapping the Highest-Sensitivity Tier"
type: "Source Summary"
description: "Air-gapping the highest-sensitivity query tier so privileged data never crosses the boundary, removing the need for a scrubber."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, devlinliles.com]
sources:
  - "references/devlinliles.com/cant-leak-what-never-leaves-air-gapping-the-highest-sensitivity-tier/cant-leak-what-never-leaves-air-gapping-the-highest-sensitivity-tier.md"
---

# Can't Leak What Never Leaves - Air-Gapping the Highest-Sensitivity Tier — Summary

**Original source**: `references/devlinliles.com/cant-leak-what-never-leaves-air-gapping-the-highest-sensitivity-tier/cant-leak-what-never-leaves-air-gapping-the-highest-sensitivity-tier.md`

## Summary

Liles built CaseLens, a law-firm research assistant handling public case-law research and privileged deposition analysis. A regex scrubber on the privileged path failed: seeded transcripts with unlabeled account numbers and nicknames still leaked privileged tokens. His fix doesn't improve the scrubber—a tier classifier routes privileged queries to a model running entirely inside the firm's network, so the leak metric reads zero by construction.

## Key Claims

- A filter that is pattern-complete on tested formats is blind to the ones nobody wrote a rule for; a scrubber can be correct on test day and still miss next week's case.
- Routing the privileged tier to an in-network model means nothing on that path leaves the boundary to be scrubbed—a stronger guarantee than any filter offers.
- Deloitte reports nearly $100 billion invested in sovereign AI compute in 2026, with the sovereign AI infrastructure market estimated at $24.8 billion.
- Everything depends on the tier classifier tagging correctly; a mistagged privileged query has no scrubber to catch it because none runs on the general path.
- Cost and latency are real: on-prem infrastructure must exist before a privileged query arrives, so set the tier boundary from a named inventory rather than vague sensitivity.

## Relevance

Illustrates [boundary enforcement](/concepts/boundary-enforcement.md) as a structural guarantee rather than a filtering one.

## Quality

Practitioner blog post by Devlin Liles. Clear construction-based argument with a candidly named limitation; supported by cited market figures and a synthetic test, not production data.

## Entities Mentioned

- None.

## Concepts Covered

- [Boundary enforcement](/concepts/boundary-enforcement.md) — the air-gap guarantee that nothing on the privileged path crosses the boundary
