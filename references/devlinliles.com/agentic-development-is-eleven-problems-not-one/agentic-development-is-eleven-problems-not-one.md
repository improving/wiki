---
type: Reference
title: "Agentic Development Is Eleven Problems, Not One"
resource: "https://www.devlinliles.com/agentic-development-is-eleven-problems-not-one/"
author: "Devlin Liles"
published: '2026-08-17'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most agent projects fail at the same place and for the same reason. A team picked up one tool, pointed it at a problem, and discovered six months later that the tool only solved one of the eleven things standing between them and a working system.

I've been mapping this space for the better part of 2026, and the clearest thing I can tell you is that agentic development is eleven distinct competency areas, each with its own vocabulary, its own failure modes, and its own tooling ecosystem. Confuse them and you'll spend three months fighting the wrong battle.

The right mental model is Lego bricks. Each competency block is a discrete, well-defined piece. Blocks in the same layer connect naturally to each other. Layers stack. Upper layers depend on what's below them, but you can start assembling from wherever your current problem demands. No single sequence fits every team. What matters is knowing which blocks you have, which ones you're missing, and how the gaps in your current assembly are costing you.

This post is the map. The eleven posts that follow go deep on each block. Read this one first: it tells you how the pieces relate and what breaks when key ones are absent.

## The four layers

**Foundation** is where agents do work and work together. Execution converts intent into action: state management, routing, parallel coordination, resource isolation. Coordination is the protocol between agents when multiple must collaborate on a single goal. Without a solid foundation, nothing built on top of it is stable.

**Operational** is what keeps the system coherent across time and failures. Memory separates an agent that improves across sessions from one that resets to baseline every morning. The field converged in 2025 on a four-type taxonomy (working, episodic, semantic, procedural), and most teams implement only the first. Context management is the discipline of keeping the working window filled with exactly the right information for the current step. Error handling is recognizing that agentic failures include semantic drift, technically correct execution toward the wrong goal, not just thrown exceptions.

**Governance** controls what happens and what's recorded. Definition answers what, exactly, each piece of work means; agents are completion-seeking and will execute correctly toward a misspecified goal. Auditing produces a complete, tamper-resistant record of decisions, tool calls, and outputs. The OpenTelemetry GenAI semantic conventions are rapidly becoming the standard here, adopted natively by Datadog from v1.37 in December 2025. Intervention is the set of mechanisms that let humans or systems modify in-flight or failed execution before damage compounds.

**Intelligence** is what makes the system smarter over time. Planning converts an underspecified goal into a structured sequence of intended actions before anything executes. A bad plan propagates into all ten other blocks. Evaluation measures behavior against defined criteria with enough rigor to detect regressions and route from data, not gut feel. Improvement closes the loop: outcome signals change future behavior. That's how agentic systems accumulate value instead of just running reliably.

## How the blocks connect

These blocks are not independent. Pull one out and you feel it in the layers above.

Teams that skip Definition find their Execution blocks executing confidently in the wrong direction. Teams that skip Memory find their Improvement blocks have no substrate to write learned behavior into. Teams that skip Auditing find their Evaluation blocks have no trace data to score against. Teams that skip Error Handling find their Intervention blocks firing too late, after the damage, not before.

The failure pattern I see most often: a team builds a solid Foundation layer, adds just enough Governance to satisfy a compliance requirement (usually Auditing), and then stalls. They can tell you what happened. They cannot yet measure whether it got better, modify it in flight, or improve it without manually rewriting prompts. The compounding value promised by agentic AI lives in the Intelligence layer. That's the reason the investment is worth making, and most teams haven't built there yet.

## What this series covers

The next eleven posts go one block at a time. Each one maps the core concepts, the approaches working in production, the tools worth knowing, and where each approach breaks down. I'm not trying to pick winners. The field is moving too fast for that. I'm trying to give you enough clarity on each problem space to audit your own stack: not just identify the gap, but understand what's failing because of it.

The blocks that rarely appear in the canonical "how to build agents" lists but matter enormously in production are Coordination and Context Management. I've put them near the end of the series, but if you're already running multi-agent systems in production, read those two first.

Every block has trade-offs. The right implementation depends on your problem, your team's current capabilities, and how much you're willing to invest in infrastructure that doesn't directly ship features. Those trade-offs are what I'll keep surfacing across every post.

---

*Sources: Augment Code agentic design pattern catalog (2026); Vellum agentic workflows guide; Confident AI observability comparison (2026); Braintrust LLM observability buyer's guide (2026); CoALA framework (arxiv 2603.04740); OpenTelemetry GenAI semantic conventions (semconv).*
