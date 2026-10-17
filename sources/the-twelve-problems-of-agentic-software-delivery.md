---
title: "The Twelve Problems of Agentic Software Delivery"
type: "Source Summary"
description: "Agentic delivery is twelve compounding problems across four layers; reliability is a property of the whole architecture."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-twelve-problems-of-agentic-software-delivery/the-twelve-problems-of-agentic-software-delivery.md"
---

# The Twelve Problems of Agentic Software Delivery — Summary

**Original source**: `references/devlinliles.com/the-twelve-problems-of-agentic-software-delivery/the-twelve-problems-of-agentic-software-delivery.md`

## Summary

Argues agentic development is not one discipline but twelve problems across four layers — Foundation (Execution, Coordination), Operational (Memory, Context Management, Error Handling), Governance (Definition, Auditing, Intervention), and Intelligence (Planning, Evaluation, Improvement) — and that they compound. Reliability isn't a property of any single component but of the architecture connecting all twelve, and a gap in one layer surfaces as a symptom two or three layers downstream wearing different clothes.

## Key Claims

- Failures don't announce themselves at their source: skip Definition and Execution is confidently wrong; skip Auditing and Evaluation has no trace to score.
- A single agent completing a task at 95% reliability, chained across twenty steps, yields roughly a 36% chance the whole thing succeeds.
- MemoryAgentBench found no current system masters all four memory competencies, and selective forgetting is hardest — so memory systems stockpile outdated facts rather than losing them.
- Semantic drift is caught last and costs proportionally to the number of steps after it starts, which is why pre-execution gates matter more than runtime safeguards.
- The governance loop (Error Handling → Intervention → Auditing → Evaluation → Improvement) breaks at its weakest stage, and the closing arrow back to Error Handling is the one most teams never draw.

## Relevance

A full-lifecycle synthesis: it situates [plan-then-execute](/concepts/plan-then-execute.md), [context pollution](/concepts/context-pollution.md), [semantic drift](/concepts/semantic-drift.md), [state isolation](/concepts/state-isolation.md), and [evals-as-code](/concepts/evals-as-code.md) as parts of one architecture rather than separate tools.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a coherent four-layer map and honest about sequencing costs. Caveat: it synthesizes the author's own series, so it restates his positions rather than presenting new evidence.

## Entities Mentioned

- [LangGraph](/entities/langgraph.md) — the stateful graph execution model, and interrupt-and-resume
- [Model Context Protocol](/entities/model-context-protocol.md) — decoupling models from enterprise data and tools
- [OpenTelemetry](/entities/opentelemetry.md) — the tracing backend the audit story depends on
- [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md) — the four span operation types for agent actions
- [MemoryAgentBench](/entities/memoryagentbench.md) — benchmark showing no system masters all memory competencies
- [ReAct](/entities/react.md) — the default reason-act-observe loop and how it drifts on long tasks
- [DeepSeek R1](/entities/deepseek-r1.md) — demonstrated RL with verifiable rewards at scale

## Concepts Covered

- [plan-then-execute](/concepts/plan-then-execute.md) — separating planning from execution to create a decision point
- [context pollution](/concepts/context-pollution.md) — stale information misleads even when there's room
- [context management](/concepts/context-management.md) — treating the window as a whiteboard, not a filing cabinet
- [semantic drift](/concepts/semantic-drift.md) — divergence from the original ask, caught last
- [working memory](/concepts/working-memory.md) — one of four memory types most systems stop at
- [state isolation](/concepts/state-isolation.md) — isolating agents to prevent shared state corruption
- [checkpointing](/concepts/checkpointing.md) — typed state at every node enabling pause and resume
- [coordination overhead](/concepts/coordination-overhead.md) — the boundary failures that appear with more than one agent
- [compensating actions](/concepts/compensating-actions.md) — unwinding irreversible steps
- [saga pattern](/concepts/saga-pattern.md) — defining a compensating action for every step up front
- [evals-as-code](/concepts/evals-as-code.md) — version-controlled definitions, graders, and test cases
- [model-as-judge](/concepts/model-as-judge.md) — subjective grading with biases needing calibration
- [process reward models](/concepts/process-reward-models.md) — scoring intermediate reasoning steps

## Related Sources

- [Agentic Systems That Don't Improve Are Just Expensive Software](/sources/agentic-systems-that-dont-improve-are-just-expensive-software.md)
- [Escalation to a Human Is Not a Confidence Score](/sources/escalation-to-a-human-is-not-a-confidence-score.md)
