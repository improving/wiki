---
title: "The 2019 Baseline: What the Books Said vs. What Your Team Actually Ran"
type: "Source Summary"
description: "In 2019 elite observability practice and the median team diverged sharply, and the gap was cultural, not a matter of tooling access."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-01-the-2019-baseline/observability-arc-01-the-2019-baseline.md"
---

# The 2019 Baseline: What the Books Said vs. What Your Team Actually Ran — Summary

**Original source**: `references/devlinliles.com/observability-arc-01-the-2019-baseline/observability-arc-01-the-2019-baseline.md`

## Summary

The first post in an observability arc argues that 2019's best-practice literature — the Google SRE books, [DORA](/entities/dora.md), and [Honeycomb](/entities/honeycomb.md)'s writing — described elite practice, not the industry median. [DORA](/entities/dora.md) found 57% of "elite performers" had integrated observability tooling, but elite was roughly the top 9% of respondents, so the headline badly overstates adoption. The problem was not tooling, which was free and available; it was a philosophical gap between monitoring known-unknowns and observing unknown-unknowns.

## Key Claims

- Tool availability led actual adoption by three to five years: Jaeger reached [CNCF](/entities/cncf.md) incubation in 2017 yet stayed aspirational for most organizations through 2019.
- Monitoring instruments failures you anticipated; observability captures enough state to reconstruct failures you did not, which is why cause-based threshold alerts produce [alert fatigue](/concepts/alert-fatigue.md) without improving user experience.
- The canonical 2019 stack — Prometheus, Grafana, Alertmanager, ELK, some Nagios or Zabbix, maybe Datadog or New Relic — was overwhelmingly infrastructure- and cause-focused.
- Teams knew the SLI/SLO framing but kept threshold alerts, because defining meaningful SLOs needs cross-team agreement that is harder to schedule than adding a rule.
- The distribution was bimodal, and the gap was a practice gap with philosophical roots, not a budget or tool gap.

## Relevance

Sets the baseline for the observability arc, contrasting [alert fatigue](/concepts/alert-fatigue.md)-producing monitoring with true observability and benchmarking against median rather than elite practice.

## Quality

Practitioner blog post by Devlin Liles. Vivid and well-sourced; the post itself notes some percentages are illustrative and derived, not direct survey figures.

## Entities Mentioned

- [DORA](/entities/dora.md) — source of the elite-versus-median adoption figures
- [Honeycomb](/entities/honeycomb.md) — the team that popularized the unknown-unknowns argument
- [CNCF](/entities/cncf.md) — home of Prometheus, Jaeger, and the standards wave
- [Charity Majors](/entities/charity-majors.md) — leading voice for high-cardinality event data

## Concepts Covered

- [alert fatigue](/concepts/alert-fatigue.md) — the consequence of cause-based threshold alerting

## Related Sources

- [Golden Paths to Observability: What Platform Engineering Actually Delivers (and What It Doesn't)](/sources/observability-arc-05-platform-engineering-idp.md)
