---
title: "site reliability engineering"
type: "Concept"
description: "Applying software engineering to operations, with SLOs, error budgets, and layered defenses that keep pagers quiet."
created: '2026-10-17'
updated: '2026-10-17'
tags: [operations, reliability, devops]
sources:
  - "/sources/of-pagers-and-exceptions.md"
  - "/sources/maximizing-developer-productivity-security-and-operational-efficiency.md"
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/observability-arc-07-self-healing-remediation.md"
---

# site reliability engineering

Site reliability engineering (SRE) applies software engineering to operations, treating reliability as an engineering problem with measurable targets rather than a matter of heroics. Its literature — the Google SRE books, [DORA](/entities/dora.md) research, and practitioner writing — describes an elite practice that most organizations have not reached, and the gap is cultural rather than a matter of tooling access. Platform engineering is now positioned as the next evolution beyond [DevOps](/concepts/devops.md) and SRE, wrapping reliability practices into self-service platforms.

## Key Claims

- Keeping pagers quiet takes layers of defense: pre-release design, high unit-test coverage, and integration tests wired into the build pipeline to reject failing changes.
- Post-release mitigations: canary tests run periodically against production, runbooks, a restricted operations API with approvals, and game days that induce failures deliberately.
- The concrete path SRE shortens: an unhandled exception becomes an HTTP 500, trips a CloudWatch alarm, and pages an engineer at 3 a.m. — common causes are null references, unvalidated parameters, and unvalidated responses from other services.
- Feature flags and observability are the foundations the operational tools rely on; feature flags also enable outage simulation for game days and quick shutdowns.
- The 2019 baseline: SRE literature described elite practice while the industry median ran infrastructure- and cause-focused threshold alerts.
- Self-healing should climb a trust ladder — start with reversible actions (restart a pod, scale a deployment, roll back a flag), require human approval above that, and auto-execute only when an action is reversible, idempotent, bounded, and historically >95% accurate.

## Related

- [observability](/concepts/observability.md) — the signals SRE depends on
- [service level objective](/concepts/service-level-objective.md) — the target reliability SRE commits to
- [alert fatigue](/concepts/alert-fatigue.md) — the cost of noisy pages
- [DevOps](/concepts/devops.md) — the discipline SRE extends
- [DORA](/entities/dora.md) — the research behind the elite-versus-median gap
