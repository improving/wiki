---
title: "Two Prices, One Model Family, Two Different Customers"
type: "Source Summary"
description: "Reads Meta's five-day, two-release model sequence as one segmentation strategy serving two distinct buyers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/two-prices-one-model-family-two-different-customers/two-prices-one-model-family-two-different-customers.md"
---

# Two Prices, One Model Family, Two Different Customers — Summary

**Original source**: `references/devlinliles.com/two-prices-one-model-family-two-different-customers/two-prices-one-model-family-two-different-customers.md`

## Summary

Liles reads Meta's five-day, two-release sequence — API-only Muse Spark 1.2 on August 5, then Apache-2.0 Glimmer on August 10 — as a single segmentation strategy wearing a version number. The closed API serves the buyer who wants Meta to run the model and pays for a relationship; the open release serves the self-hosting buyer who was never in the market for the closed tier. The five-day gap, he argues, is a deliberate choice to get shared branding without making Muse look like one confused product.

## Key Claims

- Muse Spark 1.2 launched API-only at $1.25 per million input and $4.25 per million output tokens on the standard tier, with a second tier at $0.10/$0.20 — twelve to twenty times cheaper.
- That 12–20x spread signals Meta already knows its buyers don't look alike: enterprise relationship buyers versus price-sensitive volume buyers.
- Glimmer shipped five days later under Apache 2.0 with no API key, no per-token bill, and no tier.
- The API buyer pays for uptime, support, and a roadmap; the self-hosting buyer wants to fine-tune on proprietary data or avoid variable per-token cost at scale.
- Five days is close enough for shared branding but far enough for each product to get its own coverage moment; same-day would look confused, a quarter apart would lose the family moment.
- There is no cannibalization because the two groups do not bid for the same unit of revenue.

## Relevance

Informs [open-weight models](/concepts/open-weight-models.md) as a go-to-market strategy and touches the economics of [token cost](/concepts/token-cost.md) in tiered API pricing.

## Quality

Practitioner analysis by Devlin Liles. A crisp, well-reasoned reading of a pricing and licensing decision; it is interpretation of public release choices rather than confirmed internal strategy.

## Entities Mentioned

- [Meta](/entities/meta.md) — the vendor whose two releases are analyzed

## Concepts Covered

- [open-weight models](/concepts/open-weight-models.md) — the Apache-2.0 release reaching self-hosting buyers
- [token cost](/concepts/token-cost.md) — tiered per-token pricing as the segmentation mechanism
