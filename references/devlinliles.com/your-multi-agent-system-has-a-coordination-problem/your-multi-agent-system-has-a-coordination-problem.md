---
type: Reference
title: "Your Multi-Agent System Has a Coordination Problem"
resource: "https://www.devlinliles.com/your-multi-agent-system-has-a-coordination-problem/"
author: "Devlin Liles"
published: '2026-08-20'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Single-agent systems have one set of problems. Multi-agent systems have all of those plus a new category: the problems that arise at the boundaries between agents. Who tells whom what to do. How agents share state without corrupting each other's work. What happens when agent A finishes and agent B was supposed to start. How the whole system knows it's done.

These are coordination problems, and they are distinct from execution problems. Execution is what individual agents do; coordination is the protocol between them when multiple agents must collaborate on a single goal. Getting coordination wrong is something most teams discover in production. That's the expensive way.

## The coordination model shapes everything downstream

There are six coordination models in use today, and they differ on the axes that matter most for production systems: debuggability, resilience, and coupling.

**Supervisor / worker** is a coordinator agent managing a pool of specialist workers: routing tasks, collecting results, reconciling outputs. Workers are stateless relative to each other. The supervisor has full visibility. This is the most common enterprise pattern and the most debuggable: when something goes wrong, you trace it to the supervisor's routing decision and the specific worker that handled it.

**Peer-to-peer / mesh** has agents communicate directly without a central coordinator. More resilient (no single point of failure) and much harder to debug. When the mesh produces a wrong output, tracing responsibility requires reconstructing a web of direct communications across the full graph.

**Blackboard** uses a shared state store that all agents read from and write to. Agents are decoupled from each other and only interact with the blackboard. Simple to add new agents. Complex to manage conflicts when two agents write to the same key simultaneously.

**Publish / subscribe** has agents publish events to topics and other agents subscribe and react. This is the AG2 / AutoGen v0.4 model. Fully decoupled; works well for pipelines where each agent transforms and re-publishes. It requires dedicated observability investment: when something goes wrong, the event chain is the debugging surface.

**GroupChat** puts all agents in a shared conversation; a selector agent or round-robin determines who speaks next. The natural fit for deliberation and brainstorming workflows. Less structured than the other models and better suited for exploratory tasks than production reliability.

**Handoff / swarm** has each agent, when done, explicitly name the next agent and transfer control with relevant context. Stateless and lightweight. The routing logic lives in agent outputs, not in a central orchestrator. This model fits when the next agent depends on the content of the current output, where a fixed workflow structure would be too rigid.

Start with supervisor / worker. It's the most debuggable model, the most common in production, and the most tractable when things go wrong. Move to pub/sub when your pipeline genuinely benefits from decoupling. Use mesh only when resilience requirements demand it and you're prepared to invest in observability to match.

## MCP: the bet that's already paying off

The coordination layer between agents and tools has a protocol that is becoming the standard: the Model Context Protocol (MCP), developed by Anthropic and open-sourced in late 2023.

MCP defines how LLMs interact with external systems (tools, context sources, data connectors) through a typed, versioned protocol. It went from an Anthropic-specific capability to a broadly adopted ecosystem in roughly twelve months. Claude supports it natively. Major frameworks integrate with it. There is now an expanding ecosystem of MCP connectors for the most common enterprise tools.

The strategic value of MCP is interoperability. An MCP-compliant connector works with any MCP-compliant agent. A tool built against the MCP spec today remains usable as models and frameworks turn over. This is the same argument that made REST and OpenAPI valuable: standardized interfaces reduce the coupling between the things that evolve fast (models, frameworks) and the things that evolve slowly (enterprise data sources, business tools).

Watch the Agent-to-Agent (A2A) protocol from Google. It is an early attempt at standardizing agent-to-agent communication in the same way MCP standardized agent-to-tool communication. Early, but the direction is clear: typed, versioned protocols for inter-agent communication, with framework-specific wiring on the way out.

## State isolation is a coordination requirement

The most common multi-agent failure mode is shared state corruption. Two agents write to the same memory layer with contradictory facts. Two agents modify the same file. Two agents call the same external API with conflicting payloads. None of these produce a thrown exception. They produce a subtly wrong output and a debugging session that traces back to a race condition.

State isolation is the architectural mechanism that prevents this. Each agent operates in its own lane: isolated working memory, a dedicated file system via git worktrees, and a session context that doesn't bleed into sibling agents. The coordinator owns the merge. It collects outputs from isolated workers and reconciles them deliberately. Conflicts get caught at the seam, not buried in shared state.

The rule: agents share context through explicit, versioned handoffs. Every coordination model that uses a shared store (blackboard, shared memory) needs a conflict resolution strategy built in. Every model that uses explicit handoffs gets conflict resolution structurally, without extra work.

## Escalation as a coordination mechanism

Escalation routes a decision or failure to a human when an agent lacks confidence or when the stakes exceed its authorization level. It is coordination in the same sense as the other models: a protocol for what happens when one participant cannot proceed without a resource the normal coordination model doesn't provide.

Good escalation produces a tracked record: who was escalated to, when, why, and what was decided. This record is audit data. It is also the signal for improving the agent's confidence calibration over time. If the same class of situation triggers escalation consistently, that pattern tells you the agent's capability in that area is improvable. The escalation records become the training data.

---

*Sources: Augment Code agentic design pattern catalog (2026) — coordination models; AG2 / AutoGen v0.4 documentation (pub/subscribe, GroupChat); OpenAI Swarm documentation (handoff / swarm model); Anthropic MCP documentation and open-source release; Google A2A protocol (early public documentation); DEV.to LangGraph vs CrewAI vs AutoGen comparison (2026); Iterathon agent orchestration guide.*
