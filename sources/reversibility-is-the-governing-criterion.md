---
title: "Reversibility Is the Governing Criterion"
type: "Source Summary"
description: "Argues AI agent autonomy should be governed by how reversible a failure is, not by risk category or autonomy level."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, driventodevelop.com]
sources:
  - "references/driventodevelop.com/reversibility-is-the-governing-criterion/reversibility-is-the-governing-criterion.md"
---

# Reversibility Is the Governing Criterion — Summary

**Original source**: `references/driventodevelop.com/reversibility-is-the-governing-criterion/reversibility-is-the-governing-criterion.md`

## Summary

O'Hara argues we are asking the wrong governance question about AI agents. Instead of "how risky is this agent," we should ask "if this agent gets it wrong, can we undo it?" He draws on Akamai's State of the Internet security report, which recommends granting operational autonomy based on how easily actions can be verified and how reversible a failure is — not task category, department, or risk classification. The reframe gives practitioners a design principle instead of a bureaucratic category, and the governance burden should scale with reversibility, not autonomy level.

## Key Claims

- The right question is not how risky an agent is, but whether a wrong action can be undone.
- Akamai's report recommends granting autonomy based on verifiability and reversibility of failure, not task category or risk classification.
- "Reversible and irreversible" are more useful governance buckets than "autonomous and human-supervised."
- An agent drafting an email for review is reversible (cost: seconds of review); one submitting a change order, modifying a customer record, or triggering procurement is irreversible and propagates downstream.
- Most client governance frameworks are backward: lightest controls where consequences are permanent, heaviest where error is contained.

## Relevance

Informs [reversibility](/concepts/reversibility.md), [AI Governance](/concepts/ai-governance.md), and [human-in-the-loop](/concepts/human-in-the-loop.md) as a design criterion for agent oversight.

## Quality

Practitioner blog post by David O'Hara. Clear and prescriptive; the central claim rests on a single vendor report, and the "ten minutes" mapping exercise is asserted rather than demonstrated.

## Entities Mentioned

- [Akamai](/entities/akamai.md) — publisher of the State of the Internet report whose recommendation anchors the post.

## Concepts Covered

- [reversibility](/concepts/reversibility.md) — proposed as the governing criterion for agent autonomy.
- [AI Governance](/concepts/ai-governance.md) — critiques risk-category frameworks and offers a design-principle alternative.
- [human-in-the-loop](/concepts/human-in-the-loop.md) — drafting-with-review is the post's example of a reversible regime.
