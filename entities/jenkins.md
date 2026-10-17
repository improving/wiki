---
title: "Jenkins"
type: "Entity"
description: "Long-standing CI automation server, cited here for dynamic build parameters and as a lesson in trust and secret handling."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ci-cd, devops, automation]
sources:
  - "/sources/render-jenkins-build-parameters-dynamically.md"
  - "/sources/how-to-keep-a-secret.md"
  - "/sources/trust-was-always-the-problem-from-devops-to-agentic-ai.md"
---

# Jenkins

The long-standing CI automation server, used in this corpus as both a practical tool and a historical lesson. It anchors [ci-cd](/concepts/ci-cd.md) how-to writing on dynamic build parameters, and appears in the DevOps-trust argument as tooling that "worked" but was never the real constraint on adoption.

## Build Pipelines

- Jenkins declarative pipelines must declare all parameters upfront, which is why dynamic options need the Active Choices parameter plugin (Jenkins 2.204.1 or later).
- The plugin offers three parameter types: Active Choices, Active Choices Reactive, and Active Choices Reactive Reference.
- Active Choices generates a value list from a Groovy script and can render as lists, checkboxes, or radio buttons; the Reactive variant updates based on another parameter's selection.
- Active Choices Reactive Reference can render custom HTML with JavaScript and CSS; the `name` attribute must be `value`, and checkboxes need matching `alt` and `json` attributes.
- Multi-select values arrive in the pipeline as comma-separated strings, in the order the controls were rendered.

## Trust and Secrets

- The DevOps trust argument notes that Jenkins, Git, and Docker all worked, proving tooling was not what stalled automated delivery — trust and governance were.
- Jenkins is described as a build server with a checkered security record; the secret-management advice is to eliminate credentials where possible, use identity-based access, and prefer vault API access over environment variables.

## Related

- [ci-cd](/concepts/ci-cd.md) — automated integration and delivery pipelines
- [devops](/concepts/devops.md) — the culture and practice Jenkins serves
- [secrets-management](/concepts/secrets-management.md) — controlling credentials in build systems
- [trust-infrastructure](/concepts/trust-infrastructure.md) — the audit and approval layers that make automation safe
