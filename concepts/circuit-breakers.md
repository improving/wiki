---
title: "circuit breakers"
type: "Concept"
description: "Stopping calls to a failing dependency once errors trip a threshold, bounding the blast radius of failure."
created: '2026-10-17'
updated: '2026-10-17'
tags: [reliability, safety, runtime]
sources:
  - "/sources/execution-safety-architecture-for-ai-generated-outputs-a-layered-approach.md"
  - "/sources/the-error-your-stack-trace-will-never-catch.md"
---

# circuit breakers

A circuit breaker stops calls to a failing dependency once errors cross a threshold, bounding the blast radius instead of letting failures cascade. In agent and code-execution systems it sits among the runtime safeguards — timeouts, memory limits, rate limits, and token budgets — that catch problems which cannot be detected before execution.

## Key Claims

- Execution risks like non-termination are not detectable before running the output.
- Timeouts, memory limits, circuit breakers, and rate limits bound failure blast radius.
- The layers are independent; their value comes from defense in depth.
- Agentic errors fall into five types: REG, BUG, SEC, INF, and DAT.
- Semantic drift is a gradual off-target accumulation with no exception thrown.
- Pre-execution gates include test sufficiency, scope validation, and pre-flight checks.
- Runtime safeguards include circuit breakers, timeouts, and token budgets.

## Related

- [semantic drift](/concepts/semantic-drift.md) — a silent failure that runtime safeguards must catch
- [protection harness](/concepts/protection-harness.md) — the surrounding containment structure
- [Compensating actions](/concepts/compensating-actions.md) — the recovery counterpart to bounding failure
- [Michael Nygard](/entities/michael-nygard.md) — popularized the pattern
- [Execution Safety Architecture for AI-Generated Outputs: A Layered Approach](/sources/execution-safety-architecture-for-ai-generated-outputs-a-layered-approach.md) — primary source
- [The Error Your Stack Trace Will Never Catch](/sources/the-error-your-stack-trace-will-never-catch.md) — primary source
