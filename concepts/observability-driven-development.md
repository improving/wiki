---
title: "observability-driven development"
type: "Concept"
description: "Designing for telemetry and SLOs from day one rather than instrumenting after incidents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, platform, developer-experience]
sources:
  - "/sources/observability-driven-development-designing-observable-applications.md"
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-06-aiops-rca.md"
  - "/sources/of-pagers-and-exceptions.md"
  - "/sources/observability-arc-08-finops-agentic.md"
---

# observability-driven development

Observability-driven development (ODD) moves observability left, treating telemetry, tracing, and SLOs as design concerns defined before code rather than something wired up after the application is built. The argument is that teams keep buying more tooling while mean time to resolution gets worse, because the deeper problem is that observability is a post-build task rather than a design decision. Once AI systems — which fail silently and subtly — enter the stack, designing for observability from day one stops being optional.

## Key Claims

- 70% of engineers said observability budgets increased in the past year ([Dynatrace](/entities/dynatrace.md), 2025), yet MTTR trended wrong for four straight years: 47% of teams reported over an hour in 2021, rising to 82% by 2024.
- Hourly downtime exceeds $300,000 for 90% of firms, and the median cost of a high-impact outage is $2 million per hour.
- Tracing is the neglected third pillar — teams have metrics and logs but pause when tracing comes up.
- ODD defines observability requirements like functional requirements: what a healthy end-to-end request flow looks like, which integration points carry the most risk, and what degraded versus hard failure looks like.
- Key aspects: telemetry as a design requirement, SLOs before code, [OpenTelemetry](/entities/opentelemetry.md) as the instrumentation standard, and observability gaps treated as bugs.
- Benefits: teams that design for observability cut MTTR by 40–50%, and roughly 70% of the observability data collected is unnecessary.
- AI systems fail differently — confident but wrong answers, inconsistent prompts, latency hard to attribute — so prompt and response logging, model latency, token usage, and output-quality signals must be defined upfront.

## Related

- [observability](/concepts/observability.md) — the property ODD designs for
- [service level objective](/concepts/service-level-objective.md) — the reliability target set before code
- [distributed tracing](/concepts/distributed-tracing.md) — the pillar teams neglect
- [alert fatigue](/concepts/alert-fatigue.md) — the noise intentional instrumentation reduces
- [Atulpriya Sharma](/entities/atulpriya-sharma.md) — author of the central essay
