---
title: "SOC 2 Type II"
type: "Entity"
description: "Audit standard used in this corpus as a vendor-trust artifact that goes stale and must be re-checked at request time."
created: '2026-10-17'
updated: '2026-10-17'
tags: [compliance, audit, vendor-risk]
sources:
  - "/sources/acceleration-whiplash-the-hidden-metric-ai-adoption-is-breaking.md"
  - "/sources/the-approval-that-expires-building-a-vendor-gate-on-evidence.md"
  - "/sources/the-evaluation-governance-flywheel-neither-works-without-the-other.md"
  - "/sources/the-ship-of-theseus-problem-lives-in-your-model-registry.md"
---

# SOC 2 Type II

SOC 2 Type II is an audit standard attesting that a vendor's controls operated effectively over a period. In this corpus it is the archetypal compliance artifact — valuable, but time-bound and insufficient on its own, used to argue that approvals must be earned against current evidence rather than cached on an allow-list.

## Key Claims

- An allow-list approved vendor requests against stale evidence over 30% of the time; a request-time pipeline should check pen-test, SOC 2, scan, and uptime against thresholds ([the approval that expires](/sources/the-approval-that-expires-building-a-vendor-gate-on-evidence.md))
- A vendor approved yesterday is denied today once its pen test expires, because fresh evidence is still evidence and can go stale tomorrow.
- Compliance obligations are the forcing function that keeps the [evaluation](/concepts/evaluation-harness.md)–[governance](/concepts/ai-governance.md) flywheel turning ([the evaluation-governance flywheel](/sources/the-evaluation-governance-flywheel-neither-works-without-the-other.md))
- Silent model-weight updates under stable endpoint names break identity continuity that compliance and reproducibility depend on, so teams should pin at the model version level ([the ship of theseus](/sources/the-ship-of-theseus-problem-lives-in-your-model-registry.md))
- Generation velocity that outruns review capacity degrades downstream quality: bugs per developer up 54%, incidents per PR up 242.7% ([acceleration whiplash](/sources/acceleration-whiplash-the-hidden-metric-ai-adoption-is-breaking.md))

## Related

- [Audit Trail](/concepts/audit-trail.md) — the evidence trail behind attestation
- [Version Pinning](/concepts/version-pinning.md) — the continuity fix
- [evaluation harness](/concepts/evaluation-harness.md) — the baseline compliance keeps honest
- [Review Bottleneck](/concepts/review-bottleneck.md) — the capacity constraint
- [METR](/entities/metr.md) — cited grading evidence
