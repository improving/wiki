---
title: "A Person and a Pipeline Are Asking the Same Question"
type: "Source Summary"
description: "Human search and runtime resolution of AI assets are one capability-resolution problem, and splitting them into two systems guarantees drift."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, enterprise-ai-retrieval, devlinliles.com]
sources:
  - "references/devlinliles.com/a-person-and-a-pipeline-are-asking-the-same-question/a-person-and-a-pipeline-are-asking-the-same-question.md"
---

# A Person and a Pipeline Are Asking the Same Question — Summary

**Original source**: `references/devlinliles.com/a-person-and-a-pipeline-are-asking-the-same-question/a-person-and-a-pipeline-are-asking-the-same-question.md`

## Summary

Organizations past a single AI pilot accumulate prompts, agents, and model versions with no reliable way for a person or a system to find the right one. The post argues that a person asking which agent handles invoice reconciliation and a workflow engine asking for the current, healthy, authorized version of that skill are the same operation, differing only in clock speed and tolerance for being wrong. Because they get staffed as a search UX project and a systems project, the two descriptions drift, and drift is the default outcome rather than a failure mode.

## Key Claims

- Capability resolution on a human clock is seconds, exploratory, and forgiving; on a machine clock it is milliseconds, exact, with no one in the loop to catch a stale or unauthorized answer.
- Treating the two as separate systems produces two independently owned descriptions of the same fact, which diverge by the second release.
- The chat interface and the orchestrator should be two lenses over one object: an asset's identity, capability description, version, owner, health, and authorization status.
- Building a better UI and registry and wiring them together later only hides the problem for a while.
- Classic knowledge management and distributed systems each spent two decades on halves of this problem before AI assets existed.

## Relevance

Central to enterprise [service discovery](/concepts/service-discovery.md) for AI assets, and relevant to [data catalog](/concepts/data-catalog.md) and [shared vocabulary](/concepts/shared-vocabulary.md) concerns.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a clean reframing that turns two backlogs into one design object, with a concrete drift example. Caveats: an argument piece with no measurements; the drift claims are illustrative rather than evidenced.

## Entities Mentioned

- None.

## Concepts Covered

- [service-discovery](/concepts/service-discovery.md) — resolving the current, healthy, authorized asset at runtime
