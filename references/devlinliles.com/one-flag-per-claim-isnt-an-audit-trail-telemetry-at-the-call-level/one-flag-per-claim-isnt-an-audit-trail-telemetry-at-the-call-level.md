---
type: Reference
title: "One Flag Per Claim Isn&#x27;t an Audit Trail - Telemetry at the Call Level"
resource: "https://www.devlinliles.com/one-flag-per-claim-isnt-an-audit-trail-telemetry-at-the-call-level/"
author: "Devlin Liles"
published: '2026-10-09'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# One Flag Per Claim Isn't an Audit Trail - Telemetry at the Call Level

## The problem

I built a research assistant for adjusters at a fictional insurance carrier, one I called ClaimAssist, and ran it through a short multi-step session per claim: a policy lookup, a medical-notes summary that may contain PHI on an injury claim, and a fraud-pattern check that generally doesn't touch PHI at all. Three distinct calls, one session, one claim.

The version I built first tracks sensitivity at exactly one level: the claim itself. Each claim record carries a single `contains_phi` boolean, set once, at the moment the claim gets filed. I seeded 25 fake claims with invented claimant names, fake policy numbers, and fake medical notes written to resemble PHI without being real, and then asked the obvious auditor's question against the system: which of the three calls in a given claim's session actually touched PHI, and where did that call route. The system could only answer at the claim level: the claim overall was flagged sensitive, full stop. One boolean, set at filing time, collapsed three separate executions into a single undifferentiated signal, leaving no way to say whether the exposure, if any, came from the policy lookup, the medical-notes call, or the fraud check. I measured audit resolution at call-level granularity across all 25 seeded claims, and it came back at 0%.

That gap matters more than it sounds like it should. An adjuster's session runs three calls that touch data very differently. Treating them as one signal means an auditor investigating a specific incident has no way to isolate which call actually mattered, and has to treat the entire session as suspect even when two of the three calls never went near anything sensitive.

## The pattern

The fix keeps the exact same three-step session structure and adds one thing: each node writes its own telemetry record to the shared log the moment it executes, tagged with the session's claim ID, its own node name, a `phi_touched` flag, and a `destination_endpoint` field. The policy lookup logs its own record. The medical-notes summary logs its own, independently. The fraud check logs its own. The orchestration itself stays exactly the same. Sensitivity now gets recorded at the same granularity the actual work happens at, replacing a single decision made once, well before any of the three calls actually ran.

The session graph's shared state is what makes correlating three separate records back to one claim possible without adding any new coordination logic. Each node already knew its own claim ID as part of running the session at all. I just had each node write that knowledge down, on its own, instead of relying on a single record set somewhere else entirely. Running the same audit query against this version resolved correctly for 100% of the seeded claims. An auditor asking which call touched PHI on claim 4821 gets a real, specific answer now, one that names the actual node instead of gesturing at the whole session.

This lines up with where AI-agent audit-trail practice has landed independently. Current industry guidance on what a compliance-grade agent audit trail needs converges on the same shape: the full decision context, every tool call with its own parameters and response, policy evaluation records, data flow lineage, with each data source named individually per request rather than rolled into one document-level signal. That's the identical call-level granularity ClaimAssist's telemetry targets, arrived at from the audit side of the problem rather than the architecture side.

## Design considerations

The limitation here is built into what this pattern is actually for, and I'd rather state it plainly than let the fix sound bigger than it is. Telemetry proves, after the fact, which call touched PHI and where it went, but the touch or the routing has already happened by the time telemetry records it. This is a detection and accountability layer, sitting on top of whatever gating or routing logic a system already has, and it depends entirely on that logic for the actual protection. A pipeline with perfect call-level telemetry and no gating at all would just produce a beautifully, completely documented leak. The telemetry would tell you exactly which call leaked what, and to where, and none of that changes the fact that it leaked.

That distinction matters for how I'd sequence building something like this. I'd add telemetry regardless of whether the underlying routing is already correct, because an auditable system and a correctly-gated system answer different questions, and an organization usually needs both answered eventually. But if I had to choose which to build first on a limited budget, I'd build the gate before the telemetry every time. A system that can't tell an auditor what happened is a governance gap. A system that lets PHI reach the wrong endpoint in the first place is the actual incident the governance gap was trying to catch. Telemetry catches the incident on the record after the fact, which is a different job than preventing it, and I wouldn't want anyone reading a well-instrumented audit trail and mistaking the instrumentation for the control.
