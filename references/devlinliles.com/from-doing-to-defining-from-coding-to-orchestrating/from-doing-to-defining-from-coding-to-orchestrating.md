---
type: Reference
title: "From Doing to Defining, From Coding to Orchestrating"
resource: "https://www.devlinliles.com/from-doing-to-defining-from-coding-to-orchestrating/"
author: "Devlin Liles"
published: '2026-06-19'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

"AI shifts the focus from doing to defining, from coding to orchestrating. The goal is synergy, not replacement."

That sentence is the conclusion of the POST-AI framework, and I hold it as the most accurate one-line description of what is happening to the role of every knowledge worker who encounters AI at scale. It is also frequently misread. The misreadings are worth clearing away one at a time, because the claim underneath is older and sturdier than the current AI cycle suggests.

The idea has a pedigree. In 1960, J.C.R. Licklider published "Man-Computer Symbiosis" and described the productive division of labor in advance: humans would set the goals, formulate the hypotheses, determine the criteria, and perform the evaluations, while machines did the routinizable work that prepares the way for insight. That was written when computers filled rooms and ran batch jobs on punch cards. Sixty-five years later it reads like a job description for the orchestrating developer. The technology finally caught up to the paper.

## What It Does Not Mean

It does not mean that coding stops mattering. The developer who cannot read code, evaluate its quality, identify its failure modes, and reason about its architecture will not be an effective orchestrator of AI systems that produce code. You orchestrate from competence. The path to orchestrating runs through coding, and you do not arrive at the destination by skipping the foundation.

Every prior abstraction shift made the same demand. When FORTRAN arrived in the late 1950s, John Backus's team had to convince working programmers that compiled code could compete with hand-written assembly, and the programmers who used the new abstraction best were the ones who understood the machine underneath it. The abstraction moved the work up a level. It never excused ignorance of the level below.

It does not mean that doing is deprecated. At Stages 1 through 4 of the AI trust evolution, doing remains the primary mode of work. The shift to defining and orchestrating sits at the far end of that evolution, and most practitioners should be climbing the stages on solid infrastructure before claiming a redefined role.

And it does not mean that AI replaces the human. The word synergy carries the weight in that sentence. Synergy means the combination produces something neither party could produce alone. The human's judgment, intent, and contextual understanding are irreducible. The AI's execution speed, breadth of knowledge, and ability to parallelize work are irreducible in the other direction. The combination is the point.

## What It Does Mean

At Stage 8 of the trust evolution, the primary human contribution is intent. Intent is the goal, the constraints, the ethical guardrails, the business limits, the quality minimums, the audience considerations. It is what the system should optimize for, which trade-offs are acceptable, and which values should guide decisions in the cases where explicit instructions run out.

AI cannot answer those questions. They require judgment, context, and values, the specifically human contribution that does not compress. An AI system can execute against a well-defined intent with extraordinary capability. It cannot define the intent it should execute against. Peter Naur made the underlying argument in 1985 in "Programming as Theory Building": the real product of programming is the theory the builders hold about how the system maps onto the world, and that theory never fully survives translation into text. Intent is the modern name for Naur's theory. It lives in people.

The four words in the framework sentence have precise meanings.

**Doing** is task execution: writing the code, generating the analysis, drafting the document. At Stage 2, the human does the task with AI assistance. At Stage 8, AI executes the task with human direction.

**Defining** is intent formulation: what should the task accomplish, what does success look like, where are the boundaries, how should the system behave when instructions are ambiguous. This is irreducibly human at every stage.

**Coding** is producing software through direct authorship of instructions to a machine.

**Orchestrating** is directing AI systems, defining their tasks, evaluating their outputs, managing their coordination, and adjusting their constraints, to produce software at a scale and speed that direct authorship cannot match.

The shift is real. It requires a different kind of excellence.

## The Skills That Matter

The developer who is excellent at defining and orchestrating knows how to formulate intent precisely. Vague intent produces vague output, regardless of how capable the AI system is. Translating a business need into a clear, constrained, evaluable specification is the primary technical skill of the orchestrating developer.

That developer can evaluate AI output at the system level. The question moves from line-level correctness to behavior: does this system do what the intent specified? Answering it requires enough technical depth to evaluate the output and enough contextual understanding to evaluate it against the intent.

That developer understands failure modes at scale. Orchestrating ten concurrent agents that each produce a component of a system requires understanding how those components interact, how failure in one propagates to others, and how the governance infrastructure catches cascading failures. This is systems thinking applied to AI-native architectures.

And that developer designs governance before deploying autonomy. The constraints, quality gates, and audit trails that make an agent trustworthy come first. Deployment with confidence comes second.

## Where the Argument Could Break

Three objections deserve a serious answer.

The first is the pipeline problem. If orchestration competence is built by years of doing, and AI absorbs the doing that juniors used to learn on, the next generation never builds the foundation I just called mandatory. This is the strongest objection, and I concede most of it. The answer is that the apprenticeship must be redesigned on purpose, the way aviation and medicine moved early training into simulators when the live work became too consequential to learn on. Competence stops being a byproduct of production work and becomes a deliberate program. Organizations that skip that program will discover the gap in about five years.

The second comes from Joel Spolsky's law of leaky abstractions: all non-trivial abstractions leak, and when they leak the developer gets pulled down a layer. If AI-generated systems leak constantly, the orchestrator is just a coder with extra steps and a longer feedback loop. I read the leak rate as exactly what the trust evolution measures. At low stages the abstraction leaks everywhere and orchestration is premature. Governance infrastructure, the evaluation, constraints, and audit trails, is what makes the abstraction hold well enough to stand on.

The third is the historical record of this exact promise. CASE tools, 4GLs, and low-code platforms all claimed to move developers from coding to specifying, and the role kept reverting to coding. The pattern is a fair warning about timelines. The difference in kind is that every prior wave still required a human to author exact instructions in some formal language; the specification was just code by another name. Systems that execute against intent expressed in natural language plus constraints move where ambiguity gets resolved, and that is the change the earlier waves never made.

## The Through-Line

The craftsman in 2013 held to the standard: is this right? The orchestrator in 2026 holds the same standard at a different level: is this intent clear, well-constrained, and aligned with what we should be building?

The professional obligation does not change. The scale at which it is applied does.
