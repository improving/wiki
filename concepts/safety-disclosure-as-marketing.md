---
title: "Safety Disclosure as Marketing"
type: "Concept"
description: "Vendor safety disclosures that double as marketing, so enterprises should govern by runtime enforcement and evaluation rather than self-reported risk tiers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, safety, vendors]
sources:
  - "/sources/the-warning-is-the-marketing.md"
  - "/sources/too-dangerous-to-centralize-too-dangerous-to-distribute.md"
---

# Safety Disclosure as Marketing

Safety disclosure as marketing is the observation that a vendor's warning about a model's dangerous capability also announces how powerful it is. Industrial safety reporting has always carried this double meaning, and this corpus argues that enterprise buyers should treat self-reported risk tiers as marketing, not evidence. The corollary is governance by runtime enforcement: catch bad behavior regardless of the capability tier a vendor claims, and choose platforms by an evaluation baseline against the organization's own workload rather than by stated mission.

## Key Claims

- A lab announcing a model might be dangerous also announces it is powerful.
- Industrial safety reporting has always carried this same double meaning.
- Gating model access by vendor self-reported risk tiers is governing by label.
- Runtime enforcement catches bad behavior regardless of claimed capability tier.
- Meta and Anthropic reached opposite conclusions ("too dangerous to centralize" vs. "too dangerous to distribute") from the same technology in the same month.
- Each lab's safety philosophy lands exactly when its business model needs it to be true; treating a stated mission as evidence is a category error.

## Related

- [runtime governance](/concepts/runtime-governance.md) — enforcement that does not depend on vendor labels
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the mechanism that catches behavior by tier-agnostic rules
- [Benchmark Validity](/concepts/benchmark-validity.md) — the same skepticism applied to performance claims
- [Capability Forecasting](/concepts/capability-forecasting.md) — how capability claims get evaluated rather than believed
- [Model selection](/concepts/model-selection.md) — choosing by evaluation baseline, not mission statement
- [The Warning Is the Marketing](/sources/the-warning-is-the-marketing.md) — primary source
