---
title: "Claude Security"
type: "Entity"
description: "Anthropic product that sells governed vulnerability findings instead of raw model access, pushing enterprises to build their own approval gate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [product, security, governance]
sources:
  - "/sources/the-model-stays-home-the-patch-ships.md"
  - "/sources/the-warning-is-the-marketing.md"
---

# Claude Security

Claude Security is an Anthropic offering that runs vulnerability scans on Mythos 5 and returns CWE-categorized findings and patches, rather than exposing raw model capability to the customer.

## Overview

The product embodies **access-by-output**: dangerous capability stays inside the vendor and the customer receives governed artifacts. One post argues the customer still needs its own evaluation before patches ship, and that whether access-by-output satisfies regulators depends on adversarial pressure.

A companion argument holds that vendor safety disclosures double as marketing — a lab announcing a model might be dangerous also announces it is powerful — so gating access by self-reported risk tiers is governing by label rather than by behavior.

## Key Claims

- Claude Security runs vulnerability scans on Mythos 5, returning CWE-categorized findings and patches
- Access-by-output keeps dangerous raw model capability inside the vendor
- Vendor findings still need customer-side evaluation before patches ship
- A lab announcing danger also announces power; disclosure carries double meaning
- Runtime enforcement catches bad behavior regardless of claimed capability tier

## Related

- [Mythos 5](/entities/mythos-5.md) — the model behind the scans
- [Anthropic](/entities/anthropic.md) — the vendor
- [Safety Disclosure as Marketing](/concepts/safety-disclosure-as-marketing.md) — the double-meaning argument
- [runtime governance](/concepts/runtime-governance.md) — governing by behavior, not label
- [approval gate](/concepts/human-approval-points.md) — the customer-side check before patches ship
- [The Model Stays Home. The Patch Ships.](/sources/the-model-stays-home-the-patch-ships.md) — primary source
