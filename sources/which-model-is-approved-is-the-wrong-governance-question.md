---
title: "Which Model Is Approved Is the Wrong Governance Question"
type: "Source Summary"
description: "Vendor approval is a fragile governance answer; graduated oversight tiers keyed to task risk survive a model being pulled."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/which-model-is-approved-is-the-wrong-governance-question/which-model-is-approved-is-the-wrong-governance-question.md"
---

# Which Model Is Approved Is the Wrong Governance Question — Summary

**Original source**: `references/devlinliles.com/which-model-is-approved-is-the-wrong-governance-question/which-model-is-approved-is-the-wrong-governance-question.md`

## Summary

When the US government ordered Anthropic to suspend access to Fable 5 and Mythos 5 on June 12, 2026, enterprises that had done diligent model selection still woke up with a same-day compliance gap. Liles argues this proves that "which model is approved" is the wrong governance question, because vendor trust buys no continuity. He endorses Richard Kang's "Governed AI-Assisted Engineering" paper, which borrows SAE J3016's graded autonomy levels and routes each code-generation task to one of three oversight tiers based on regulatory impact, customer proximity, reversibility, and data sensitivity.

## Key Claims

- Mythos 5 was partially restored for some US organizations on June 26; Fable 5 came back July 1 — nineteen days after the order.
- The government's cited evidence was a narrow, non-universal jailbreak; Anthropic said no universal jailbreak existed and named GPT-5.5 as offering the same capability without a bypass.
- Kang's modeling puts uniform human-in-the-loop review at 45–65% of ungoverned agentic coding velocity, versus 84–97% (central estimate 91%) for three-tier graduated oversight.
- Tier 1 (human-in-the-loop) catches strategic functions, Tier 2 (human-over-the-loop) gates customer-facing deploys, Tier 3 (automated with monitoring) covers internal tooling and CI.
- Tiers key their approval evidence to test results and monitoring, not the vendor's name, shrinking a vendor pull's blast radius.

## Relevance

Extends [AI governance](/concepts/ai-governance.md) beyond [model selection](/concepts/model-selection.md) toward risk-proportionate [human-in-the-loop](/concepts/human-in-the-loop.md) oversight and durable [audit trails](/concepts/audit-trail.md).

## Quality

Practitioner blog post by Devlin Liles. Strong, concrete case study tied to a real arXiv paper, but the velocity figures are analytical modeling not yet validated against production telemetry, as the author notes.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — subject of the suspension order
- [Mythos 5](/entities/mythos-5.md) — one of the two suspended models

## Concepts Covered

- [human-in-the-loop](/concepts/human-in-the-loop.md) — the Tier 1 oversight mode for strategic functions
- [AI Governance](/concepts/ai-governance.md) — the domain the argument reframes
- [Model selection](/concepts/model-selection.md) — the question the post calls wrong
- [Audit Trail](/concepts/audit-trail.md) — vendor-independent evidence the tiers produce
