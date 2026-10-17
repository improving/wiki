---
title: "DevBox"
type: "Entity"
description: "Agent development harness studied in the corpus for trainable skills, coordination overhead, and PR mergeability failure modes."
created: '2026-10-17'
updated: '2026-10-17'
tags: [tool, harness, multi-agent, evaluation]
sources:
  - "/sources/biological-coordination-patterns-applied-to-multi-agent-software-delivery.md"
  - "/sources/the-scaffolding-just-got-a-learning-rate.md"
  - "/sources/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation.md"
---

# DevBox

DevBox is an agent development harness that appears across this corpus as the experimental setting for harness research: trainable skill documents, multi-agent coordination, and a controlled 216-run evaluation of LLM-generated pull requests.

## Overview

- Coordination overhead grows faster than agent count, echoing Brooks's law; scope inhibition generalizes file locking to prevent conflicting parallel work.
- Skill documents can be optimized like weights behind a validation gate; producing harness updates is flat across model strength, and mid-tier models benefit most.
- Instructions decay over long trajectories, so governance must be runtime.
- In 216 runs, all 25 mergeability failures were test-additions that passed automated tests.
- The high tier merged constrained test-additions worse than mid (47% vs 53%); scope-discipline failures worsen with better models while capability-gap failures improve.

## Related

- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — specialization, inhibition, and convergence primitives
- [Coordination Overhead](/concepts/coordination-overhead.md) — why more agents cost more than they add
- [evaluation harness](/concepts/evaluation-harness.md) — the controlled runs behind the findings
- [runtime governance](/concepts/runtime-governance.md) — enforcement that survives instruction decay
- [The Scaffolding Just Got a Learning Rate](/sources/the-scaffolding-just-got-a-learning-rate.md) — primary source
