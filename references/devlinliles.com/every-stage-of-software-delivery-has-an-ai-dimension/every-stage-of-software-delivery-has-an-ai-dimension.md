---
type: Reference
title: "Every Stage of Software Delivery Has an AI Dimension"
resource: "https://www.devlinliles.com/every-stage-of-software-delivery-has-an-ai-dimension/"
author: "Devlin Liles"
published: '2026-07-06'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

One of the most common mistakes I see in organizations investing in AI for development is that they find one place where AI is clearly useful — usually code completion or generation — and treat that as their AI strategy.

Code completion is real value. But it is one point on a loop that has eight stages, and limiting your AI investment to one stage leaves most of the available leverage untouched.

## The ALM Infinity Loop

Software delivery is not a waterfall and it is not a sprint. It is a continuous loop: **Plan → Code → Build → Test → Release → Deploy → Operate → Monitor** — and then back to Plan, informed by what you learned from operating and monitoring.

Every organization running modern software delivery is moving through this loop continuously, often with multiple teams at different points simultaneously. The loop is the unit of analysis, and every stage has a distinct AI leverage point.

## Stage by Stage

**Plan + AI.** Requirements quality is the largest upstream defect source in most software organizations. AI can analyze a proposed feature or user story for ambiguity, internal contradiction, missing edge cases, and alignment with existing system behavior — before a single line of code is written. The cost of fixing a requirements defect in the planning stage is a fraction of the cost of fixing it in production. AI in planning is force multiplication on the most cost-effective defect prevention available.

**Code + AI.** This is where most teams have invested. AI code assistants reduce the time required to translate intent into implementation. The more important capability, which most teams underutilize: AI code review. Automated review that catches security vulnerabilities, performance issues, and pattern violations before human review reduces review cycle time and consistently catches classes of defects that human reviewers miss because they have seen the same codebase for too long.

**Build + AI.** Intelligent build systems can learn which tests to run based on what changed, dramatically reducing build times for large codebases. AI-assisted dependency analysis can flag breaking changes before they reach the broader team. Build intelligence is an underinvested area with significant compounding value.

**Test + AI.** AI-generated test cases cover edge cases that human test designers miss — particularly the combinatorial edge cases that are practically impossible to enumerate manually. AI can also analyze test failures across runs to identify flaky tests (tests that sometimes fail for environmental reasons rather than code defects), which are a significant source of developer friction and wasted CI capacity.

**Release + AI.** Risk-scoring for releases: analyzing the scope of changes, their history of causing incidents, and the current system state to produce a release risk score that informs go/no-go decisions. This is particularly valuable for organizations with complex microservice architectures where the blast radius of a given change is difficult to assess manually.

**Deploy + AI.** Progressive deployment with AI-monitored rollout: AI watches system health metrics during canary or blue/green deployments and automatically rolls back when anomalous patterns are detected, faster than any human monitoring process. Amazon's data shows this is where some of the most significant cost reductions in production operations have been achieved.

**Operate + AI.** AI-assisted incident response: pattern-matching against historical incidents to surface likely causes, similar past incidents, and effective remediation paths — while the on-call engineer is under pressure. Reducing mean time to detection and mean time to recovery are among the highest-ROI investments available in mature operations organizations.

**Monitor + AI.** Anomaly detection at scale: distinguishing signal from noise in a monitoring system that produces thousands of events per minute is beyond practical human attention. AI can learn baseline patterns and surface the anomalies worth human attention, dramatically reducing alert fatigue and improving the signal-to-noise ratio.

## The Compounding Effect

Here is the insight that changes the framing from "AI tools" to "AI-native delivery": these capabilities compound.

Fewer requirements defects in Plan means fewer defects reaching Code. Better Code review means fewer defects reaching Test. Better Test means fewer defects reaching Release. Progressive deployment with AI rollback means fewer incidents reaching Operate. Anomaly detection in Monitor feeds better context back into Plan.

The loop closes. Quality improvements in early stages reduce cost in later stages. The further left in the loop you can catch a defect, the less it costs.

An AI-native delivery organization does not have eight independent AI investments. It has a system where AI assists at each stage and the improvement in each stage cascades through the loop.

## The Practical Starting Question

Not "which AI tool should we adopt?" but: "In which stage of our loop do we have the most quality problems, the most wasted time, or the biggest risk?" Start there. Build the capability at that stage. Measure the improvement. Then ask: "What does the next highest-leverage stage look like?"

The loop is the strategy.

---

*Part of the *[*Thought Leadership series*](https://www.devlinliles.com/tag/thought-leadership/)* — Thread 2: Technology Practice & Evolutionary Change.*
