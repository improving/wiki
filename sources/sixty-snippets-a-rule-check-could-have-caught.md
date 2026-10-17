---
title: "Sixty Snippets a Rule Check Could Have Caught"
type: "Source Summary"
description: "Tier a review pipeline cheapest-first — rules, then model judge, then human — so expensive checks only see cases that need them."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/sixty-snippets-a-rule-check-could-have-caught/sixty-snippets-a-rule-check-could-have-caught.md"
---

# Sixty Snippets a Rule Check Could Have Caught — Summary

**Original source**: `references/devlinliles.com/sixty-snippets-a-rule-check-could-have-caught/sixty-snippets-a-rule-check-could-have-caught.md`

## Summary

A compliance review pipeline for marketing copy sent all two hundred snippets through the same full [model-judge](/concepts/model-as-judge.md) call, regardless of what was wrong. Measuring it revealed sixty snippets had violations a plain rule check catches instantly (banned word, missing disclaimer, dead link), thirty genuinely needed judgment, and ten were edge cases even a human would want to second-opinion. The fix reorders the pipeline into three tiers run in strict cost order — deterministic rules, then model judge, then [human review](/concepts/human-in-the-loop.md) — escalating only what the prior tier cannot resolve.

## Key Claims

- The first version paid full judge cost and latency on all two hundred snippets, including the sixty whose answer was in plain sight.
- Reordering into rules → judge → human drops total review cost by more than half while holding the catch rate the same or better.
- Stage order is the whole mechanism: running the judge first and the rule check afterward saves nothing because the expensive call already ran.
- The [confidence threshold](/concepts/confidence-thresholds.md) deciding what the judge escalates is a calibration question with consequences both ways; tune it by watching what humans overturn.
- The pattern assumes the tiers genuinely differ in cost; if cheap and expensive tiers cost alike, tiering buys little.

## Relevance

Informs [model-as-judge](/concepts/model-as-judge.md) pipelines, [human-in-the-loop](/concepts/human-in-the-loop.md) design, and [confidence thresholds](/concepts/confidence-thresholds.md) in AI evals.

## Quality

Practitioner blog post by Devlin Liles. Uses a concrete two-hundred-snippet build with category counts (60/30/10), but the human tier is a scripted stand-in and results are not independently reproducible.

## Entities Mentioned

- None.

## Concepts Covered

- [Model-as-judge](/concepts/model-as-judge.md) — the expensive mid-tier that only sees what the rule check misses.
- [human-in-the-loop](/concepts/human-in-the-loop.md) — the final, most expensive tier, reserved for genuinely ambiguous cases.
- [Confidence Thresholds](/concepts/confidence-thresholds.md) — governs what the judge escalates to human review.
- [deterministic validation](/concepts/deterministic-validation.md) — the first, cheapest tier absorbing everything it can.
