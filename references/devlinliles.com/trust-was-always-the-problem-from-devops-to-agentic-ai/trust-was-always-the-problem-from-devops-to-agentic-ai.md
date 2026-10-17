---
type: Reference
title: "Trust Was Always the Problem: From DevOps to Agentic AI"
resource: "https://www.devlinliles.com/trust-was-always-the-problem-from-devops-to-agentic-ai/"
author: "Devlin Liles"
published: '2026-07-11'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

When I look back at the decade of DevOps adoption, the honest explanation for why it stalled in so many organizations has nothing to do with tooling. Jenkins worked. Git worked. Docker worked. The tools were not the limiting factor.

Trust was the limiting factor.

Specifically: developers did not trust that an automated pipeline would do the right thing. Operations teams did not trust that developers' code was ready to deploy. Leadership did not trust that "we deploy on Fridays now" would not produce a crisis. The entire manual handoff culture of pre-DevOps software delivery was a trust management system. Slow, expensive, and frustrating — but it produced legible accountability. Someone signed off. Someone was responsible.

Automation threatened that. The solution was not better automation. The solution was building the trust infrastructure that made automation safe to rely on: automated tests that developers trusted, deployment pipelines with observable outcomes, rollback mechanisms that made failure recoverable, monitoring that made the post-deployment state visible. DevOps matured when organizations built the governance infrastructure that made the automated systems trustworthy.

## The Same Pattern Is Running in Agentic AI

Every conversation I have with senior leaders about agentic AI adoption follows the same structure. The capability question is answered quickly: yes, the AI can do that. Then the conversation stalls.

It stalls on trust.

Can we trust that the agent will stay within its intended scope? Can we trust that it will not take an irreversible action we did not intend? Can we audit what it did and why? If it goes wrong, can we recover? Who is responsible when an autonomous system makes a mistake?

These are not technology questions. They are governance questions. And they are the same questions that stalled DevOps adoption — restated for a more capable, more autonomous class of system.

## The 8-Stage Trust Evolution

The model I use for thinking about this is the 8-Stage AI Trust Evolution:

**Stage 1: AI as reference.** AI is a search tool. No autonomy. No trust required beyond "is this information accurate enough to inform my thinking?"

**Stage 2: AI as assistant.** AI drafts, suggests, generates. Human reviews and decides. Trust is required at the output level: is this good enough to use?

**Stage 3: AI as task agent.** AI takes a defined task and executes it with minimal human oversight. Trust is required at the process level: can I rely on the agent to stay within bounds and flag exceptions?

**Stage 4: AI as workflow coordinator.** AI manages multi-step workflows, delegating to other tools and agents. Trust is required at the integration level: can I rely on the handoffs between systems?

**Stage 5: AI as domain operator.** AI operates within a domain with significant autonomy, escalating to humans at defined thresholds. Trust is required at the governance level: are the thresholds right? Are the escalations landing in the right places?

**Stage 6: AI as cross-domain coordinator.** AI orchestrates across multiple domains with peer coordination. Trust is required at the architecture level: are the agent boundaries well-designed? Is the coordination protocol sound?

**Stage 7: AI as enterprise system.** AI operates as an enterprise-scale system with meta-coordination and strategic alignment functions. Trust is required at the institutional level: does the system reflect the organization's actual values and risk tolerance?

**Stage 8: AI as organizational nervous system.** AI is embedded in the organization's core operating model. Trust is required at the existential level: what is the organization's relationship with this system?

Most organizations are at Stage 2 or 3. The organizations that are stalling are not stalling because they cannot get the technology to Stage 4 or 5. They are stalling because they have not built the trust infrastructure that makes Stage 4 or 5 safe to operate.

## Building the Trust Infrastructure

The parallel to DevOps is instructive because DevOps gives us the template:

**Observability first.** You cannot trust what you cannot see. Before extending autonomy, build the observability infrastructure that makes the agent's actions visible, auditable, and interpretable. This is the equivalent of application performance monitoring in the DevOps era — a precondition for trust, not an afterthought.

**Reversibility as a design constraint.** The DevOps practice of blue-green deployments and feature flags was fundamentally about making deployment reversible. The same constraint applies to agentic AI: design agent actions to be reversible where possible, and require explicit human approval before irreversible actions. Stacking errors compound in irreversible pipelines.

**Boundary enforcement before capability extension.** DevOps teams learned to define deployment environments with explicit, enforced boundaries — what production could and could not access, what the build pipeline could and could not touch. Agent boundaries require the same rigor: what data can this agent see, what systems can it modify, what actions can it take without escalation?

**Governance as a feature, not overhead.** The organizations that successfully scaled DevOps were the ones that treated governance infrastructure — audit trails, change management, incident post-mortems — as features of the delivery system rather than friction on top of it. The same reframe is required for agentic AI: the governance infrastructure is the capability that makes everything else trustworthy.

The organizations that move fastest with agentic AI will not be the ones with the most aggressive deployment timelines. They will be the ones that build trust infrastructure with the same intentionality they brought to building DevOps infrastructure — and then extend autonomy incrementally as that trust is earned.

Capability was never the bottleneck. It wasn't in 2015 with DevOps, and it isn't now.

---

*Part of the *[*Thought Leadership series*](https://www.devlinliles.com/tag/thought-leadership/)* — Overlap: Thread 2 × Thread 3.*
