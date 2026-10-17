---
title: "Closing the Loop: The Graduated Case for Self-Healing Systems"
type: "Source Summary"
description: "Self-healing without a Learn step merely defers root causes; teams should climb a trust ladder measured by recurring failure rate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-07-self-healing-remediation/observability-arc-07-self-healing-remediation.md"
---

# Closing the Loop: The Graduated Case for Self-Healing Systems — Summary

**Original source**: `references/devlinliles.com/observability-arc-07-self-healing-remediation/observability-arc-07-self-healing-remediation.md`

## Summary

[Kubernetes](/entities/kubernetes.md) self-healing — liveness probes, ReplicaSets, node replacement — is table stakes, and runbook automation via [Datadog](/entities/datadog.md) Workflow Automation, PagerDuty, and Ansible is the mature middle layer. But restarting a pod around a six-month memory leak automates the symptom and defers the cause; self-healing without learning is deferral with better optics. The author prescribes a trust ladder climbed through measurement, and a six-step loop — Detect, Diagnose, Decide, Act, Verify, Learn — where Learn is the step teams skip and the one that actually closes the loop.

## Key Claims

- The closed-loop pattern requires all six steps; remediation telemetry must change something (a backlog item, runbook version, or SLO trend) or the loop is open.
- Trust is earned by running the semi-automated version long enough to prove the automation matches a senior SRE's decisions across a meaningful sample.
- Start with low-risk, reversible actions — restart a pod, scale a deployment, roll back a flag, disable a [circuit breaker](/concepts/circuit-breakers.md) — and require human approval above that.
- A proposed decision rule: auto-execute when an action is reversible, idempotent, and bounded, and the automation's historical accuracy exceeds 95%.
- Track recurring failure rate by root cause; if MTTR improves while it stays flat or rises, automation is masking [technical debt](/concepts/technical-debt.md).

## Relevance

Informs [circuit breakers](/concepts/circuit-breakers.md) and [technical debt](/concepts/technical-debt.md), and follows the arc's AIOps piece toward graduated autonomy.

## Quality

Practitioner blog post by Devlin Liles. Strong on the operational trust argument and a concrete metric; the 95% threshold is explicitly a derived heuristic, not a universal benchmark.

## Entities Mentioned

- [Kubernetes](/entities/kubernetes.md) — native self-healing baseline
- [Datadog](/entities/datadog.md) — Workflow Automation at the runbook layer

## Concepts Covered

- [circuit breakers](/concepts/circuit-breakers.md) — cited as a bounded, reversible auto-remediation action
- [technical debt](/concepts/technical-debt.md) — what symptom-only automation masks

## Related Sources

- [If You Can't Reconstruct What the Agent Did, You Don't Have a System](/sources/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md)
- [Datadog, Dynatrace, and the Bill That Ate Your Engineering Budget](/sources/observability-arc-03-apm-boom-observability-tax.md)
