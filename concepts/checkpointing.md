---
title: "checkpointing"
type: "Concept"
description: "Splitting long or expensive work into durable sub-steps so a failure resumes instead of redoing completed work."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, pipelines, agents]
sources:
  - "/sources/checkpointing-inside-the-node-resuming-instead-of-redoing.md"
  - "/sources/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift.md"
---

# checkpointing

Checkpointing splits long or expensive work into durable sub-steps so that a failure resumes from where it stopped rather than redoing everything. It appears at two scales in this corpus: inside a single pipeline node, and as explicit stage boundaries across a long agent run.

## Key Claims

- An atomic node treats every timeout as a full-cost do-over, discarding finished work.
- Decomposing enrich into fetch-record, transform, and attach enables fine-grained resume.
- Idempotency keys of {doc_id, substep} make checkpoint durability trustworthy.
- The pattern targets long-running, expensive operations; fast nodes gain nothing.
- Long uninterrupted agent chains compound early errors into late, expensive failures.
- Draw stage boundaries where unwinding a downstream decision becomes expensive.
- Reliability degrades with run length regardless of per-step accuracy.

## Related

- [Task Decomposition](/concepts/task-decomposition.md) — the decomposition that enables fine-grained resume
- [Compensating actions](/concepts/compensating-actions.md) — what to unwind when a step cannot simply resume
- [cascading hallucination](/concepts/cascading-hallucination.md) — what short bounded stages limit
- [state isolation](/concepts/state-isolation.md) — keeping checkpointed stage state clean
- [Checkpointing Inside the Node - Resuming Instead of Redoing](/sources/checkpointing-inside-the-node-resuming-instead-of-redoing.md) — primary source
- [Short, Bounded Pipelines - Trading a Seamless Run for a Shorter Leash on Drift](/sources/short-bounded-pipelines-trading-a-seamless-run-for-a-shorter-leash-on-drift.md) — primary source
