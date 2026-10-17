---
type: Reference
title: "The Orchestration Model You Pick Is the Architecture Decision You Can&#x27;t Undo"
resource: "https://www.devlinliles.com/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo/"
author: "Devlin Liles"
published: '2026-08-18'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# The Orchestration Model You Pick Is the Architecture Decision You Can't Undo

Teams tend to pick an orchestration framework the way they pick a JavaScript framework: whatever the first engineer already knew, or whatever had the best tutorial. Three months later, they're fighting the architectural constraints of that choice, and migrating is as painful as migrating a database schema with live traffic on it.

The orchestration model is not just a tooling preference. It determines what error handling you can build, how you checkpoint state, what intervention looks like in live systems, and whether your system can be debugged when things go wrong. Picking it casually is expensive.

There are three dominant models in deployed workflows today. They are not points on a spectrum. They disagree at the level of how state is owned, who coordinates, and what failure looks like.

## Stateful graph execution: the production-grade option

LangGraph models workflows as directed acyclic graphs with typed state. Edges can be conditional. Nodes can run in parallel. State is checkpointed at each node. This is the most capable execution model available today for complex workflows.

The tradeoffs are real: setup is not simple, debugging requires understanding graph traversal, and the DAG abstraction adds cognitive overhead that simpler models don't. But the benefits are concrete. Checkpointing means you can pause at any node, inspect state, modify it, and resume. That's what makes LangGraph's interrupt-and-resume the only deployed pattern I've seen that lets you pause mid-graph, modify state, and replay without restarting the task. Conditional edges mean error handling is first-class, not bolted on. Typed state means you can reason about what an agent knows at each step.

Most teams that start with a simpler framework eventually migrate to LangGraph when they hit real traffic. The migration is hard. Starting here, if you can tolerate the learning curve, saves that work.

## Role-based crew execution: fast to start, limited at scale

CrewAI organizes agents as a team with defined roles, researcher, writer, reviewer, and handles agent-to-agent handoffs. Configuration is simple. If your workflow maps cleanly onto a set of roles with sequential or hierarchical handoffs, CrewAI gets you to a working prototype faster than anything else in this category.

The ceiling appears when you need fine-grained state control, complex error handling, or intervention mechanisms for deployed systems. The framework handles handoffs; it doesn't expose the state machinery needed to pause, inspect, and resume mid-execution. Teams running CrewAI typically either constrain their workflows to fit the framework's model, or they migrate to LangGraph. The pattern from the field is consistent: CrewAI for prototyping, LangGraph for what ships.

## Event-driven execution: built for async pipelines

AG2 (AutoGen v0.4) is async-first. Agents communicate by publishing and subscribing to events. A selector agent determines who acts next, or the system uses GroupChat coordination for deliberative workflows. This model works well for conversational and research pipelines where the next step depends on the content of what was just produced.

The strength of the event-driven model is decoupling. Agents don't need to know about each other, only about the events they care about. Adding a new agent is a matter of subscribing it to the right topics. The weakness is debuggability: when something goes wrong in an event chain, tracing the failure back to its origin requires following a log of published events across potentially many agents. Observability is not optional with this model.

## The supervisor / subagent pattern

The dominant multi-agent structure in deployed systems is supervisor / subagent. A coordinator agent decomposes tasks and delegates to specialist subagents. The coordinator tracks completion, handles failures, and merges results. Workers are stateless relative to each other; they receive tasks from the coordinator and return results.

This structure is compatible with any of the three orchestration models above. The supervisor is a node in your graph, a role in your crew, or an agent in your event system. What makes it a design choice rather than a framework feature is the explicit separation of concerns: the coordinator knows the full problem and none of the domain; the specialists know the domain and none of the full problem.

The failure mode to watch for is a coordinator that grows too large. If your coordinator is doing substantive reasoning about domain content rather than routing and tracking, you've blurred the separation and created something that is hard to debug and hard to replace.

## Execution primitives worth understanding

Reliability compounds downward. A single agent completing a single task with 95% reliability sounds acceptable. Twenty chained steps at 95% per step gives you a 36% chance the whole chain succeeds. The chart above makes this concrete. Execution architecture matters because the mechanisms that prevent failures from cascading, circuit breakers, worktree isolation, bounded sessions, are basic correctness requirements for multi-step workflows. Not performance optimizations.

Worktree isolation deserves specific mention for development workflows. Each agent gets its own git worktree, preventing file-system conflicts when multiple agents write in parallel. Without isolation, two agents modifying the same file produces merge conflicts at best and silent overwrites at worst.

Skill composition is the unit of reuse. A mature agentic system invokes versioned, tested skill definitions rather than regenerating behavior from scratch for every task. Each well-defined skill reduces the surface area of future failures. The investment compounds in the same direction technical debt does, just in the other direction.

## Where execution choices bind you

LangGraph is the right answer for workflows that need human oversight or complex error handling. The cost is upfront: setup time, learning curve, and a team that has to understand graph traversal. CrewAI gets you to a working prototype in a day. It costs you later, when you need to scale past the happy path. AG2 is a different shape entirely. If your workflow is async and conversational, it fits well. If it's not, you'll fight it.

Match the model to your actual requirements. The prototype that ships fastest is not always the one that survives contact with real traffic.

---

*Sources: DEV.to LangGraph vs CrewAI vs AutoGen comparison (2026); Iterathon agent orchestration guide; LangGraph documentation; CrewAI documentation; AG2 / AutoGen v0.4 documentation; Augment Code agentic design pattern catalog (2026); OpenAI Swarm (experimental / educational reference).*
