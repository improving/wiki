---
title: "service level objective"
type: "Concept"
description: "The target reliability a service commits to, defined before code and rigorous enough to catch capacity failure before users do."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, operations, reliability]
sources:
  - "/sources/observability-driven-development-designing-observable-applications.md"
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-08-finops-agentic.md"
  - "/sources/what-youre-actually-buying-when-you-choose-managed-inference.md"
---

# service level objective

A service level objective (SLO) is the reliability target a service commits to, expressed as a measurable indicator and a threshold the team agrees to hold. The SLI/SLO framing was well known by 2019, but teams kept cause-based threshold alerts instead, because defining meaningful SLOs requires cross-team agreement that is harder to schedule than adding another rule. SLOs are what turn reliability from an aspiration into a number a team can design against, budget for, and alert on.

## Key Claims

- In the 2019 baseline, teams knew the SLI/SLO framing but kept threshold alerts; meaningful SLOs need cross-team agreement that is harder to schedule than adding a rule.
- [observability-driven development](/concepts/observability-driven-development.md) defines SLOs before code, alongside telemetry requirements.
- SLOs on AI inference endpoints, run with the same rigor as core APIs, would catch capacity failures before users do — [Datadog](/entities/datadog.md)'s April 2026 trace data showed ~5% of AI requests failed, about 60% from capacity limits rather than model quality.
- Queue-aware routing holds 99.9% SLO compliance at high load, where load-blind baselines fall below 50%, with up to 7× lower latency.
- The gap an SLO leaves is the error budget a team spends deliberately: reliability work versus feature velocity, decided against a number rather than by argument.
- 41% of leaders still hear about interruptions from customers rather than their own telemetry — a sign the SLO is not wired to alerting.

## Related

- [observability](/concepts/observability.md) — the signals an SLO is measured from
- [observability-driven development](/concepts/observability-driven-development.md) — SLOs defined as a design concern
- [site reliability engineering](/concepts/site-reliability-engineering.md) — the discipline built on SLOs and error budgets
- [alert fatigue](/concepts/alert-fatigue.md) — what threshold alerting without SLOs produces
- [model routing](/concepts/model-routing.md) — routing that holds SLO compliance under load
