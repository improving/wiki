---
type: Reference
title: "The Plan Is a First-Class Artifact"
resource: "https://www.devlinliles.com/the-plan-is-a-first-class-artifact/"
author: "Devlin Liles"
published: '2026-08-17'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Ask most engineers how their agent decides what to do next and they'll say "it reasons through it." That's true as far as it goes, and it's precisely the problem. Reasoning through it is not a plan. It is a series of local decisions made without any view of the whole: what distributed systems engineers call a greedy algorithm, and what everyone else calls winging it.

Planning is the domain that sits upstream of all ten others in agentic development. A wrong plan does not stay in planning. It propagates. You execute confidently in the wrong direction. You consume budget. You create artifacts that have to be unwound. The cost of a bad plan is not paid at planning time; it's paid across everything that follows.

The field has converged on several patterns. They are not interchangeable.

## ReAct: the dominant loop that doesn't scale

ReAct (Reason, then Act) is the planning model most people encounter first because it is what most LLM agent frameworks implement by default. The agent reasons about what to do, acts, observes the result, reasons again. Step by step. One decision at a time.

This works well for simple, bounded tasks. It fails in a specific and predictable way when tasks get complex: the agent cannot look ahead. Each step is optimal given what came before, but there is no mechanism for evaluating whether the accumulated path is taking the agent toward the actual goal. By step fifteen of a fifty-step task, a ReAct agent has drifted. No single step was wrong. No step had visibility into the whole.

## Plan-then-Execute: the production pattern

Plan-then-Execute separates the planning phase entirely from execution. The plan is produced first as a reviewable artifact: a structured sequence of intended actions before anything in the real world changes. Then someone (human or automated gate) approves it. Then execution begins.

This matters for one reason above all others: it inserts a decision point between intent and consequence. The plan can be rejected. It can be modified. It can be compared against prior plans for similar tasks. None of that is possible when planning and execution are interleaved.

Production teams converge on this pattern because it is the only approach that gives you a meaningful approval gate. You cannot audit or approve something that doesn't exist as an artifact.

## Tree of Thought and LATS: when the cost of being wrong is high

Tree of Thought (ToT) generates multiple candidate plans and evaluates them before committing to any one. Where ReAct makes one bet per step, ToT explores the search space. It carries a real inference cost. It is also correct in a way ReAct cannot be for tasks where a wrong first decision is high-stakes and hard to walk back.

Language Agent Tree Search (LATS) takes this further: Monte Carlo tree search combined with an LLM value function. The agent samples paths, expands them, and back-propagates value estimates across the tree before committing. It is the state of the art for planning under uncertainty, and the inference cost reflects that. You run LATS on tasks where the wrong path is expensive to discover and even more expensive to undo, not on anything you can roll back with a quick fix.

Match the planning pattern to the reversibility of the work. ReAct for anything you can roll back cheaply. Plan-then-Execute at minimum for anything you cannot. ToT when you can afford the inference overhead and the cost of a bad path justifies it.

## Hierarchical planning: making large goals tractable

Hierarchical planning decomposes goals at multiple levels of abstraction: goal to epic to story to task. Each level is planned independently with appropriate context. No single planning context has to hold the whole problem.

This is what makes large goals manageable. A single flat plan for a complex engineering initiative will either be too shallow (misses dependencies) or too long (overflows the planning context and degrades). Hierarchical planning sidesteps both problems by scoping each level to what is knowable at that level of abstraction.

Watch for the failure mode where levels don't actually decompose. A hierarchy where every task at the story level is still underspecified produces the same problems as flat planning, with added overhead on top. If your story-level tasks could have been written by anyone who never read the epic, the hierarchy isn't doing anything.

## The human-in-the-loop spectrum

Human oversight of planning exists on a dial. Most teams treat it like a switch.

The gate question is not whether to have human oversight. It's where. Teams that approve every step create friction that kills adoption; teams that approve nothing ship agents that send emails they didn't mean to send. The answer most production systems land on: run freely through anything reversible, pause before anything that cannot be undone.

Two tools make this workable in practice. HumanLayer is an open-source library that wraps any agentic workflow with approval gates via Slack DM, email, or custom UI, using a decorator pattern. LangGraph's interrupt-and-resume pauses execution at any graph node, surfaces state to a human, accepts modifications, and resumes from that point. The latter is more powerful and more complex; the former is easier to retrofit to an existing system.

Set your gate position by asking: if this step runs and produces a wrong result, how hard is it to undo? If the answer involves a support ticket, a compensating transaction, or a conversation with a customer, the gate belongs before that step.

## Where planning breaks down

Constraint propagation is the mechanism for threading hard constraints through the planning hierarchy: budget, timeline, technical dependencies. Most planning implementations skip this. The result is a plan that is internally consistent but violates a constraint the planner didn't know to enforce. The most common version of this: a plan that is technically correct and schedule-breaking, discovered only when someone compares the plan against the project timeline.

Planning also assumes the goal is well-specified. It has no mechanism for discovering what the goal should be. That is definition's job, and definition is where this series goes next.

---

*Sources: Augment Code agentic design pattern catalog (2026); Vellum agentic workflows guide; DEV.to LangGraph vs CrewAI vs AutoGen comparison (2026); HumanLayer documentation; LangGraph interrupt-and-resume docs; arxiv: Language Agent Tree Search (LATS); Andrew Ng's agentic design patterns series.*
