---
title: "LangSmith"
type: "Entity"
description: "LangChain's tracing and evaluation platform, positioned in this corpus as tooling for eval-driven, observable agent development."
created: '2026-10-17'
updated: '2026-10-17'
tags: [tooling, evaluation, observability, agents]
sources:
  - "/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md"
  - "/sources/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md"
  - "/sources/the-error-your-stack-trace-will-never-catch.md"
---

# LangSmith

LangSmith is LangChain's platform for tracing and evaluating LLM applications. This corpus treats it as part of the tooling layer that makes eval-driven, observable agent development practical.

## Overview

The posts argue teams should write evals before agents, running deterministic, model-graded, and human tiers in sequence — with 57% of organizations already running agents in production and quality the top barrier. Observability then requires reconstructing the full decision trace, not just API calls and database writes, which is where tracing platforms and emerging OpenTelemetry GenAI conventions fit. A distinct error taxonomy (REG, BUG, SEC, INF, DAT) covers the silent failures a stack trace will never catch.

## Key Claims

- 57% of organizations run agents in production, and quality is the top barrier
- An eval is an automated test suite that serves as the specification for AI behavior
- Three tiers run in sequence: deterministic, model-graded, then human review
- An agentic audit log must capture reasoning, not just API calls and database writes
- Agentic errors fall into five types, including semantic drift that raises no exception

## Related

- [evals-as-code](/concepts/evals-as-code.md) — the discipline LangSmith supports
- [Audit Trail](/concepts/audit-trail.md) — reconstructing the decision trace
- [semantic drift](/concepts/semantic-drift.md) — a silent failure mode with no exception
- [OpenTelemetry](/entities/opentelemetry.md) — the emerging trace standard
- [LangChain](/entities/langchain.md) — the parent project
- [Eval-Driven Development: The Discipline Agent Teams Are Missing](/sources/eval-driven-development-the-discipline-agent-teams-are-missing.md) — primary source
