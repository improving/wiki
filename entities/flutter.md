---
title: "Flutter"
type: "Entity"
description: "Google's Dart-based cross-platform UI toolkit for building native mobile, desktop, and web apps from one codebase."
created: '2026-10-17'
updated: '2026-10-17'
tags: [mobile, developer-tools, cross-platform]
sources:
  - "/sources/whats-the-flap-over-flutter.md"
---

# Flutter

Flutter is Google's Dart-based cross-platform framework, evaluated in this corpus through a hands-on IMDB-search app. The verdict was a strong choice for shipping one codebase across mobile, desktop, and web, with a widget-first programming model and solid built-in testing.

## Characteristics

- Launched at version 1.0 in 2018, building native apps for iOS, Android, Windows, macOS, Linux, and web from a single Dart codebase.
- Everything is a widget; widgets are stateless or stateful, and developers must explicitly notify Flutter when state changes.
- Dart is an object-oriented, garbage-collected, C-style language using async/await and Futures on a single-threaded event loop, with isolates for heavy work; the viral async/await style is a shift for Java developers.
- Supports unit (with Mockito), widget, and integration tests; the sample app took under a day to build plus a partial day to test, and hot reload made UI work fast.
- A poor fit when a feature depends on hardware APIs available on only one platform, though platform-specific APIs are supported.
- Main friction reported was choosing among layout widgets and platform-specific setup.

## Related

- [Google](/entities/google.md) — maker of Flutter and Dart
- [test automation](/concepts/test-automation.md) — unit, widget, and integration testing
- [developer-experience](/concepts/developer-experience.md) — hot reload and framework ergonomics
