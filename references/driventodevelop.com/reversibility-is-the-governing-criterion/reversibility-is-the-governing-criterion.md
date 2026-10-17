---
type: Reference
title: "Reversibility Is the Governing Criterion"
resource: "https://driventodevelop.com/2026/10/02/reversibility-is-the-governing-criterion/"
author: "David O'Hara"
published: '2026-10-02'
fetched: '2026-10-17'
tags: [blog, driventodevelop.com]
---

![Reversibility Is the Governing Criterion](images/reversibility-is-the-governing-criterion.jpg)

We've been asking the wrong question about AI agent governance. The right question isn't how risky is this agent. It's if this agent gets it wrong, can we undo it?

Akamai released its State of the Internet security report this week with a recommendation that stopped me: grant operational autonomy to AI agents based on how easily their actions can be verified and how reversible a potential failure is. Not based on task category. Not based on department or risk classification. Based on reversibility. That reframe matters because it gives practitioners an actual design principle rather than a bureaucratic category. Autonomous and human-supervised are not useful governance buckets when you're deploying agents in production systems. Reversible and irreversible are.

Think through what this means in practice. An agent that drafts an email for human review is operating in a reversible regime. If it gets it wrong, the human catches it before it goes anywhere. The cost of a mistake is a few seconds of review time. An agent that submits a change order to a financial system, modifies a customer record, or triggers a procurement workflow is in an irreversible regime. A mistake there doesn't wait for review. It propagates downstream through whatever depends on it.

The governance burden scales with reversibility, not with autonomy level. An agent doing highly autonomous work in a reversible context (drafting, summarizing, preparing) needs less oversight than an agent doing limited work in an irreversible one (approving, committing, triggering). Most governance frameworks I've seen in client environments have this backward: they apply the lightest controls where the consequences are permanent and the heaviest controls where the risk of error is contained.

Map your current agent deployments against reversibility, not risk category. You'll find the governance mismatches in about ten minutes.
