---
title: "HumanLayer"
type: "Entity"
description: "Human-in-the-loop tooling for agents, used in this corpus to argue for intervention and approval design."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, human-in-the-loop, tooling, orchestration]
sources:
  - "/sources/how-to-stop-an-agent-thats-gone-wrong.md"
  - "/sources/the-plan-is-a-first-class-artifact.md"
---

# HumanLayer

HumanLayer is tooling for putting humans into agent workflows — approvals, interventions, and review gates. In this corpus it is the reference point for the argument that oversight mechanisms must be designed before incidents and chosen by how reversible each agent action is.

## Overview

- Reversibility determines where oversight gates belong in a workflow.
- Approving before irreversible actions is the right default for production systems.
- LangGraph interrupt-and-resume is described as the most powerful production intervention mechanism.
- The saga pattern manages actions that cannot be rolled back via compensating actions.
- Planning patterns differ: ReAct reasons step by step and drifts on long tasks, while Plan-then-Execute inserts an approval gate between intent and consequence.
- Tree of Thought and LATS explore candidate plans when errors are costly.

## Related

- [human-in-the-loop](/concepts/human-in-the-loop.md) — the pattern HumanLayer operationalizes
- [human approval points](/concepts/human-approval-points.md) — where intervention is placed
- [Plan-then-Execute](/concepts/plan-then-execute.md) — the pattern that creates a reviewable gate
- [LangGraph](/entities/langgraph.md) — the runtime offering interrupt-and-resume
- [How to Stop an Agent That's Gone Wrong](/sources/how-to-stop-an-agent-thats-gone-wrong.md) — primary source
