---
title: "Productivity Tips: Write It Once"
type: "Source Summary"
description: "Using code templates and snippets to express intent quickly cuts friction between intent and implementation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, legacy-dotnet, devlinliles.com]
sources:
  - "references/devlinliles.com/productivity-tips-write-it-once/productivity-tips-write-it-once.md"
---

# Productivity Tips: Write It Once — Summary

**Original source**: `references/devlinliles.com/productivity-tips-write-it-once/productivity-tips-write-it-once.md`

## Summary

A short productivity note arguing for targeted code generation via templates, snippets, and extensions. The author demonstrates building a simple `Person` class and an NUnit test through keystroke-driven templates (CodeRush templates, ReSharper mnemonics), generating the class in 19 seconds with no mouse. The point is not typing speed but reducing friction between intent and implementation, so producing lots of high-quality code becomes second nature.

## Key Claims

- Templates like `c<tab>`, `pi<tab>`, `ps<tab>`, `ms<tab>`, and `ts<tab>` scaffold classes, properties, methods, and tests by intent.
- The `Person` class was generated in 19 seconds using those keystrokes alone.
- The same template approach produced the TDD-style NUnit test (Arrange/Act/Assert) for `FullName`.
- Targeted use of code generation yields fewer typographical errors and faster expression of intended code.
- The goal is reducing friction between intent and implementation, not raw typing speed.

## Relevance

Informs [test-driven development](/concepts/test-driven-development.md) and [productivity amplification](/concepts/productivity-amplification.md) in .NET tooling.

## Quality

Practitioner blog post by Devlin Liles. A short, demonstration-style tip with a single worked example and a specific (but self-reported) 19-second figure.

## Entities Mentioned

- [CodeRush](/entities/coderush.md) — the template tooling used for the demonstration
- [ReSharper](/entities/resharper.md) — mnemonics cited as another template source
- [NUnit](/entities/nunit.md) — the test framework in the TDD example
- [C#](/entities/c-sharp.md) — the language of the generated code

## Concepts Covered

- [test-driven development](/concepts/test-driven-development.md) — the author writes the test with the same template system
- [Productivity amplification](/concepts/productivity-amplification.md) — tooling that multiplies how fast intent becomes code
