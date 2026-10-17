---
title: "Herbert Simon Was Right About Your AI Budget"
type: "Source Summary"
description: "Uses Herbert Simon's bounded rationality to argue thinking budgets should be calibrated to where accuracy plateaus, not ignored or maxed."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/herbert-simon-was-right-about-your-ai-budget/herbert-simon-was-right-about-your-ai-budget.md"
---

# Herbert Simon Was Right About Your AI Budget — Summary

**Original source**: `references/devlinliles.com/herbert-simon-was-right-about-your-ai-budget/herbert-simon-was-right-about-your-ai-budget.md`

## Summary

Liles argues the "thinking budget" on a reasoning model is a satisficing dial: teams either ignore it or set it to maximum, and both choices are wrong. Drawing on Herbert Simon's bounded rationality, he contends that accuracy improvements follow diminishing returns, so budgets should be calibrated empirically to the point where additional tokens stop helping.

## Key Claims

- Simon showed real agents satisfice—search until a solution clears an aspiration level, then stop—rather than optimize; the optimization model is a fiction.
- TALE-EP work (ACL 2025, arXiv:2412.18547) achieved roughly 80% average accuracy while cutting output token costs by 67% versus unconstrained chain-of-thought.
- Past a task-specific ceiling, extra tokens add almost nothing to accuracy while multiplying cost; the model is traversing ground it has already covered.
- Calibration means running evals at tiers like 256, 512, 1024, 2048, and 4096 tokens, finding the elbow of the curve, setting the budget there, and reviewing quarterly as workloads drift.
- Dynamic budget allocation by request difficulty can match or exceed a fixed-large budget at substantially lower average cost—satisficing more precisely, not optimizing.

## Relevance

Applies [Herbert Simon](/entities/herbert-simon.md) to AI cost governance; touches [token cost](/concepts/token-cost.md) and [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md).

## Quality

Practitioner blog post by Devlin Liles. Concrete figures and a named paper give it weight; the 80%/67% result is reported from TALE-EP rather than independently verified, and the "elbow" calibration advice is experience-based.

## Entities Mentioned

- [Herbert Simon](/entities/herbert-simon.md) — bounded rationality and satisficing, the post's central lens

## Concepts Covered

- [token cost](/concepts/token-cost.md) — the spend that uncalibrated thinking budgets multiply
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — the intermediate reasoning the budget caps
