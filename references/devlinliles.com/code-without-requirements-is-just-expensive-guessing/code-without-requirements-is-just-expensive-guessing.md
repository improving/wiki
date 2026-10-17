---
type: Reference
title: "Code Without Requirements Is Just Expensive Guessing"
resource: "https://www.devlinliles.com/code-without-requirements-is-just-expensive-guessing/"
author: "Devlin Liles"
published: '2026-07-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The fastest way to slow down an AI-enabled development team is to let them skip requirements.

This sounds counterintuitive. AI coding tools are speed machines. Describe what you want, get code back in seconds. Why would you add a requirements phase to something that eliminates the need for one?

Because the code isn't the expensive part. The rework is.

This is one of the oldest findings in software engineering. Barry Boehm's research in the 1970s and 1980s showed that the cost of fixing a defect climbs steeply the later it is found, and the most expensive defects are the ones planted at the requirements stage. Fred Brooks made the same point in "No Silver Bullet": the hardest single part of building a software system is deciding precisely what to build. AI changed the economics of writing code. It did not change the economics of deciding what to build.

## The Vague-Spec Shortcut

Every AI coding tool on the market right now optimizes for the same thing: speed from prompt to code. Type a description, get an implementation. The tighter the loop, the better the demo. And the demos are spectacular.

The problem shows up at week three. The implementation doesn't match what the stakeholder actually needed. The edge cases weren't captured. The non-functional requirements, the performance thresholds, security constraints, and accessibility standards, were never articulated, so the AI never considered them. The team has working code that works on the wrong problem.

This isn't an AI failure. It's a process failure that AI accelerates. Before AI, the cost of skipping requirements was high but contained. A developer might spend a week building the wrong thing. With AI, a developer can build the wrong thing in an afternoon and have it pass basic tests by dinner. The blast radius of a vague spec expanded by an order of magnitude.

I've watched teams hit this wall consistently. Around day 60, velocity peaks. But delivery, code that solves the problem it was supposed to solve, flattens or declines. The specification stage disappeared, and everything downstream paid for it. Review bottlenecks pile up. Architectural decisions compound. Integration failures cascade. Teams wonder why they're shipping code faster but hitting quarterly milestones slower. The answer is usually buried in rework nobody's measuring.

## Requirements Are Constraints

The instinct when someone says "requirements" is to picture a 40-page Word document that nobody reads. That's not what this is about. In an AI-enabled workflow, requirements serve a different function. They're the constraints that prevent AI agents from optimizing in the wrong direction.

An AI agent without requirements will generate code that compiles, passes the tests it wrote for itself, and looks reasonable in a PR. It will also make architectural decisions you didn't authorize, introduce dependencies you didn't evaluate, and solve adjacent problems you didn't ask for. It's doing its job. You just didn't define the job.

Formal requirements give AI agents a target to hit and boundaries to stay inside. A product requirements document that specifies acceptance criteria, non-functional constraints, and architectural guardrails doesn't slow down AI development. It focuses it. The difference between a 15-minute prompt session that generates throwaway code and a 15-minute prompt session that generates shippable code is almost always the quality of the spec that preceded it.

## The Pattern That Works

I've seen the most effective AI-enabled teams structure their workflow around a hard discipline: requirements come before implementation. Not "let's write requirements as we go." Not "we'll document what we meant after delivery." Before the first AI prompt touches a feature, the requirements exist.

This looks like a pipeline with sequence gates. A product team frames the problem: acceptance criteria, non-functional constraints, architectural boundaries. Those artifacts become the evaluation criteria for everything downstream. A QA function writes test plans against the acceptance criteria. A security review validates against the constraints. An architecture review checks the implementation against the documented boundaries.

The effect on delivery speed runs counter to intuition. Teams that lock in requirements upfront land the first implementation closer to correct. Review cycles compress because reviewers have a spec to measure against, not just intuition. Stakeholder feedback arrives earlier, before code drift creates rework. The 60-day velocity wall never materializes.

This isn't proprietary. It's not tied to any specific tool. It's a pattern that scales across different development stacks and team sizes. The core principle: AI accelerates your process. If the process is sloppy, you accelerate sloppiness at machine speed.

## Where the Argument Could Break

Two objections deserve a straight answer. The first is that this sounds like waterfall wearing new clothes. The agile movement spent two decades teaching that requirements are discovered through working software, and the Agile Manifesto explicitly valued working software over comprehensive documentation. The objection lands if requirements means a frozen document signed off before anyone codes. It misses if requirements means the acceptance criteria, constraints, and boundaries for the next increment of work. Iteration still happens. Each iteration just starts with a spec the agents can be measured against, which is closer to what the manifesto authors actually practiced than the prompt-and-pray loop sometimes defended in their name.

The second objection is sharper: AI makes building so cheap that building the wrong thing is the requirements process. Generate three prototypes, put them in front of the stakeholder, learn from the reaction. For true discovery work, that is right, and I work that way myself. The mistake is letting prototype economics govern production work. A throwaway prototype that misses the mark costs an afternoon. A production feature that misses the mark carries integration surface, review load, security exposure, and stakeholder trust along with it. The discipline is knowing which mode you are in, and the 60-day wall is what happens to teams that ship prototypes as production.

## The Traceability Artifact

There's a second-order problem that most teams don't confront until they're in regulated industries. When a compliance officer or client auditor asks "show me which requirement this code satisfies," most AI-assisted teams stall. The code exists. The prompt that generated it might be buried in a chat log. The connection between business need and implementation is a handwaving story.

The pattern to fix this: flow requirements through your entire delivery pipeline as data, not documentation. Every test that's written maps back to a requirement. Every code artifact references the requirement it satisfies. That happens as a byproduct of structured process, never as manual bookkeeping. You end up with traceability matrices built into your delivery pipeline instead of bolted on after.

This matters because it separates "AI helped us build it" from "AI helped us build it and we can prove it meets the spec." The first is a story. The second is evidence. In healthcare, financial services, and regulated manufacturing, evidence is the deliverable.

## Start Here

The pattern works with any AI tooling stack. Before you prompt an agent to implement a feature, write down three things: what the feature must do (acceptance criteria), what constraints it must respect (non-functional requirements), and what architectural boundaries it must stay inside.

Put those three things in the prompt context. Make them explicit. Then evaluate the output against them, not against your gut sense of whether the code "looks right."

The teams that do this stop hitting the 60-day velocity wall. The teams that don't keep generating code faster and shipping slower, wondering why the AI tools aren't delivering on the promise.

The tools are fine. The specs are missing. And in AI-enabled development, a missing spec costs you time at AI speed.
