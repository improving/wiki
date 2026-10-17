---
type: Reference
title: "The Engineer&#x27;s Evolution, Stage 3: Directing the Work Instead of Doing It"
resource: "https://www.devlinliles.com/the-engineers-evolution-stage-3-directing-the-work-instead-of-doing-it/"
author: "Devlin Liles"
published: '2026-06-25'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Engineer's Evolution, Stage 3: Directing the Work Instead of Doing It

*Part 2 of a series on how the software engineer's role changes as teams climb the AI maturity curve. This post takes Stage 3 and follows two example careers through it: a software developer and a QA engineer.*

---

Stage 3 is where the job changes in a way you can see. At Stage 2 an engineer used an assistant and kept working the old way. At Stage 3 they stop and write down how they work, turn that into agents the team can share, and move from the keyboard to the director's chair. The center of the day shifts from producing code to defining intent and judging output. This is the first stage where the role looks meaningfully different from the one most engineers trained for.

The model calls this stage Task. The phrase that captures it: use and build agents to accelerate your own competency. The key word is *your own*. Stage 3 agents are personal. They reflect one engineer's judgment, encoded so that engineer can move faster without lowering their bar. The team-wide version comes later. Stage 3 is about an individual learning to manage a small fleet of agents that think the way they think.

## The developer becomes a director and reviewer

Before any speed shows up, the developer does something that feels slow. They document how they actually work. They write down their opinions, their process, and the standards they hold, and they encode all of it into repeatable task agents and skills. A test-driven loop, for example, gets broken into discrete steps an agent can run. Then they put those artifacts somewhere the team can find them.

A skill is a written job description for a unit of work. Here is how we do this thing, and here is the context required to do it well. That framing carries through the rest of the curve, because every later stage builds on it. The developer's work moves up a level. They are specifying how a class of problems should be solved, in enough detail that something else can execute the specification.

Once those agents exist, the day inverts. The developer spends far less time typing code and far more time overseeing agents, directing intent, and reviewing output after each step. They become the evaluation point in the loop. Where they have a firm standard, they let the agent run and they check the result. Where they have no trusted standard yet, they still do the work by hand and watch closely, because that hands-on pass is how the next standard gets discovered.

One number gauges the stage. A healthy Stage 3 runs at an acceptance rate of roughly 92 to 94 percent on agent output. Fall below that band and it means trust or definitions are weak: the agent keeps producing things the developer has to reject or rework. Climb above it and a different problem appears. The team is over-trusting the agent, waving work through without real scrutiny, and quietly accumulating downstream defects that will surface later. The acceptance rate is a health gauge, and the goal is to keep it honest. Honest beats high.

The signature skills of a Stage 3 developer map where the role has grown. Prompt and context engineering. Writing skills an agent can actually be evaluated against. Critical review of generated code. And the coding depth to step in the moment an agent is weak. That last one is the floor that never moves. The developer reviews far more code than they write, which means they have to be good enough at the craft to catch a plausible-but-wrong answer at a glance.

## The tester becomes a test designer

QA makes the same move on its own terms. The tester encodes the craft of testing into task agents. Take a defined user story with acceptance criteria and generate a test plan, or generate the test scenarios that cover it. The agent drafts. The tester directs and reviews.

What changes is where the human value sits. The valuable skill stops being the manual authoring of tests and becomes test design, test architecture, and the recognition of patterns and edge cases an agent will miss. The tester reviews what the agent produces against the real intent of the story, then feeds corrections back into the agent so the next pass is better. That feedback loop is the work now.

This is also the stage where a long-standing constraint finally breaks. Automation coverage has always been capped by how much a labor-constrained QA team can author by hand. Once the team can generate well-designed tests from acceptance criteria, coverage can rise past anything a fixed headcount could reach. The lever is no longer how fast the tester types. It is how well the tester has taught the agent what good testing looks like.

The signature skills follow the same pattern as the developer's: test architecture, translating acceptance criteria into tests, edge-case recognition, and the judgment to evaluate generated tests against intent. The ability to read code and requirements closely does not fade. It is what makes the evaluation trustworthy.

## Managing agents starts to feel like managing people

By Stage 3 a useful intuition kicks in. Directing a fleet of agents starts to resemble managing a small team. You set expectations. You review output. You decide how much to trust each one. The mechanics line up well enough that engineers who already manage people tend to make this jump fastest.

The analogy is worth leaning on at Stage 3, with one caution we will return to in later posts. Agents do not fail where people fail. A capable person's error rate tracks difficulty, and they usually know when they are out of their depth. Agents invert that. They can nail a hard task and then produce something confidently wrong on something trivial. Confidence and correctness come apart in a way they rarely do with a competent colleague. So the Stage 3 reviewer cannot relax on the easy stuff. Easy is exactly where an agent will surprise you.

## What Stage 3 sets up

Stage 3 produces a real change in throughput and a real change in the engineer. The developer is now a director and reviewer with a personal library of agents that encode their judgment. The tester is a test designer whose coverage is no longer capped by their typing speed. Both spend their days defining intent and judging output, and both keep the hands-on skill that lets them catch what the agents get wrong.

The ceiling at Stage 3 is that all of it is still personal. Each engineer's agents reflect their own standards, which means the team has as many definitions of good as it has engineers. The reviewing is still done by a human, in the moment, one piece of work at a time. To go faster the team has to reconcile those personal agents into shared workflows and move the checking out of human heads and into systems. That move is Stage 4, and it is where the role becomes a team event. The next post picks it up.

*Next in the series: Stage 4, where the developer becomes a systems architect and governor, and the tester becomes a quality architect.*
