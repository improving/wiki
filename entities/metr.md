---
title: "METR"
type: "Entity"
description: "Research nonprofit whose time-horizon and grading studies anchor claims about AI capability, mergeability, and evaluation gaps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [research, evaluation, ai-capability]
sources:
  - "/sources/acceleration-whiplash-the-hidden-metric-ai-adoption-is-breaking.md"
  - "/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
  - "/sources/governance-as-the-control-plane-for-ai.md"
  - "/sources/not-every-ticket-needs-the-250000-engineer.md"
  - "/sources/the-evaluation-governance-flywheel-neither-works-without-the-other.md"
  - "/sources/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md"
  - "/sources/which-failure-mode-can-you-afford-the-security-personality-of-your-model.md"
---

# METR

METR is a research organization cited repeatedly across this corpus as the source of the capability time-horizon curve and of findings that automated graders overstate what AI coding agents can actually deliver. Its measurements supply the quantitative backbone for arguments about verification, model routing, and governance.

## Overview

Writers lean on METR for two kinds of evidence: how fast frontier capability is growing, and how much evaluation flatters it. The time-horizon doubling rate and the gap between graded and human-mergeable pull requests both originate here.

## Key Claims

- Frontier capability time horizons double roughly every seven months, accelerating to 4.3 months since 2023.
- METR found automated graders overstated PR mergeability by about 24 points.
- One analysis puts the overstatement as high as 6.25x versus human maintainers.
- Half of graded AI pull requests were judged unmergeable by maintainers.
- Harness quality explains 17 to 21 points of task-completion variance.

## Related

- [time horizon](/concepts/time-horizon.md) — METR's central capability metric
- [evaluation harness](/concepts/evaluation-harness.md) — where its grading findings land
- [SWE-bench](/entities/swe-bench.md) — benchmark whose scores it helped qualify
- [The Evaluation-Governance Flywheel](/sources/the-evaluation-governance-flywheel-neither-works-without-the-other.md) — primary source
