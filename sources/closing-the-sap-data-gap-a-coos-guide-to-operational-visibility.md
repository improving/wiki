---
title: "Closing the SAP Data Gap: A COO’s Guide to Operational Visibility"
type: "Source Summary"
description: "Argues COOs lose margin to siloed SAP and non-SAP data, and that embedding intelligence in the workflow beats dashboards that only show problems."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, platform, improving.com]
sources:
  - "references/improving.com/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility.md"
---

# Closing the SAP Data Gap: A COO’s Guide to Operational Visibility — Summary

**Original source**: `references/improving.com/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility/closing-the-sap-data-gap-a-coos-guide-to-operational-visibility.md`

## Summary

Even wall-to-wall SAP shops have operational systems that are non-SAP, leaving a COO unable to see how an operational decision translates to finance. The post argues the cost of that gap shows up as margin erosion when pricing and procurement are driven by institutional knowledge, plus hidden people costs as analysts spend half their day joining data manually. It describes an Improving engagement that joined operational data in a Databricks lakehouse with financial data in S/4HANA using SAP Business Data Cloud's zero-delta copy, then used Databricks for AI modeling — and argues that embedding action into the workflow, not just a dashboard, is what changes decisions.

## Key Claims

- Non-SAP operational data gets pushed into a third-party tool, data lake, or warehouse, making the join slow and manual.
- The biggest impact of poor visibility is margin erosion when procurement decisions are not tied to their financial effect.
- A price-optimization engagement married Databricks lakehouse operational data to S/4HANA financial data with Business Data Cloud's zero-delta copy, giving real-time access without a stale copy.
- Databricks then ran AI and large language modeling to predict where price optimization would be most impactful.
- A dashboard only shows what is happening; users still jump between systems to investigate and fix, and each step adds delay.
- Building an application directly in BTP lets users act from where they see the anomaly, pushing changes back into S/4HANA without navigating there.
- Timelines: a six-, twelve-, or eighteen-month roadmap; specific use cases like procurement in ten to twelve weeks; pre-configured BTP portals accelerate early wins.

## Relevance

Ties [data integration](/concepts/data-integration.md) and a [lakehouse](/concepts/lakehouse.md) architecture to [business intelligence](/concepts/business-intelligence.md), showing how [data platform modernization](/concepts/data-platform-modernization.md) changes operational decisions.

## Quality

Practitioner guide by Sean Antonello; concrete architecture and timelines, though vendor-aligned and short on quantified results.

## Entities Mentioned

- [SAP](/entities/sap.md) — ERP vendor
- [SAP Business Data Cloud](/entities/sap-business-data-cloud.md) — zero-delta data sharing
- [SAP S/4HANA](/entities/sap-s4hana.md) — financial core
- [SAP BTP](/entities/sap-btp.md) — embedded application platform
- [Databricks](/entities/databricks.md) — lakehouse and AI modeling
- [Sean Antonello](/entities/sean-antonello.md) — author

## Concepts Covered

- [data integration](/concepts/data-integration.md) — joining SAP and non-SAP data
- [lakehouse](/concepts/lakehouse.md) — Databricks operational store
- [business intelligence](/concepts/business-intelligence.md) — visibility into operations
- [data platform modernization](/concepts/data-platform-modernization.md) — modern analytics layer
