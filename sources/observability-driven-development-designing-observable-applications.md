---
title: "Observability-Driven Development"
type: "Source Summary"
description: "Treating observability as a post-deployment task yields more tooling and slower recovery; ODD makes it a day-one design concern."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, platform, improving.com]
sources:
  - "references/improving.com/observability-driven-development-designing-observable-applications/observability-driven-development-designing-observable-applications.md"
---

# Observability-Driven Development — Summary

**Original source**: `references/improving.com/observability-driven-development-designing-observable-applications/observability-driven-development-designing-observable-applications.md`

## Summary

Teams keep buying more observability tooling while mean time to resolution gets worse, because observability is still treated as something wired up after the application is built. Observability-driven development (ODD) moves observability left, defining telemetry, tracing, and SLOs as design concerns from day one — which the post argues is not optional once AI systems, with their silent and subtle failures, enter the stack.

## Key Claims

- Hourly downtime exceeds $300,000 for 90% of firms, and 41% of enterprises put hourly downtime at $1 million to over $5 million; the median cost of a high-impact outage is $2 million per hour.
- 70% of engineers said observability budgets increased in the past year (Dynatrace 2025), yet MTTR trended wrong for four straight years: 47% of teams reported over an hour in 2021, rising to 82% by 2024.
- 41% of leaders still learn about service interruptions through customer complaints, incident tickets, or manual checks — dashboards are green while users are already affected.
- Tracing is the neglected third pillar; teams have metrics and logs but pause when tracing comes up, and the deeper issue is that observability is a post-build task rather than a design decision.
- ODD defines observability requirements like functional requirements: what a healthy end-to-end request flow looks like, which integration points carry the most risk, what failure modes exist, and what degraded versus hard failure looks like.
- Key aspects: telemetry as a design requirement, SLOs before code, OpenTelemetry as the instrumentation standard (now the second largest CNCF project after Kubernetes), and observability gaps treated as bugs.
- Implement ODD by identifying what must be observable in design, instrumenting during development, and validating telemetry before launch.
- Benefits: teams that design for observability cut MTTR by 40 to 50%, developers spend over 57% of their time firefighting (Cisco research), full-stack observability halves outage cost, and about 70% of observability data collected is unnecessary.
- AI systems fail differently — confident but wrong answers, inconsistent prompts, latency hard to attribute — so designing for observability from day one means defining prompt and response logging, model latency, token usage, and output quality signals upfront.

## Relevance

Informs [observability-driven development](/concepts/observability-driven-development.md), [observability](/concepts/observability.md), [distributed tracing](/concepts/distributed-tracing.md), and [service level objective](/concepts/service-level-objective.md).

## Quality

Practitioner essay by Atulpriya Sharma; data-rich with cited sources, mildly promotional at the close.

## Entities Mentioned

- [Atulpriya Sharma](/entities/atulpriya-sharma.md) — author
- [Improving](/entities/improving.md) — the observability and support team behind the post
- [OpenTelemetry](/entities/opentelemetry.md) — the instrumentation standard
- [CNCF](/entities/cncf.md) — home of OpenTelemetry and Kubernetes
- [Dynatrace](/entities/dynatrace.md) — source of the 2025 observability budget research

## Concepts Covered

- [observability-driven development](/concepts/observability-driven-development.md) — the main topic
- [observability](/concepts/observability.md) — understanding state from system outputs
- [distributed tracing](/concepts/distributed-tracing.md) — the neglected third pillar
- [service level objective](/concepts/service-level-objective.md) — defined before code
- [alert fatigue](/concepts/alert-fatigue.md) — reduced by intentional instrumentation
