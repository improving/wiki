---
title: "How to Render Jenkins Build Parameters Dynamically?"
type: "Source Summary"
description: "Using the Jenkins Active Choices plugin to render build parameters and even HTML input controls dynamically from Groovy scripts."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, devops, platform, improving.com]
sources:
  - "references/improving.com/render-jenkins-build-parameters-dynamically/render-jenkins-build-parameters-dynamically.md"
---

# How to Render Jenkins Build Parameters Dynamically? — Summary

**Original source**: `references/improving.com/render-jenkins-build-parameters-dynamically/render-jenkins-build-parameters-dynamically.md`

## Summary

Nirav Katarmal explains how to work around the static nature of Jenkins declarative pipelines using the Active Choices parameter plugin. Because declarative jobs must declare all parameters upfront, he shows how Groovy scripts and HTML can generate parameter options — and entire form controls — at the moment the build is triggered, using three plugin parameter types.

## Key Claims

- The Active Choices plugin requires Jenkins 2.204.1 or later and offers three parameter types: Active Choices, Active Choices Reactive, and Active Choices Reactive Reference.
- Active Choices generates a value list from a Groovy script (or Scriptler catalog) and can render as lists, checkboxes, or radio buttons, with an optional filter box.
- Active Choices Reactive additionally updates its values based on the selection of another build parameter — e.g., cities for a chosen state.
- Active Choices Reactive Reference can render custom HTML (lists, images, text boxes) with JavaScript and CSS, letting you place a checkbox and a text box side by side.
- In the HTML controls, the `name` attribute must be `value`; checkboxes must use matching `alt` and `json` attributes to identify which was selected, and only selected checkboxes appear in the pipeline.
- Multi-select values arrive in the pipeline as comma-separated strings, in the order the controls were rendered.

## Relevance

A hands-on technique for [CI/CD](/concepts/ci-cd.md) pipelines on [Jenkins](/entities/jenkins.md), part of the broader [DevOps](/concepts/devops.md) toolchain.

## Quality

Practitioner how-to by Nirav Katarmal; detailed and code-complete, though tied to a single plugin and version.

## Entities Mentioned

- [Jenkins](/entities/jenkins.md) — the CI server hosting the Active Choices plugin

## Concepts Covered

- [CI/CD](/concepts/ci-cd.md) — parameterized build pipelines
- [DevOps](/concepts/devops.md) — automating delivery tooling
