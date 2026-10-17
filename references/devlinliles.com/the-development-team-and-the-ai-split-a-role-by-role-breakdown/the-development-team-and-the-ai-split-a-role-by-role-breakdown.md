---
type: Reference
title: "The Development Team and the AI Split: A Role-by-Role Breakdown"
resource: "https://www.devlinliles.com/the-development-team-and-the-ai-split-a-role-by-role-breakdown/"
author: "Devlin Liles"
published: '2026-07-30'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The productivity story for AI on development teams has been loud for three years. Code generation. Test scaffolding. Documentation. The headline numbers are real, and the gains in form-bound work are significant. But the development team is also where judgment-bound errors are most expensive, because the output ships. A shallow persona document goes into a Confluence page. Shallow architectural reasoning goes into production.

This post applies the framework to each role on the development team. The goal is the high-stakes cases: where category confusion is most likely and most costly. In consulting work, bad personas live in Confluence. In software, those same architectural mistakes get compiled and deployed.

## Software Engineer

Engineering is where the form-bound tooling story is most mature and most validated. Code generation for boilerplate, test scaffolding from defined acceptance criteria, documentation generation from code, commit message and PR description formatting: all of these have well-established tools, well-understood review patterns, and real productivity returns. A senior engineer who isn't using AI for these tasks is trading judgment time for formatting time.

**Judgment-bound:** Debugging novel failures is the clearest example of engineering judgment-bound work. When something breaks in a way that hasn't been seen before, the diagnosis requires forming hypotheses, designing experiments to test them, interpreting results that were unexpected, and changing the mental model when the first interpretation is wrong. AI can search the codebase and surface related code. It cannot run the mental model iteration that finds the answer when the obvious explanation doesn't hold. The engineer who asks AI "why is this failing" and accepts the first answer is skipping the judgment step.

API design is judgment-bound. The questions that determine whether an API ages well: what do callers actually need, where will requirements change, what coupling is acceptable here. Answering them requires understanding the domain, the current system, and the likely future trajectory. AI can generate a structurally correct API. It cannot judge whether the abstraction is right.

Code review for logic correctness is judgment-bound. AI-assisted code review catches style violations, obvious anti-patterns, and missing test coverage reliably. The review that catches a subtle concurrency issue, or recognizes that the logic is correct for today's input range but will fail when the edge case arrives, requires someone who understands both the domain and the system.

**Form-bound:** Boilerplate generation, test scaffolding from a defined spec, documentation from working code, migration script generation from a schema change, PR description generation from a commit log, dependency update summaries. All form-bound. The right investment is automating them with confidence and protecting the engineer's judgment time for the work that cannot be automated.

The judgment-bound checklist for an engineer debugging a hard problem: What's the expected behavior? What's the actual behavior? What's the simplest explanation? What would I have to see to falsify that explanation? What are the three alternatives? Has anyone on this team seen something like this before? AI can hold that structure and prompt through it. The engineer fills in the answers.

## Tech Lead

The tech lead sits at the intersection of technical work and team coordination, and both dimensions have judgment-bound components that are easy to outsource incorrectly.

**Judgment-bound:** Technical direction decisions require the tech lead to integrate things a model can't: which approach to take when the team is split, how to sequence a large refactor, what to defer versus what to do now, set against team capacity, timeline reality, and the specific risks of this system. AI can model the technical tradeoffs. It cannot weigh the team's current energy level or the political cost of delaying a capability the stakeholder has been waiting for.

Mentoring and code review as a growth tool are judgment-bound. The tech lead who reviews code for correctness is doing quality work. The tech lead who reviews code as a teaching instrument, choosing which feedback to give, how to frame it, what to leave for the engineer to find themselves, is doing judgment-bound work with a significant long-term return. AI can suggest feedback. Deciding whether to give the feedback directly or to ask a question that leads the engineer to it is the tech lead's call.

Sprint and iteration planning is partially judgment-bound. The mechanics of estimation and sprint construction are form-bound enough that AI handles them reasonably. The judgment layer is knowing which estimates are optimistic because the engineer hasn't done this type of work before, and which are conservative because they've been burned recently. That context lives in the tech lead.

**Form-bound:** Technical design document structure, ADR formatting, sprint review write-ups, retrospective facilitation guides, onboarding documentation templates, and team status reports are all form-bound. A tech lead who builds AI tooling for these artifacts gets that time back for the judgment work.

## Architect

Architecture is the role on the development team with the highest concentration of judgment-bound work, which makes it the role with the highest AI misuse risk.

**Judgment-bound:** Technology selection is judgment-bound in a way that looks form-bound because there are frameworks for it. DORA metrics, total cost of ownership models, capability matrices: all form-bound scaffolding for a judgment call. The actual decision integrates the team's existing skills, the organization's operational maturity, the specific failure modes of this system, and a read on which vendors will still be a reasonable bet in five years. The architect who runs a scoring model and accepts the output has produced an artifact that justifies a decision rather than made one.

Failure mode analysis is judgment-bound. Identifying the failure modes worth caring about in a specific system, in a specific operational environment, requires understanding what has actually failed in similar systems and why. AI can enumerate textbook failure modes for a given architecture pattern. It cannot calibrate which of them are actually likely given this team, this deployment environment, and this usage pattern.

System boundary decisions are among the highest-stakes judgment calls an architect makes: where to split services, what to encapsulate, which domain concepts belong together. These decisions have a five-to-seven-year half-life and shape every future change. Getting them wrong creates compounding rework. AI can model the tradeoffs. The judgment about what the organization can actually operate is the architect's.

**Form-bound:** Architecture Decision Record structure is entirely form-bound. ADRs have a well-defined format: context, decision, status, consequences. A skill that generates a complete ADR from a structured conversation is high-value tooling that every architect should have. System diagram conventions, documentation structure, capacity planning templates, and RFC formats are all form-bound. The content within them is judgment-bound; the containers are not.

The architect's judgment-bound checklist for a technology decision: What problem are we actually solving? What do we have to believe about how this system will evolve for this choice to age well? What does our operational team need to know to run this? What breaks first? Who on the current team can own this decision?

## QA Engineer

QA is interesting because it has more form-bound volume than most roles, and also has a judgment-bound core that is frequently underinvested.

**Judgment-bound:** Test strategy development is judgment-bound. The decision about what to test, how thoroughly, and from what angle requires understanding the risk profile of the system, the failure modes that matter most, and the gap between what the spec says and what users will actually do. AI can generate test cases from acceptance criteria. It cannot decide whether the acceptance criteria are testing the right thing.

Exploratory testing is judgment-bound by definition. The value of an experienced QA engineer doing exploratory testing is precisely that they are bringing pattern recognition across similar systems to find the failure modes that weren't anticipated. AI can suggest areas to explore. The exploration itself, and the judgment about what constitutes a meaningful failure, is human.

Defect triage is judgment-bound. Deciding whether a bug is a critical regression or an acceptable edge case behavior requires understanding the user impact, the likelihood of occurrence in production, and the cost of the fix relative to the risk of shipping it. That's a business judgment that requires domain context.

**Form-bound:** Test case generation from acceptance criteria and user stories is almost entirely form-bound. Test plan structure, regression test scaffolding from existing test suites, bug report templates, and test coverage reports are all form-bound. A QA engineer with good tooling for these tasks can redirect their time toward exploratory testing and test strategy work, which is where the actual value is.

## DevOps and SRE

DevOps and SRE work has a clean split: the reasoning under an incident is judgment-bound, and almost everything else is form-bound.

**Judgment-bound:** Incident response decisions are judgment-bound under time pressure, which is the hardest version. During an active incident, the SRE is integrating signals from monitoring, making a hypothesis about the failure mode, deciding whether to escalate, and choosing between remediation options with incomplete information. Runbooks help, but every incident has novel characteristics. The SRE's judgment about when to deviate from the runbook is the critical variable.

Capacity planning is judgment-bound. The models are form-bound: trend lines, headroom calculations, cost projections. The judgment is about which trends to trust, which usage patterns are transient versus structural, and what the cost of being wrong in each direction looks like. An organization that ships too early on infrastructure is over-spending. Too late and they're scrambling during a growth event. Neither end is free, and the tradeoff is a judgment call.

Infrastructure architecture decisions mirror the architect's role: the reasoning about what to build as managed services versus what to operate directly, and how to draw service boundaries in the infrastructure layer, requires judgment about the team's actual operational capacity and the organization's risk tolerance.

**Form-bound:** Runbook generation from a known incident pattern is form-bound. Alert configuration from defined SLOs, pipeline scaffolding, infrastructure-as-code boilerplate from a reference architecture, incident post-mortem template structure, and capacity model templates are all form-bound. A DevOps team that isn't automating these artifacts is spending engineering time on documentation when they should be on the judgment work.

The judgment-bound checklist for incident response: What are the symptoms? What systems are affected? What changed in the last two hours? What's the hypothesis? What would confirm it? What are we doing in the next five minutes? AI holds the checklist and prompts through it. The answers come from the SRE who understands the system.

## Engineering Manager

The engineering manager's entire role is judgment-bound, which creates a specific and common failure mode: using AI to produce artifacts that look like management work while skipping the reasoning that makes those artifacts true.

**Judgment-bound:** Performance assessment is entirely judgment-bound. The manager who generates an employee review from a list of Jira tickets and peer feedback summaries has produced a form-bound artifact with an absence of judgment in the place that matters most. The assessment of where an engineer actually is relative to their potential, what's holding them back, and what the right intervention is: that comes from the manager observing the work, having the conversations, and forming a considered view. AI can organize the evidence. It cannot form the view.

Hiring decisions are judgment-bound. Technical screens have form-bound components: structured interview questions, scoring rubrics, and reference check templates. The judgment about whether this person will grow into the team's needs and whether their working style will amplify or diminish the team they're joining is the manager's call.

Team structure and project assignment decisions are judgment-bound. Deciding who should own a hard project, how to pair a senior engineer with a junior one for maximum learning, and when an engineer is ready for a stretch assignment requires knowing the people, not just the org chart.

**Form-bound:** One-on-one meeting preparation templates, goal-setting document structure, job description formatting, offer letter templates, sprint planning facilitation guides, and team onboarding checklists are all form-bound. Generating a first-draft performance review template from a role leveling matrix is form-bound. The manager who builds tooling for these artifacts and redirects the time toward actually observing and coaching the team has made a sound investment.

## The Compounding Argument

The pattern across every development team role is that judgment-bound work is the work that cannot be recovered. If an architect makes the wrong system boundary decision, no amount of AI tooling fixes the rework later. If a tech lead skips the real mentoring conversation, the engineer doesn't grow on the timeline they could have. If an SRE uses a runbook mechanically when the incident is novel, the MTTR climbs.

Form-bound work done manually just costs time. Judgment-bound work done wrong costs architecture, team capability, and system reliability.

AI on development teams is most powerful when it's compressing the time on form-bound work hard enough to expand the time budget for judgment-bound work. More deliberate debugging. More real code review. More architecture reasoning. More actual coaching.

The question isn't which AI tools your team is using. It's whether the time being freed is going to the work that requires judgment, or just producing more form-bound artifacts faster.

---

*Part 3 of 3 in the "Two Kinds of AI Work" series.*
