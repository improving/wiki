---
type: Reference
title: "Why Your Agent Forgets Everything Every Morning"
resource: "https://www.devlinliles.com/why-your-agent-forgets-everything-every-morning/"
author: "Devlin Liles"
published: '2026-08-18'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

The most common complaint I hear from teams that have deployed agents into real workflows: "it keeps making the same mistakes." They've seen the failure mode. They've told the agent about it. They've watched it fix the problem in the session where they mentioned it, and then seen the exact same mistake three sessions later with a different user.

The agent isn't broken. It just has no place to put what it learns. In most deployed agentic systems, retention is not designed. It happens by accident, incompletely, or not at all.

Memory is the domain that separates an agent that compounds value over time from one that resets to baseline every session. The field converged in 2025 on a framework for thinking about this clearly.

## The CoALA taxonomy: four types, not one

The cognitive architecture research community gave the agentic field a useful gift in 2024: the CoALA framework (Cognitive Architectures for Language Agents, arxiv 2603.04740), which maps agent memory onto four types borrowed from cognitive science. Every memory capability an agent can have fits into one of these categories. Most deployed systems implement only the first.

**Working memory** is the active context window: what the agent can see right now. It is finite, ephemeral, and the primary constraint on agent capability. Every other memory type is a mechanism for extending effective working memory beyond what fits in the context limit at any given moment.

**Episodic memory** records what happened: past sessions, interactions, decisions, outcomes. It is temporal and event-anchored. "The agent has encountered this error pattern three times in the past month" is an episodic claim. Episodic memory is what allows an agent to say "I've seen this before" and act differently because of it.

**Semantic memory** stores extracted facts and beliefs: user preferences, entity properties, domain knowledge, architectural decisions. It is largely atemporal. It represents what the agent currently believes is true, not what happened. Semantic memory is what allows an agent to answer questions from retained knowledge rather than re-deriving it each time.

**Procedural memory** encodes learned strategies and workflows. "When this class of error occurs, follow these steps." LangMem takes this furthest: it allows agents to rewrite their own system prompts based on procedural learning that builds over time. This is the hardest memory type to implement well and the highest-leverage when it works. An agent with procedural memory doesn't just know more. It behaves differently.

## What MemoryAgentBench found

The primary evaluation benchmark for agent memory systems as of 2026 is MemoryAgentBench, which probes four competencies: accurate retrieval, test-time learning, long-range understanding, and selective forgetting. The benchmark's central finding: no current system masters all four.

Selective forgetting is the hardest. This is the ability to intentionally remove or down-weight outdated, contradicted, or low-signal memories. Every other memory operation (retrieval, consolidation, compaction) is additive or neutral. Forgetting requires the system to identify what should no longer be believed. Current systems are far better at retaining knowledge than at discarding it when it goes stale.

The practical consequence: agent memory systems degrade in a specific direction. They don't lose facts. They stockpile outdated ones. An agent told in January that the team uses Postgres and told in April that the team migrated to CockroachDB will, without selective forgetting, hold both beliefs simultaneously and make unpredictable choices about which to act on.

## The memory operations that matter

Retrieval is finding relevant memories given current context. The standard approach is semantic similarity search over a vector store: the agent embeds the current query and retrieves the most similar past entries. This works well when the relevant memory is semantically close to the current question and poorly when the relationship is structural or temporal rather than semantic.

Consolidation is merging related episodic records into a durable semantic fact. The process by which short-term experience becomes long-term knowledge. "We've seen this API return a 429 three times in the past week" is episodic. "This API rate-limits at roughly 100 calls per minute" is a consolidated semantic fact. The consolidation process is what prevents episodic memory from growing unboundedly.

Temporal tracking is recording not just what a fact is but when it became true and when it changed. Mem0 stores facts with timestamps; Zep / Graphiti builds a temporal knowledge graph that tracks the full history of belief changes. For knowledge that evolves (team structure, architectural decisions, API contracts), temporal tracking is what distinguishes "this was true" from "this is true."

## The tools that are working

Mem0 is the most widely deployed memory system in production agentic applications as of mid-2026, with approximately 48,000 GitHub stars and $24 million raised in October 2025. It focuses on semantic memory with temporal tracking. It is the pragmatic choice for teams that need production-grade memory without building their own retrieval infrastructure.

LangMem, part of the LangChain SDK, handles episodic, semantic, and procedural memory, including the system-prompt rewriting capability that makes procedural memory actionable. Zep / Graphiti is the right choice when temporal knowledge tracking is a primary requirement: when you need to know not just what the agent believes but when it started believing it and what changed. Letta, built on the MemGPT architecture, is the most memory-complete framework available, treating memory as a first-class architectural concern.

The vector store layer (Chroma, Pinecone, Weaviate) is the retrieval backend for any of these. Choosing a vector store is not the same as choosing a memory architecture. The store is infrastructure, and most production teams should pick the managed option (Pinecone) unless they have a specific reason to run their own.

## What good memory design looks like

Before you pick a framework, name what you actually need the agent to remember. That sounds obvious. Most teams skip it.

The failure pattern I see most often: a team ships Mem0 because it's production-ready and has strong semantic memory support, gets six months in, and discovers their customer support agent has zero procedural memory. Every mistake gets repeated because nothing feeds back into behavior. The agent remembers facts about the user but has no mechanism to learn from its own errors. Those are different gaps, and conflating them is how you end up six months in with a vector store that covers one memory type and silent holes in the other three.

A customer support agent that can't recall a user's preferences across sessions isn't broken. It's missing semantic and episodic memory. That's a design gap with a specific solution. Reach for Mem0 or LangMem and define what gets consolidated into long-term storage at session end. For an agent that needs to reason about what was true three months ago, temporal tracking is the requirement, and that points to Zep / Graphiti specifically.

The CoALA taxonomy is useful precisely because it forces the question upfront: memory for what purpose? Name the type first. Then pick the tool.

---

*Sources: CoALA framework (Cognitive Architectures for Language Agents, arxiv 2603.04740); MemoryAgentBench (2026); Mem0 documentation and funding announcement (Oct 2025, ~48K GitHub stars, $24M raised); LangMem (LangChain SDK) documentation; Zep / Graphiti documentation; Letta / MemGPT documentation; Zylos Research on memory architectures (Apr 2026); Atlan memory type taxonomy.*
