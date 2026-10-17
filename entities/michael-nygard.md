---
title: "Michael Nygard"
type: "Entity"
description: "Author of Release It! whose stability patterns inform this corpus's layered defense and execution-safety architecture for AI agents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [author, reliability, architecture]
sources:
  - "/sources/engineering-reliability-into-autonomous-ai-agents.md"
  - "/sources/execution-safety-architecture-for-ai-generated-outputs-a-layered-approach.md"
---

# Michael Nygard

Michael Nygard is the author of Release It!, the catalog of stability patterns — circuit breakers, timeouts, bulkheads, and graceful degradation — that shaped how production systems absorb failure. This corpus applies his defense-in-depth reasoning to autonomous AI agents.

## Key Claims

- Execution risks like non-termination are not detectable before running the output.
- Architectural chain analysis flags out-of-scope data and service access before execution.
- Timeouts, memory limits, circuit breakers, and rate limits bound failure blast radius.
- The layers are independent; their value comes from defense in depth.
- Ten steps at 95 percent accuracy yield only about 60 percent end-to-end pipeline reliability.

## Work

Nygard's patterns become the execution-safety layers that limit the blast radius of AI-generated code, and the six defense layers between a model call and a trusted output. The corpus's emphasis on independent, redundant layers — and on prevention over retry — is a direct extension of his stability catalog.

## Related

- [Jim Gray](/entities/jim-gray.md) — the fault-tolerance tradition Nygard's patterns operationalize
- [Kubernetes](/entities/kubernetes.md) — a platform where his patterns are routinely applied
- [circuit breakers](/concepts/circuit-breakers.md) — his best-known stability pattern
- [Compensating actions](/concepts/compensating-actions.md) — a recovery pattern for irreversible actions
- [Execution Safety Architecture for AI-Generated Outputs](/sources/execution-safety-architecture-for-ai-generated-outputs-a-layered-approach.md) — primary source
