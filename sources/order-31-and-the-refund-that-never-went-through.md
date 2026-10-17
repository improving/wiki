---
title: "Order 31 and the Refund That Never Went Through"
type: "Source Summary"
description: "Ad hoc tool response shapes let a buried \"ok\" field pass as success; a schema-validated envelope forces failures to surface."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/order-31-and-the-refund-that-never-went-through/order-31-and-the-refund-that-never-went-through.md"
---

# Order 31 and the Refund That Never Went Through — Summary

**Original source**: `references/devlinliles.com/order-31-and-the-refund-that-never-went-through/order-31-and-the-refund-that-never-went-through.md`

## Summary

An order-support agent over 40 synthetic orders called three mocked tools whose responses each had their own shape. Order 31's refund processor returned a nested object that, read whole, meant failure, but contained a `"result": "ok"` field; the orchestrator read only that field and logged the refund as resolved. A second version forced every tool response through a `{status, data, error, tool_name, schema_version}` envelope before the orchestrator read it, so malformed responses are flagged rather than waved through.

## Key Claims

- Every individual call succeeded on its own terms; the failure came from three tools never sharing a definition of success.
- The envelope version catches the order-31 failure mode by construction, since the orchestrator never reads a tool's native output.
- Success is measured by a silent-failure propagation rate (bar at or below 2%) and erroneous-action count (near zero) across the same 40 orders.
- The envelope checks shape, not truth: a cleanly lying tool returning `{"status":"success"}` sails through, so verifying a claim needs an independently observable artifact.
- It does not catch a schema changing shape between calls, and its overhead only pays off once independently authored tools (other teams, third-party MCP servers) feed the same orchestrator.

## Relevance

Informs [schema drift](/concepts/schema-drift.md), [data contract](/concepts/data-contract.md), and [independent verification](/concepts/independent-verification.md) thinking in agent pipelines.

## Quality

Practitioner blog post by Devlin Liles. Controlled synthetic reproduction (40 orders, seeded failures) with stated thresholds; illustrative rather than production evidence.

## Entities Mentioned

- None.

## Concepts Covered

- [Schema drift](/concepts/schema-drift.md) — a failure the envelope explicitly does not catch
- [Data Contract](/concepts/data-contract.md) — the validated envelope as a shared shape across tools
- [Independent Verification](/concepts/independent-verification.md) — needed to catch a well-formed lie the envelope passes
