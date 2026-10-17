---
title: "What This Senior Developer Learned From His First Big Rust Project"
type: "Source Summary"
description: "Lessons from a five-day Rust IoT MVP: tiny binaries, mDNS discovery, and error-handling debt from overusing .unwrap()."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, engineering, improving.com]
sources:
  - "references/improving.com/what-this-senior-developer-learned-from-his-first-big-rust-project/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
---

# What This Senior Developer Learned From His First Big Rust Project — Summary

**Original source**: `references/improving.com/what-this-senior-developer-learned-from-his-first-big-rust-project/what-this-senior-developer-learned-from-his-first-big-rust-project.md`

## Summary

Andrew Watson describes building a simulated IoT system in Rust — sensors, a controller, actuators, and an environment communicating via mDNS — as a five-day MVP that spilled into about four person-weeks. He reports binaries of 3.6–4.8MB and containers around 13.5MB, and catalogs lessons: over 100 `.unwrap()` calls, `String` error types, `Display` misuse for serialization, and remaining ergonomic gaps in Rust.

## Key Claims

- The MVP's goals: low-resource services, network service discovery without hard-coded IPs, inter-service messaging, and simulated visualizable data.
- The five-day plan spilled over into about four person-weeks total.
- A Cargo workspace with eight dependencies kept binaries to 3.6–4.8MB and containers to ~13.5–13.7MB, versus a JRE of 50–100MB.
- Services discovered each other via mDNS (`mdns-sd`) and communicated over HTTP/TCP; each service needs its own `ServiceDaemon`.
- In ~5,000 lines there were over 100 `.unwrap()` calls; `clippy`'s `unwrap_used` and `expect_used` lints can forbid them.
- Using `Display` for serialization and `String` for all `Err` variants are practices he would replace with `serde` and error enums.
- Explicit `clone` before `move` into threads is a known ergonomic pain (open RFC since 2018).
- Recommendations: implement `PartialEq` on public types and prefer `S: Into<String>` over `&str` for ergonomics.

## Relevance

Informs [software craftsmanship](/concepts/software-craftsmanship.md), [design patterns](/concepts/design-patterns.md), and [type safety](/concepts/type-safety.md) in systems programming.

## Quality

Honest, detailed retrospective by Andrew Watson; strong on specifics, but single-project and self-critical by design.

## Entities Mentioned

- [Rust](/entities/rust.md) — the language of the project
- [Scala](/entities/scala.md) — the author's prior primary language
- [Improving](/entities/improving.md) — the author's employer

## Concepts Covered

- [software craftsmanship](/concepts/software-craftsmanship.md) — error handling and code quality
- [design patterns](/concepts/design-patterns.md) — workspace, newtype, and trait patterns
- [type safety](/concepts/type-safety.md) — proper error types and traits
