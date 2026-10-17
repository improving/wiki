---
title: "observability"
type: "Concept"
description: "Understanding system state from its outputs — metrics, logs, and traces — without shipping new code to ask a new question."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, platform, operations]
sources:
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-03-apm-boom-observability-tax.md"
  - "/sources/observability-arc-08-finops-agentic.md"
  - "/sources/observability-driven-development-designing-observable-applications.md"
  - "/sources/end-to-end-observability-with-prometheus-grafana-loki-opentelemetry-tempo.md"
  - "/sources/the-attribution-budget-why-telemetry-never-answers-why.md"
---

# observability

Observability is the property that lets a team understand a running system's internal state from its outputs, so a failure nobody anticipated can still be reconstructed after the fact. Monitoring instruments failures you expected; observability captures enough state to answer questions you did not know to ask. The distinction matters because tool availability has consistently run years ahead of adoption, leaving most organizations paying for telemetry without gaining the ability to diagnose novel failures.

## Key Claims

- [DORA](/entities/dora.md) found 57% of "elite performers" had integrated observability tooling, but elite was roughly the top 9% of respondents — the headline badly overstates industry adoption.
- Tool availability led actual adoption by three to five years: Jaeger reached [CNCF](/entities/cncf.md) incubation in 2017 yet stayed aspirational for most organizations through 2019.
- The canonical 2019 stack — [Prometheus](/entities/prometheus.md), [Grafana](/entities/grafana.md), Alertmanager, ELK, Nagios — was infrastructure- and cause-focused, producing [alert fatigue](/concepts/alert-fatigue.md) without improving user experience.
- 41% of leaders still learn about service interruptions through customer complaints, incident tickets, or manual checks; dashboards are green while users are already affected.
- Teams that design for observability cut MTTR by 40–50%, while about 70% of the observability data collected is unnecessary.
- Observability is now a FinOps problem: AI workloads generate 10–100× more telemetry, and enterprise observability spend grows 28% year-over-year with "no natural ceiling."
- Complete telemetry answers *what* happened, not *why*: on a ten-incident set with documented ground truth, attribution coverage from telemetry alone landed under 50%.

## Related

- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the metrics/logs/traces split and its storage tax
- [observability-driven development](/concepts/observability-driven-development.md) — designing for telemetry from day one
- [metrics logs traces](/concepts/metrics-logs-traces.md) — the three telemetry pillars
- [distributed tracing](/concepts/distributed-tracing.md) — following a request across services
- [OpenTelemetry](/entities/opentelemetry.md) — the vendor-neutral instrumentation standard
- [Datadog](/entities/datadog.md) — the commercial platform whose pricing drives the cost debate
