---
title: "alert fatigue"
type: "Concept"
description: "The desensitization that follows noisy, low-signal alerting, undermining the observability and safety systems that depend on human response."
created: '2026-10-17'
updated: '2026-10-17'
tags: [observability, operations, safety]
sources:
  - "/sources/observability-arc-01-the-2019-baseline.md"
  - "/sources/safety-and-compliance-at-the-edge.md"
---

# alert fatigue

Alert fatigue is the erosion of human responsiveness that happens when a system emits more alerts than a team can meaningfully act on. It matters across this corpus because both observability platforms and edge safety systems ultimately depend on someone responding, and volume without signal destroys that response.

## Key Claims

- Monitoring solves known unknowns; observability solves unknown unknowns — a distinction that changes what deserves to page a human.
- The widely cited 57 percent observability figure described elite performers, not the industry median, so baselines built on it set unrealistic alerting expectations.
- Vendor-specific instrumentation was the structural friction holding teams back, fragmenting signal and compounding noise.
- Tool availability led actual adoption by three to five years, meaning teams often run noisier stacks than they assume.
- In edge safety, periodic checks and cloud round trips defeat the purpose of the system; continuous local inference catches the hardhat removed ten minutes after the gate scan.
- Detection value is lost without an escalation path built for immediacy, so alert design must match the response it expects.

## Related

- [anomaly detection](/concepts/anomaly-detection.md) — the signal layer that feeds or floods alerting
- [three pillars of observability](/concepts/three-pillars-of-observability.md) — the telemetry foundation behind alert quality
- [edge inference](/concepts/edge-inference.md) — continuous local detection that avoids periodic-check blind spots
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — response speed the escalation path must respect
- [The 2019 Baseline: What the Books Said vs. What Your Team Actually Ran](/sources/observability-arc-01-the-2019-baseline.md) — primary source
- [Safety and Compliance at the Edge](/sources/safety-and-compliance-at-the-edge.md) — primary source
