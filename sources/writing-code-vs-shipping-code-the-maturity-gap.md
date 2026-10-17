---
title: "Writing Code vs. Shipping Code: The Maturity Gap"
type: "Source Summary"
description: "AI coding tools lift commit volume far more than shipped features or value, because bottlenecks move from writing to shipping to choosing."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/writing-code-vs-shipping-code-the-maturity-gap/writing-code-vs-shipping-code-the-maturity-gap.md"
---

# Writing Code vs. Shipping Code: The Maturity Gap — Summary

**Original source**: `references/devlinliles.com/writing-code-vs-shipping-code-the-maturity-gap/writing-code-vs-shipping-code-the-maturity-gap.md`

## Summary

Liles uses a 2026 MIT/Wharton study of 100,000+ GitHub developers to update Solow's productivity paradox for AI coding tools. The data shows gains attenuate across three layers: commits rose 180% and lines of code sevenfold, released software rose only 30%, and consumer usage of the resulting software was essentially flat. He maps this onto Improving's eight-stage AI maturity model, arguing the bottlenecks are process-architecture failures at two handoffs — shipping features and producing value — not failures of the tools. The fixes are workflow redesign with deterministic validation, and upstream problem selection.

## Key Claims

- Commits rose 180% and lines of code sevenfold across three AI tool generations; released software rose 30%; consumer usage rose essentially zero.
- The attenuation maps to a failure of process architecture at two handoffs, consistent with O-ring theory.
- Stage 4 (Workflow) requires deterministic validation, adversarial agents, human punch-out points, and audit trails; it is the first stage requiring team and IT, not just individual skill.
- Teams deploying sync agents without redesigning review see commit volume rise in month one but PR approval times extend by month three.
- New iOS app releases roughly doubled between early 2025 and April 2026 while consumer engagement stayed flat.
- Improving teams pairing Stage 2–3 tooling with workflow redesign ship 12–30% more features; committed governance teams exceed 50%.

## Relevance

Central to the [AI maturity model](/concepts/ai-maturity-model.md), [deterministic validation](/concepts/deterministic-validation.md), the [review bottleneck](/concepts/review-bottleneck.md), and the [demand limit](/concepts/demand-limit.md).

## Quality

Practitioner blog post by Devlin Liles. Strong empirical anchor in the CEPR/NBER study and Improving program data; the consumer-usage row is flagged as illustrative.

## Entities Mentioned

- [Robert Solow](/entities/robert-solow.md) — origin of the productivity-paradox framing
- [Claude Code](/entities/claude-code.md) — named as a sync-agent tool generation
- [Improving](/entities/improving.md) — source of the maturity model and delivery data

## Concepts Covered

- [AI maturity model](/concepts/ai-maturity-model.md) — the eight-stage frame the study maps onto
- [deterministic validation](/concepts/deterministic-validation.md) — the Stage 4 control at every handoff
- [Review Bottleneck](/concepts/review-bottleneck.md) — the first process bottleneck the post names
- [demand limit](/concepts/demand-limit.md) — why more supply doesn't grow usage

## Related Sources

- [Five Firms Built Five AI Frameworks. None of Them Built a Ruler.](/sources/five-firms-built-five-ai-frameworks-none-of-them-built-a-ruler.md)
- [The 8-Stage AI Trust Evolution: A Map for the Journey](/sources/the-8-stage-ai-trust-evolution-a-map-for-the-journey.md)
