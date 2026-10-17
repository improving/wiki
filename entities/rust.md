---
title: "Rust"
type: "Entity"
description: "Memory-safe systems language with compile-time guarantees, cited for security and for its learning-curve trade-offs."
created: '2026-10-17'
updated: '2026-10-17'
tags: [language, systems, security]
sources:
  - "/sources/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
  - "/sources/this-golang-behavior-is-unexpected-or-is-it.md"
  - "/sources/boosting-security-in-the-ai-era-how-improving-leads-the-charge.md"
---

# Rust

Rust is a memory-safe systems language that appears in this corpus both as a security recommendation and as a concrete learning experience. Its compile-time ownership and move semantics are held up as preventing classes of bugs that other languages leave to runtime.

## Characteristics

- Compile-time safety: `Vec::push` takes `&mut self` and move semantics reject the aliasing pattern that causes Go's surprising slice/append behavior, with the compiler suggesting a borrow instead.
- In a five-day IoT MVP that spilled to about four person-weeks, a Cargo workspace with eight dependencies produced binaries of 3.6–4.8MB and containers of ~13.5MB, versus a 50–100MB JRE.
- Real-world friction: over 100 `.unwrap()` calls in ~5,000 lines (clippy can forbid them), `String` error types, `Display` misuse for serialization, and explicit `clone` before `move` into threads.
- Recommended among memory-safe languages (Rust, C#, Go, Java, Ruby, Swift) that reduce memory leaks, buffer overflows, operational overhead, and maintenance burden when replacing vulnerable legacy code.

## Related

- [Go](/entities/go.md) — the comparison language with weaker compile-time checks
- [type safety](/concepts/type-safety.md) — compile-time prevention of whole bug classes
- [software craftsmanship](/concepts/software-craftsmanship.md) — error handling and code quality
- [application security](/concepts/application-security.md) — memory safety as a security foundation
