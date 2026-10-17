---
title: "The Corrections Are the Leak"
type: "Source Summary"
description: "Every correction a team makes to a frontier model feeds the provider's improvement loop, so the eval-and-correction layer — not the model — is the real moat."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, driventodevelop.com]
sources:
  - "references/driventodevelop.com/the-corrections-are-the-leak/the-corrections-are-the-leak.md"
---

# The Corrections Are the Leak — Summary

**Original source**: `references/driventodevelop.com/the-corrections-are-the-leak/the-corrections-are-the-leak.md`

## Summary

O'Hara argues that every time a consultant corrects a model's output — in a proposal, a code review, or on a client project — a lesson is recorded, and the unasked question is whose model is learning it. Building on Satya Nadella's phrase "the reverse information paradox," he points out that the prompts, fixes, and evaluation sets that define correctness for a specific business become institutional knowledge somewhere, just not necessarily the client's institution. Because rivals refining the same frontier model with the same kind of corrections all get slightly smarter assistants, the advantage accumulates in the model rather than in any one company.

## Key Claims

- The enterprise AI pitch is that the model gets smarter with use; what goes unsaid is whose model gets smarter.
- The real differentiator teams spend months building is not the model but the layer around it: the eval set encoding "correct" for the business and the library of corrections.
- That layer is fed back into the provider's loop one correction at a time, invisibly, in a format nobody signed off on sharing.
- If every company in an industry runs the same frontier model and refines it with similar corrections, nobody gets a moat — everyone gets a slightly smarter assistant.
- "We won't train on your data" contract clauses are worth reading closely, because the leak is not the data but the pattern of how you correct it.

## Relevance

Informs [AI Governance](/concepts/ai-governance.md), [Platform Lock-In](/concepts/platform-lock-in.md), and [Data Ownership](/concepts/data-ownership.md), and reframes where [evals-as-code](/concepts/evals-as-code.md) assets create value.

## Quality

Practitioner blog post by David O'Hara. Strong conceptual framing built on a named executive's phrase; argument is persuasive but largely anecdotal, with no empirical measurement.

## Entities Mentioned

- None.

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — contract terms and data-handling assumptions that need scrutiny
- [Platform Lock-In](/concepts/platform-lock-in.md) — corrections deepening dependence on a provider's model
- [Data Ownership](/concepts/data-ownership.md) — who owns the correction patterns and eval sets
- [evals-as-code](/concepts/evals-as-code.md) — the eval layer that encodes business-specific correctness
