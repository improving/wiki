---
title: "The Go Context"
type: "Source Summary"
description: "Go's context carries deadlines, cancellation, and request-scoped values across API boundaries — a shift for Java developers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, engineering, improving.com]
sources:
  - "references/improving.com/the-go-context/the-go-context.md"
---

# The Go Context — Summary

**Original source**: `references/improving.com/the-go-context/the-go-context.md`

## Summary

Paul Ferguson, a long-time Java developer learning Go, explains Go's context: an object that carries deadlines, cancellation signals, and request-scoped values across API boundaries and between processes. He shows how cancellation propagates through database and HTTP calls, when to use context.Background() instead, and how to pass a request ID for logging.

## Key Claims

- A Go context carries deadlines, cancellation signals, and request-scoped values across API boundaries.
- Requests can be cancelled by a closed browser, network failure, or client timeout; the context signals done so remaining work is skipped.
- Packages like pgx require a context and will stop processing and return an error once the context is done.
- context.Background() is never cancelled and should be limited to main functions, initialization, tests, and top-level incoming requests.
- Prefer context.WithCancel, WithTimeout, or WithDeadline; always call the cancel function to release resources.
- Request-scoped values (e.g. a request ID) can be threaded through the context for logging and tracing.
- If the context is not passed to an HTTP request, that request will not be cancelled and will waste resources.

## Relevance

Relevant to [distributed tracing](/concepts/distributed-tracing.md) and [observability](/concepts/observability.md) via propagated request IDs; a [Go](/entities/go.md) pattern contrasted with the author's [Java](/entities/java.md) background.

## Quality

Hands-on explainer by Paul Ferguson with a public example repo; concrete and clear, framed for developers new to Go.

## Entities Mentioned

- [Go](/entities/go.md) — the language whose context is explained
- [Java](/entities/java.md) — the author's prior language, used as contrast

## Concepts Covered

- [distributed tracing](/concepts/distributed-tracing.md) — request IDs threaded through context
- [observability](/concepts/observability.md) — correlating logs with request-scoped values
