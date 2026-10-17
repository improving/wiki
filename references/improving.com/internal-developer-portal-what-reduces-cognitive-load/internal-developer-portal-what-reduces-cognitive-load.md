---
type: Reference
title: "Internal Developer Portal (IDP): What Reduces Cognitive Load"
resource: "https://www.improving.com/thoughts/internal-developer-portal-what-reduces-cognitive-load/"
author: "Atulpriya Sharma"
published: '2026-07-23'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

At KubeCon London, I spoke about [Abstraction Debt](https://youtu.be/M5X5NCzlzIA?si=ekZaMx7BjB1SdGpF) – the idea that every abstraction or simplification you add to a platform becomes a blocker later on. At the end of the session, the most common consensus was “this happened to us as well!”

Everyone’s story was exactly the same. They all had a full fledge platform in place – [golden paths](https://www.improving.com/thoughts/building-golden-paths/), service catalog, guardrails and a self-service mechanism for everything else. But when something failed, the developer had to go through the docs & logs because they didn’t know what broke. They file a ticket and wait. Eventually they SSH directly into the cluster to see what happened.

The platform didn't fail because it didn't exist. It failed because it was built to standardize tasks. And that’s the difference between an Internal Developer Portal (IDP) that reduces cognitive load and one that just relocates friction to a different address.

In this blog post, we'll explore where IDPs consistently break down, what patterns genuinely work, and why AI makes every unresolved failure mode significantly worse.

## Where IDPs Break Down

Most IDPs fail because they focus solely on standardization using golden paths and templates instead of considering the actual needs of the developers that use the platform eventually affecting their productivity. Enforcing consistency across teams is valuable, but not at the cost of productivity. Let us look at some of the scenarios where IDPs break down. These are edge cases, but they appear in every organization of every size and maturity.

### Golden Paths Nobody Uses

Golden paths fail when they're designed around the platform team's governance needs rather than the developer's actual workflow. The result is predictable:

- **Common case works fine -** the happy path is smooth, onboarding looks great, and early adoption numbers are encouraging
- **Every edge case becomes a ticket** - anything outside the 80% use case gets routed back to the platform team as a feature request or a workaround.
- **Developers route around the abstraction entirely** - when the platform costs more time than it saves, engineers make a rational decision and go back to kubectl directly and bypass the platform.

This is the golden cage anti-pattern. When you optimize so hard for standardization that real-world use cases don't fit, you haven't paved a golden path, you've built a wall.

### Abstractions that hide context instead of complexity

Good abstractions reduce the decisions a developer has to make. They don't eliminate the developer's ability to reason about the system.

When a platform hides context instead of complexity, it creates confident deployments and helpless incident responses. Developers ship faster until something breaks, and then they're completely dependent on the platform team to interpret what happened.

This is what I called abstraction debt. Every layer you add to simplify the developer experience is a layer of context you're taking away. At some point, the debt comes due.

### Catalog That Became a Documentation Site

If there’s one feature in an IDP that is over-invested and under-delivered, it’s the service catalog.

Everything looks great at launch, services are listed, dependencies are mapped and associated owners and documentations are in place. The problem arises 6 months down the line when teams are reorganized, services are deprecated, entries become stale and nobody remembers to update the catalog.

A catalog that tells you a service exists but can't tell you its current health, who's on-call, or how to interact with it during a live incident isn't a platform feature, but a liability with a nice interface.

### Platform Team Structured as an Infrastructure Team

When a platform team sits deep in the infrastructure org, reports into SRE, and is measured on availability rather than developer velocity, the IDP they build reflects that positioning. It's reliable, well-engineered, and solves the problems the infrastructure team cares about. But it doesn’t focus on the problems the developers actually have. Such a platform team never really talks to the developers and builds a platform that they will never use. The organizational failure mode is predictable:

- No user research - features are built on assumptions, not observed pain
- No roadmap - priorities shift based on whoever filed the last ticket
- No outcome metrics - success is measured in uptime and throughput, not developer velocity

A team without direct developer contact, a product roadmap, and outcome-based metrics is only an infrastructure team with a portal.

### Shipping Features but Not Outcomes

Platform teams that measure success in portal logins, catalog registrations, and golden path completions are measuring activity, not outcomes. 90% golden path adoption looks excellent in a quarterly review but it tells you nothing about whether cognitive load went down. During reviews, nobody has answers to the following questions:

- Did developers make fewer decisions this quarter because the platform made them on their behalf?
- Did incidents go down?
- Did lead times improve?

The vanity adoption numbers are covering for a platform that hasn't delivered on its actual promise yet.

## What Actually Reduces Cognitive Load

All the failures that we discussed in the earlier section solved the platform team’s problem rather than reducing a developer’s cognitive load.

We’ll now look at the patterns that actually work. When implemented consistently, they reliably reduce the decisions a developer has to make that have nothing to do with business logic.

One thing to remember is that cognitive load reduces when the platform absorbs the decisions.

### Self-service that completes the workflow

Almost all the IDPs are good at provisioning; that’s the easiest part. But what happens after that is where most IDPs fail.

A developer provisions a service, deploys successfully, and then hits their first incident. Rollback? Ticket. Scaling? Ticket. Observability context for what broke? Another tab, another tool, another mental context switch.

The platform solved Day 1 and abandoned Day 50, that’s the problem. To address this problem, I wrote a blog post - [*What Nobody Tells You About Golden Paths at Scale *](https://www.improving.com/thoughts/what-nobody-tells-you-about-golden-paths-at-scale/), where I focused on how the real operational decisions compound after deployment and exactly where a platform either absorbs them or pushes them back onto the developer.

### Clear Feedback Baked into the Platform

Clear feedback and outcome to tasks was identified as the platform’s capability that most correlated with a positive developer experience as per a [DORA's 2025 research.](https://dora.dev/capabilities/platform-engineering/)

Logs, deployment status, diagnostics were present where the developer already is, not in a separate dashboard they have to navigate to every time they were debugging an issue. Every time a developer hits a failure and gets nothing actionable back from the platform, they mentally file it as something to work around rather than work with.

Instead, platforms must give clear error messages and updates to developers. This early and correct feedback helps them debug and move faster.

### Escape Hatches Alongside Golden Paths

A platform is used by a diverse group of developers. For some the golden path suffices, but for a few, especially the architects, they need flexibility and that’s where these escape hatches help – *abstractions that help both junior developers and architects alike.*

Teams that fit the standard workflow move fast. Teams that don't are either stuck waiting for a new path to be paved or quietly building shadow infrastructure outside the platform entirely. Escape hatches help keeping the platform relevant for teams with legitimate edge cases.

### Opinionated Defaults with Visible Reasoning

Platforms were built to reduce the cognitive load of developers and one way they do this is by taking decisions on behalf of the developers – which policies to apply, what resources limits to set, which region to deploy etc.

But a decision taken without valid reasoning is a rule.

Developers don't resist rules. They resist rules they don't understand. When a Kyverno policy blocks a deployment with no explanation, the developer's first instinct is to find a way around it. When the same policy explains what it enforced and what needs to change, the developer has enough context to act.

### Platform as a Product, With Organizational Structure to Back it

A platform without product discipline isn't a platform, it's infrastructure with a portal on top. The platform as product thinking is critical. Without regular contact with developers, they build toward technical elegance rather than reduced friction. Features get prioritized based on what's interesting to build, not what removes the most decisions from a developer's day. Fixing this requires org structure to back it:

- A roadmap shaped by developer pain, not infrastructure priorities
- User research and developer interviews as a regular practice, not a one-time exercise
- Adoption signals that measure outcomes - time to first deploy, self-service completion rate, incident resolution time - not just usage

## When AI Meets a Platform that was Already Struggling

We all have embraced AI into our software lifecycles. Faster code generation, less boilerplate, more time for business logic, we’re using it everywhere to improve our productivity.

But with platforms, every problem that we discussed earlier, gets amplified with the introduction of AI. It doesn't know your platform is broken. It will generate code, raise PRs, trigger pipelines, and provision infrastructure regardless. And it will do all of that faster than your platform team can respond, thus scaling your platform troubles at a rapid pace.

### AI Amplifies Platform Dysfunction

Leaky abstractions are the most affected ones. Stale catalogs get referenced more confidently, leading to incorrect outputs. Ungoverned pipelines process more changes with less human review. The platform was already struggling to absorb decisions. AI just increased the volume and the velocity of everything flowing through it.

The teams seeing real productivity gains from the AI are the ones who had a solid platform foundation before they started using AI.

### Your Platform Was Built for Human Actors

AI agents are everywhere, they now raise PRs, provision infrastructure, and trigger pipelines. None of that was in the design model when most IDPs were built.

Your golden paths assume a human is deciding which path to take. Your RBAC assumes a human identity is behind the request. Your audit logs assume someone accountable initiated the action. When an AI agent is the actor, all of those assumptions break - quietly, with no error message.

### Governance Gap is Now a Production Risk

An agent is configured to handle routine infrastructure tasks. It has broad access because the developer who set it up had broad access. There are no scoped permissions, no audit trail distinguishing agent actions from human ones, no policy layer that understands the difference between a developer making a deliberate decision and an agent executing a workflow autonomously.

Three weeks later, the agent calls an external API it shouldn't have access to. Nobody notices until a security review six weeks after that.

This isn't hypothetical. It's the default state of most organizations adopting AI tooling without extending their platform governance model to cover it. Read more about it in my previous blog post on [*Your Most Privileged User Isn't Human*](https://www.improving.com/thoughts/platform-security-governance-ai-agents/).

### Prompt Fatigue Is the New Cognitive Overload

Adding AI to platform means developers now manage prompts, context windows, agent outputs, tool permissions, and hallucination validation - on top of the infrastructure decisions the platform was supposed to have already absorbed.

If the platform has no opinionated integration layer for AI tooling, every developer is making those decisions individually, inconsistently, and without guardrails. That's not productivity. That's a new class of cognitive load wearing a productivity hat.

## Summary

Platform engineering is maturing. The tooling is stable, the patterns are documented, the community is large. And yet the core problem - cognitive load on developers - remains largely unsolved in most organizations.

The next phase of platform engineering isn't about better tooling. It's about better questions. Not "did we ship the catalog?" but "did we absorb a decision?" Not "what's our golden path adoption rate?" but "what's our escape velocity?" Not "is the platform available?" but "do developers trust it?"

Connect with [Improving's platform engineering team](https://www.improving.com/contact/) if you're thinking through where your platform stands - or find me on [LinkedIn](https://www.linkedin.com/in/atulpriyasharma/).
