---
title: "Seventy Easy Questions Paying Premium Rates"
type: "Source Summary"
description: "A difficulty classifier routing help-desk requests to matched reasoning budgets cut average cost 40% with no accuracy loss."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/seventy-easy-questions-paying-premium-rates/seventy-easy-questions-paying-premium-rates.md"
---

# Seventy Easy Questions Paying Premium Rates — Summary

**Original source**: `references/devlinliles.com/seventy-easy-questions-paying-premium-rates/seventy-easy-questions-paying-premium-rates.md`

## Summary

A help-desk triage agent ran 100 requests through a fixed 4,096-token reasoning budget regardless of difficulty, so 70 trivial requests paid the same as 10 hard ones with no accuracy benefit. The fix inserts a cheap classifier that tags each request easy, medium, or hard and routes it to a matched budget. The author reports a 40%+ drop in average cost with hard-request accuracy unchanged, then examines the assumptions that make the pattern safe.

## Key Claims

- All 100 requests (70 trivial, 20 medium, 10 hard) ran at an identical 4,096-token budget; the trivial bucket was already at its accuracy ceiling with a fraction of it.
- A cheap up-front classifier routes at least 90 of 100 requests to their correct true-difficulty tier.
- Average cost per request drops by 40% or more, trivial-request accuracy shows no measurable drop, and the ten hard requests keep the full budget and the same accuracy.
- Classifier accuracy is the load-bearing assumption: a hard request misrouted to the easy tier gets shortchanged in exactly the way the pattern was meant to prevent.
- Tier boundaries are a design decision, not given by the data; forcing a workload into an unnatural number of tiers just relocates the misclassification problem.
- Some research finds accuracy can fall off past a complexity threshold, complicating the assumption that more budget always helps.

## Relevance

Informs [model routing](/concepts/model-routing.md) and [token cost](/concepts/token-cost.md) control for mixed-difficulty workloads.

## Quality

Practitioner blog post by Devlin Liles built on an internal pilot. Figures are single-case illustrative measurements rather than published benchmarks; the author states caveats directly.

## Entities Mentioned

- None.

## Concepts Covered

- [model routing](/concepts/model-routing.md) — classifier-driven routing to matched reasoning budgets
- [token cost](/concepts/token-cost.md) — the cost the pattern recovers on easy requests
