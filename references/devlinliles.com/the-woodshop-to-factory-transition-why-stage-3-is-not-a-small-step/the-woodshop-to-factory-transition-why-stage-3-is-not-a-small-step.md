---
type: Reference
title: "The Woodshop-to-Factory Transition: Why Stage 3 Is Not a Small Step"
resource: "https://www.devlinliles.com/the-woodshop-to-factory-transition-why-stage-3-is-not-a-small-step/"
author: "Devlin Liles"
published: '2026-06-16'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most teams approach the move from AI-assisted work to autonomous AI agents the way they approached the move from manual deployments to CI/CD: they expect an increment.

It is a category change. The transition from Stage 2, AI as tool, to Stage 3, task agents with real autonomy, is a change in operating environment, and the best analogy I know is the move from the woodshop to the factory. Manufacturing made this exact transition once, and the history of how it went is worth keeping in view.

## The Woodshop

A skilled craftsman works in a woodshop. The environment is personal. Every tool is in the craftsman's hands. Every motion is controlled by the craftsman's judgment: the pressure of the saw, the depth of the chisel, the angle of the plane. When something goes wrong, the craftsman is there to notice it, stop, and correct. The feedback loop is continuous and immediate.

The craftsman's quality standard is enforced by the craftsman's presence. There is no quality gate independent of the craftsman's judgment because the craftsman is always the quality gate.

Stage 2 AI use is the woodshop. The developer uses AI-assisted tools, reviews every output, makes every decision. The AI is a tool in skilled hands. Quality is enforced by the developer's continuous presence. The mental model is: I am here, I am watching, I will catch anything that goes wrong.

This works well. It is productive. It is also not autonomous.

## The Factory

A factory runs machinery that operates without the craftsman's continuous physical presence. The machines produce output continuously, at volume, on defined cycles. The craftsman who designed the factory does not stand next to each machine watching every cut.

The factory also does not let the machines run and hope. The transition from craft shop to factory required building an entirely different operating environment:

- **Safety systems** that stop machinery the moment it exceeds its safe operating parameters, without waiting for anyone to notice
- **Quality standards** codified in written specifications that exist outside any one person's head
- **Inspection points** where output is measured against specification before it passes to the next stage
- **Maintenance protocols** that keep machinery operating within its design parameters
- **Material specifications** that ensure inputs meet standards before they enter the process

None of these existed in the woodshop. The craftsman was all of them. In the factory, each one had to be designed, built, and operated explicitly.

Industrial history records how hard this lesson was to learn. Quality in the craft era lived in the person. Quality in the factory era had to live in the process, and it took decades to work out how to put it there. Walter Shewhart's control charts at Bell Labs in 1924 marked the moment manufacturing accepted that inspecting finished goods was too late, and that quality had to be measured and managed throughout the process. Statistical process control, and Deming's postwar work in Japan, descend from that shift.

You cannot bring the woodshop mindset into the factory. If you run factory machinery on continuous personal oversight, you will discover that the machinery runs whether you are watching or not. Things will go wrong that you did not catch, and the failures will cascade in ways the safety systems would have contained.

## Stage 3 Requires Factory Infrastructure

Stage 3 autonomous AI agents are factory machinery.

They execute without continuous human oversight. They make decisions in sequence, at speed, at scale, faster than the human who designed the workflow can review individually. When they encounter an edge case, they do not pause and wait. They apply their best judgment and continue.

The woodshop AI user who graduates to Stage 3 without building factory infrastructure will experience what every craftsman who went into factory production without safety systems experienced: things go wrong in surprising ways, the errors compound before anyone notices, and the conclusion is often that autonomous AI does not work, when the actual problem is that the operating environment for autonomous AI was never built.

The factory infrastructure required for Stage 3:

**Agent boundaries:** What is the agent allowed to do? What data can it access? What systems can it modify? What decisions require human approval? These boundaries need to be explicit, codified, and enforced. A boundary assumed to be implicit in the agent's training is a hope, and hope is poor infrastructure.

**Quality gates:** At what points in the pipeline does output get validated against defined criteria before passing forward? What happens when validation fails: retry, fallback, or human review? These need to be designed and implemented before the pipeline runs.

**Audit trails:** What did the agent do, when, why (what input produced what decision), and what were the outcomes? Without audit trails, debugging a Stage 3 agent failure is guesswork. With them, it is diagnosis.

**Error handling:** What happens when a step fails? Does the pipeline stop? Does it roll back? Does it route to a human for decision? The error handling protocol needs to be designed before the first production run, because designing it after the first production failure costs far more.

## Where the Argument Could Break

Two counterarguments deserve attention. The first says the analogy will age badly: models are improving fast, and an agent that monitors its own work makes external infrastructure unnecessary. I read self-monitoring as factory infrastructure. A safety interlock built into the machine is still a safety interlock. What matters is that the check exists and was deliberately engineered; where it lives is an implementation detail.

The second says infrastructure-first is waterfall thinking, and that teams learn which gates they need by running the pipeline. Partially right. Nobody can specify every quality gate in advance, and the factory analogy carries the answer here too: factories run pilot lines at low volume before committing to full production. Run the agent pipeline small, watched, and instrumented. Learn where it breaks. Build the gates. Then scale. What the history does not support is scaling first and retrofitting safety after the incident.

## The Investment Required

The woodshop-to-factory transition requires investment before it produces return. This is where many organizations get into trouble: they see the potential value of autonomous agents, skip the infrastructure investment to capture the value faster, and end up with unreliable systems that damage organizational confidence in autonomous AI.

The factory infrastructure is the mechanism by which the factory produces reliable output at scale. The craftsman who skips it is building a system that cannot be trusted to operate at the volume that makes it valuable.

Build the infrastructure first. The machinery runs better, and it runs reliably.
