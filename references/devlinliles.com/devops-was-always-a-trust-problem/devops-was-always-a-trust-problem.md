---
type: Reference
title: "DevOps Was Always a Trust Problem"
resource: "https://www.devlinliles.com/devops-was-always-a-trust-problem/"
author: "Devlin Liles"
published: '2026-07-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

By 2018, the tooling was solved.

Source control had been mainstream for over a decade. Continuous Integration had mature, well-documented patterns. Infrastructure as Code was no longer experimental. Containerization had moved through the Early Adopter phase and was approaching mainstream adoption. The entire technology stack required to implement DevOps practices was not only available but well-understood, with clear implementation guides, active communities, and mature commercial tooling.

And yet: most organizations had not adopted these practices.

The obstacle was not technological. It was human.

## What Was Actually Blocking Adoption

When I mapped DevOps practices against the adoption curve in 2018, the pattern that stood out was not the usual "tooling is immature" or "the problem isn't well-defined" explanations for slow adoption. The tooling was mature. The problem was well-defined. The ROI case was clear.

The pattern I saw: "Trust in Agile (Technologists)."

Organizations — specifically, the leadership of organizations — did not trust their development teams to do what they said they would do. They didn't trust that automated deployments would not break production without the manual review steps that the operations team had always performed. They didn't trust that developers moving faster would actually move in the right direction. They didn't trust that reduced process overhead would produce quality rather than chaos.

This was not irrational. The trust had often not been earned. Development teams that had promised reliable deployments and then caused production incidents had a track record to overcome. Operations teams that had built manual processes over years to catch quality problems were not wrong to be skeptical of automation.

But the trust problem cannot be solved with tooling. You cannot deploy a CI server and fix organizational trust. You cannot containerize your way to a culture where developers and operations teams share goals.

## The Trust-Tooling Sequence

This is the insight I have carried forward from 2018: the sequence matters.

The common approach: adopt the tooling first, and expect the trust to follow as the tooling proves itself.

The problem with this approach: tooling deployed in a low-trust environment tends to be adopted defensively. Automation is implemented but surrounded by manual checkpoints that prevent it from delivering its value. CI pipelines are deployed but the builds are always marked optional. Infrastructure as Code is used for new environments but the production configuration remains manually managed because "that's too critical to automate."

The result is that the tooling does not deliver the expected ROI — because it was never allowed to. And the lack of ROI is taken as evidence that the tooling is not valuable, which reinforces the original trust gap.

The more effective sequence: establish the conditions for trust before deploying the tooling that requires it. Be explicit about what success looks like, what the constraints are, what the feedback loop will be. Let teams demonstrate reliability in lower-stakes contexts before extending autonomy in higher-stakes ones. Build the track record first.

This takes longer. The payoff is that the automation, when deployed, is actually allowed to run.

## The Parallel to Agentic AI

I have been making this argument for five years, and I now make it in a different context.

Autonomous AI agents are failing in organizations for the same reason DevOps failed in organizations in 2015: the trust infrastructure was not in place before the autonomy was deployed.

Teams are deploying AI agents into workflows without establishing what the agents are allowed to do, what happens when they make an error, how their decisions are audited, and what the human approval points are. The agents encounter edge cases that their designers did not anticipate, produce outputs that the organization is not set up to verify, and eventually get shut down because they "cannot be trusted."

The conclusion is correct. They cannot be trusted. But the reason is not that autonomous AI is inherently untrustworthy — it is that trust requires infrastructure, and the infrastructure was not built first.

The governance engine that makes agentic AI trustworthy — audit trails, boundary enforcement, quality gates, human approval points — is the DevOps trust infrastructure of the AI era. The organizations building that infrastructure first, before deploying broad autonomy, are the ones that will arrive at Stage 7 and 8 of the AI trust evolution with systems that actually work.

The organizations that skip the trust infrastructure to deploy autonomy faster will be having, in 2027, the same conversation we were having in 2018 about DevOps: "we tried it and it didn't work." The problem will not be the technology.

---

*Part of the *[*Thought Leadership series*](https://www.devlinliles.com/tag/thought-leadership/)* — Thread 2: Technology Practice & Evolutionary Change.*
