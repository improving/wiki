---
type: Reference
title: "The Most Important Person in Your AI Governance Program Isn&#x27;t in Your C-Suite"
resource: "https://www.devlinliles.com/the-most-important-person-in-your-ai-governance-program-isnt-in-your-c-suite/"
author: "Devlin Liles"
published: '2026-07-18'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Most Important Person in Your AI Governance Program Isn't in Your C-Suite

The AI governance org charts I see most often look the same. Board oversight at the top. A CAIO or CTO in the middle. A cross-functional council below that. Legal, InfoSec, HR, a few business leads. Lines connecting everyone. Approval workflows labeled by risk tier.

The chart is correct. Those roles are real. The council should exist.

What the chart is almost always missing is the person closest to the work.

I've reviewed governance frameworks that specify, in careful detail, who approves a high-risk AI deployment and what the escalation path looks like. The same framework has nothing to say about who finds out when the deployed workflow starts producing wrong answers at step seven of an agent chain. That gap is where most AI programs quietly fail. The approval process worked. The deployment went live. No one was close enough to the work to catch what was going wrong.

**Two tiers, both required**

An active AI governance program needs two distinct organizational layers.

The first is the governance layer: the people accountable for policy, risk, and oversight at the enterprise level. At the top sit the Board and executive committee (risk appetite, AI posture attestation), a Chief AI Officer or equivalent (approving above-threshold use cases), and the CRO (risk register, escalation authority for high-risk deployments). Underneath: the CISO managing non-human identity provisioning and shadow AI, the Data Privacy Officer owning EU AI Act compliance and vendor data agreements, and the Enterprise Architect maintaining the AI system inventory and mapping deployments to business processes.

None of these roles are new. Most mature organizations can fill them. What's new is the AI-specific scope. A CISO who has spent a career thinking about human identity now has to think with the same rigor about agent identity. An EA who managed system architecture maps now needs an AI inventory that covers shadow deployments and the AI features embedded in SaaS platforms your teams didn't tell IT about.

The second layer is operational, and this is where most frameworks are thin.

A cross-functional AI Governance Council reviews use cases, resolves tradeoffs, and signs off on deployments above a defined risk threshold. For organizations actively deploying, bi-weekly is right. Reactive councils that only convene when someone submits a request don't govern; they react.

Below the council, and more important in practice, is the AI Champion.

**The AI Champion is the governance mechanism that works**

One per automated workflow. A designated front-line employee who pilots the agent, reviews its failures on a weekly cadence, updates the skill definition, and iterates until satisfaction reaches roughly 95%. Only then does the workflow publish org-wide.

This role is the most undervalued position in enterprise AI right now, and I say that having watched a lot of governance programs succeed and fail. The AI Champion converts governance from a top-down mandate into a ground-level quality signal. They are close enough to the work to recognize when the output is subtly wrong before it compounds. They have enough context to fix it. They have the organizational standing to hold the rollout until the work is actually ready.

Organizations that have AI Champions are catching problems in the iteration phase. Organizations that don't are finding them in production: in front of customers, in regulatory submissions, in finance processes where an error compounds across forty records before anyone notices.

The governance layer sets the policy. The AI Champion enforces the reality.

**The intake process that prevents bad deployments**

Before a workflow reaches an AI Champion, it has to pass an intake process. Two filters matter most.

The first is the complexity-versus-difficulty distinction. AI handles complexity well — a well-defined checklist where correct execution is deterministic. AI handles difficulty poorly — contextual interpretation, weighing tradeoffs with incomplete information, reading a situation that doesn't fit prior patterns. Every proposed use case has to be assessed against this distinction. Workflows that require difficulty judgment need mandatory human-in-the-loop routing, full stop.

The second is demand constraint. Is demand for this workflow's output bounded or unconstrained? Payroll runs twelve times a year — constrained. Sales outreach and code generation are unconstrained. AI can produce volume that was never possible before. Map this before you build, because the resource implications of getting it wrong are significant.

**Human-in-the-loop is a design decision, not a feeling**

For each approved use case, the governance process has to define explicitly and technically: what the agent does autonomously, what triggers a human review, and what always routes to a human regardless of what the agent produces.

This cannot be vague. "Sensitive decisions go to a human" is not a governance boundary. "Any external communication containing a dollar figure above $10,000 routes to a human before sending" is a governance boundary. The difference between those two statements is the difference between a policy and a control.

The rule we apply in our client work: AI does not communicate with external humans on the company's behalf. Conditions, negotiations, and exception cases always route to a person. That boundary is blunt, and it means some workflows are less automated than they theoretically could be. It also means the failure modes are contained and manageable.

The governance program that works is the one with explicit boundaries, an AI Champion watching the deployed system weekly, a council that meets whether or not there's a pending request, and an escalation path that activates before anyone needs to convene an emergency review.

---

*Part 3 of this series: the tooling stack — four layers, and where most enterprises actually are on each.*
