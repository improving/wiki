---
title: "Your Multi-Agent System Has a Coordination Problem"
type: "Source Summary"
description: "Surveys six multi-agent coordination models, MCP as the tool protocol, state isolation, and escalation as coordination mechanisms."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/your-multi-agent-system-has-a-coordination-problem/your-multi-agent-system-has-a-coordination-problem.md"
---

# Your Multi-Agent System Has a Coordination Problem — Summary

**Original source**: `references/devlinliles.com/your-multi-agent-system-has-a-coordination-problem/your-multi-agent-system-has-a-coordination-problem.md`

## Summary

The post argues that multi-agent systems add a distinct class of coordination problems to ordinary execution problems, and that the coordination model shapes debuggability, resilience, and coupling downstream. It compares six models — supervisor/worker, peer-to-peer/mesh, blackboard, publish/subscribe, GroupChat, and handoff/swarm — and recommends starting with supervisor/worker as the most debuggable. It then treats [state isolation](/concepts/state-isolation.md) as a coordination requirement, positions [MCP](/entities/model-context-protocol.md) as the emerging agent-to-tool standard, and frames escalation as a coordination mechanism that produces audit and calibration data.

## Key Claims

- Six coordination models exist; supervisor/worker is the most common and most debuggable enterprise pattern, while mesh is most resilient but hardest to debug.
- [MCP](/entities/model-context-protocol.md), developed by [Anthropic](/entities/anthropic.md) and open-sourced in late 2023, went from an Anthropic-specific capability to broad adoption in roughly twelve months; Google's A2A is an early agent-to-agent counterpart.
- The most common multi-agent failure is shared state corruption — contradictory writes with no thrown exception, only a subtly wrong output.
- State isolation gives each agent its own working memory, git worktree, and session context; the coordinator owns the merge and conflicts surface at the seam.
- Escalation should produce a tracked record (who, when, why, decision) that doubles as audit data and training signal for confidence calibration.

## Relevance

Informs [multi-agent coordination](/concepts/multi-agent-coordination.md), [state isolation](/concepts/state-isolation.md), and [orchestration layer](/concepts/orchestration-layer.md) design, plus the coordination trade-offs behind [coordination overhead](/concepts/coordination-overhead.md).

## Quality

Practitioner blog post by Devlin Liles. Useful taxonomy with a clear default recommendation; evidence is design experience plus cited vendor docs rather than measured results.

## Entities Mentioned

- [Model Context Protocol](/entities/model-context-protocol.md) — the agent-to-tool protocol positioned as the emerging standard
- [Anthropic](/entities/anthropic.md) — developer of MCP
- [AutoGen](/entities/autogen.md) — cited as the AG2/AutoGen v0.4 pub/sub model
- [OpenAI Swarm](/entities/openai-swarm.md) — source of the handoff/swarm model

## Concepts Covered

- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — the post's central topic
- [state isolation](/concepts/state-isolation.md) — framed as a coordination requirement
- [orchestration layer](/concepts/orchestration-layer.md) — where routing and merge logic live
- [Coordination Overhead](/concepts/coordination-overhead.md) — the boundary cost that distinguishes multi-agent systems
