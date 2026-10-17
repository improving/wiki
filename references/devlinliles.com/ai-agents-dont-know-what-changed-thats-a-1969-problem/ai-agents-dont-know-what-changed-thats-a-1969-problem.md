---
type: Reference
title: "AI Agents Don&#x27;t Know What Changed. That&#x27;s a 1969 Problem."
resource: "https://www.devlinliles.com/ai-agents-dont-know-what-changed-thats-a-1969-problem/"
author: "Devlin Liles"
published: '2026-08-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most common failure mode in production AI agents isn't hallucination. It's something more subtle and more insidious: the agent doesn't know what it already did, what's still true, and what changed as a result of its last action. It operates on a stale picture of the world and produces outputs that are locally coherent but globally wrong.

This problem was identified in 1969. John McCarthy and Patrick Hayes named it the frame problem. The original formulation was about formal logic systems for AI planning: how does an agent know which facts remain true after an action is taken? You move a block from table A to table B. The block's position changes. Everything else stays the same. A human reasoner handles this effortlessly through background common sense. A formal planning system has to explicitly account for every fact that didn't change, or it can't reason correctly about the resulting state.

The frame problem has never been solved. It's been partially managed, in narrow domains, through various engineering workarounds. And now we've deployed agents that do complex multi-step tasks in the real world, and the frame problem is back: at scale, in production, causing enterprise AI projects to fail in exactly the ways the original problem predicted.

A 2026 analysis found that roughly 65% of enterprise AI failures traced to context drift or memory loss during multi-step reasoning, not raw context window exhaustion. The agents fail silently, producing plausible-looking output while operating on degraded, incorrect, or incomplete world state. State persistence is the largest category: the agent doesn't correctly track what state it's in. Context drift (where the agent's effective world model diverges from actual system state as a chain of actions accumulates) is the second.

None of these are exotic edge cases. They're the predictable consequences of deploying an architecture that was never designed to track state across a sequence of actions in a changing world.

The frame problem is hard because naive solutions don't scale. You could tell the agent to re-verify every relevant fact after every action. That solves the correctness problem and creates a performance problem: the verification overhead becomes prohibitive for any non-trivial task. Modern agent frameworks have converged on a partial solution: explicit state management as a first-class architectural component. Structured checkpointing, working memory that the agent reads and writes explicitly rather than relying on context window history, and tool calls that verify current state before acting rather than assuming state from prior context.

The frame problem gives you a specific vocabulary for agent design decisions that teams are currently making by intuition. Task decomposition is a frame management strategy — when you break a long agentic task into shorter sub-tasks with explicit handoff points and state summaries between them, you're resetting the frame at each boundary. State schemas are frame definitions. Verification steps are frame reset operations. The most reliable agentic systems in enterprise production include explicit verification calls before consequential actions: before writing a record, confirm the record doesn't already exist; before sending a communication, confirm the prior step completed.

Context engineering is becoming a recognized discipline for exactly this reason. A 2025 paper framing it as a field treats context as a first-class system component with its own architecture, lifecycle, and constraints. That framing maps almost exactly onto what the frame problem requires: you can't just let the agent figure out what's relevant from a long context window. You have to design the context explicitly, the same way you'd design any other system with state.

The frame problem wasn't solved in the symbolic AI era. Current research on memory architectures, structured agent state, and context engineering represents the latest iteration of the same management strategy: don't solve the problem, build scaffolding that constrains it. The deliberateness of that scaffolding's design determines whether agents are reliable or whether they're completing most steps correctly and failing silently on the rest.
