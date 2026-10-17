---
title: "Multi-Agent Coordination"
type: "Concept"
description: "The problem of making specialized agents work together, where failures concentrate at the boundaries between them."
created: '2026-10-17'
updated: '2026-10-17'
tags: [orchestration, reliability, agents]
sources:
  - "/sources/agentic-development-is-eleven-problems-not-one.md"
  - "/sources/biological-coordination-patterns-applied-to-multi-agent-software-delivery.md"
  - "/sources/check-it-before-it-crosses-verifying-a-claim-before-the-next-agent-trusts-it.md"
  - "/sources/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled.md"
  - "/sources/the-orchestration-layer-is-the-reliability-lever.md"
  - "/sources/the-single-agent-ceiling-why-one-ai-cant-hold-your-whole-delivery-lifecycle.md"
  - "/sources/your-multi-agent-system-has-a-coordination-problem.md"
---

# Multi-Agent Coordination

Multi-agent coordination is the problem of making several specialized agents work together on one delivery lifecycle. The recurring claim across this corpus is that coordination is a distinct problem from execution: individually competent agents still ship errors at the seams between them, and coordination failures usually surface in production rather than in tests. Architecture — not raw model strength — is the reliability lever.

## Key Claims

- Coordination overhead grows faster than agent count, echoing Brooks's law; ten nodes yield up to 45 connection pairs, and staffing one human overseer per agent lowered throughput below the single-agent baseline.
- The supervisor/worker model is the most debuggable and most common enterprise pattern; shared-state corruption is the most common multi-agent failure mode, so state isolation and standardized protocols matter.
- Orchestration beats model quality: FlowReasoner's query-specific flows beat o1-mini's fixed pipeline by 10.52%, MPO planning let Llama-3.1-8B beat GPT-4o-mini by 30.1%, and Anthropic's orchestrated research beat a single Opus 4 agent by 90.2% at roughly 15x tokens.
- Single agents plateau at a 15–50% gain because one perspective cannot hold every competing delivery concern.
- A verify-claim node before each handoff checks groundedness before claims reach shared state, sharply cutting claim-survival and unsupported-claim rates.
- Brain-inspired primitives — specialization as interface definition, scope inhibition, checkpoint synchronization, and convergence — address the coordination layer.
- MCP standardizes agent-to-tool communication while A2A targets agent-to-agent.

## Related

- [Coordination Overhead](/concepts/coordination-overhead.md) — the quadratic cost of connections
- [Single-Agent Ceiling](/concepts/single-agent-ceiling.md) — why one agent plateaus
- [state isolation](/concepts/state-isolation.md) — preventing shared-state corruption
- [orchestration layer](/concepts/orchestration-layer.md) — the reliability lever
- [Model Context Protocol](/entities/model-context-protocol.md) — the tool-communication standard
- [Your Multi-Agent System Has a Coordination Problem](/sources/your-multi-agent-system-has-a-coordination-problem.md) — primary source
