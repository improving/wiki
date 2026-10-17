---
title: "Every Ticket Went to the Expensive Model, Just in Case"
type: "Source Summary"
description: "A 600-ticket case study showing that defaulting every request to a premium model wastes money, and that cheap-first escalation fixes it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/every-ticket-went-to-the-expensive-model-just-in-case/every-ticket-went-to-the-expensive-model-just-in-case.md"
---

# Every Ticket Went to the Expensive Model, Just in Case — Summary

**Original source**: `references/devlinliles.com/every-ticket-went-to-the-expensive-model-just-in-case/every-ticket-went-to-the-expensive-model-just-in-case.md`

## Summary

A freight-logistics assistant routed all 600 sample tickets to a premium model "just in case," so spend scaled with volume rather than difficulty. Liles shows the waste hid because every ticket still got resolved and approval rates were unchanged. The fix sends every ticket to the cheap tier first, scores its output against a fixed quality bar, and escalates only failures to the premium tier — cutting spend at least 40% at equal or better quality.

## Key Claims

- Cheap tier ran ~0.2 cents/ticket and premium ~15x that; the premium advantage was spent on ~70% of tickets the cheap tier handled identically.
- Retrospective escalation (cheap first, check, then escalate) dropped total spend ≥40% on the same 600 tickets with equal-or-better pass rates.
- FrugalGPT (2023) is the academic ancestor, reporting cost cuts up to 98% at matched quality; Azure AI Foundry's Model Router ships the same shape.
- This differs from prospective classifier routing, which predicts the tier before spending; here escalation follows measured failure.
- Its safety depends almost entirely on the quality-bar check — confidently wrong cheap answers that pass it never escalate.

## Relevance

A concrete case for [model routing](/concepts/model-routing.md) and for treating [token cost](/concepts/token-cost.md) as a per-outcome metric rather than a per-call one.

## Quality

Practitioner blog post by Devlin Liles. Grounded in a specific 600-ticket engagement; the figures come from that single workload and may not generalize.

## Entities Mentioned

- None.

## Concepts Covered

- [model routing](/concepts/model-routing.md) — routing across cost tiers, contrasting retrospective escalation with prospective classification
- [token cost](/concepts/token-cost.md) — dollars spent per resolved ticket as the metric the failure hides behind
