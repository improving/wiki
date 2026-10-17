---
title: "Go"
type: "Entity"
description: "Google's compiled, concurrent-friendly language, used here for services and contrasted with Rust on type safety."
created: '2026-10-17'
updated: '2026-10-17'
tags: [language, backend, cloud-native]
sources:
  - "/sources/this-golang-behavior-is-unexpected-or-is-it.md"
  - "/sources/the-go-context.md"
  - "/sources/boosting-security-in-the-ai-era-how-improving-leads-the-charge.md"
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/showcasing-women-in-tech-yang-xia-and-apache-tinkerpop.md"
---

# Go

Go is Google's compiled language for concurrent services, appearing in this corpus through a language-semantics deep dive, a context-pattern explainer, and several real systems. It is also named among the memory-safe languages recommended for replacing vulnerable legacy code.

## Language and Patterns

- Go slices carry both a length and a capacity: `append` reuses the backing array when spare capacity exists and allocates a new one when it does not, so whether a mutation leaks back to the caller depends on capacity — a bug Rust's move semantics catch at compile time.
- A Go context carries deadlines, cancellation signals, and request-scoped values across API boundaries; packages like pgx stop processing once the context is done, and `context.Background()` should be limited to main functions, initialization, tests, and top-level requests.
- Request IDs threaded through the context support logging and tracing, tying the pattern to distributed tracing.
- Real systems built in Go include LiveKit, the Go-based Apache 2.0 SFU, and Yang Xia's Go implementation of the Gremlin query language for Apache TinkerPop.

## Related

- [Rust](/entities/rust.md) — the comparison language with stronger compile checks
- [Java](/entities/java.md) — the author's prior language, used as contrast
- [LiveKit](/entities/livekit.md) — a Go-based real-time media server
- [distributed tracing](/concepts/distributed-tracing.md) — request IDs carried through context
- [application security](/concepts/application-security.md) — memory safety as a security foundation
