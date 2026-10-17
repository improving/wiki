---
title: "Schema Drift"
type: "Concept"
description: "Divergence between a copied schema and its canonical source, silently invalidating data until something fails."
created: '2026-10-17'
updated: '2026-10-17'
tags: [data-quality, agents, integration]
sources:
  - "/sources/load-the-schema-dont-paste-it.md"
  - "/sources/order-31-and-the-refund-that-never-went-through.md"
---

# Schema drift

Schema drift is what happens when a schema is copied out of its system of record and pasted somewhere it can no longer track changes. The copy becomes a second, unsynchronized source of truth, and every later edit to the canonical schema widens the gap. Across this corpus drift is a recurring failure mode of extraction agents and tool contracts: the work looks correct until validation, refunds, or downstream joins quietly disagree.

## Key Claims

- A pasted schema creates a second, unsynchronized source of truth that nothing keeps in step with the original.
- One account reports 15 of 25 purchase orders failing validation against a drifted schema.
- Loading the canonical schema at assembly time propagates schema changes automatically instead of requiring prompt edits.
- Referenced schemas trade a runtime dependency and growing token cost for correctness.
- Independently authored tool responses each invent their own success shape; a schema-validated envelope forces one contract and makes malformed responses fail loudly.
- A validated envelope cannot catch a well-formed lie — that still requires independent verification.

## Related

- [Data Contract](/concepts/data-contract.md) — the explicit agreement drift erodes
- [deterministic validation](/concepts/deterministic-validation.md) — how drift is caught mechanically
- [Independent Verification](/concepts/independent-verification.md) — needed when shapes are valid but values are wrong
- [Load the Schema, Don't Paste It](/sources/load-the-schema-dont-paste-it.md) — primary source
- [Order 31 and the Refund That Never Went Through](/sources/order-31-and-the-refund-that-never-went-through.md) — primary source
