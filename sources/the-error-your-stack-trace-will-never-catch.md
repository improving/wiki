---
title: "The Error Your Stack Trace Will Never Catch"
type: "Source Summary"
description: "Argues the fatal agentic errors are silent successes toward the wrong goal, and prescribes an error taxonomy, pre-execution gates, and runtime safeguards."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/the-error-your-stack-trace-will-never-catch/the-error-your-stack-trace-will-never-catch.md"
---

# The Error Your Stack Trace Will Never Catch — Summary

**Original source**: `references/devlinliles.com/the-error-your-stack-trace-will-never-catch/the-error-your-stack-trace-will-never-catch.md`

## Summary

The post argues the errors that kill agentic systems in production are not exceptions but technically successful executions toward the wrong goal—clean logs, 200 responses, wrong output. It presents a five-type error taxonomy (REG, BUG, SEC, INF, DAT) and identifies semantic drift as the failure with no exception, detectable only by comparing output to the original goal. It then prescribes pre-execution gates and runtime safeguards.

## Key Claims

- Five error types: REG (regression), BUG (new defect), SEC (security, always P1), INF (infrastructure), and DAT (data)—the most insidious because it is a bias discovered in outcomes, not a crash in logs.
- Semantic drift is the divergence between what an agent is doing and what it was asked to do; similarity scoring against the goal spec is the state of the art and is imperfect.
- Three pre-execution gates belong in every system: test sufficiency analysis, scope validation, and pre-flight environment checks.
- Runtime safeguards are circuit breakers (sliding error-rate window), timeout enforcement on every tool call and step, and per-session/per-task token budgets.
- In multi-agent systems a failure in a shared tool, memory, or infrastructure layer can cascade silently across many concurrent sessions; blast-radius mapping makes triage tractable.

## Relevance

Core to [semantic drift](/concepts/semantic-drift.md) and [circuit breakers](/concepts/circuit-breakers.md); also touches [prompt injection](/concepts/prompt-injection.md) and [token cost](/concepts/token-cost.md).

## Quality

Practitioner blog post by Devlin Liles. The taxonomy is borrowed from the Augment Code catalog and figures such as "50K tokens on a 5K task" are illustrative examples rather than measured results.

## Entities Mentioned

- [Augment Code](/entities/augment-code.md) — source of the error taxonomy and blast-radius framing
- [LangSmith](/entities/langsmith.md) — cited for tracing and error detection

## Concepts Covered

- [semantic drift](/concepts/semantic-drift.md) — the error with no exception
- [circuit breakers](/concepts/circuit-breakers.md) — halting bad runs via a sliding error-rate window
- [prompt injection](/concepts/prompt-injection.md) — a SEC-class agentic error
- [token cost](/concepts/token-cost.md) — per-session budgets that halt runaway agents
