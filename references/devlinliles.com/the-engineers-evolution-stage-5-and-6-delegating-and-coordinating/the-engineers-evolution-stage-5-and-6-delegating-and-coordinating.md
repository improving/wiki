---
type: Reference
title: "The Engineer&#x27;s Evolution, Stage 5 and 6: Delegating and Coordinating"
resource: "https://www.devlinliles.com/the-engineers-evolution-stage-5-and-6-delegating-and-coordinating/"
author: "Devlin Liles"
published: '2026-06-27'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Engineer's Evolution, Stage 5 and 6: Delegating and Coordinating

*Part 4 and final post in a series on how the software engineer's role changes as teams climb the AI maturity curve. This post looks up the curve at the next two stages and follows two example careers into them: a software developer and a QA engineer.*

---

Most teams will operate at Stage 3 and 4 for a good while, so why look further up the curve. Because the shape of Stage 5 and 6 explains why the Stage 4 habits matter so much. Everything you build at Stage 4, the gates, the scoring, the discipline of earning trust one workflow at a time, is the foundation the later stages stand on. Skimp at Stage 4 and the cracks do not show up until you try to delegate, when they show up all at once and at scale.

A planning fact frames this whole post. The stages are not equal in effort, and the gap is the most important number on the curve. Measured across our own instrumentation, more than 250 build samples per stage, each layer costs roughly seven times the effort of the one below it. A team that stands up a task agent in two or three days should expect a full workflow to take the better part of a month, an autonomous system several months, and a coordinated network the better part of a year. These hours buy the orchestration itself, the agents and gates and harness, not the software it produces. The work is building the factory. The output comes later. That sevenfold step-up is why the move from Stage 4 to Stage 5 is where most organizations stall, and it is why you earn the right to delegate by first making each workflow cheap to trust.

## Stage 5: Delegate

Through Stage 4, engineers invoke agents inside the IDE they already use. At Stage 5 they delegate across multiple workflows through an agent that runs on its own, outside the editor. That agent can spin up environments, kick off builds, remediate issues, and pull work from the backlog without a human starting each step.

The defining requirement is trusted signals. The delegated agent decides how to handle an error and when to pull in a human, and it makes those calls based on deterministic checks and adversarial validators that confirm an output is good before any handoff completes. Without those signals, delegation is just unattended risk. With them, it is leverage. This is the jump where developer-level skill becomes non-negotiable in a way it was not at Stage 3, because when a delegated workflow fails it fails further from a human, and unwinding it takes someone who can read the whole chain.

### The developer becomes an orchestration engineer

The Stage 5 developer moves trusted, well-protected workflows out of the IDE and delegates them to an agent that runs on its own. They design the trusted signals that decide how errors are handled and when a human is pulled in, along with the adversarial validators that confirm an output before a handoff completes. They delegate only what is proven and keep a hand on the rest. The job grows to include cost, model selection, and the DevOps harness that makes delegation safe rather than merely faster. The signature skills are delegation and DevOps-harness design, cross-workflow validation, cost and model-selection judgment, and the engineering depth to unwind a compounded failure by hand when one slips through.

### The tester becomes an assurance engineer

QA at Stage 5 builds the adversarial agents and cross-workflow protection gates that validate outputs before any delegated handoff completes. The tester defines the trusted signals that let a delegated workflow proceed or escalate to a human, and they keep the rejection logs and branch-detection records that prove the gates actually hold. They own the assurance that makes delegation safe, since a weak gate at this layer compounds downstream where it is most expensive to catch. The signature skills are adversarial-agent design, cross-workflow gate enforcement, test-sufficiency and validation rigor, and system-level debugging. This role depends entirely on developer-level skill and close partnership with the team.

## Stage 6: Coordinate

At Stage 6, multiple agents work in parallel on shared infrastructure. The engineer's work becomes branch isolation, merge strategy, conflict arbitration, recovering from blocked states, and reading status across many streams rather than watching any single one. The human is now closer to an operator of a system than an author of code. The skill is keeping many concurrent agents from colliding, and seeing trouble in the aggregate before it cascades.

This is also where the earlier example from Stage 4 comes home to roost. A concurrency agent at this layer can package a hundred commits into a single pull request. If a gate two layers down was weak, the coordinated layer multiplies the damage before anyone reads a line. That is why the cost curve and the competency floor are the two things to carry away from this whole series. The later a mistake is caught, the more it costs, and only engineers who can still read and debug the code can trace a coordinated failure back to its root.

Stages 7 and 8, supervision and orchestration, are aspirational today. No production-grade patterns or toolchains support them reliably yet. We name them so the map is complete, and we make no promises about them.

## The constant across every stage

One narrative is worth retiring before we close: the idea that engineering simply becomes judgment and the coding skill fades away. Engineering does become more judgment-centric. The ability to read, write, and debug code has arguably never mattered more. The bulk of hands-on production may shift to agents. The floor of competency cannot, because it is what lets an engineer catch a wrong output before it compounds across delegated and parallel work.

Step back and the arc is clear. The developer grows from someone with an assistant, to a director and reviewer, to a systems architect and governor, to an orchestration engineer. The tester grows from someone with a faster draft, to a test designer, to a quality architect, to an assurance engineer. At every step the work moves further from producing software and closer to designing and governing the systems that produce it. The demand for design, architecture, and judgment rises the whole way. The titles change and the balance of the day shifts. The competency floor stays exactly where it is.

The climb is uneven. Juniors often gain speed quickly. Seniors gain more slowly at first, because they are rightly critical of agent output, and their breakthrough comes when their standards are encoded into the team's agents rather than applied by hand. Roughly sixty percent of people make the metacognitive shift comfortably. The rest need support, a different role, or time. The future engineer is more than a faster coder. They manage agents and design the systems that produce and verify software, and their edge is judgment built on a floor of real engineering skill they never stop using. That is the shape of the role the field is converging on.
