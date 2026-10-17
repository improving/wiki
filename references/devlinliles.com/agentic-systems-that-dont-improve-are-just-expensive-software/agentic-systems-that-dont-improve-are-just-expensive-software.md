---
type: Reference
title: "Agentic Systems That Don&#x27;t Improve Are Just Expensive Software"
resource: "https://www.devlinliles.com/agentic-systems-that-dont-improve-are-just-expensive-software/"
author: "Devlin Liles"
published: '2026-08-19'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# Agentic Systems That Don't Improve Are Just Expensive Software

The pitch for agentic AI is that it compounds. You invest in building a system, the system gets better over time, and the return on that investment grows without proportional additional effort. That pitch is true, but only for systems that have a feedback loop. Without one, you have expensive software that does the same thing next month that it does today, and you've added the operational complexity of managing agents on top of it.

Improvement is the domain that closes the loop between what the system does and what you want it to do. Most teams skip it, or implement it only superficially, because it is the hardest domain to build and the least visible in a demo. The compounding value promised by agentic AI lives here.

## Reflection: the pattern that's already in your prompt

The simplest improvement mechanism available is also the most widely deployed: reflection. Andrew Ng formalized this as a pattern: the agent reviews its own output before finalizing it, identifies weaknesses, and iterates. Write, critique, rewrite, applied in a loop.

This works. For tasks where a first draft is reliably improvable through self-critique, a reflection loop adds meaningful quality at a predictable inference cost. The ceiling is real: an agent can only critique its own output from its own perspective, so systematic blind spots don't get caught. Reflection is a within-session improvement pattern. It doesn't carry learning across sessions, and the behavior of the system itself doesn't change. It improves a specific output.

Reflexion, the formalized research version, goes one step further: it stores verbal memories of past mistakes and injects them into future prompts. The agent accumulates a failure diary that prevents repeating known errors. This is a bridge between within-session reflection and the session-to-session learning that memory enables. Reflexion is still primarily a prompting pattern. The learning lives in text that gets injected, not in a structured memory architecture.

## Process Reward Models: catching errors early in the chain

Most evaluation happens at the end. The output is produced; then it is assessed. For short tasks, this is fine. For long chains of reasoning, the kind that characterize complex agentic workflows, evaluating only the final output means errors in step three compound through steps four, five, and six before anyone catches them.

Process Reward Models (PRMs) evaluate the quality of intermediate reasoning steps, not just final outputs. A separate model is trained to score each step in the chain. When a step scores poorly, the system catches the error before it propagates. This is more expensive to build than an output-level judge and more reliable at scale for long-horizon tasks.

The PRM approach requires training data: examples of good and bad intermediate steps with scores. This investment is significant and is why PRMs are more common in research contexts than in production deployments. The direction is clear, and the teams that invest in PRMs for their highest-stakes workflows get meaningful reliability improvements that output-only evaluation cannot produce.

## RLHF vs RLVR: the practical choice

The dominant approach for training improvement into foundation models is Reinforcement Learning from Human Feedback (RLHF). A reward model is trained from human preference data, then used to optimize the agent toward high reward. This works. It also requires a significant investment in human annotation, reward model training infrastructure, and RL expertise that most application-layer teams do not have.

DeepSeek R1, released in January 2025, demonstrated a more tractable path: Reinforcement Learning with Verifiable Rewards (RLVR). The insight is that many structured tasks have objectively verifiable outcomes. Code compiles or it doesn't, and tests pass or fail. In domains like those, the environment is the reward signal. No annotation pipeline. No trained reward model required.

For application-layer teams building agentic workflows around structured tasks, RLVR is the practical path. The investment is defining the verification function, writing the test, building the checker, rather than building the annotation pipeline and reward model. For tasks with clear correctness criteria, this is a genuine simplification.

## How successful runs teach the system

Most improvement systems are failure-oriented. They log what went wrong and try to prevent recurrence. Trajectory-informed memory, documented in arxiv 2603.10600, takes the complementary approach: store complete action sequences of successful runs as trajectories, and when a new task arrives, retrieve similar past trajectories and use them as strategy templates.

This has a specific advantage: it compounds positive performance rather than only clamping negative outcomes. A system that learns from successes builds a library of proven approaches. A system that only catalogs failures converges on avoiding known mistakes while potentially leaving proven patterns unused.

The chart above shows what these feedback loops look like over time. A system with no feedback loop plateaus at wherever it starts. A system with reflection improves incrementally. A system with trajectory-informed memory and verifiable rewards compounds, not without limit, but along a curve that looks meaningfully different at month six than it did at month one.

## What harness simplification actually means

There is an improvement pattern that sounds mundane and consistently outperforms the exotic ones: harness simplification. Systematic identification and removal of unnecessary complexity from prompts and workflows, with measurement of adherence delta before and after.

The finding, consistent across every team we've run this with: prompt complexity is often the primary obstacle to improvement, and removing it yields more gains than model upgrades. An agent navigating a long, internally-contradictory prompt is doing work that doesn't benefit the task. Every constraint that isn't serving the goal is degrading performance on the goal.

The practice: audit prompts for dead instructions, constraints that outlived their purpose, and any formatting rule the model is gaming rather than following. Measure adherence before and after. This is unglamorous work that consistently produces results, which is probably why it's rarely what teams reach for first.

---

*Sources: Andrew Ng's agentic design patterns series (reflection pattern); Reflexion paper (Shinn et al.); DeepSeek R1 (Jan 2025) — RLVR at scale; arxiv: trajectory-informed memory (2603.10600); arxiv: six sigma agent (2601.22290, Jan 2026); Aman's AI Journal agentic RL primer; Daily Dose of DS on RL agents in labs (2026); Zylos Research on reflection patterns (Mar 2026).*
