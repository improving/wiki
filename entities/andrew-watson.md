---
title: "Andrew Watson"
type: "Entity"
description: "Improving writer on types, Rust, and code review."
created: '2026-10-17'
updated: '2026-10-17'
tags: [author, engineering, types, code-review]
sources:
  - "/sources/what-this-senior-developer-learned-from-his-first-big-rust-project.md"
  - "/sources/make-invalid-states-unrepresentable.md"
  - "/sources/drop-everything-and-review.md"
---

# Andrew Watson

An Improving senior developer and writer on type systems, systems programming, and code review. His posts favor precise, example-driven arguments — Scala refined types, a Rust IoT retrospective — and a craftsman's focus on error handling and review flow.

## Topics and Work

- Walks a Scala `age` field from `String` to `Int` to runtime assertions to refined and tagged types, arguing that modeling data with precise types lets the compiler do the validation and makes invalid states unrepresentable.
- Recounts building a simulated Rust IoT system as a five-day MVP that spilled into ~four person-weeks, reporting 3.6–4.8MB binaries versus a 50–100MB JRE, mDNS service discovery, and lessons from 100+ `.unwrap()` calls.
- Proposes a "middle loop" of software development — the code review loop between the fast inner loop and the slow outer loop — and argues async review inflates it.
- Offers the DEAR norm (Drop Everything and Review): after production incidents, reviewing code should be the first task on a developer's list, with synchronous review or pairing shrinking the middle loop.

## Related

- [type safety](/concepts/type-safety.md) — using the type system to catch errors at compile time
- [make invalid states unrepresentable](/concepts/make-invalid-states-unrepresentable.md) — the technique he demonstrates
- [code review](/concepts/code-review.md) — the middle loop he names
- [software craftsmanship](/concepts/software-craftsmanship.md) — standards held under pressure
