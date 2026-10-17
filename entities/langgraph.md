---
title: "LangGraph"
type: "Entity"
description: "An agent orchestration framework built on checkpointed DAGs, presented as the production-grade option for complex agent workflows."
created: '2026-10-17'
updated: '2026-10-17'
tags: [orchestration, agents, checkpointing]
sources:
  - "/sources/checkpointing-inside-the-node-resuming-instead-of-redoing.md"
  - "/sources/how-to-stop-an-agent-thats-gone-wrong.md"
  - "/sources/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md"
  - "/sources/the-plan-is-a-first-class-artifact.md"
  - "/sources/the-twelve-problems-of-agentic-software-delivery.md"
---

# LangGraph

LangGraph is an agent orchestration framework whose checkpointed DAG model makes it the production-grade option in this corpus for complex, stateful workflows. Because the [orchestration layer](/concepts/orchestration-layer.md) fixes error handling, state ownership, and debuggability, choosing it is treated as an architecture decision that is hard to reverse.

## Overview

Its checkpointing underpins two capabilities the corpus returns to repeatedly: fine-grained resume after a failure, and human intervention at a chosen point. Interrupt-and-resume is described as the most powerful production [human-in-the-loop](/concepts/human-in-the-loop.md) mechanism, while checkpoint durability depends on idempotency keys such as `{doc_id, substep}`.

## Key Claims

- Checkpointed DAGs are the production-grade choice for complex agent workflows.
- An atomic node treats every timeout as a full-cost do-over; splitting a node into checkpointed sub-steps lets a run resume instead of redoing completed work.
- The checkpointing pattern pays off only for long-running, expensive operations — fast nodes gain nothing.
- LangGraph interrupt-and-resume is the strongest production intervention mechanism.
- Chained 95%-reliable steps yield only 36% end-to-end success across twenty steps, which is why checkpointed recovery matters.

## Related

- [Checkpointing](/concepts/checkpointing.md) — the mechanism LangGraph is known for
- [Human-in-the-loop](/concepts/human-in-the-loop.md) — enabled by interrupt-and-resume
- [Approval gate](/concepts/human-approval-points.md) — where oversight is placed
- [Orchestration layer](/concepts/orchestration-layer.md) — the decision LangGraph settles
- [The Orchestration Model You Pick Is the Architecture Decision You Can't Undo](/sources/the-orchestration-model-you-pick-is-the-architecture-decision-you-cant-undo.md) — primary source
