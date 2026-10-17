---
title: "OpenTelemetry GenAI semantic conventions"
type: "Entity"
description: "Emerging telemetry standard defining span types for agent observability, so decision traces can be reconstructed."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, standards, agents]
sources:
  - "/sources/agentic-development-is-eleven-problems-not-one.md"
  - "/sources/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md"
---

# OpenTelemetry GenAI semantic conventions

The OpenTelemetry GenAI semantic conventions are the emerging standard this corpus points to for agentic observability. They define a shared vocabulary of span types so that an agent's decision trace can be reconstructed after the fact — the difference, one post argues, between having a system and merely having calls that happened to run.

## Overview

The observability post makes the core claim: an agentic audit log must capture reasoning, not just API calls and database writes. OpenTelemetry's GenAI semconv defines four span types for agent observability, and Datadog adopted these conventions natively from version 1.37 in December 2025. For regulated industries, append-only logs are the tamper-evidence requirement.

The eleven-problems post places this in a larger map: agentic development spans eleven competency areas across foundation, operational, governance, and intelligence layers, and most teams build foundation, add minimal governance, then stall. Coordination and context management matter most in production — exactly the areas that a common telemetry schema makes debuggable. Without reconstruction, governance has nothing to audit.

## Key Claims

- An agentic audit log must capture reasoning, not just API calls and database writes.
- OpenTelemetry GenAI semconv defines four span types for agent observability.
- Datadog adopted these conventions natively from version 1.37 in December 2025.
- Append-only logs are the tamper-evidence requirement for regulated industries.
- Most teams build Foundation, add minimal Governance, then stall.

## Related

- [Audit Trail](/concepts/audit-trail.md) — what the spans feed
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the wider discipline
- [Runtime Lineage](/concepts/runtime-lineage.md) — trace reconstruction in practice
- [OpenTelemetry](/entities/opentelemetry.md) — the parent standard
- [Datadog](/entities/datadog.md) — an early native adopter
- [If You Can't Reconstruct What the Agent Did](/sources/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md) — primary source
