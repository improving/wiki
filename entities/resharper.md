---
title: "ReSharper"
type: "Entity"
description: "JetBrains .NET productivity extension for Visual Studio, favoured for refactoring navigation and solution-wide code generation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [tooling, dotnet, productivity]
sources:
  - "/sources/coderush-vs-resharper-six-months-later.md"
  - "/sources/productivity-tips-write-it-once.md"
---

# ReSharper

ReSharper is a JetBrains productivity extension for Visual Studio that adds refactoring, navigation, analysis, and code-generation features to .NET development. It is the recommended tool in one six-month comparison against CodeRush.

## Overview

The comparison concludes that CodeRush wins on context-aware mnemonic templates and unified account-based licensing, while ReSharper wins on refactoring navigation and generating files from the solution explorer. Despite overriding Visual Studio shortcuts, ReSharper's single consistent key-binding set fit the author better, and the recommendation is simply to adopt one of the two. A companion post shows the payoff of template-driven generation: a `Person` class produced in 19 seconds, with TDD tests scaffolded and assertions pre-filled.

## Key Claims

- ReSharper wins on refactoring navigation and file generation from the solution explorer
- CodeRush wins on context-aware mnemonic templates and unified account-based licensing
- ReSharper's single key-binding set fit the author better despite overriding Visual Studio shortcuts
- Templates and snippets scaffold tests with assertions pre-filled, cutting typographical errors
- The goal is reducing friction between intent and implementation, not raw typing speed

## Related

- [CodeRush](/entities/coderush.md) — the compared alternative
- [Visual Studio](/entities/visual-studio.md) — the host IDE both extend
- [Code Readability](/concepts/code-readability.md) — refactoring navigation serves this goal
- [Test-Driven Development](/concepts/test-driven-development.md) — templates scaffold tests directly
- [CodeRush vs. ReSharper: Six Months Later](/sources/coderush-vs-resharper-six-months-later.md) — primary source
