---
title: "Review Bottleneck"
type: "Concept"
description: "AI made generation fast but verification slow, so effective throughput is gated by human review capacity."
created: '2026-10-17'
updated: '2026-10-17'
tags: [review, verification, delivery]
sources:
  - "/sources/the-model-found-the-zero-day-who-signs-the-patch.md"
  - "/sources/the-review-bottleneck-nobody-talks-about.md"
---

# Review Bottleneck

The review bottleneck is the observation that AI-assisted delivery shifts the constraint from *producing* work to *verifying* it. Generation became fast and cheap, but review, evaluation, and sign-off stayed human-paced, so effective throughput is gated by review capacity rather than generation speed. Across this corpus the bottleneck is treated as the central unsolved problem of agentic delivery — and as a thing to be redesigned, not endured.

## Key Claims

- Effective throughput is gated by review capacity, not generation speed.
- Permission mode (approve-every-action) makes humans a linear throughput constraint.
- A model surfacing a vulnerability is a claim, not a verified fact; 1Password found models can be right about the bug and wrong about the fix.
- The commit still needs a human signature — review is the unaccounted bottleneck behind flashy capability.
- Specialized evaluation agents can run review as a pipeline stage rather than an interrupt.
- Trust is earned through progressive delegation, calibrated over time rather than granted up front.

## Related

- [verification tax](/concepts/verification-tax.md) — the cost that accumulates at the review stage
- [human-in-the-loop](/concepts/human-in-the-loop.md) — where the bottleneck physically sits
- [human approval points](/concepts/human-approval-points.md) — gates that trade throughput for safety
- [Independent Verification](/concepts/independent-verification.md) — the discipline review capacity must fund
- [Model-as-judge](/concepts/model-as-judge.md) — one way to run review as a pipeline stage
- [AI Trust Evolution](/concepts/ai-trust-evolution.md) — the progressive-delegation path that widens the bottleneck
- [The Review Bottleneck in AI-Assisted Delivery](/sources/the-review-bottleneck-nobody-talks-about.md) — primary source
