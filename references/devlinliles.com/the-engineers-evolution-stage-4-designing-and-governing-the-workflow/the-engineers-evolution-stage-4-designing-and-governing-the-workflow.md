---
type: Reference
title: "The Engineer&#x27;s Evolution, Stage 4: Designing and Governing the Workflow"
resource: "https://www.devlinliles.com/the-engineers-evolution-stage-4-designing-and-governing-the-workflow/"
author: "Devlin Liles"
published: '2026-06-26'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Engineer's Evolution, Stage 4: Designing and Governing the Workflow

*Part 3 of a series on how the software engineer's role changes as teams climb the AI maturity curve. This post takes Stage 4 and follows two example careers through it: a software developer and a QA engineer.*

---

Stage 4 is the destination most teams should be aiming for, and it is where the engineer's role completes its transformation. At Stage 3 a developer directed agents and reviewed their output by hand, one step at a time, using their own personal standards. At Stage 4 they take the checking they were doing by hand and make it programmatic. The reviewing moves out of the engineer's head and into the system. Velocity stops depending on how fast a human can inspect each step, and it starts to compound.

The model calls this stage Workflow, and it carries a phrase worth holding onto: offload workflows behind a protection harness, least complex first. Two ideas live in that sentence. The first is the protection harness, the set of automated gates that catch mistakes so a human does not have to. The second is sequencing, the discipline of starting with the simplest workflows and earning your way up to the hard ones. Both matter, and skipping either is how Stage 4 goes wrong.

There is also a structural shift at this stage that the earlier ones did not have. Stage 4 is a team event. The personal agents each engineer built at Stage 3 have to be reconciled into shared workflows the whole team agrees on. That reconciliation is the moment the engineers who leaned in early become the technical leaders guiding everyone else. Stage 4 also pulls in IT, because the gates, the scoring, and the pipelines now have to live in shared infrastructure rather than on one person's laptop.

## The developer becomes a systems architect and governor

The Stage 4 developer wires individual task agents into a workflow and builds a protection harness between the steps. That harness does the work the developer used to do by eye. Lint, build, and test gates run automatically. A model acts as a judge, or a council of models weighs in on a piece of work. Automated recovery loops re-run a step when a check fails, so the system fixes its own routine mistakes before a human ever sees them.

With that harness in place, the developer hands full autonomy to the parts of the workflow that are protected, and keeps partial autonomy where protections do not yet exist. Their attention moves to the exceptions and the edges, the places the system flags because it does not know what to do. The point of all of it is to offload workflows so velocity compounds. The discipline that makes it safe is sequencing. Start with the least complex workflow, prove the gates actually hold, then move up to the harder ones. A team that tries to automate its gnarliest workflow first will spend its time debugging the harness instead of shipping.

The developer's day now concentrates in six areas: audit, review, error handling, quality gates, boundary enforcement, and the human touchpoints where the system needs a decision. Those touchpoints are narrow and specific. Status. Ambiguity. Clarification. Approval. The developer is no longer reading every line of generated code. They are deciding the handful of questions the system cannot decide for itself, and they are designing the gates that let everything else run untouched.

The signature skills tell the story. Workflow and harness design. Defining deterministic gates and the human punch-out points where a person has to weigh in. Setting team standards rather than personal ones. And debugging failures that span chained steps, which is a harder skill than debugging a single function, because the bug might live in the seam between two agents rather than inside either one.

## The tester becomes a quality architect

At Stage 4, verification stops being a phase at the end and becomes part of the harness itself. The tester designs the gates that sit between workflow steps and writes the evaluation criteria that decide whether an agent's output is acceptable. They build verifiable shims and workflow artifacts that make automated tests easier to generate and easier to trace back to a product owner's intent. Coverage that used to be a fraction of the suite becomes the majority of it.

The tester's leverage now comes from architecture and judgment. That does not cost them the ability to read and debug a failing test path by hand. When a gate is wrong, someone has to trace why, and that someone is the quality architect.

Stage 4 also hands QA a hard lesson, the one teams learn the expensive way. The early gates have to be rigorous. That includes checking whether the test suite itself is sufficient for the change in front of it, which is a question most automated gates never think to ask. A weak Stage 4 gate does not stay contained. It surfaces later as compounded failure, after the cheap moment to catch it has passed. The harness is only as good as its weakest gate.

Here is what that looks like in practice, drawn from our own work. We had a Stage 4 gate that, after any code change, ran the test suite, fixed whatever failed, and required everything to pass. It worked exactly as designed. The flaw was upstream of the design: we never checked whether the suite was sufficient for the change in front of it. The suite ran against mocked API results rather than a true end-to-end path, so the read operations passed while the write, update, and delete paths sat broken behind the mocks. Nothing caught it. A later concurrency agent then packaged the work into a roughly hundred-commit pull request and shipped it for review. It did not work. The cause was a single missed expectation two layers down. Fixing it meant unwinding the pull request and repairing several layers of harness. The judgment set the gate. The competency caught the failure the gate missed. Only engineers who could still read and debug the code could trace it back and repair it.

## Managing agents, and where the people analogy breaks

By Stage 4, managing agents looks a lot like performance management. We score agents on a ten-point scale against real test cases. Agents above the bar are trusted to run, and the strongest can be moved to leaner, cheaper models to control cost. Any that fall below the bar are pulled from service until they are fixed. Authoring a skill is writing a job description. Defining gates is setting guardrails. Scoring against a rubric is the performance review. The mechanics map cleanly.

The analogy breaks on the part that matters most: deciding what to hand over and why. Three differences make agent delegation its own discipline. Agent failures are correlated. Ten people will not make the identical mistake on the same line, but one agent can get the same class of problem wrong repeatedly, at scale, which is exactly why the protection harness matters more than human review. Agents also do not learn within the relationship. A person improves because of feedback you gave last week. An agent carries nothing forward unless you encode it into the skill or the context, so what looks like coaching is really editing a specification. And the real delegation decision is a simple test applied to every piece of work: is the agent strong here, and can I verify the output cheaply. Delegate where the answer is yes. Keep a human on, or heavily gate, the work where the agent is weak or where a wrong answer is expensive and hard to detect.

## Where Stage 4 leaves the engineer

By Stage 4 the developer is a systems architect and governor, and the tester is a quality architect. Both spend their days building and tending the machine that produces and verifies software rather than producing it directly. Maintaining the codebase has quietly expanded to mean maintaining the agents, skills, gates, and evaluations that write and check the codebase. New feature skills, harness updates, and agent test suites are normal backlog items now, reviewed and tested like any other deliverable, because a flaw in the harness affects everything it touches.

A focused four-to-six person team operating well at Stage 4 can outpace the eight-to-ten person team it replaces. That is the promise, and it is real. It is also where most organizations stop for a while, because the next step costs far more to build than this one did. The final post in the series looks up the curve at Stage 5 and 6, and at why the jump is so steep.
