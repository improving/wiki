---
title: "context drift"
type: "Concept"
description: "Production agents act on stale world state after multi-step actions, silently diverging from reality."
created: '2026-10-17'
updated: '2026-10-17'
tags: [agents, reliability, state]
sources:
  - "/sources/ai-agents-dont-know-what-changed-thats-a-1969-problem.md"
  - "/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md"
---

# context drift

Context drift is the silent divergence between what an agent believes about the world and what is actually true, accumulating as multi-step actions change state the agent never re-checks. It matters because it is a leading cause of production failure: one analysis traces 65% of enterprise AI failures to context drift or memory loss, and it is the modern face of the 1969 frame problem.

## Key Claims

- Roughly 65% of enterprise AI failures trace to context drift or memory loss.
- The frame problem explains it: agents cannot track what stays true after each action, so they operate on stale world state.
- Explicit state management is now a first-class architectural component, not an implementation detail.
- Verification steps act as frame resets before consequential actions.
- Prompts also degrade from model updates, context drift, and input distribution shift, which is why regression gates are needed.
- An evaluation harness with a golden dataset and regression gate converts measurement into enforcement against drift.

## Related

- [Context Management](/concepts/context-management.md) — the discipline that bounds drift
- [Working Memory](/concepts/working-memory.md) — the state agents most often lose
- [Model Drift Detection](/concepts/model-drift-detection.md) — detecting one source of drift
- [Evaluation Harness](/concepts/evaluation-harness.md) — regression gates against degradation
- [AI Agents Don't Know What Changed](/sources/ai-agents-dont-know-what-changed-thats-a-1969-problem.md) — primary source
- [Building an Evaluation Harness for Prompt Engineering](/sources/building-an-evaluation-harness-for-prompt-engineering-moving-beyond-intuition.md) — measurement response
