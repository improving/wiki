---
type: Reference
title: "What Nobody Tells You About Golden Paths at Scale"
resource: "https://www.improving.com/thoughts/what-nobody-tells-you-about-golden-paths-at-scale/"
author: "Atulpriya Sharma"
published: '2026-01-22'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

Your platform team just celebrated hitting 85% golden path adoption. Everyone is excited. Onboarding time for new members dropped from three weeks to two days. New services spin up in minutes. Leadership loved the improved metrics.

Six months later, you've got 23 capability requests in your backlog. Your platform team is drowning with requests. ML folks need custom GPU scheduling. Data team wants streaming pipeline patterns. API teams are building their own rate limiting because yours doesn't fit their needs.

You nailed Day 1. You're dying on Day 50.

This is the hidden scaling problem with golden paths. And it's not going away by building more golden paths.

## Golden Path Promise vs What Actually Happens

The platform engineering playbook says golden paths reduce cognitive load and bring in the much-needed standardization across teams. They give developers a blessed path from code to production in a self-service way which also speeds up feature development.

It works well for most scenarios, especially for onboarding newer members to the team. C[reating new projects and features is maybe 1% of an application's lifetime](https://platformengineering.org/blog/how-to-pave-golden-paths-that-actually-go-somewhere). The other 99% are operations, debugging, scaling, adding features, and dealing with edge cases.

Golden paths excel at first 1%. They're still not up to the mark for the rest. [Netflix learned this the hard way.](https://www.youtube.com/watch?v=36FcxlPerdQ) They built a beautiful developer portal. Documentation, recommended tools, curated paths. Their developers said it "wasn't compelling enough" to change their habits. Why? Because the portal helped them *start* things, not *run* things.

The real work happens after deployment. That's where the pain is. And that's where centralized golden paths become bottlenecks.

## Why Your Platform Team Hits a Ceiling

Your platform team can't scale linearly with your organization. It's math.

Say you've got 200 engineers across 20 teams. Each team has different needs:

- ML team needs GPU scheduling, Kubeflow integrations, model serving patterns
- Data engineering wants Kafka, Airflow, stream processing
- API teams need advanced rate limiting, circuit breakers, distributed tracing
- Mobile backend needs push notification infrastructure

Your platform team has 6 people. They're good generalists. But they're not ML experts, data experts, or mobile experts.

So what happens?

- **Queue problem:** Every capability request goes through your platform team. Typically, teams prioritize on the basis of who screams loudest, not what creates most value. High-impact capabilities wait behind simple requests because simple is faster to ship.
- **Expertise problem:** You build "good enough" solutions. The ML team knows they need 12 specific GPU configurations. You give them 3 because that's what you have time to build and maintain. It checks the box. It doesn't solve their problem. Similarly, the security team has implemented auth service with best practices, but your platform team builds something that’s not up to the mark for them.
- **Maintenance trap:** You ship 30 capabilities over two years. Now you maintain all 30. Kubernetes upgrades? You're updating 30 capability configs. Security patch? 30 capabilities to test. The team that asked for capability #17 moved to a different project. You're stuck with it forever.
- **Rigidity issue:** You built abstractions for the 80% use case. The other 20% either fight your platform or route around it. I talked about this at [KubeCon London - it's "abstraction debt](https://www.infracloud.io/blogs/measuring-managing-abstraction-debt/)." The simplification you built yesterday becomes the blocker today.

Your platform team becomes the bottleneck for every capability, every edge case, every new tool the organization needs. And that's not sustainable in the long run.

## Go with Marketplace Approach

At KubeCon Atlanta, I discussed a different model. Why should your platform team become the bottleneck in the process? Why not turn your platform into the marketplace?

At a particular point, the platform team should stop being the sole provider. They should focus on becoming the marketplace operator and let developer teams contribute capabilities back to the platform.

For instance, the ML team builds GPU scheduling patterns. The data team contributes streaming pipelines. The API team creates their rate limiting solution and the security team can contribute their authorization solution.

This way, your platform provides the infrastructure for contribution, not the capabilities themselves.

### How IDP Marketplace Model Works

- **Define clear interfaces:** Your platform exposes APIs for capability integration. A team building a new capability knows exactly what to implement: health checks, metrics endpoints, deployment patterns.
- **Build contribution templates: **Don't make teams figure out how to package their capability. Give them scaffolding. "Here's how you wrap your thing so it plugs into the platform."
- **Automate validation**: When someone contributes a capability, automated tests check if it meets standards. Does it expose metrics? Does it pass security scans? Does it have documentation?
- **Create recognition systems**. Contribution isn't charity work. It's valuable engineering. Track it. Reward it. Make "shipped capability used by 5 teams" count in performance reviews.

### Advantages of IDP Marketplace Model

- Multiple teams building simultaneously instead of queuing behind your platform team. The ML capability ships in parallel with the streaming pipeline.
- Deep domain expertise embedded in each capability. The ML team knows what GPU configurations matter. Your platform team doesn't need to become GPU experts.
- Your platform team focuses on primitives, not products. You build the contribution framework, the validation pipeline, the quality standards. Not every database connector under the sun.
- Network effects. More contributors means more capabilities. More capabilities means more value. More value means more adoption.
- Organizations running mature marketplace models see 3-4x faster capability development compared to centralized teams. The scaling is parallel, not linear.

## But Here's the Part Nobody Talks About

It was interesting to know that after my talk at KubeCon Atlanta, quite a few people reached out and discussed how their organization tried to implement a similar approach but had issues implementing it.

Below are some highlights from the discussions I had with them:

### Governance breakdown

No quality standards mean capability sprawl. You end up with 50 ways to deploy a database. All slightly different and broken in subtle ways.

Developers don't trust community capabilities. They either use your blessed golden paths or they build their own thing. The marketplace becomes a junk drawer.

One team told me they had three different Postgres operators contributed by different teams. None properly maintained. Developers gave up and just installed Postgres manually.

### Quality problem

A team contributes a capability. It works for their use case. They ship their product and move to the next project.

Six months later, there's a security CVE. Or Kubernetes upgrades and the capability breaks. Or another team tries to use it and discovers it only works if you have a specific network configuration.

Who fixes it? The contributing team is working on something else. Your platform team didn't build it. Nobody owns it.

The capability becomes orphaned. Other teams can't rely on it.

### Contribution friction

Your platform APIs are complex because your infrastructure is complex. Contributing a new capability requires understanding service mesh configurations, CI/CD pipelines, monitoring integrations, and security policies.

Only your senior engineers can navigate this. Contributions dry up because the barrier is too high.

### Maintenance nightmare

Software can get outdated if not maintained properly and develop risk surfaces.

Kubernetes 1.35 comes out. You need to update 40 contributed capabilities. Who does that work? A critical security patch drops. Who verifies every marketplace capability is patched? Production breaks at 3am because of a contributed capability. Who's on-call?

## Prerequisites for Making Marketplaces Work

Building a marketplace for platform capabilities may be a great solution to all your problems. But more often than not, teams aren’t prepared to adopt it. Hence, don't start with a marketplace if you don't have these foundations:

### 1. Platform Primitives that Make Contribution Possible

You have clear extension points with well-documented interfaces. A capability should plug in without requiring platform team code changes.

If adding a new database type requires your platform team to modify core infrastructure code, your platform isn't ready for marketplace.

### 2. Quality Standards with Enforcement

Automated testing requirements. Every capability must have health checks, metrics, and integration tests. The tests ensure that only the capabilities that meet the automated checks are sent to the platform team to review and approve.

Security scanning runs automatically on every contribution. At the same time, check for CVEs, detect exposed secrets and validate against security policies. If a capability fails security scans, it doesn't ship. No exceptions.

Documentation standards matter. Every capability needs a runbook, troubleshooting guide, and usage examples. If someone can't figure out how to use it or debug it, the capability isn't ready. Make the documentation accessible to everyone in the organization - not buried in a team wiki.

### 3. Ownership Model Beyond Initial Contribution

Define lifecycle management responsibilities upfront. Who updates this capability when Kubernetes versions change? Who patches security issues? Who provides support?

Define this before accepting contributions. "You built it, you own it for 12 months minimum" is a valid policy.

Establish clear deprecation policies. How do capabilities get retired? What's the migration path for teams using the deprecated capability? Document this process before you need it.

Handoff mechanisms. When the contributing team can't maintain it anymore, what happens? Does your platform team take it over? Does it get deprecated? Be explicit.

### 4. Cultural Readiness

Your organization needs an established inner-source culture. Teams should already contribute to shared libraries and tools. Don't make marketplace your first experiment in cross-team contribution.

Measure teams on cross-team impact. If capability contributions don't count toward team goals or performance reviews, contributions won't happen. Make it explicit in team objectives.

Get leadership support for contribution time. A team spending 20% of their sprint maintaining a marketplace capability needs air cover from their manager. If leadership sees contributions as "not real work," the marketplace will fail.

## Hybrid approach

One of the ways to implement this would be to not go full marketplace model but adopt a hybrid approach.

Your platform team maintains "golden capabilities" for the most common patterns. Databases, caching, message queues, basic API patterns. This covers 70-80% of teams.

Marketplace for specialized needs. GPU scheduling, streaming pipelines, ML model serving, advanced rate limiting. Domain-specific stuff where application teams have deeper expertise.

Clear capability tiers:

- **Platform-blessed:** Maintained by platform team, guaranteed SLAs, full support
- **Community-maintained:** Contributed by teams, supported by contributors, use at own risk
- **Experimental:** Proof-of-concepts, no stability guarantees

Teams know what they're signing up for. Nobody's surprised when an experimental capability breaks.

## Next Step for You

If you're hitting golden path scaling problems:

- **Audit your backlog:** How many requests are domain-specific? How many could be built by application teams if they had a way to contribute?
- **Identify teams with deep expertise: **Which teams keep asking for capabilities your platform team doesn't understand well?
- **Start with a pilot:** Pick one low-risk capability. Let a domain team contribute it. Build the contribution framework around that real use case. Learn what's hard before you open the floodgates.
- **Build the contribution framework, not just documentation:** Templates, validation pipelines, quality checks. Make contribution a paved road itself.
- **Establish governance before you need it:** Quality standards, ownership model, deprecation policies. Don't figure this out when you already have 20 contributed capabilities.

If you're building your first platform:

- **Start with golden paths for common patterns:** Get good at centralized before you distribute.
- **Build extensibility from day 1:** Even if you're not doing marketplace yet, design your platform APIs with contribution in mind. Add extensibility later is painful.
- **Don't prematurely optimize for marketplace:** If you have 30 engineers and simple needs, you don't need marketplace complexity.

## Real Insight

The platform engineering maturity curve isn't "build golden paths and you're done." It's "build golden paths, recognize when they become the bottleneck, and evolve your model."

The organizations that scale their platforms successfully know when to be centralized and when to distribute. They understand the prerequisites for making each model work.

Most importantly, they're honest about tradeoffs.

- Centralized golden paths give you control and consistency. They also make your team a bottleneck.
- Marketplace models give you scale and domain expertise. They also require governance, quality standards, and cultural maturity.

The question isn't which model is better. It's which model fits your organization's stage.

I explored the economics of platform marketplaces and contribution frameworks in depth at KubeCon Atlanta. The talk covers specific implementation patterns, governance models, real-world failure modes, and when to make the transition from centralized to distributed models.

Want to discuss platform scaling challenges or share your marketplace experience? Connect with me on [LinkedIn](https://www.linkedin.com/in/atulpriyasharma/) - I'd love to hear about your platform journey. If you are struggling with platform engineering, [contact our consultant](https://www.improving.com/contact/), and we will help you build developer platforms that complement your requirements.
