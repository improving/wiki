---
title: "Of Pagers and Exceptions"
type: "Source Summary"
description: "Traces how an HTTP 500 becomes a 3 a.m. page and lays out layered pre- and post-release mitigations for REST API reliability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, platform, improving.com]
sources:
  - "references/improving.com/of-pagers-and-exceptions/of-pagers-and-exceptions.md"
---

# Of Pagers and Exceptions — Summary

**Original source**: `references/improving.com/of-pagers-and-exceptions/of-pagers-and-exceptions.md`

## Summary

Using AWS as the example, the author traces how an unhandled exception in a REST API becomes an HTTP 500, trips a CloudWatch alarm, and pages a site reliability engineer at 3 a.m. He argues that keeping pagers quiet requires layers of defense: design, unit tests, and integration tests before release, and canary tests, runbooks, an operations API, and game days after. Feature flags and observability are the foundations the operational tools rely on.

## Key Claims

- Unhandled exceptions yield HTTP 500 responses; a crashed request processor yields 502 from API Gateway.
- Common causes include null reference exceptions, unvalidated API parameters, and unvalidated responses from other services such as S3.
- Pre-release mitigations: design for failure localization and security, high unit-test coverage, and integration tests wired into the build pipeline to reject failing changes.
- Post-release mitigations: canary tests run periodically against production, runbooks, a restricted operations API (with approvals where needed), and game days that induce failures deliberately.
- Feature flags enable outage simulation for game days and quick feature shutdowns.
- Observability requires sufficient metrics, logs, and traces; high coverage makes root cause easy and feeds better tests.

## Relevance

Informs [observability](/concepts/observability.md), [site reliability engineering](/concepts/site-reliability-engineering.md), and [alert fatigue](/concepts/alert-fatigue.md); also [quality gates](/concepts/quality-gates.md) and [three pillars of observability](/concepts/three-pillars-of-observability.md).

## Quality

Practitioner essay by Max Ksyunz; well-structured and specific, using AWS as a worked example of general principles.

## Entities Mentioned

- [AWS](/entities/aws.md) — the concrete platform used

## Concepts Covered

- [observability](/concepts/observability.md) — metrics, logs, and traces
- [site reliability engineering](/concepts/site-reliability-engineering.md) — on-call recovery tooling
- [alert fatigue](/concepts/alert-fatigue.md) — the cost of noisy pages
- [quality gates](/concepts/quality-gates.md) — tests gating the build pipeline
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — metrics, logs, traces
