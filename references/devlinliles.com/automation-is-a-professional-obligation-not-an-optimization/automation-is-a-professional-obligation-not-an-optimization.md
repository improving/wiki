---
type: Reference
title: "Automation Is a Professional Obligation, Not an Optimization"
resource: "https://www.devlinliles.com/automation-is-a-professional-obligation-not-an-optimization/"
author: "Devlin Liles"
published: '2026-06-18'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

In 2013, I gave a conference talk where I made this claim:

*Deploy Early, Deploy Often, then Deploy some more. When you are done with that, use Robots to Deploy for you while you sleep.*

This was a professional standard, not a prediction. And it was controversial enough in that room that I want to revisit why I still hold it — and why it matters even more now.

## The "When We Have Time" Trap

Every team I have ever worked with that did not have automated deployments had the same reason: they had not had time to set it up yet. They were planning to. After this sprint. After the release. After things calmed down.

Things never calm down. The manual deployment process persists, accumulates institutional knowledge in the heads of two people who now cannot take vacations, and becomes so embedded in the team's operation that it eventually feels more risky to automate than to continue doing it manually.

This is the trap. The "when we have time" framing treats automation as an optional enhancement — something you add to a working process to make it more efficient. But that framing is backwards. The manual process is the enhancement. The automated process is the baseline.

## What a Professional Standard Looks Like

A craftsman's obligation to automation is equivalent to their obligation to tests: it is not about having enough time. It is about understanding that *not* doing it is a failure to meet professional standards.

Here is the test I apply: if a human is doing something repetitive, predictable, and rule-based — and the technology to automate that thing exists — then choosing not to automate it is a choice to apply skilled human attention to work that machines do better. That is waste. Not inefficiency. Waste.

Manual deployments require skilled people to be available, sober, not on vacation, not distracted, every time a deployment needs to happen. They introduce variability: the steps the senior engineer follows are subtly different from the steps the junior engineer follows, and neither set of steps is written down. They create bottlenecks, hero dependencies, and deployment anxiety.

None of those problems exist in an automated deployment pipeline. The pipeline does the same thing every time. It is documented in code. It does not get tired.

## The "Do Less Work" Principle

This connects to a broader principle I held in those early talks: **Do Less Work**. Not in the lazy sense — in the elimination-of-waste sense.

Work that does not require human judgment should not be done by humans. Build and deployment automation, test execution, code formatting, static analysis — these are all tasks where a machine makes better, faster, more consistent decisions than a human. Assigning these to humans is not a virtue. It is a failure to understand what humans are for.

The craftsman's obligation is to identify the boundary: where does human judgment matter, and where does it just get in the way? Everything on the "gets in the way" side of that boundary should be automated.

## Managing the Process vs. Watching the Process

One more principle from those early talks: *Don't manage the automated process. Monitor it.*

There is a category of people who automate deployment and then spend their time watching the pipeline run, ready to intervene if something goes wrong. This is better than manual deployment, but it is not the goal. The goal is a pipeline where failures are caught by automated quality gates, failures are reported clearly, and human attention is engaged only when the machine genuinely cannot proceed.

If you are watching a pipeline run, you are still doing work that a monitor can do.

## Why This Still Matters

I have spent the last few years talking about agentic AI, autonomous systems, and the Intelligence Operating System. The foundational thinking behind all of it started here: humans should be applied to problems that require human judgment, and machines should handle the rest.

In 2013, the machines that could help were CI/CD pipelines and deployment robots. In 2026, the machines are autonomous AI agents that can research, write, test, review, and deploy. The principle is identical. The scale is different.

A team that never built the discipline of trusting automated processes will struggle enormously with trusting autonomous agents. The governance infrastructure for agentic AI — audit trails, quality gates, automated boundary enforcement — is a direct evolution of the CI/CD discipline those early talks were advocating. You cannot skip the automation discipline and arrive at trustworthy AI-native operations. You have to build it one layer at a time.

The robots that deploy while you sleep in 2013 are the agents that build while you sleep in 2026. The professional obligation is the same.

---

*Part of the *[*Thought Leadership series*](https://www.devlinliles.com/tag/thought-leadership/)* — Thread 1: People, Culture & Organizational Systems.*
