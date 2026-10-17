---
type: Reference
title: "What Is an Enterprise AI Operating Model and How Do You Build One"
resource: "https://www.improving.com/thoughts/enterprise-ai-operating-model/"
author: "Devlin Liles"
published: '2026-10-08'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Ask ten organizations what their AI governance looks like, and in my experience eight will describe a code review policy. That answers a real question, but only one-eighth of it: one stage of an eight-stage delivery loop.

An AI operating model is the full answer to a single question, asked repeatedly at every stage where work moves through your organization.

*Who has the authority to decide, and what happens when that decision turns out to be wrong.*

Most organizations have answered that question rigorously for exactly one stage. The other seven go ungoverned by default because nobody was ever asked to decide anything about them.

## What an Enterprise AI Operating Model Includes

In formal terms, an enterprise AI operating model, sometimes called an AI governance operating model, is the set of decision rights and enforcement mechanisms that determine who has authority over AI-assisted work at each stage of the delivery loop. It also settles what happens when a decision made or influenced by AI turns out wrong.

In practice, it takes the form of a stage-by-stage assignment of accountability, backed by tooling that enforces it. It works alongside an AI governance framework: the framework lists the controls an organization should have, and the operating model assigns who invokes them at each stage.

## **Why AI Operational Governance Matters**

Without AI governance checks in place, it is almost impossible to find the root cause of an incident involving an AI system. A useful signal, such as a risk score or an anomaly flag, turns into something a team either blindly trusts or reflexively ignores.

Both failure modes trace back to one gap: authority that was never assigned. We cover this pattern in our series on why AI projects fail, where [ignoring ethics and compliance](https://www.improving.com/thoughts/top-reasons-ai-projects-fail-10-ignoring-ethics-and-compliance/) ranks as a top cause.

## **Loop Underneath the Question**

AI now touches every phase of the software development lifecycle, and that lifecycle runs as a continuous loop: Plan, Code, Build, Test, Release, Deploy, Operate, Monitor, and back to Plan, informed by whatever Monitor surfaced.

Every stage in that loop has its own AI leverage point. Here is the same loop through the lens of AI accountability: who owns the decisions AI now makes or assists at each stage, and how was that ownership assigned?

### **Plan**

An AI system that flags a requirement as ambiguous, or surfaces a contradiction with existing system behavior, is making a substantive judgment call about what the team builds next.

Who owns the decision to accept or override that judgment? In most organizations I've evaluated, the answer is whoever happened to be looking at the screen when the flag appeared.

### **Release**

A risk score that recommends holding a deployment based on the blast radius of the changes involved is a governance decision wearing the clothes of a dashboard number.

Somebody has to own the authority to override that score, under defined circumstances and with documented reasoning. Without that, the score is a number nobody is accountable for.

### **Operate and Monitor**

Of everything in the loop, these are the two stages I see least governed.

When an AI system compares an incident with past cases and recommends a fix, it is making a judgment while the on-call engineer is under pressure and may not have time to question it. If the team has not decided in advance how much authority that recommendation carries, the engineer will either follow it without scrutiny or ignore a good one out of doubt.

Working through this stage by stage with clients is most of what our [AI adoption and transformation](https://www.improving.com/expertise/ai/adoption-transformation/) practice does before we touch a tool or a team structure. Code, Build, Test, and Deploy raise the same question, and the next section shows why each can need a different answer.

## AI Decision Rights Differ at Every Stage of the Loop

After an organization notices this gap, the natural instinct in enterprise AI governance is to centralize everything under one governance board and one set of rules for all eight stages. That instinct is understandable, but the stages differ, and each requires a different kind of decision.

**Common mistake:** Treating Plan and Code as if they need the same governance model. A central board adjudicating both will get at least one of them wrong because it does not know the other's working context.

**Plan and Release decisions carry organization-wide risk: **An unclear requirement that reaches production can create a defect whose cost grows as it moves downstream. A release risk score, meanwhile, can affect production systems that other teams and customers depend on. These are the stages where centralized decision-making makes sense, with a small accountable group that has the authority to say no.

**Code, Build, and Test decisions are usually team-specific: **What acceptable AI-assisted coding looks like for a Java monolith is different from what works for a set of independently deployed services. These stages benefit from a federated governance model, where the team closest to the code makes the call within broad guardrails. This often works better than having every decision reviewed and approved centrally.

**Deploy, Operate, and Monitor sit in between:** This is where many operating models get sloppy. The policy for when a canary deployment should automatically roll back is a central decision because the definition of "unsafe" should not vary from team to team. But the specific thresholds and the meaning of an anomaly depend on the context of each system, which the central board may not fully understand.

The right approach is a hybrid: central policy and local execution, with a written definition of where each begins and ends.

Most of the failures I see at this stage come from one omission: nobody wrote down whether central policy or local judgment applies at a given moment, so both sides assume the other is covering it.

## AI Governance Mechanisms Make Decision Rights Real

A decision right that lives only as a sentence in a document must be instrumented to mean anything. Otherwise it decays, which is the same failure as an unowned Plan-stage decision.

- **Centralized decision needs a gate:** The release does not proceed without a recorded sign-off from the accountable party.
- **Federated decision needs a documented boundary:** What the team can decide without escalation and what triggers one, specific enough that a new team member can read it and know which category a given choice falls into.
- **Hybrid decision needs something different again:** An explicit handoff point, the exact condition under which a locally scoped judgment call becomes something that requires the central policy instead.

We worked with a mid-cap enterprise software company that found this out directly at the Code stage. Their vulnerability-scanning process was tuned to catch the mistakes human developers typically make. What we found once AI-assisted coding scaled across their engineering org: the vulnerabilities showing up were a different shape entirely, and a review process built for one risk profile was structurally blind to the other. The fix was a persona-based compliance agent wired directly into the CI/CD pipeline, a standing reviewer that could hold a pull request the same way a human gatekeeper would, in the spirit of [platform governance for non-human identities](https://www.improving.com/thoughts/platform-security-governance-ai-agents/), so the decision right about what's safe to merge had an actual mechanism enforcing it instead of a paragraph describing it.

**Instrumentation beats documentation:** Take two organizations with the same governance policy. The one that wires it into the pipeline has a decision right that holds. The one that leaves it as a paragraph has a right that exists only on the days someone remembers to check.

## Feedback Loop Is Where the AI Operating Model Meets the Technology Stack

The loop closes. What Monitor learns is supposed to inform the next round of Plan, and that only happens when the operating model includes a working mechanism connecting the two.

That mechanism has to answer one question. When Monitor surfaces a pattern, such as a recurring incident type or a class of requirement ambiguity that keeps producing the same downstream defect, who has the authority to change how Plan works, and through what channel does that change get made?

If the answer is "someone should mention it in a retro," the loop is decorative rather than closed. Organizations can have genuinely sophisticated monitoring and genuinely thoughtful planning practices that never connect the two, because nobody owned the connective tissue between them, and the operating model on paper implied a loop that the actual technology stack had no wiring to support.

This is also where the operating model has to reach down into the platform engineering itself.

- A decision right for Release only means something if the deployment pipeline actually enforces the gate it implies.
- A federated Code-stage boundary only means something if the tooling gives a team the latitude the boundary promises. If everything still routes through a central review queue, the boundary promises more than the tooling delivers. Our post on [building golden paths](https://www.improving.com/thoughts/building-golden-paths/) explores this further.

The operating model has to be true in two places: the policy and the configuration of the systems that execute it. The gap between the two is usually where an audit finds discrepancies.

## Centralized, Federated, or Hybrid AI Governance Depends on the Stage

Resist any framing that asks an organization to pick one of the three models and apply it uniformly. The question that determines the right answer has two parts: how much organization-wide risk does a decision at this stage carry, and how much does it depend on knowledge only the local team has? The answer differs at Plan, at Code, and again at Operate.

An AI operating model that is centralized everywhere recreates the bottleneck problem at every stage where local knowledge matters. One that is federated everywhere recreates the ungoverned-stage problem at every point where organization-wide risk exists. A working AI operating model is a stage-by-stage answer, documented and instrumented. A single governance philosophy stamped across all eight stages is easier to put on a slide, and that is its only advantage.

Most organizations I evaluate have governed the one stage where a vendor happened to ship a tool, which is usually code review. The other seven are waiting for someone to ask the same question about them: who decides, and what happens when the decision is wrong. That question, answered eight times instead of once, is the operating model. Everything else is an org chart. People draw it because the question feels too granular to ask stage by stage, right up until the ungoverned stage produces the incident.

Pick the stage in your delivery loop that AI has touched most recently (Plan, Code, Release, and Operate are common ones) and ask who holds the decision right there today. Ask who a new hire would learn to go to if that decision turned out wrong last quarter, whatever the org chart says. If the answer is "whoever happened to be looking at the screen," you have found your next stage to instrument before an incident finds it for you.

Which stage in your loop would fail that test right now?

If naming the owner took more than a few seconds, that stage is where to start. Improving's AI team maps who holds each decision right across your delivery loop and helps you instrument the stages where nothing enforces it. You can see how we approach this on our [AI expertise page](https://www.improving.com/expertise/ai/), or begin with an [AI assessment ](https://www.improving.com/resources/ai-readiness-assessment/)of your own delivery loop.

## **FAQ**

**Do we need to instrument all eight stages before this is worth doing?**

No. Start with the one stage where an AI-influenced decision already went wrong, or where you can't name who owns it today. The framework is stage-by-stage by design, not an all-or-nothing rollout.

**What if our organization is too small for a centralized governance board?**

The size of the group matters less than whether it exists and has real authority to say no. A two-person accountable group with actual sign-off power beats a large committee with none.

**How is this different from a standard AI governance framework or compliance checklist?**

Most compliance frameworks (ISO 42001, NIST AI RMF) describe what controls should exist. This is about who holds the authority to invoke those controls at each stage, and what mechanism actually enforces that authority day to day.

**What happens if we skip the instrumentation step and just document the decision rights?**

The rights exist on paper only. The same accident-of-attention failure mode returns, because nothing in the actual pipeline or tooling enforces who decides.

If you want to work through where your own delivery loop is actually governed versus assumed, reach out through our [AI adoption and transformation](https://www.improving.com/expertise/ai/adoption-transformation/) page.
