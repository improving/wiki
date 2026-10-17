---
title: "Two Failure Modes in LLM-Generated Pull Requests: Capability-Gap and Scope-Discipline Haircuts in a Controlled 216-Run Evaluation"
type: "Source Summary"
description: "A 216-run study separating capability-gap from scope-discipline failures in LLM-generated pull requests."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md"
---

# Two Failure Modes in LLM-Generated Pull Requests — Summary

**Original source**: `references/devlinliles.com/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md`

## Summary

A controlled 216-run evaluation separates two structurally distinct reasons LLM-generated pull requests fail mergeability review. A capability-gap haircut means the model cannot produce maintainer-quality output even when tests pass; a scope-discipline haircut means functionally correct, test-passing output exceeds the permitted diff envelope. The paper argues the two respond to opposite interventions, so conflating them misroutes model-selection investment.

## Key Claims

- Design: 24 enterprise-representative tasks (7 bugfix, 6 feature, 6 refactor, 5 test-addition) × 3 Anthropic tiers (Opus/Sonnet/Haiku families) × 3 repetitions = 216 runs on the Devbox platform with a deterministic rubric.
- Token spend was 0.1%–2.3% of total cost per mergeable PR; the verification tax dominated token spend by 40x–1,000x.
- All 25 mergeability failures were test-addition tasks, and all 25 passed automated tests — a pure scope-discipline pattern.
- The high tier underperformed mid on constrained test-additions (47% vs. 53% merge rate) because more capable models produced more code and violated size gates more often.
- Bugfix confirmed the capability curve (high 78% vs. mid 67% vs. low 44%); refactors were hardest but showed the high tier's most consistent advantage.
- Routing implication: capability-gap tasks get the premium tier; scope-constrained tasks get explicit limits and possibly a mid or low tier.

## Relevance

Directly tests [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) and the [verification tax](/concepts/verification-tax.md), and connects to [time horizon](/concepts/time-horizon.md) via the METR h₅₀ methodology.

## Quality

Practitioner research post by Devlin Liles with a documented design, tiers, and repetitions. Figures are illustrative of one provider's tiers on a curated corpus; the sharpest claim (tier inversion) rests on 25 failures in a single task category.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — the model provider for all tiers
- [DevBox](/entities/devbox.md) — the agentic development platform used to run tasks
- [METR](/entities/metr.md) — source of the time-horizon methodology referenced

## Concepts Covered

- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — the framework the evaluation tests and refines
- [verification tax](/concepts/verification-tax.md) — the dominant cost per mergeable PR
- [time horizon](/concepts/time-horizon.md) — task-length threshold used to predict the capability-gap regime
