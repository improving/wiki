---
type: Reference
title: "Social Capital in the Age of Autonomous Agents"
resource: "https://www.devlinliles.com/social-capital-in-the-age-of-autonomous-agents/"
author: "Devlin Liles"
published: '2026-06-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The Corporate Currency framework I developed in my VP years was about the informal economy of human trust in organizations: how it is earned, spent, and depleted, and why commitment failures are the most expensive action in the system.

When I developed it, I was thinking about humans navigating relationships with other humans. I have recently started applying the same framework to how organizations navigate their relationship with AI systems — and the parallels are more direct than I expected.

## The Problem of Extending Trust

In the Corporate Currency framework, you extend trust — giving someone authority, autonomy, or responsibility — in proportion to the Social Capital they have accumulated. You do not give a new hire authority over a critical system without observing their judgment first. You do not extend a vendor large discretionary budgets without a track record. The trust is earned, incrementally, through demonstrated reliability.

Extending trust to autonomous AI systems requires the same logic, but most organizations violate it in the same direction: they extend too much trust too fast, without the track record that should precede it.

The 8-Stage AI Trust Evolution is, at its core, a framework for earning trust incrementally. Stage 2 (AI as tool, human reviews everything) is zero autonomous trust extended — the AI earns no independent authority. Stage 3 (task agents with quality gates) is limited trust extended within defined boundaries, with infrastructure that constrains the consequences of error. Each stage extends more trust, earns it through demonstrated reliability at the previous stage.

## The Commitment Accounting Parallel

In the Corporate Currency framework, broken commitments are the most expensive action. Each time you fail to do what you said you would do, the trust balance depletes at a rate that exceeds the value of the original commitment.

Autonomous AI systems make commitments of a kind: they are deployed to perform defined tasks reliably. When they fail — particularly when they fail in ways that produce visible consequences (wrong data sent to a customer, a production system modified outside its defined scope, a report distributed with fabricated facts) — the trust balance depletes sharply.

Organizational confidence in autonomous AI is the social capital of the AI system. It is earned through consistent, reliable behavior within defined scope. It is depleted, rapidly, by high-profile failures. And like human social capital, it is much harder to rebuild than to maintain.

## The Governance Infrastructure as Trust Bank

The governance infrastructure I recommend for autonomous AI systems — audit trails, boundary enforcement, quality gates, human approval points — is, in Corporate Currency terms, the infrastructure that keeps the trust balance from depleting.

Without audit trails, a failure is invisible until it produces consequences. The social capital depletion comes from the consequences, not from the failure that caused them. With audit trails, the failure is visible at the source, before consequences cascade, and the organization can respond before the social capital hit lands.

Without boundary enforcement, an agent that encounters an edge case can take actions that exceed its intended scope. The social capital hit from an out-of-scope action is catastrophic — it signals that the system cannot be trusted to stay in its lane. With boundary enforcement, the agent cannot exceed its scope regardless of what it encounters. The lane is guaranteed.

Quality gates and human approval points are the commitments the AI system makes that it can actually keep: "this output has been validated against these criteria before it reached you" and "this action was approved by a human before it executed." These are the commitment closes that build trust incrementally.

## The Look-at-Me Tax Applied to AI Adoption

One more parallel worth naming: the organizational tendency to announce AI adoption as a transformation when the actual deployment is still early-stage.

In Corporate Currency terms, claiming a win before it is fully earned applies the look-at-me tax: the announcement costs social capital even as it tries to earn it, because the audience knows the gap between the claim and the current state.

Organizations that announce "AI transformation" while still at Stage 2 of the AI trust evolution, or that over-claim the capabilities of their early governance infrastructure, are drawing on credibility they have not yet accumulated. When the system performs below the announced level — as early-stage systems often do — the social capital hit from the gap between claim and reality is more damaging than if no claim had been made.

The more sustainable path: deploy, demonstrate reliability within defined scope, earn trust through accumulated track record, then extend the scope. Let the AI system's track record make the announcement.

---

*Part of the *[*Thought Leadership series*](https://www.devlinliles.com/tag/thought-leadership/)* — Overlap: Thread 1 × Thread 3.*
